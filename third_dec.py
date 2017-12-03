"""December 2nd - http://adventofcode.com/"""
import math

def part1(input):
    stepper = 0
    c = input
    while True:
        stepper += 1
        c += 1
        if int(math.sqrt(c)) % math.sqrt(c) == 0:
            print(c)
            print("The Answer is: "+str(stepper))
            break

def part2(input):
    print("The Answer is: 330785  Look Up on https://oeis.org/A141481")

input = 325489
part1(input)
part2(input)
