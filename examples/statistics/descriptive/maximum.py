import numpy as np
from ml_from_scratch.statistics.descriptive.maximum import maximum

def maximum_example():

    '''
    Compare maximum calculated from scratch with NumPy.
    '''

    np.random.seed(42)

    numbers = np.random.randint(-50, 50, size=30)
    numbers_list = numbers.tolist()

    numpy_max = np.max(numbers)
    from_scratch_max = maximum(numbers_list)

    print(f'Maximum using function from scratch: {from_scratch_max}')
    print(f'Maximum using NumPy: {numpy_max}')

if __name__ == '__main__':
    maximum_example()