from inputs import input_day9
rule = input_day9

def initialize():
    free_spaces,free_spaces_indexes,number_spaces,number_values,number_indexes,list_of_ids = [],[],[],[],[],[]
    incr, id_, numbers, indexes = 0, 0, 0, 0
    for num in input_day9:
        order = incr%2
        if order == 0:
            number_spaces.append(int(num))
            for n in range(int(num)):
                number_indexes.append(indexes)
                list_of_ids.append(id_)
                numbers += 1
                indexes += 1
            free_spaces_indexes.append(indexes)
            number_values.append(id_)
            id_ += 1
        elif order == 1:
            free_spaces.append(int(num))
            for n in range(int(num)):
                list_of_ids.append(".")
                indexes += 1
        incr += 1
    return free_spaces,free_spaces_indexes,number_spaces,number_values,number_indexes,list_of_ids, numbers

free_spaces,free_spaces_indexes,number_spaces,number_values,number_indexes,list_of_ids,numbers = initialize()
ordered_list = list_of_ids
removing = list_of_ids
for num in range(numbers):
    if removing[num] == ".":
        while True:
            last_number = removing.pop()
            if last_number != ".":
                ordered_list[num] = last_number
                break

def check_sum(ordered_list_):
    sum_ = 0
    for index, number in enumerate(ordered_list_):
        sum_ += (index*number)
    return sum_

part1_sum = check_sum(ordered_list)
print(part1_sum)

free_spaces = []
free_spaces_indexes = []
number_spaces = []
number_values = []
number_indexes = []
incr, id_, numbers, indexes = 0, 0, 0, 0
list_of_ids = []
for num in input_day9:
    order = incr%2
    if order == 0:
        number_indexes.append(indexes)
        number_spaces.append(int(num))
        for n in range(int(num)):
            list_of_ids.append(id_)
            numbers += 1
            indexes += 1
        free_spaces_indexes.append(indexes)
        number_values.append(id_)
        id_ += 1
    elif order == 1:
        free_spaces.append(int(num))
        for n in range(int(num)):
            list_of_ids.append(".")
            indexes += 1
    incr += 1

reverse_number_spaces = number_spaces[::-1]
reverse_number_values = number_values[::-1]
reverse_number_indexes = number_indexes[::-1]

second_ordered_list = list_of_ids
for inde, number_space in enumerate(reverse_number_spaces):
    for ind, free_space in enumerate(free_spaces):
        if free_space >= number_space and free_spaces_indexes[ind] < reverse_number_indexes[inde]:
            second_ordered_list = [x if x != reverse_number_values[inde] else "." for x in second_ordered_list]
            for n in range(number_space):
                second_ordered_list[free_spaces_indexes[ind]+n] = reverse_number_values[inde]
                free_spaces[ind] -= 1
            free_spaces_indexes[ind] += number_space
            break

sum_ = 0
for index, number in enumerate(second_ordered_list):
    if number != ".":
        sum_ += (index*number)
print(sum_)