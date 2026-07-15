import numpy as np

from ml_from_scratch.statistics.descriptive.variance import variance_sample


def variance_example():

    '''
    Compare sample variance calculated from scratch with NumPy.
    '''

    np.random.seed(42)

    numbers = np.random.randint(-20, 20, size=500)
    numbers_list = numbers.tolist()

    from_scratch_sample_variance = variance_sample(numbers_list)
    np_sample_variance = np.var(numbers, ddof=1)

    print(
        f'Sample variance using function from scratch: '
        f'{from_scratch_sample_variance}'
    )
    print(f'Sample variance using NumPy: {np_sample_variance}')


if __name__ == '__main__':
    variance_example()