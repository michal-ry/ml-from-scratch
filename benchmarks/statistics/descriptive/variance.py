import numpy as np
import timeit

from ml_from_scratch.statistics.descriptive.variance import variance_sample


def variance_benchmark():

    '''
    Benchmark sample variance from scratch vs NumPy.
    '''

    np.random.seed(42)

    numbers = np.random.randint(-100, 100, size=100000)
    numbers_list = numbers.tolist()

    from_scratch_time = timeit.timeit(lambda: variance_sample(numbers_list), number=1000)
    numpy_time = timeit.timeit(lambda: np.var(numbers, ddof=1), number=1000)

    ratio = from_scratch_time / numpy_time

    print(f'From scratch time: {from_scratch_time:.2f} seconds')
    print(f'NumPy time: {numpy_time:.2f} seconds')

    if ratio > 1:
        print(f'NumPy is {ratio:.2f}x faster.')
    elif ratio < 1:
        slower_ratio = 1 / ratio
        print(f'NumPy is {slower_ratio:.2f}x slower.')
    else:
        print('NumPy and from scratch are equally fast.')


if __name__ == "__main__":
    variance_benchmark()