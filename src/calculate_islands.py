"""Islands calculation from the given matrix of 0s and 1s."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class CalculateIslands:
    """Count how many islands in a given matrix."""
    whole_map: List = field(default_factory=list)

    def create_whole_map(self, input_file: List) -> None:
        """Create whole map from given input file as a list of lists.

        Remove new lines, check if only 1s and 0s and append rows to self.whole_map.
        Raise a ValueError if there is any other character than 1 or 0.

        Parameters
        ----------
        input_file: list
            List of lists - matrix of 1s and 0s
        """
        for line in input_file:
            row = line.rstrip('\n')
            if set(row) in ({'1', '0'}, {'0'}, {'1'}):
                row = [int(digit) for digit in row]
                self.whole_map.append(row)
            else:
                extra_element = set(row)
                extra_element -= {'1', '0'}
                raise ValueError(
                    f"There is at least one element that is not zero or one: {extra_element}")

    def run_scraper(self, i: int, j: int) -> None:
        """Mark the whole island started in row: i, column: j as X.

        Starting from self.whole_map[i][j] recursively check each adjacent 1,
        and replace with X.

        Parameters
        ----------
        i: int
        j:int
            Starting point of discovered island.        
        """
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

    def run(self, input_file: List) -> int:
        """Run the algorithm - count the islands.

        Starting from counter as 0, count the number of islands (connected 1s).
        Check every point of a given matrix. If 0 - mark as X, if X - pass and
        if 1 - trigger self.run_scraper method to mark as X  each adjacent 1.
        Print the counter.


        Parameters
        ----------
        input_file: list
            List of strings with 1s and 0s, i.e. ['101', '000']

        Returns
        ----------
        counter: int
            Counted number of islands (connected 1s)
        """
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
        print(counter)
        return counter
