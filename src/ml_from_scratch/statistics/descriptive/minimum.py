def minimum(numbers):

    '''
    Find the minimum value in a list of numbers.

    Args:
        numbers (list): List of numeric values (int, float).

    Returns:
        number: Minimum value.
    '''

    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list.")

    if not numbers:
        raise ValueError("numbers must not be empty.")
    
    if any(isinstance(n, bool) for n in numbers):
        raise TypeError("numbers must not contain bool values.") 

    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("numbers must contain only int or float values.")
    
    minimum = numbers[0]

    for n in numbers[1:]:
        if n < minimum:
            minimum = n

    return minimum

