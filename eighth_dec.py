import sys
import re

TEST_STRING = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

MY_INPUT  = open("inputs/eighth.txt","r").read()
regs = dict()

highest_val = 0

def part1(input_string):
    highest_val = 0
    for line in input_string.splitlines():
        groups = re.findall(r"(\w+) (inc|dec) (-?[\d]+) if (\w+) ([!=<>]+) (-?[\d]+)", line)[0]
        if groups[3] not in regs:
            regs[groups[3]] = 0
        if condition(regs[groups[3]], groups[4], groups[5]) == True:
            if groups[0] not in regs:
                regs[groups[0]] = 0
            regs[groups[0]] = instruction(groups[1], regs[groups[0]], groups[2])
            if regs[groups[0]] > highest_val:
                highest_val = regs[groups[0]]
    return highest_val

def instruction(inst, var, val):
    if inst == "dec":
        var -= int(val)
    elif inst == "inc":
        var += int(val)
    return var

def condition(var, op, val):
    if op == "<":
        return int(var) < int(val)
    elif op == "<=":
        return int(var) <= int(val)
    elif op == "==":
        return int(var) == int(val)
    elif op == ">=":
        return int(var) >= int(val)
    elif op == ">":
        return int(var) > int(val)
    elif op == "!=":
        return int(var) != int(val)

highest_val = part1(MY_INPUT)
print("Part 1: "+str(regs[max(regs, key=lambda i: regs[i])]))
print("Part 2: " + str(highest_val))
sys.exit(0)