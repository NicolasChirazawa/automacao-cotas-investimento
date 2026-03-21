def income_tax_calculation(sum_days: int) -> float:

    '''
    Calculate the income tax rate based on the duration in days.

    Parameters:
        sum_days (int): Total days of the operation.

    Returns:
        float: Tax rate percentage.
    '''
    if (sum_days < 0):
        raise ValueError("'sumDays' can be only non-negative values")

    if sum_days <= 180:
        return 22.5
    elif sum_days <= 360:
        return 20.0
    elif sum_days <= 720:
        return 17.5
    else:
        return 15.0
    
def iof_tax_calculation(sum_days: int) -> float:

    '''
    Calculate the iof tax rate based on the duration in days.

    Parameters:
        sum_days (int): Total days of the operation.

    Returns:
        float: Tax rate percentage.
    '''
    if (sum_days < 0):
        raise ValueError("'sumDays' can be only non-negative values")

    percentage_base = 96
    MULTIPLICATION = 3

    tax_rate = percentage_base - (MULTIPLICATION * sum_days)

    if tax_rate < 0:
        return 0
    else:
        return tax_rate

__all__ = [income_tax_calculation, iof_tax_calculation]