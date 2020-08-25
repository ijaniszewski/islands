
import numpy as np
from src.calculate_islands import CalculateIslands


ci = CalculateIslands()


def generate_whole_map(columns=10, rows=10):
    whole_map = []
    for row in range(rows):
        row_ = np.random.choice([0, 1], size=(columns,), p=[1./3, 2./3])
        row_ = list(row_)
        row_ = "".join(str(v) for v in row_)
        whole_map.append(row_)
    return whole_map


def test_sample():
    input_file = generate_whole_map()
    counter = ci.create_whole_map(input_file)
    assert type(counter) == int
    assert counter == 'tak'
