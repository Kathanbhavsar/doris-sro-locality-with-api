from scrape import get_doris_data
from data_cleanup import data_cleanup
from postgres_write import postgres_write

def main():
    """
    Function main that retrieves data from the website, cleans it up, and writes it to a PostgreSQL database.

    Calls the get_doris_data function to scrape data from the website for the localities from the third to fifth locality (inclusive). The resulting DataFrame is stored in doris_df.
    Calls the data_cleanup function to clean up the data in doris_df and stores the resulting DataFrame in doris_df.
    Calls the postgres_write function to write doris_df to the PostgreSQL database.

    """
    doris_df = get_doris_data(start_locality=3,no_of_locality=3)
    doris_df = data_cleanup(doris_df)
    postgres_write(doris_df)

if __name__ == '__main__':
    main()