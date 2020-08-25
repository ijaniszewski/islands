"""Get txt file from passed argument."""

import argparse
from typing import Callable

from calculate_islands import CalculateIslands


class GetArgument:
    """Get txt file passed while the script is executed."""

    def ext_check(self, expected_extension: str, openner: argparse.FileType) -> Callable:
        """Check if extension is as expected.

        Wrapper for argparse.FileType

        Parameters
        ----------
        expected_extension: str
            Extension that is expected
        openner: argparse.FileType

        Return
        ----------
        extension: Callable
            If extension is not as expected, error occurs.
            If passed, the filename is passed to openner.
        """
        def extension(filename):
            if not filename.lower().endswith(expected_extension):
                raise argparse.ArgumentTypeError("Only .txt files supported!")
            return openner(filename)
        return extension

    def get_argument(self):
        """Get the given argument if it is txt file.

        Return
        ----------
        input_file: list
            List of strings with 1s and 0s, i.e. ['101', '000']
        """
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-f',
            '--file',
            help="Path to the txt input file.",
            type=self.ext_check('.txt', argparse.FileType('r')),
            required=True)
        input_file = parser.parse_args().file.readlines()
        return input_file

    def from_file(self):
        """Get the input_file from txt file and create CalculateIslands object."""
        input_file = self.get_argument()
        ci = CalculateIslands()
        ci.run(input_file)


if __name__ == "__main__":
    ga = GetArgument()
    ga.from_file()
