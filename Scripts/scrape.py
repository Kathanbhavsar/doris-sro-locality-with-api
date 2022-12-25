from selenium import webdriver
from shutil import which
import io
import urllib3
import pytesseract 
from PIL import Image, ImageEnhance
from selenium.webdriver.support.select import Select
import urllib.request
import pandas as pd
import cv2
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def select_sro(driver):
    """
     select_sro function to navigate to the website and select the "Central -Asaf Ali (SR III)" locality from the dropdown menu.
    """
    url = "https://esearch.delhigovt.nic.in/Complete_search.aspx"
    driver.get(url)
    sro = driver.find_element_by_xpath('//*[(@id = "ctl00_ContentPlaceHolder1_ddl_sro_s")]')
    sro.click()
    sro.send_keys("Central -Asaf Ali (SR III)")
    
def read_table(driver):
    table = driver.page_source
    dfs = pd.read_html(table)
    df = dfs[0]
    df = df.dropna(axis=0)
    return df
    
def check_exists(driver,value,by):
    try: 
        f = f"driver.find_element_by_{by}"
        eval(f)(value)
    except NoSuchElementException:
        return False
    return True


def get_doris_data(start_locality=None, no_of_locality=None):
    """
    Function get_doris_data that scrapes data from a webpage and returns a Pandas DataFrame.

    The function takes two optional arguments: start_locality and no_of_locality. If these arguments are provided, the function will scrape data for only the specified number of localities, starting from the start_locality-th locality. If these arguments are not provided, the function will scrape data for all localities.
    Initializes the Chrome webdriver and defines the path to the Chrome driver executable.
    Calls the select_sro function to navigate to the website and select the "Central -Asaf Ali (SR III)" locality from the dropdown menu.
    Scrapes a list of all localities from the dropdown menu and stores it in the locality_list variable.
    If start_locality and no_of_locality are provided, the function updates locality_list to contain only the specified number of localities, starting from the start_locality-th locality. Otherwise, the function updates locality_list to remove the first element, which is a placeholder.
    Initializes an empty list df_list to store the DataFrames for each locality.
    Loops through each locality in locality_list and does the following:
    Selects the current locality from the dropdown menu.
    Selects the year "2021-2022" from the year dropdown menu.
    Prompts the user to enter the captcha text.
    Enters the captcha text and submits the form.
    Waits for the table to load and then scrapes the table using the read_table function.
    Appends the resulting DataFrame to df_list.
    Concatenates all the DataFrames in df_list into a single DataFrame and returns it.
    """
    chrome_path = which("/Users/kathanbhavsar/Desktop/Task/chromedriver")
    driver = webdriver.Chrome(chrome_path)
    locality_list = []
    select_sro(driver)
    locality = driver.find_element_by_xpath('//*[(@id = "ctl00_ContentPlaceHolder1_ddl_loc_s")]')
    dd = Select(locality)

    for opt in dd.options:
        ##print(opt.text)
        locality_list.append(opt.text)
    print(len(locality_list))
    if start_locality or no_of_locality:
        locality_list = locality_list[start_locality:start_locality+no_of_locality]
    else:
        locality_list = locality_list[1:]

    df_list = []

    for i,local in enumerate(locality_list):
        locality = driver.find_element_by_xpath('//*[(@id = "ctl00_ContentPlaceHolder1_ddl_loc_s")]')
        dd = Select(locality)
        dd.select_by_visible_text(locality_list[i])

        year = driver.find_element_by_xpath('//*[(@id = "ctl00_ContentPlaceHolder1_ddl_year_s")]')
        year_list = Select(year)
        year_list.select_by_visible_text('2021-2022')
        
        # captcha = driver.find_element_by_xpath('//*[(@id = "ctl00_ContentPlaceHolder1_UpdatePanel4")]//img')
        # image_url = captcha.get_attribute('src')

        # image = cv2.imread(io.BytesIO(image_url))

        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # #gray = cv2.medianBlur(gray, 3)

        # filename = "{}.png".format("temp")
        # cv2.imwrite(filename, gray)
        # text = pytesseract.image_to_string(Image.open('temp.png'))
        # print(text)
        
        #captcha_code = str(input("Enter the captcha code"))
        # captcha_field = driver.find_element_by_css_selector('#ctl00_ContentPlaceHolder1_txtcaptcha_s')
        # ##captcha_field.send_keys(captcha_code)
        time.sleep(10)
        ## Clicking the submit button 
        # submit = driver.find_element_by_xpath('//*[(@id = "ctl00_ContentPlaceHolder1_btn_search_s")]')
        # submit.click()
        button = driver.find_element_by_xpath('//*[(@id = "ctl00_ContentPlaceHolder1_btn_search_s")]')
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)
        try:
            
            table_flag = check_exists(driver,'ctl00_ContentPlaceHolder1_gv_search','id')
            print(table_flag)
            
        # Find the table element
            if table_flag:
                
                page_flag = True
                print("Table found looking for the next pages to paginate!")
                
                while page_flag:
                    page_flag = check_exists(driver,'//*[(@id = "ctl00_ContentPlaceHolder1_gv_search_ctl13_Button2")]','xpath')
                    
                    df = read_table(driver)
                    ##print(df)
                    df_list.append(df)
                    time.sleep(3)
                    if page_flag:
                        print("Page Found Going to the next page!")
                        page_button = driver.find_element_by_xpath('//*[(@id = "ctl00_ContentPlaceHolder1_gv_search_ctl13_Button2")]')
                        driver.execute_script("arguments[0].click();",page_button)
                        time.sleep(3)
                        #print(df.head())      
                    
            select_sro(driver) ## Going Back again to the home page 
            
        except Exception as e:
            print(str(e))
    final_df = pd.concat(df_list)
    
    return final_df