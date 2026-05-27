def maximum(numbers):

    '''
    Find the largest value in a list of numbers.

    Args:
        numbers (list): List of numeric values (int, float).

    Returns:
        number: Maximum value.
    '''

    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list.")
    
    if not numbers:
        raise ValueError("numbers must not be empty.")
    
    if any(isinstance(n, bool) for n in numbers):
        raise TypeError("numbers must not contain bool values.")
    
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("numbers must contain only int or float values.")
    
    maximum = numbers[0]

    for n in numbers[1:]:
        if n > maximum:
            maximum = n

    return maximum

