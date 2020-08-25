"""The script to calculate the islands from the given matrix of 0s and 1s."""

import argparse

from calculate_islands import CalculateIslands


class GetArgument:
    def ext_check(self, expected_extension, openner):
        def extension(filename):
            if not filename.lower().endswith(expected_extension):
                raise argparse.ArgumentTypeError("Only .txt files supported!")
            return openner(filename)
        return extension

    def get_argument(self):
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
        input_file = self.get_argument()
        ci = CalculateIslands()
        ci.create_whole_map(input_file)


ga = GetArgument()
ga.from_file()
