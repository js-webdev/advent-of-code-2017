"""December 4th - http://adventofcode.com/"""

lines = open('fourth.txt', 'r')

MY_TEST = """aaa bbb ccc aa dd
aa bb cc aa
aaa ddd asdf"""

#lines = MY_TEST.split("\n")

phrases = [line.split() for line in lines]
print(sum(len(phrase) == len(set(phrase)) for phrase in phrases))
print(sum(len(phrase) == len(set([tuple(sorted(word)) for word in phrase])) for phrase in phrases))
