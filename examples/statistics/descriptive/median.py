from ml_from_scratch.statistics.descriptive.median import median as fs_median
import numpy as np

def median_example():

    '''
    Compare median calculated from scratch with NumPy.
    '''

    odd_list = [1, 2, 3, 4 ,5]
    even_list = [3, 4, 1, 2]

    fs_median_odd = fs_median(odd_list)
    np_median_odd = np.median(odd_list)

    fs_median_even = fs_median(even_list)
    np_median_even = np.median(even_list)

    print('Odd list:')
    print(f'Median using function from scratch: {fs_median_odd}')
    print(f'Median using numpy: {np_median_odd}')

    print()
    print('Even list:')
    print(f'Median using function from scratch: {fs_median_even}')
    print(f'Median using numpy: {np_median_even}')

if __name__ == '__main__':
    median_example()