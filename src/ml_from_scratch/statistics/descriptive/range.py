from ml_from_scratch.statistics.descriptive.maximum import maximum
from ml_from_scratch.statistics.descriptive.minimum import minimum

def data_range(numbers):

    '''
    Calculate the range of a list of numbers.

    Args:
        numbers (list): List of numeric values (int, float).

    Returns:
        number: Difference between maximum and minimum value.
    '''
    
    return maximum(numbers) - minimum(numbers)