import datetime

class Errors_Redeem_Simulation:

    # Date Init: 

    def dto_invalid_date_init_before_row_start(self, str_investment_start: str, new_date_investment_start: datetime, date_first_row: datetime, DATE_OFFSET: int):
        return {
            'str_investment_start': str_investment_start, 
            'str_new_investment_start': str(new_date_investment_start), 
            'str_first_row': str(date_first_row), 
            'str_offset': str(DATE_OFFSET)
        }

    def str_invalid_date_init_before_row_start(self, str_investment_start, str_new_investment_start, str_first_row, str_offset):
        return(
            "\nInvestment Date Start: " + str_investment_start + 
            "\nDate Offset: " + str_offset +
            "\nInvestment Date Start + Offset: " + str_new_investment_start +
            "\nFirst Row Date: " + str_first_row +
            "\n'Investment Date Start + Offset' inits before the 'First Row Date'." +
            "\n Hit: Processing data (START_DATE) is later than 'PURCHASE_DATE'"
        )
    
    def dto_invalid_date_init_after_row_end(self, str_investment_start: str, last_row_date: int):
        return {
            'str_investment_start': str_investment_start, 
            'str_last_row_date': str(last_row_date), 
        }

    def str_invalid_date_init_after_row_end(self, str_investment_start, str_last_row_date):
        return(
            "\nInvestment Date Start: " + str_investment_start + 
            "\nLast row date: " + str_last_row_date +
            "\n'Investment Date' inits after the 'Last Row Date'." +
            "\n Hit: Processing data (END_DATE) is earlier than 'PURCHASE_DATE'"
        )
    
    def dto_invalid_date_init_quota_adjust(self, str_investment_start: str, last_row_date: datetime, COTA_APLICACAO):
        return {
            'str_investment_start': str_investment_start, 
            'str_last_row': str(last_row_date), 
            'index_cota_aplicacao': str(COTA_APLICACAO)
        }

    def str_invalid_date_init_quota_adjust(self, str_investment_start, str_last_row, index_cota_aplicacao):
        return(
            "\nInvestment Date Start + Quota Index Aplicacao: " + str_investment_start + " D+" + index_cota_aplicacao +
            "\nLast row date: " + str_last_row +
            "\nInvestment Date Start + Quota Index Aplicacao' inits after the 'Last Row Date'."
            "\nHit: Processing data (END_DATE) is earlier than 'PURCHASE_DATE' + 'INVESTMENT_QUOTA'"
        )

    # Date End: 

    def dto_invalid_date_end_before_row_start(self, str_investment_end: str, first_row_date: datetime):
        return {
            'str_investment_end': str_investment_end, 
            'str_first_row_date': str(first_row_date), 
        }

    def str_invalid_date_end_before_row_start(self, str_investment_end, str_first_row_date):
        return(
            "\nInvestment Date End: " + str_investment_end + 
            "\nFirst Row Date: " + str_first_row_date +
            "\n'Investment Date End' inits before the 'First Row Date'." +
            "\n Hit: Processing data (START_DATE) is later than 'SOLD_DATE'"
        )

    def dto_invalid_date_end_after_row_end(self, last_row_date: datetime, date_investment_end: datetime):
        return {
            'str_last_row': str(last_row_date), 
            'str_investment_end': str(date_investment_end), 
        }

    def str_invalid_date_end_after_row_end(self, str_last_row, str_investment_end):
        return(
            "\nInvestment Date End: " + str_last_row + 
            "\nLast Row Date: " + str_investment_end +
            "\n'Investment Date End' ends after the 'Last Row Date'."
            "\n Hit: Processing data (END_DATE) is earlier than 'SOLD_DATE'"
        )

    def dto_invalid_date_end_quota_adjust(self, str_investment_end: str, last_row_date: datetime, COTA_RESGATE: int):
        return {
            'str_investment_end': str_investment_end, 
            'str_last_row': str(last_row_date), 
            'index_cota_resgate': str(COTA_RESGATE)
        }

    def str_invalid_date_end_quota_adjust(self, str_investment_end, str_last_row, index_cota_resgate):
        return(
            "\nInvestment Date Start + Quota Index Resgate: " + str_investment_end + " D+" + index_cota_resgate +
            "\nLast Row Date: " + str_last_row +
            "\n'Investment Date End' ends after the 'Last Row Date'.",
            "\nHit: Processing data (END_DATE) is earlier than 'SOLD_DATE' + 'REDEEM_QUOTA'"
        )

    # Date Init X Date End:

    def dto_conflict_date_start_end(self, str_investment_start_quota: str, str_investment_end: str):
        return {
            'str_investment_start_quota': str_investment_start_quota, 
            'str_investment_end': str_investment_end, 
        }

    def str_conflict_date_start_end(self, str_investment_start_quota, str_investment_end):
        return(
            "\nInvestment Date Start + Quota Index Aplicacao: " + str_investment_start_quota + 
            "\nInvestment Date End: " + str_investment_end +
            "\n'Investment Date End' starts before the 'Investment Date Start + Quota Index Aplicacao'.",
            "\nHit: Adjust 'PURCHASE_DATE + INVESTMENT_QUOTA' to 'SOLD_DATE'"
        )

_all_ = [ Errors_Redeem_Simulation ]