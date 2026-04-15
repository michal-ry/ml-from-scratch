from ml_from_scratch.statistics.descriptive.median import median as fs_median
import numpy as np
import timeit

def median_benchmark():

    '''
    Benchmark median from scratch vs NumPy.
    '''

    np.random.seed(42)
    numbers = np.random.randint(0, 100000, 100000).tolist()

    from_scratch_time = timeit.timeit(lambda: fs_median(numbers), number=1000)
    numpy_time = timeit.timeit(lambda: np.median(numbers), number=1000)
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
    median_benchmark()