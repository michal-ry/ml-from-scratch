def mean(numbers):

    '''
    Calculate mean of a list of numbers.

    Args:
        numbers (list): List of numeric values (int, float).

    Returns:
        float: Mean value.
    '''

    if not isinstance(numbers, list):
        raise TypeError ("numbers must be a list.")
    
    if not numbers:
        raise ValueError ("numbers must not be empty.")
    
    if any(isinstance(n, bool) for n in numbers):
        raise TypeError ("numbers must not contain bool values.") 
    
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError ("numbers must contain only int or float values."))

    numbers_len = len(numbers)
    numbers_sum = sum(numbers)

    result = numbers_sum/numbers_len

    return result