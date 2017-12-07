import sys

TEST_INPUT = "0 2 7 0"
MY_INPUT = "4 10 4 1 8 4 9 14 5 1 14 15 0 15 3 5"

steps = 0
input_array = list(map(int, MY_INPUT.split()))
reocc_strings = list()
reocc_strings_two = list()

def get_max_index(def_input_array):
    maxmimum = max(def_input_array)
    for i, val in enumerate(def_input_array):
        if val == maxmimum:
            return i
    return False


while True:
    steps += 1
    max_mem = max(input_array)
    arr_index = get_max_index(input_array)
    input_array[arr_index] = 0
    next_index = arr_index
    for i in range(max_mem):
        if next_index+1 < len(input_array):
            next_index += 1
        else:
            next_index = 0
        input_array[next_index] += 1
    num_string = " ".join(str(x) for x in input_array)
    if num_string in reocc_strings:
        reocc_strings.append(num_string)
        break
    else:
        reocc_strings.append(num_string)

input_array_two = list(map(int, reocc_strings[len(reocc_strings)-1].split()))

while True:
    max_mem = max(input_array_two)
    arr_index = get_max_index(input_array_two)
    input_array_two[arr_index] = 0
    next_index = arr_index
    for i in range(max_mem):
        if next_index+1 < len(input_array_two):
            next_index += 1
        else:
            next_index = 0
        input_array_two[next_index] += 1
    num_string = " ".join(str(x) for x in input_array_two)
    if num_string == reocc_strings[len(reocc_strings)-1]:
        reocc_strings_two.append(num_string)
        break
    else:
        reocc_strings_two.append(num_string)


#print(reocc_strings)
print(len(reocc_strings))
print(len(reocc_strings_two))
