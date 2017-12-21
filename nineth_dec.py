MY_INPUT = open("inputs/nineth.txt", 'r').readline()


def solve(input_string):
    group_count = 0
    group_open = 0
    is_garbage = False
    garbage_char_count = 0
    i = 0
    while i < len(input_string):
        #Part 2
        if is_garbage is True:
            if input_string[i] != "!" and input_string[i] != ">" and input_string != "<":
                garbage_char_count += 1
        #Part 1
        if input_string[i] == "<" and is_garbage is False:
            is_garbage = True
        elif input_string[i] == ">" and is_garbage is True:
            is_garbage = False
        elif input_string[i] == "!" and is_garbage is True:
            i += 1
        elif is_garbage is False:
            if input_string[i] == "{":
                group_open += 1
            elif input_string[i] == "}":
                group_count += group_open
                group_open -= 1
        i += 1
    print("Part 1: "+str(group_count))
    print("Part 2: "+str(garbage_char_count))

solve(MY_INPUT)
