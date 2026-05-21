import numpy as np
from ml_from_scratch.statistics.descriptive.minimum import minimum

def minimum_example():

    '''
    Compare minimum calculated from scratch with NumPy.
    '''

    np.random.seed(42)

    numbers = np.random.randint(-50, 50, size=30)
    numbers_list = numbers.tolist()

    numpy_min = np.min(numbers)
    from_scratch_min = minimum(numbers_list)

    print(f'Minimum using function from scratch: {from_scratch_min}')
    print(f'Minimum using NumPy: {numpy_min}')

if __name__ == '__main__':
    minimum_example()