class IpeaLink:
    '''
    Classe para criação de links UVM.

    Attributes:

        url (str):
            Link pré-settado.
        api (str): 
           Caminho da API.
        extension (str): 
            Endereço da API.
    
    Methods:
        adjust_data(num_month, year): Lê um arquivo CSV baseado no 'path' e preenche o atributo 'df'.
        create_link(month, year): Cria o link e devolve o link 
    '''
    def __init__(self, api, extension):
        self.url = "https://www.ipeadata.gov.br/api/odata4/Metadados"
        self.api = api
        self.extension = extension
    
    def create_link(self):
        return self.url + self.api + self.extension
    
__all__ = [IpeaLink]