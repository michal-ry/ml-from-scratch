import re

import pytest

from ml_from_scratch.statistics.descriptive.variance import variance_sample


def test_sample_variance_numbers_not_a_list_error():

    numbers = 10
    expected_error = "numbers must be a list."

    with pytest.raises(TypeError, match=re.escape(expected_error)):
        variance_sample(numbers=numbers)


def test_sample_variance_list_with_one_value_error():

    numbers = [10]
    expected_error = "numbers must contain at least 2 values."

    with pytest.raises(ValueError, match=re.escape(expected_error)):
        variance_sample(numbers=numbers)


def test_sample_variance_bool_value_error():

    numbers = [True, False]
    expected_error = "numbers must contain numerical values only."

    with pytest.raises(TypeError, match=re.escape(expected_error)):
        variance_sample(numbers=numbers)


def test_sample_variance_non_numeric_value_error():

    numbers = ['one', 'two']
    expected_error = "numbers must contain numerical values only."

    with pytest.raises(TypeError, match=re.escape(expected_error)):
        variance_sample(numbers=numbers)


def test_sample_variance_for_positive_integers():

    numbers = [2, 4, 6, 8, 10]
    expected_variance = 10

    sample_variance = variance_sample(numbers)

    assert sample_variance == pytest.approx(expected_variance)


def test_sample_variance_for_mixed_sign_integers():

    numbers = [-2, 4, 4, 6]
    expected_variance = 12

    sample_variance = variance_sample(numbers)

    assert sample_variance == pytest.approx(expected_variance)


def test_sample_variance_for_float_values():

    numbers = [1.5, 2.5, 3.5, 4.5]
    expected_variance = 5 / 3

    sample_variance = variance_sample(numbers)

    assert sample_variance == pytest.approx(expected_variance)


def test_sample_variance_for_mixed_int_and_float_values():

    numbers = [1, 2.5, 4, 5.5]
    expected_variance = 3.75

    sample_variance = variance_sample(numbers)

    assert sample_variance == pytest.approx(expected_variance)


def test_sample_variance_for_two_values():

    numbers = [2, 8]
    expected_variance = 18

    sample_variance = variance_sample(numbers)

    assert sample_variance == pytest.approx(expected_variance)


def test_sample_variance_for_identical_values():

    numbers = [2, 2, 2, 2]
    expected_variance = 0

    sample_variance = variance_sample(numbers)

    assert sample_variance == pytest.approx(expected_variance)