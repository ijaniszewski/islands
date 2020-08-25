import pytest

from src.calculate_islands import CalculateIslands


def count_counter_from_example(example_no: str) -> int:
    """Create counter from given example number.

    From given txt files in examples directory create counter from CalculateIslands object.

    Parameters
    ----------
    example_no: str
        Number of example file

    Return
    ----------
    counter: int
        Number of islands in a given txt file
    """
    input_file_path = f"examples/ex{example_no}.txt"
    input_file = open(input_file_path, "r").readlines()
    ci = CalculateIslands()
    counter = ci.run(input_file)
    return counter


def test_example_1():
    """Test for example 1."""
    counter = count_counter_from_example('1')
    assert counter == 5


def test_example_2_value_error():
    """Test for example 2 - not onlu 1s and 0s in given txt file."""
    with pytest.raises(ValueError) as e:
        count_counter_from_example('2')
    assert str(
        e.value) == "There is at least one element that is not zero or one: {'z'}"


def test_example_3():
    """Test for example 3."""
    counter = count_counter_from_example('3')
    assert counter == 21


def test_example_4():
    """Test for example 4."""
    counter = count_counter_from_example('4')
    assert counter == 1
