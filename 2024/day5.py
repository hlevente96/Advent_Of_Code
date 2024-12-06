from day5_input import input_data_1, input_data_2

rules = [tuple(map(int, row.split("|"))) for row in input_data_1.strip().split("\n")]
data = [list(map(int, row.split(","))) for row in input_data_2.strip().split("\n")]

correct_rows, invalid_rows = [], []
for check_row in data:
    valid_row = True
    for r1, r2 in rules:
        if r1 in check_row and r2 in check_row:
            index_0, index_1 = 0, 0
            for index, element in enumerate(check_row):
                if element == r1:
                    index_0 = index
                elif element == r2:
                    index_1 = index
            if index_0 > index_1:
                valid_row = False
    correct_rows.append(check_row) if valid_row else invalid_rows.append(check_row)

def sum_of_middle(list_: list) -> int:
    middle = 0
    for lst in list_:
        middle_index = len(lst) // 2
        middle += lst[middle_index]
    return middle

part_1 = sum_of_middle(correct_rows)
print(f"Part 1 Solution: {part_1}")

def ordering_rows(row, rules):
    before_element_number = {num: 0 for num in row}
    after_elements = {num: [] for num in row}
    for r1, r2 in rules:
        if r1 in row and r2 in row:
            after_elements[r1].append(r2)
            before_element_number[r2] += 1

    first_element = [num for num in row if before_element_number[num] == 0]
    sorted_row = []
    while first_element:
        current = first_element.pop(0)
        sorted_row.append(current)
        for neighbor in after_elements[current]:
            before_element_number[neighbor] -= 1
            if before_element_number[neighbor] == 0:
                first_element.append(neighbor)
    return sorted_row

reordered_rows = [ordering_rows(row, rules) for row in invalid_rows]
part_2 = sum_of_middle(reordered_rows)
print(f"Part 2 Solution: {part_2}")
