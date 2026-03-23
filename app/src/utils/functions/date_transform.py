from datetime import datetime, timedelta

def transform_string_on_number_list(date_str: str) -> dict[str, int]:
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

def transform_string_into_date(date_str: str) -> datetime:
    '''
    Convert a string into a date

    Parameters:
        date_str (str): Date string in format YY-MM-DD.
    
    Returns:
        date: Return a date in format YY-MM-DD.
    '''
    format = "%Y-%m-%d"
    return datetime.strptime(date_str, format).date()

def transform_date_into_string(date: datetime) -> str:
    '''
    Convert a date into a string

    Parameters:
        date (str): Date in format YY-MM-DD.
    
    Returns:
        date: Return a date string in format YY-MM-DD.
    '''
    format = "%Y-%m-%d"
    return datetime.strftime(date, format)

def add_days_on_date (date: datetime, days: int) -> datetime:
    '''
    Add days on a date

    Parameters:
        date (datetime): Date string in format YY-MM-DD.
        days (int): Days to add
    
    Returns:
        datetime: Return a datetime in format YY-MM-DD.
    '''
    return date + timedelta(days=days)

def subtract_days_on_date (date: datetime, days: int) -> datetime:
    '''
    Subtract days on a date

    Parameters:
        date (datetime): Date string in format YY-MM-DD.
        days (int): Days to subtract
    
    Returns:
        datetime: Return a datetime in format YY-MM-DD.
    '''
    return date - timedelta(days=days)

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

def calculate_days(start_str_date, end_str_date):
    
    start_date = transform_string_into_date(start_str_date)
    end_date   = transform_string_into_date(end_str_date)

    if start_date > end_date:
        raise Exception(
            "\nStart date: " + str(start_date) + 
            "\nEnd date: " + str(end_date) +
            "\nThe start date is greater than end date."
        )
    
    start_date_list = transform_string_on_number_list(start_str_date)
    end_date_list  = transform_string_on_number_list(end_str_date)
    
    sum_days = 0
    while (True):
        if (start_date_list['year'] == end_date_list['year'] and start_date_list['month'] == end_date_list['month']):
            sum_days += (end_date_list['day'] - start_date_list['day'])
            break

        final_day = final_day_of_month(start_date_list['month'], start_date_list['year'])

        if (start_date_list['day'] != 1):
            sum_days += (final_day - start_date_list['day'] + 1)
            start_date_list['day'] = 1
        else:
            sum_days += final_day
        
        start_date_list['month'] += 1
        if start_date_list['month'] > 12:
            start_date_list['month'] = 1
            start_date_list['year'] += 1
        
    return sum_days

def final_day_of_month (month: int, year: int) -> int:
    '''
    Determine how many days a given month has.

    Parameters:
        month (int): The month (1-12).
        year (int): The year.
    
    Returns:
        int: Number of the days in the given month
    '''

    if(month < 1 or month > 12):
        raise ValueError("Month must be between 1 and 12")

    if (month == 2):
        is_leap_year = is_a_leap_year(year)
        
        if is_leap_year == True:
            return 29
        else:
            return 28

    month_final_day = {
        1: 31,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    return month_final_day[month]

def is_a_leap_year (year: int) -> bool:
    '''
    Determine whether a given year is a leap year.

    Parameters:
        year (int): The year to be evaluated.
    
    Returns:
        bool: 'True' if the year is a leap year, 'False' otherwise
    '''
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    
    return False

__all__ = [ 
    "transform_string_on_number_list", 
    "transform_string_into_date", 
    "transform_date_into_string", 
    "get_date_loop", 
    "calculate_days", 
    "final_day_of_month", 
    "is_a_leap_year", 
    "add_days_on_date", 
    "subtract_days_on_date" 
]