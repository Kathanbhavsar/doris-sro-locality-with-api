import time
import pandas as pd
from sqlalchemy import create_engine
import re

def postgres_write(df):
#INPUT YOUR OWN CONNECTION STRING HERE
    conn_string = 'postgresql://postgres:password@localhost/doris_db'

    #Import .csv file
    # df = pd.read_csv('/Users/kathanbhavsar/Desktop/final_task_folder/Central_Asaf_Ali_(SR III)_final.csv')
    #perform to_sql test and print result
    db = create_engine(conn_string)
    conn = db.connect()

    start_time = time.time()
    df.to_sql('doris_sro_locality_test', con=conn, if_exists='replace', index=False)
    print("to_sql duration: {} seconds".format(time.time() - start_time))