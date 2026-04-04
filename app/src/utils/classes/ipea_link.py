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
    """

    def __init__(self, api, extension):
        self.url = "https://www.ipeadata.gov.br/api/odata4/Metadados"
        self.api = api
        self.extension = extension
    
    def create_link(self):
        """
        Creates the full API request link.

        Returns:
            str:
                Complete URL for the API request.
        """
        return self.url + self.api + self.extension
    

__all__ = ["IpeaLink"]