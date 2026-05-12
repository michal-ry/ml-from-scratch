from ml_from_scratch.statistics.descriptive.mode import mode as fs_mode
import pandas as pd
import numpy as np
import timeit

def mode_benchmark():

    '''
    Benchmark mode from scratch vs Pandas.
    '''

    np.random.seed(42)
    numbers = np.random.randint(0, 20, 100000).tolist()
    numbers_series = pd.Series(numbers)

    from_scratch_time = timeit.timeit(lambda: fs_mode(numbers), number=1000)
    pandas_time = timeit.timeit(lambda: numbers_series.mode(), number=1000)
    ratio = from_scratch_time / pandas_time

    print(f'From scratch time: {from_scratch_time:.2f} seconds')
    print(f'Pandas time: {pandas_time:.2f} seconds')

    if ratio > 1:
        print(f'Pandas is {ratio:.2f}x faster.')
    elif ratio < 1:
        slower_ratio = 1 / ratio
        print(f'Pandas is {slower_ratio:.2f}x slower.')
    else:
        print('Pandas and from scratch are equally fast.')

if __name__ == "__main__":
    mode_benchmark()