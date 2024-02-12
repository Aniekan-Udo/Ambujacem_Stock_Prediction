import sqlite3

import pandas as pd
import requests
from config import settings


class AlphaVantageAPI:
    def __init__(self, api_key=settings.alpha_api_key):
        self.__api_key = api_key

    """Get daily time series of an equity from AlphaVantage API.

            Parameters
            ----------
            ticker : str
                The ticker symbol of the equity.
            output_size : str, optional
                Number of observations to retrieve. "compact" returns the
                latest 100 observations. "full" returns all observations for
                equity. By default "full".

            Returns
            -------
            pd.DataFrame
                Columns are 'open', 'high', 'low', 'close', and 'volume'.
                All are numeric.
            """

    def get_data(self, ticker, output_size='full'):
        # Create url
        url = ("https://learn-api.wqu.edu/1/data-services/alpha-vantage/query?"
            "function=TIME_SERIES_DAILY&"
            f"symbol={ticker}&"
            f"apikey={settings.alpha_api_key}")

        # Send request to the url
        response = requests.get(url=url)

        # Extract Json data
        response_data = response.json()
        if "Time Series (Daily)" not in response_data.keys():
            raise Exception(
                f"Invalid API call: check that ticker symbol '{ticker}' is correct"
            )
        # read data into dataframe
        crypto_data = response_data["Time Series (Daily)"]
        df = pd.DataFrame.from_dict(crypto_data, orient='index', dtype=float)

        # Convert index column to datetime
        df.index = pd.to_datetime(df.index)

        # Remove numbering from columns
        df.columns = [c.split(". ")[1] for c in df.columns]
        df.sort_index(ascending=False, inplace=True)

        # Name index column as 'date'
        df.index.name = 'date'


        # Return df
        return df

class SQLRepository:
    def __init__(self, connection):
        self.connection = connection

    def insert_data(self, table_name, record, if_exists='fail'):
        """Insert DataFrame into SQLite database as table

                Parameters
                ----------
                table_name : str
                records : pd.DataFrame
                if_exists : str, optional
                    How to behave if the table already exists.

                    - 'fail': Raise a ValueError.
                    - 'replace': Drop the table before inserting new values.
                    - 'append': Insert new values to the existing table.

                    Dafault: 'fail'

                Returns
                -------
                dict
                    Dictionary has two keys:

                    - 'transaction_successful', followed by bool
                    - 'records_inserted', followed by int
                """

        n_inserted = record.to_sql(name=table_name, con=self.connection, if_exists=if_exists)
        return {
            "transaction_successful": True,
            "records_inserted": n_inserted}

    def read_data(self, table_name, limit):

        """Read table from database.

                Parameters
                ----------
                table_name : str
                    Name of table in SQLite database.
                limit : int, None, optional
                    Number of most recent records to retrieve. If `None`, all
                    records are retrieved. By default, `None`.

                Returns
                -------
                pd.DataFrame
                    Index is DatetimeIndex "date". Columns are 'open', 'high',
                    'low', 'close', and 'volume'. All columns are numeric.
                """

        if limit:
            sql = f"SELECT * FROM '{table_name}' LIMIT {limit}"
        else:
            sql = f"SELECT * FROM '{table_name}'"

        df = pd.read_sql(sql = sql, con = self.connection, parse_dates = ["date"], index_col = "date")

        return df


