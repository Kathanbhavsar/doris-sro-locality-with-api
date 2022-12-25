import pandas as pd
import re
# df = pd.read_csv("Central -Asaf Ali (SR III).csv") ## Reading in the scraped data to convert the area into a same unit

def convert_to_sq_feet(area): 
    """
    The convert_to_sq_feet function takes in a string area and converts it to square feet by:
    Splitting the string into three parts: the value, the string "sq", and the unit.
    Converting the value to a float.
    If the unit is "Meter", the value is converted to square feet by multiplying it by 10.764.
    If the unit is "Yard", the value is converted by multiplying it by 9. If the unit is anything else, the original value is returned
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
    """
    function data_cleanup that takes in a Pandas DataFrame df as an argument. The function does the following:

    Renames the columns of the DataFrame by replacing all non-alphanumeric characters with underscores and making the names lowercase.
    Filters out rows with the string "Show rows" in the "reg_no" column.
    Applies the convert_to_sq_feet function to the "area" column to convert the area values to square feet.
    Renames the "area" column to "area_in_sq_feet".
    Converts the "reg_date" column to datetime format.
    Returns the cleaned DataFrame.
    """
    df.columns = [re.sub('[^a-zA-Z0-9]', '_', c).lower() for c in df.columns]
    # df["reg_no"] = df["reg_no"].astype(str)
    df = df[~df["reg_no"].str.contains("Show rows")]

    df["area"] = df["area"].apply(convert_to_sq_feet) ## Applying the function to convert the area
    df = df.rename(columns={'area': 'area_in_sq_feet'}) ## Renaming the column name


    df["reg_date"] = pd.to_datetime(df["reg_date"], format = "%d-%m-%Y")
    # df["reg_no"] = df["reg_no"].round().astype(int)
    
    # df.to_csv("/Users/kathanbhavsar/Desktop/final_task_folder/Central_Asaf_Ali_(SR III)_final.csv", index= False)
    return df