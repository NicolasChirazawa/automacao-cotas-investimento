import pandas as pd

class PandasDataframe:
    """
    Class responsible for the standardization and manipulation of Pandas DataFrames.

    Attributes:
        path (str):
            Absolute path to the CSV file.

        df (pandas.DataFrame):
            Data stored in the dataframe.

        list (list, optional):
            List of dataframes used for concatenation.

        dict (dict, optional):
            Dictionary used to create a dataframe.
    """

    def __init__(self, path, df, **kwargs):
        self.path = path
        self.df = df
        self.list = kwargs.get('list') or None
        self.dict = kwargs.get('dict') or None

    def csv_to_df(self):
        """
        Reads a CSV file from the specified path and loads it into the dataframe.
        """
        self.df = pd.read_csv(self.path, sep=';', encoding='utf-8', index_col=None)
    
    def df_to_csv(self, path):
        """
        Exports the current dataframe to a CSV file.

        Args:
            path (str):
                Destination path for the CSV file.
        """
        self.df.to_csv(path, sep=';', index=False)

    def list_to_df(self):
        """
        Concatenates a list of dataframes into a single dataframe.
        """
        self.df = pd.concat(self.list, ignore_index=True)
    
    def dict_to_df(self):
        """
        Converts the stored dictionary into a dataframe.
        """
        self.df = pd.DataFrame(self.dict)

    def drop_column(self, column, direction):
        """
        Drops rows or columns from the dataframe.

        Args:
            column (str or list):
                Column name(s) or row label(s) to drop.

            direction (int):
                Axis to drop from (0 for rows, 1 for columns).
        """
        self.df = self.df.drop(column, axis=direction)

    def query_date(self, start_date, end_date, column_name):
        """
        Filters rows between two dates based on a specified date column.

        Args:
            start_date (str or datetime):
                Start date for filtering.

            end_date (str or datetime):
                End date for filtering.

            column_name (str):
                Name of the date column.
        """
        self.df[column_name] = pd.to_datetime(self.df[column_name])

        self.df = self.df.loc[
            (self.df[column_name] >= start_date) &
            (self.df[column_name] <= end_date)
        ]

    def query_element_in(self, column, collection):
        """
        Filters rows where column values are within a given collection.

        Args:
            column (str):
                Column name to filter.

            collection (list or set):
                Collection of values to match.
        """
        self.df = self.df[self.df[column].isin(collection)]
    
    def query_date_and_element(self, start_date, end_date, date_column_name, investment_cnpj, investment_column_cnpj):
        """
        Filters rows based on both a date range and a specific element.

        Args:
            start_date (str or datetime):
                Start date for filtering.

            end_date (str or datetime):
                End date for filtering.

            date_column_name (str):
                Name of the date column.

            investment_cnpj (str):
                Value to filter in the investment column.

            investment_column_cnpj (str):
                Column name containing the investment identifier.

        Returns:
            pandas.DataFrame:
                Filtered dataframe.
        """
        new_df_reference = self.df

        new_df_reference = new_df_reference[
            new_df_reference[investment_column_cnpj].isin([investment_cnpj])
        ]

        new_df_reference[date_column_name] = pd.to_datetime(new_df_reference[date_column_name])

        new_df_reference = new_df_reference.loc[
            (new_df_reference[date_column_name] >= start_date) &
            (new_df_reference[date_column_name] <= end_date)
        ]

        return new_df_reference

    def reset_index(self):
        """
        Resets the dataframe index.
        """
        self.df = self.df.reset_index()
    
    def get_column_in_list(self, column):
        """
        Returns a dataframe column as a Python list.

        Args:
            column (str):
                Column name.

        Returns:
            list:
                Column values as a list.
        """
        return self.df[column].tolist()
    
    def sort_elements_list(self, sort_list):
        """
        Sorts the dataframe by the specified columns.

        Args:
            sort_list (list):
                List of column names to sort by.
        """
        self.df = self.df.sort_values(by=sort_list)
    
    def order_columns(self, order_list):
        """
        Reorders the dataframe columns.

        Args:
            order_list (list):
                Desired column order.
        """
        self.df = self.df[order_list]

    def group_element(self, group_element):
        """
        Groups the dataframe by the specified column(s).

        Args:
            group_element (str or list):
                Column(s) to group by.
        """
        self.df = self.df.groupby(group_element)

    def find_row_date_greater_or_equals_than_indicated(self, date_str) -> tuple[bool, int]:
        """
        Finds the first row where the date is greater than or equal to the given date.

        Args:
            date_str (str or datetime):
                Reference date.

        Returns:
            tuple:
                (True, index) if found, otherwise (False, 0).
        """
        column_date = pd.to_datetime(self.df['DT_COMPTC'])
        mask = column_date >= date_str

        if mask.any():
            idx = mask.idxmax()
            return [True, idx]
        else:
            return [False, 0]

    def find_row_data(self, row):
        """
        Retrieves a row from the dataframe by index.

        Args:
            row (int):
                Row index.

        Returns:
            pandas.Series:
                Row data.
        """
        return self.df.iloc[row]


__all__ = ["PandasDataframe"]