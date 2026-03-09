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

    Methods:
        csv_to_df():
            Reads a CSV file from 'path' and loads it into 'df'.

        df_to_csv(path):
            Exports the dataframe to a CSV file.

        dict_to_df():
            Converts the stored dictionary into a dataframe.

        list_to_df():
            Concatenates a list of dataframes into a single dataframe.

        drop_column(column, direction):
            Drops rows or columns depending on the axis provided.

        query_date(start_date, end_date, column_name):
            Filters rows between two dates based on a date column.

        query_element_in(column, collection):
            Filters rows where column values are inside a collection.

        reset_index():
            Resets the dataframe index.

        get_column_in_list(column):
            Returns a column as a Python list.

        sort_elements_list(sort_list):
            Sorts the dataframe by the specified columns.

        order_columns(order_list):
            Reorders dataframe columns.

        group_element(group_element):
            Groups the dataframe by the specified column(s).
    """
    def __init__(self, path, df, **kwargs):
        self.path = path
        self.df = df
        self.list = kwargs.get('list') or None
        self.dict = kwargs.get('dict') or None

    def csv_to_df(self):
        self.df = pd.read_csv(self.path, sep=';', encoding='utf-8', index_col=None)
    
    def df_to_csv(self, path):
        self.df.to_csv(path, sep=';', index=False)

    def list_to_df(self):
        self.df = pd.concat(self.list, ignore_index=True)
    
    def dict_to_df(self):
        self.df = pd.DataFrame(self.dict)

    def drop_column(self, column, direction):
        self.df = self.df.drop(column, axis=direction)

    def query_date(self, start_date, end_date, column_name):
        self.df[column_name] = pd.to_datetime(self.df[column_name])

        self.df = self.df.loc[
            (self.df[column_name] >= start_date) &
            (self.df[column_name] <= end_date)
        ]

    def query_element_in(self, column, collection):
        self.df = self.df[self.df[column].isin(collection)]

    def reset_index(self):
        self.df = self.df.reset_index()
    
    def get_column_in_list(self, column):
        return self.df[column].tolist()
    
    def sort_elements_list(self, sort_list):
        self.df = self.df.sort_values(by=sort_list)
    
    def order_columns(self, order_list):
        self.df = self.df[order_list]

    def group_element(self, group_element):
        self.df = self.df.groupby(group_element)

__all__ = [PandasDataframe]
