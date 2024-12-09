from inputs import input_day9

rule = input_day9
test = "2333133121414131402"

free_spaces = []
free_spaces_indexes = []
number_spaces = []
number_values = []
incr, id_, numbers, indexes = 0, 0, 0, 0
list_of_ids = []
for num in test:
    order = incr%2
    if order == 0:
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

#ordered_list = list_of_ids
#removing = list_of_ids
#for num in range(numbers):
#    if removing[num] == ".":
#        while True:
#            last_number = removing.pop()
#            if last_number != ".":
#                ordered_list[num] = last_number
#                break

def check_sum(ordered_list_):
    sum_ = 0
    for index, number in enumerate(ordered_list_):
        sum_ += (index*number)
    return sum_

#part1_sum = check_sum(ordered_list)
#print(part1_sum)

test = "2333133121414131402"

second_ordered_list = list_of_ids
print(f"Free spaces: {free_spaces}")
print(f"Free spaces indexes: {free_spaces_indexes[:-1]}")
reverse_number_spaces = number_spaces[::-1]
reverse_number_values = number_values[::-1]
print(f"Reverse numbers: {reverse_number_values}")
print(f"Reverse number spaces: {reverse_number_spaces}")

free_space_length_index = 0
for free_space_index in free_spaces_indexes:
    free_spaces_length = free_spaces[free_space_length_index]
    number_index = 0
    add_ = 0
    for number_sp in reverse_number_spaces:
        if free_spaces_length == 0:
            add_ = 0
            break
        if free_spaces_length >= number_sp:
            free_spaces_length -= number_sp
            for n in range(number_sp):
                second_ordered_list[free_space_index+add_] = reverse_number_values[number_index]
                add_ += 1
            reverse_number_values.pop(number_index)
            reverse_number_spaces.pop(number_index)
        number_index += 1

print(second_ordered_list)

