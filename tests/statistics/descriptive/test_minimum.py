import pytest
import re
from ml_from_scratch.statistics.descriptive.minimum import minimum

def test_not_a_list_error():

    numbers = 10
    expected_error = "numbers must be a list."

    with pytest.raises(TypeError, match=re.escape(expected_error)):
        minimum(numbers)

def test_empty_list_error():

    numbers = []
    expected_error = "numbers must not be empty."

    with pytest.raises(ValueError, match=re.escape(expected_error)):
        minimum(numbers)

def test_boolean_error():

    numbers = [1, True]
    expected_error = "numbers must not contain bool values."

    with pytest.raises(TypeError, match=re.escape(expected_error)):
        minimum(numbers)

def test_list_non_numeric_error():

    numbers = [1, 'one']
    expected_error = "numbers must contain only int or float values."

    with pytest.raises(TypeError, match=re.escape(expected_error)):
        minimum(numbers)

def test_list_one_value():

    numbers = [11]

    expected_minimum = 11
    minimum_value = minimum(numbers)

    assert minimum_value == expected_minimum

def test_list_multiple_values():

    numbers = [11, 5, 7, 42]

    expected_minimum = 5
    minimum_value = minimum(numbers)

    assert minimum_value == expected_minimum

def test_list_with_negative_minimum():

    numbers = [-11, 0, 1, 11]

    expected_minimum = -11
    minimum_value = minimum(numbers)

    assert minimum_value == expected_minimum

def test_float_values():

    numbers = [1.1, 2.2, 11.11]

    expected_minimum = 1.1
    minimum_value = minimum(numbers)

    assert minimum_value == expected_minimum

def test_mixed_list():

    numbers = [-1, 0, 5.5, -4.1, 3]

    expected_minimum = -4.1
    minimum_value = minimum(numbers)

    assert minimum_value == expected_minimum

def test_same_values_list():

    numbers = [1, 1, 1]

    expected_minimum = 1
    minimum_value = minimum(numbers)

    assert minimum_value == expected_minimum

def test_minimum_at_the_end():
    
    numbers = [11, 7, 5, -2]

    expected_minimum = -2
    minimum_value = minimum(numbers)

    assert minimum_value == expected_minimum