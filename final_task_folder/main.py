from scrape import get_doris_data
from data_cleanup import data_cleanup
from postgres_write import postgres_write

def main():
    doris_df = get_doris_data(start_locality=3,no_of_locality=3)
    doris_df = data_cleanup(doris_df)
    postgres_write(doris_df)

if __name__ == '__main__':
    main()