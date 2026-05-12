import pytest
import re
from ml_from_scratch.statistics.descriptive.mode import mode

def test_not_a_list_error():

    elements = 5
    expected_error = "elements must be a list."

    with pytest.raises(TypeError, match=re.escape(expected_error)):
        mode(elements)

def test_empty_list_error():

    elements = []
    expected_error = "elements must not be empty."

    with pytest.raises(ValueError, match=re.escape(expected_error)):
        mode(elements)

def test_bool_values_error():

    elements = [True]
    expected_error = "elements must not contain bool values."

    with pytest.raises(TypeError, match=re.escape(expected_error)):
        mode(elements)

def test_mode_for_numerical_values():

    elements = [1, 2, 3, 1]

    mode_elements = mode(elements)
    mode_expected = [1]

    assert mode_elements == mode_expected

def test_mode_for_categorical_values():

    elements = ['Natalia', 'Marek', 'Michal', 'Agata', 'Michal']

    mode_elements = mode(elements)
    mode_expected = ['Michal']

    assert mode_elements == mode_expected

def test_mode_returns_multiple_modes():

    elements = ['Michal', 'Natalia', 'Michal', 'Natalia']

    mode_elements = mode(elements)
    mode_expected = ['Michal', 'Natalia']

    assert mode_expected == mode_elements

def test_mode_for_mixed_values():

    elements = [1, 'Michal', 'Michal']

    mode_elements = mode(elements)
    mode_expected = ['Michal']

    assert mode_elements == mode_expected

def test_mode_all_unique_values():

    elements = [1, 2, 3]

    mode_elements = mode(elements)
    mode_expected = [1, 2, 3]

    assert mode_elements == mode_expected