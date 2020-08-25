from dataclasses import dataclass, field
from typing import List


@dataclass
class CalculateIslands:
    whole_map: List = field(default_factory=list)

    def print_whole_map(self, whole_map):
        for row in whole_map:
            print(row)

    def create_whole_map(self, input_file):
        print(input_file)
        for line in input_file:
            # REMOVE NEW LINES
            row = line.rstrip('\n')
            # CHECK IF THERE ARE JUST ZEROS AND ONES
            if set(row) in ({'1', '0'}, {'0'}, {'1'}):
                row = [int(digit) for digit in row]
                print(row)
                self.whole_map.append(row)
            else:
                extra_element = set(row)
                extra_element -= {'1', '0'}
                raise ValueError(
                    f"There is at least one element that is not zero or one: {extra_element}")
        print("kurwa!", self.whole_map)

    def run_scraper(self, i, j):
        self.whole_map[i][j] = 'X'
        if i != len(self.whole_map)-1:
            if self.whole_map[i+1][j] == 1:
                self.run_scraper(i+1, j)
        if i != 0:
            if self.whole_map[i-1][j] == 1:
                self.run_scraper(i-1, j)
        if j != len(self.whole_map[i])-1:
            if self.whole_map[i][j+1] == 1:
                self.run_scraper(i, j+1)
        if j != 0:
            if self.whole_map[i][j-1] == 1:
                self.run_scraper(i, j-1)

    def run(self, input_file):
        counter = 0
        self.create_whole_map(input_file)
        for i in range(len(self.whole_map)):
            for j in range(len(self.whole_map[i])):
                if self.whole_map[i][j] == 'X':
                    pass
                if self.whole_map[i][j] == 0:
                    self.whole_map[i][j] = 'X'
                if self.whole_map[i][j] == 1:
                    self.run_scraper(i, j)
                    counter += 1
        print(f"There is {counter} island(s)")
        return counter


# input_file = ['1101110101', '0100110101', '0111111111', '1111110011', '1101010110',
#               '1010011111', '0111110110', '1111110011', '0101001011', '1101001110']
# ci = CalculateIslands()
# ci.run(input_file)
