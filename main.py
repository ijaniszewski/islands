input_file_path = "examples/ex6.txt"
input_file = open(input_file_path, "r") 

def print_whole_map(whole_map):
    for row in whole_map:
        print(row)

whole_map = []
for line in input_file.readlines():
    # REMOVE NEW LINES
    row = line.rstrip('\n')
    # CHECK IF THERE ARE JUST ZEROS AND ONES
    if set(row) in ({'1', '0'}, {'0'}, {'1'}):
        row = [int(digit) for digit in row]
        whole_map.append(row)
    else:
        extra_element = set(row)
        extra_element -= {'1', '0'}
        raise ValueError(f"There is at least one element that is not zero or one: {extra_element}")
print_whole_map(whole_map)
print("---"*30)

counter = 2
add_counter = False
this_time = True
for i in range(len(whole_map)):
    for j in range(len(whole_map[i])):
        if whole_map[i][j] == 1:

            # CHECK THE DIGIT ON THE LEFT
            if j !=0:
                digit_left = whole_map[i][j-1]
            else:
                digit_left = 0


            # CHECK THE DIGIT ABOVE
            if i != 0:
                digit_above = whole_map[i-1][j]
            else:
                digit_above = 0

            
            if digit_left != digit_above:
                if this_time:
                    if digit_above != 0:
                        counter -= 1
                        this_time = False
                whole_map[i][j] = digit_above

            whole_map[i][j] = counter
            add_counter = True
        if add_counter:
            if whole_map[i][j] == 0:
                counter += 1
                add_counter = False
                this_time = True


if counter != 1:
    counter -= 2
print_whole_map(whole_map)
print(f"The number of islands: {counter}")