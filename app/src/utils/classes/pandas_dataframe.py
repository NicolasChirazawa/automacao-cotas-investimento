import pandas as pd

class PandasDataframe:
    '''
    Classe para padronizar e acelerar a construção de 'Dataframes'.

    Attributes:

        path (str): 
            Guardo o caminho absoluto da origem de seu conteúdo.
        df (Dataframe): 
            Pandas 'dataframe'.
    
    Methods:
        csv_to_df(): Lê um arquivo CSV baseado no 'path' e preenche o atributo 'df'.
        df_to_csv(path): Exporta o DataFrame atual para um arquivo CSV.
        dict_to_df(data_dict): Converte um dicionário Python num DataFrame.
        drop_column(column, direction): Remove colunas ou linhas específicas.
        query_date(start_date, end_date, column): Filtra o DataFrame sobre um intervalo de datas.
        query_element_in(column, collection): Filtra linhas onde o valor da coluna está na lista.
        reset_index(): Reinicia o índice do DataFrame.
        sort_elements_list(sort_list): Ordena as linhas com base em colunas específicas.
        order_columns(order_list): Reorganiza a sequência das colunas no DataFrame.
        group_element(group_element): Agrupa os dados
    '''
    def __init__(self, path, df):
        self.path = path
        self.df = df

    def csv_to_df(self):
        self.df = pd.read_csv(self.path, sep=';', encoding='utf-8', index_col=None)
    
    def df_to_csv(self, path):
        self.df.to_csv(path, sep=';', index=False)
    
    def dict_to_df(self, dict):
        self.df = pd.DataFrame(dict)

    def drop_column(self, column, direction):
        self.df = self.df.drop(column, axis=direction)

    def query_date(self, start_date, end_date, column):
        self.df[column] = pd.to_datetime(self.df[column])

        self.df = self.df.loc[
            (self.df[column] >= start_date) &
            (self.df[column] <= end_date)
        ]

    def query_element_in(self, column, collection):
        self.df = self.df[self.df[column].isin(collection)]

    def reset_index(self):
        self.df = self.df.reset_index()
    
    def sort_elements_list(self, sort_list):
        self.df = self.df.sort_values(by=sort_list)
    
    def order_columns(self, order_list):
        self.df = self.df[order_list]

    def group_element(self, group_element):
        self.df = self.df.groupby(group_element)

__all__ = [PandasDataframe]
