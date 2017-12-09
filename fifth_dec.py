"""December 5th - http://adventofcode.com/"""
import sys

TEST_STRING = """0
3
0
1
-3"""

def part1():
    INPUT_FILE = open('inputs/fifth.txt', 'r')
    lines = list(map(int, INPUT_FILE.read().splitlines()))
    i = 0
    steps = 0
    while i<len(lines):
        last_i = i
        steps += 1
        i += lines[i]
        lines[last_i] += 1
    return steps

def part2():
    INPUT_FILE = open('inputs/fifth.txt', 'r')
    lines = list(map(int, INPUT_FILE.read().splitlines()))
    i = 0
    steps = 0
    while i < len(lines):
        last_i = i
        steps += 1
        i += lines[i]
        if lines[last_i] >= 3:
            lines[last_i] -= 1
        else:
            lines[last_i] += 1
    return steps

print("Part 1: "+str(part1()))
print("Part 2: "+str(part2()))
sys.exit(0)
