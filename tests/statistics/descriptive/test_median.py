import pytest
from ml_from_scratch.statistics.descriptive.median import median

def test_not_a_list():
    
    invalid_input = 5

    with pytest.raises(TypeError):
        median(invalid_input)

def test_empty_list():

    empty_list = []

    with pytest.raises(ValueError):
        median(empty_list)

def test_list_with_boolean():

    bool_list = [1, 5, True]

    with pytest.raises(TypeError):
        median(bool_list)

def test_list_non_numeric():

    non_numeric_list = [1, 5, 'two']

    with pytest.raises(TypeError):
        median(non_numeric_list)

def test_median_odd():

    numbers = [1, 2, 3, 4, 5]

    numbers_median = median(numbers)
    expected_median = 3

    assert numbers_median == expected_median

def test_median_even():

    numbers = [1, 2, 3, 4]

    numbers_median = median(numbers)
    expected_median = 2.5

    assert numbers_median == expected_median

def test_median_single_number():

    numbers = [1]

    numbers_median = median(numbers)
    expected_median = 1

    assert numbers_median == expected_median

def test_median_unsorted():

    numbers = [5, 1, 2, 4, 3]

    numbers_median = median(numbers)
    expected_median = 3

    assert numbers_median == expected_median