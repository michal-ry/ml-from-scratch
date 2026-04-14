from ml_from_scratch.statistics.descriptive.mean import mean as fs_mean
import numpy as np


def mean_example():

    '''
    Compare mean calculated from scratch with NumPy
    '''

    numbers = [3, 3, 4, 50]

    from_scratch_mean = fs_mean(numbers)
    numpy_mean = np.mean(numbers)

    print(f'Mean using function from scratch: {from_scratch_mean}')
    print(f'Mean using numpy: {numpy_mean}')

if __name__ == "__main__":
    mean_example()