import pytest
from ml_from_scratch.statistics.descriptive.range import data_range

def test_list_one_value():

    numbers = [11]

    expected_range = 0
    range_value = data_range(numbers)

    assert range_value == expected_range

def test_list_multiple_values():

    numbers = [11, 5, 7, 42]

    expected_range = 37
    range_value = data_range(numbers)

    assert range_value == expected_range

def test_list_with_negative_numbers():

    numbers = [-11, -5, -1, -15]

    expected_range = 14
    range_value = data_range(numbers)

    assert range_value == expected_range

def test_float_values():

    numbers = [1.1, 2.2, 11.11]

    expected_range = 10.01
    range_value = data_range(numbers)

    assert range_value == pytest.approx(expected_range)

def test_mixed_list():

    numbers = [-1, 0, 5.5, -4.1, 3]

    expected_range = 9.6
    range_value = data_range(numbers)

    assert range_value == pytest.approx(expected_range)

def test_same_values_list():

    numbers = [1, 1, 1]

    expected_range = 0
    range_value = data_range(numbers)

    assert range_value == expected_range