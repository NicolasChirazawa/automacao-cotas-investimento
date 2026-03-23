class IpeaLink:
    """
    Class responsible for generating IPEA API request links.

    Attributes:
        url (str):
            Base URL for the IPEA API.

        api (str):
            API endpoint path.

        extension (str):
            Data format or query extension.

    Methods:
        create_link():
            Creates and returns the full API request link.
    """
    def __init__(self, api, extension):
        self.url = "https://www.ipeadata.gov.br/api/odata4/Metadados"
        self.api = api
        self.extension = extension
    
    def create_link(self):
        return self.url + self.api + self.extension
    
__all__ = [ "IpeaLink" ]