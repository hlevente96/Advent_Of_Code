from inputs import input_day1

floor = 0
found_index = False
for index, char in enumerate(input_day1):
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    if floor < 0 and not found_index:
        print(f"Second Solution: {index + 1}")
        found_index = True
print(f"First Solution: {floor}")