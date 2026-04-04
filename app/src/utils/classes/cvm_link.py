class CvmLink:
    """
    Class responsible for generating CVM dataset download links.

    Attributes:
        url (str):
            Base URL for CVM dataset downloads.

        zip_extension (str):
            File extension for the compressed dataset.
    """

    def __init__(self):
        self.url = "https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_"
        self.zip = ".zip"
    
    def adjust_data(self, num_month, year):
        """
        Formats the month and year values, ensuring the month has two digits.

        Args:
            num_month (int):
                Month value.

            year (int or str):
                Year value.

        Returns:
            tuple:
                A tuple containing the formatted month and year as strings.
        """
        if num_month < 10:
            num_month = '0' + str(num_month)
        
        return (str(num_month), str(year))
    
    def create_link(self, month, year):
        """
        Creates the CVM dataset download link based on the given month and year.

        Args:
            month (int or str):
                Month value.

            year (int or str):
                Year value.

        Returns:
            str:
                Complete URL for downloading the dataset.
        """
        month = str(month)
        year = str(year)

        cvm_link = self.url + year + month + self.zip
        return cvm_link
    

__all__ = ["CvmLink"]