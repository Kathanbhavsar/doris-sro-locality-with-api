import time
import pandas as pd
from sqlalchemy import create_engine
import re

def postgres_write(df):
    """
    Function postgres_write that takes in a Pandas DataFrame df as an argument and writes it to a PostgreSQL database.

    Defines a connection string to connect to the database.
    Creates an engine using the create_engine function from the sqlalchemy library with the connection string.
    Connects to the database using the engine.
    Uses the to_sql method of the DataFrame to write the DataFrame to the database table 'doris_sro_locality_test', replacing any existing data in the table.
    Prints the duration of the to_sql operation.
    This function can be called by passing a DataFrame as an argument. It will write the DataFrame to the specified PostgreSQL table.
    """
    conn_string = 'postgresql://postgres:password@localhost/doris_db'

    #Import .csv file
    # df = pd.read_csv('/Users/kathanbhavsar/Desktop/final_task_folder/Central_Asaf_Ali_(SR III)_final.csv')
    db = create_engine(conn_string)
    conn = db.connect()

    start_time = time.time()
    df.to_sql('doris_sro_locality_test', con=conn, if_exists='replace', index=False)
    print("to_sql duration: {} seconds".format(time.time() - start_time))