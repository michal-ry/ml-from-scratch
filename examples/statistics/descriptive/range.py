import numpy as np
from ml_from_scratch.statistics.descriptive.range import data_range

def data_range_example():

    '''
    Compare range calculated from scratch with NumPy.
    '''

    np.random.seed(42)

    numbers = np.random.randint(-50, 50, size=30)
    numbers_list = numbers.tolist()

    numpy_range = np.max(numbers) - np.min(numbers)
    from_scratch_range = data_range(numbers_list)

    print(f'Range using function from scratch: {from_scratch_range}')
    print(f'Range using NumPy: {numpy_range}')

if __name__ == '__main__':
    data_range_example()