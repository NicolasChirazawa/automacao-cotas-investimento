class CvmLink:
    '''
    Classe para criação de links UVM.

    Attributes:

        url (str): 
           Link pré-settado. 
        zip (str): 
            Extensão do arquivo.
    
    Methods:
        adjust_data(num_month, year): Lê um arquivo CSV baseado no 'path' e preenche o atributo 'df'.
        create_link(month, year): Cria o link e devolve o link 
    '''
    def __init__(self):
        self.url = "https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_"
        self.zip = ".zip"
    
    def adjust_data (self, num_month, year):
        if num_month < 10:
            num_month = '0' + str(num_month)
        
        return [str(num_month), str(year)]
    
    def create_link(self, month, year):
        month = str(month)
        year = str(year)

        uvm_link = self.url + year + month + self.zip
        return uvm_link
    
__all__ = [CvmLink]