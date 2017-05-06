#!/usr/bin/env python3

import argparse
import re

from collections import Counter
from pathlib import Path


class UniqWordsNumber():
    def __init__(self, file_name):
        if Path(file_name).is_file():
            self.file_name = file_name
        else:
            raise Exception("File '{}' does not exist".format(file_name))
        self.counter = Counter()

    def parse(self):
        with open(self.file_name) as f:
            for line in f:
                for word in re.findall(r'\w+', line.lower()):
                    self.counter[word] += 1

    def print_stats(self):
        for word, occurrence_number in sorted(self.counter.items(), key=lambda kv: (-kv[1], kv[0])):
            print("{}: {}".format(word, occurrence_number))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    args = parser.parse_args()
    u = UniqWordsNumber(args.file_name)
    u.parse()
    u.print_stats()

