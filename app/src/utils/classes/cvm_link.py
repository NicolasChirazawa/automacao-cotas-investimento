class CvmLink:
    """
    Class responsible for generating CVM dataset download links.

    Attributes:
        url (str):
            Base URL for CVM dataset downloads.

        zip_extension (str):
            File extension for the compressed dataset.

    Methods:
        adjust_data(num_month, year):
            Formats the month and year values, ensuring the month has two digits.

        create_link(month, year):
            Creates and returns the CVM dataset download link.
    """

    def __init__(self):
        self.url = "https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_"
        self.zip = ".zip"
    
    def adjust_data (self, num_month, year):
        if num_month < 10:
            num_month = '0' + str(num_month)
        
        return (str(num_month), str(year))
    
    def create_link(self, month, year):
        month = str(month)
        year = str(year)

        cvm_link = self.url + year + month + self.zip
        return cvm_link
    
__all__ = [ "CvmLink" ]