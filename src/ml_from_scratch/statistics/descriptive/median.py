def median(numbers):

    '''
    Calculate median of a list of numbers.

    Args:
        numbers (list): List of numeric values (int, float).

    Returns:
        float: Median value.
    '''

    if not isinstance(numbers, list):
        raise TypeError ("numbers must be a list.")
    
    if not numbers:
        raise ValueError ("numbers must not be empty.")
    
    if any(isinstance(n, bool) for n in numbers):
        raise TypeError ("numbers must not contain bool values.") 
    
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError ("numbers must contain only int or float values.")

    numbers_sorted = sorted(numbers)
    n = len(numbers_sorted)
    odd = n % 2 
    

    if odd: 
        position = n // 2
        return numbers_sorted[position]

    else:
        position_1 = n // 2 - 1
        position_2 = n // 2
        return (numbers_sorted[position_1] + numbers_sorted[position_2]) / 2