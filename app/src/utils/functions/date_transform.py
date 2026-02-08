def transform_date_string_on_number_list(date_str: str) -> dict[str, int]:
    """
    Splits a date string in the format 'YYYY-MM-DD' into 'year', 'month', 'day'.

    Parameters:
        date_str (str): Date string formatted as 'YYYY-MM-DD'.
    
    Returns:
        dict (dict[str, int]): Retorna um dicionário com as chaves 'year', 'month', 'day'.
    """
    date_list = date_str.split('-')

    date_object = {
        'year': int(date_list[0]),
        'month': int(date_list[1]),
        'day': int(date_list[2]),
    }

    return date_object

def get_date_loop(start_year: int, end_year: int, start_month: int, end_month: int, year: int) -> tuple[int, int]:
    """
    Return the interval of months in an loop.

    Parameters:
        start_year (int): 
        end_year (int):
        start_month (int):
        end_month (int):
        year (int):
    
    Returns:
        tuple ([int, int]): (start_month_loop, end_month_loop)
    """
    FIRST_MONTH_YEAR, LAST_MONTH_YEAR = 1, 12
    start_month_loop, end_month_loop = '', ''

    if start_year == year:
        start_month_loop = start_month
    else:
        start_month_loop = FIRST_MONTH_YEAR

    if end_year == year:
        end_month_loop = end_month
    else:
        end_month_loop = LAST_MONTH_YEAR
    
    return [start_month_loop, end_month_loop]

def is_first_date_previous_than_second (first_date: dict[str, int], second_date: dict[str, int]) -> bool:
    """
    Realize a comparison between a date dict and other date dict.

    Parameters:
        first_date (dict [str, int]): 
        second_date (dict[str, int]):
    
    Returns:
        comparison (bool):
    """

    if first_date['year'] > second_date['year']:
        return False
    elif first_date['year'] < second_date['year']:
        return True

    if first_date['month'] > second_date['month']:
        return False
    elif first_date['month'] < second_date['month']:
        return True
    
    if first_date['day'] > second_date['day']:
        return False
    elif first_date['day'] < second_date['day']:
        return True
   
    return False

__all__ = [transform_date_string_on_number_list, get_date_loop, is_first_date_previous_than_second]