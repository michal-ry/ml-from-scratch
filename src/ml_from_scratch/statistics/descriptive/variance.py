from ml_from_scratch.statistics.descriptive.mean import mean


def variance_sample(numbers):

    '''
    Calculate the sample variance of a list of numbers.

    Args:
        numbers (list): List of numeric values (int, float).

    Returns:
        number: Sample variance.
    '''

    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list.")
    
    if len(numbers) < 2:
        raise ValueError("numbers must contain at least 2 values.")
    
    if any(isinstance(n, bool) for n in numbers):
        raise TypeError("numbers must contain numerical values only.")
    
    if not all(isinstance(n, (float, int)) for n in numbers):
        raise TypeError("numbers must contain numerical values only.")
    
    n = len(numbers)
    
    numbers_mean = mean(numbers)
    
    squared_deviations = [(number - numbers_mean) ** 2 for number in numbers]
    sum_of_squared_deviations = sum(squared_deviations)

    return sum_of_squared_deviations / (n - 1)