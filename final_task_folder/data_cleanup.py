import pandas as pd
import re
# df = pd.read_csv("Central -Asaf Ali (SR III).csv") ## Reading in the scraped data to convert the area into a same unit

def convert_to_sq_feet(area): 
    """
    Method to convert area into sq. Feet
    Split the area value into value and unit
    """
    value, sq, unit = area.split()
    value = float(value)
    if unit == "Meter":
        return value * 10.764
    elif unit == "Yard":
        return value * 9
    else:
        return value

def data_cleanup(df):
    df.columns = [re.sub('[^a-zA-Z0-9]', '_', c).lower() for c in df.columns]
    # df["reg_no"] = df["reg_no"].astype(str)
    df = df[~df["reg_no"].str.contains("Show rows")]

    df["area"] = df["area"].apply(convert_to_sq_feet) ## Applying the function to convert the area
    df = df.rename(columns={'area': 'area_in_sq_feet'}) ## Renaming the column name


    df["reg_date"] = pd.to_datetime(df["reg_date"], format = "%d-%m-%Y")
    # df["reg_no"] = df["reg_no"].round().astype(int)
    
    # df.to_csv("/Users/kathanbhavsar/Desktop/final_task_folder/Central_Asaf_Ali_(SR III)_final.csv", index= False)
    return df