import pytest
from ml_from_scratch.statistics.descriptive.descriptive import mean

def test_not_a_list():
    
    invalid_input = 5

    with pytest.raises(TypeError):
        mean(invalid_input)

def test_empty_list():

    empty_list = []

    with pytest.raises(ValueError):
        mean(empty_list)

def test_list_with_boolean():

    bool_list = [1, 5, True]

    with pytest.raises(TypeError):
        mean(bool_list)

def test_list_non_numeric():

    non_numeric_list = [1, 5, 'two']

    with pytest.raises(TypeError):
        mean(non_numeric_list)

def test_return_correct_mean_for_int():

    numbers = [3, 3, 4, 50]
    expected = 15.0
    result = mean(numbers)

    assert result == expected

def test_return_correct_mean_for_float():

    numbers = [2.5, 3.5, 3.5, 50.5]
    expected = 15.0
    result = mean(numbers)

    assert result == expected

def test_return_correct_mean_for_mixed_values():

    numbers = [2.5, 3, 4.5, 50]
    expected = 15.0
    result = mean(numbers)

    assert result == expected

def test_return_correct_mean_for_single_value():
    
    numbers = [15]
    expected = 15.0
    result = mean(numbers)

    assert result == expected

def test_return_float():

    numbers = [3, 3, 4, 50]
    result = mean(numbers)

    assert isinstance(result, float)
