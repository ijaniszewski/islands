
import numpy as np
from src.calculate_islands import CalculateIslands


def generate_whole_map(values=[0, 1]):
    whole_map = []
    for row in range(10):
        row_ = np.random.choice(values, size=(10,))
        row_ = list(row_)
        row_ = "".join(str(v) for v in row_)
        whole_map.append(row_)
    return whole_map


def create_counter(input_file):
    ci = CalculateIslands()
    counter = ci.run(input_file)
    return counter


def assert_counter(values, counter):
    input_file = generate_whole_map(values=[values])
    counter = create_counter(input_file)
    assert counter == counter


def test_if_counter_is_integer():
    input_file = generate_whole_map()
    counter = create_counter(input_file)
    assert type(counter) == int


def test_only_ones():
    assert_counter(1, 1)


def test_only_zeros():
    assert_counter(0, 0)


def test_only_ones_one_zero():
    input_file = generate_whole_map(values=[0])
    input_file[0] = '1' + input_file[0][1:]
    counter = create_counter(input_file)
    assert counter == 1


def test_only_zeros_one_one():
    input_file = generate_whole_map(values=[1])
    input_file[0] = '0' + input_file[0][1:]
    counter = create_counter(input_file)
    assert counter == 1
