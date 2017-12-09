import sys
import re

TEST_STRING = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

MY_INPUT  = open("inputs/seventh.txt","r").read()

def part1(input_string):
    groups = re.findall(r"(\w*) \([\d]{1,5}\) -> (?:(.*,?))\n", input_string)
    all_subs = list()
    parents  = list()
    for disks in  groups:
        all_subs.extend(disks[1].split(", "))
        parents.append(disks[0])
    
    for i, val in enumerate(parents):
        if val not in all_subs:
            return val

print(part1(MY_INPUT))
sys.exit(0)