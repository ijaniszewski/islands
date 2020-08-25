
import numpy as np
from src.calculate_islands import CalculateIslands


def generate_whole_map(values: list = [0, 1]) -> list:
    """Generate list of strings based on given values.

    Parameters
    ----------
    values: list
        Default: 0s and 1s

    Return
    ----------
    whole_map: list
        List of strings with 1s and 0s, i.e. ['101', '000']
    """
    whole_map = []
    for row in range(10):
        row_ = np.random.choice(values, size=(10,))
        row_ = list(row_)
        row_ = "".join(str(v) for v in row_)
        whole_map.append(row_)
    return whole_map


def create_counter(input_file: list) -> int:
    """Initialize CalculateIslands object and call run method to get counter.

    Parameters
    ----------
    input_file: list
        List of strings with 1s and 0s, i.e. ['101', '000']

    Return
    ----------
    counter: int
        Counter from run method (CalculateIslands object) based on input_file
    """
    ci = CalculateIslands()
    counter = ci.run(input_file)
    return counter


def assert_counter(values: list, counter: int) -> None:
    """Assert if counter is as expected.

    Parameters
    ----------
    values: list
        List of values to create whole map
    counter: int
        Expected counter
    """
    input_file = generate_whole_map(values=[values])
    counter = create_counter(input_file)
    assert counter == counter


def test_if_counter_is_integer():
    """Test if obtained counter is integer."""
    input_file = generate_whole_map()
    counter = create_counter(input_file)
    assert type(counter) == int


def test_only_ones():
    "Test if counter is 1 when only 1s in matrix."
    assert_counter(1, 1)


def test_only_zeros():
    "Test if counter is 0 when only 0s in matrix."
    assert_counter(0, 0)


def test_only_zeros_one_one():
    "Test if counter is 1 when only 0s with one 1 in matrix."
    input_file = generate_whole_map(values=[0])
    input_file[0] = '1' + input_file[0][1:]
    counter = create_counter(input_file)
    assert counter == 1


def test_only_ones_one_zero():
    "Test if counter is 1 when only 1s with one 0 in matrix."
    input_file = generate_whole_map(values=[1])
    input_file[0] = '0' + input_file[0][1:]
    counter = create_counter(input_file)
    assert counter == 1
