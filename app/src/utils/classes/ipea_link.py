class IpeaLink:
    '''
    Class responsable for creating an IPEA link.

    Attributes:

        url (str):
           Link.
        api (str): 
           API url.
        extension (str): 
            API data extension.
    
    Methods:
        adjust_data(num_month, year): Read a '.csv' archive using the 'path'.
        create_link(month, year): Create and return a link.
    '''
    def __init__(self, api, extension):
        self.url = "https://www.ipeadata.gov.br/api/odata4/Metadados"
        self.api = api
        self.extension = extension
    
    def create_link(self):
        return self.url + self.api + self.extension
    
__all__ = [IpeaLink]