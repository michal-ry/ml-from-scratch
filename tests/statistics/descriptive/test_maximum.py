import pytest
import re
from ml_from_scratch.statistics.descriptive.maximum import maximum

def test_not_a_list_error():

    numbers = 5
    expected_error = "numbers must be a list."

    with pytest.raises(TypeError, match=re.escape(expected_error)):
        maximum(numbers)

def test_empty_list_error():

    numbers = []
    expected_error = "numbers must not be empty."

    with pytest.raises(ValueError, match=re.escape(expected_error)):
        maximum(numbers)

def test_boolean_error():

    numbers = [1, 2, True]
    expected_error = "numbers must not contain bool values."

    with pytest.raises(TypeError, match=re.escape(expected_error)):
        maximum(numbers)

def test_list_non_numeric_error():

    numbers = [1, 'one']
    expected_error = "numbers must contain only int or float values."

    with pytest.raises(TypeError, match=re.escape(expected_error)):
        maximum(numbers)

def test_list_one_value():

    numbers = [11]

    expected_maximum = 11
    maximum_value = maximum(numbers)

    assert maximum_value == expected_maximum

def test_list_multiple_values():

    numbers = [11, 5, 7, 42]

    expected_maximum = 42
    maximum_value = maximum(numbers)

    assert maximum_value == expected_maximum

def test_list_with_negative_maximum():

    numbers = [-11, -5, -1, -15]

    expected_maximum = -1
    maximum_value = maximum(numbers)

    assert maximum_value == expected_maximum

def test_float_values():

    numbers = [1.1, 2.2, 11.11]

    expected_maximum = 11.11
    maximum_value = maximum(numbers)

    assert maximum_value == expected_maximum

def test_mixed_list():

    numbers = [-1, 0, 5.5, -4.1, 3]

    expected_maximum = 5.5
    maximum_value = maximum(numbers)

    assert maximum_value == expected_maximum

def test_same_values_list():

    numbers = [1, 1, 1]

    expected_maximum = 1
    maximum_value = maximum(numbers)

    assert maximum_value == expected_maximum

def test_maximum_at_the_end():
    
    numbers = [11, 7, 5, 15]

    expected_maximum = 15
    maximum_value = maximum(numbers)

    assert maximum_value == expected_maximum