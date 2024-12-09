from inputs import input_day5
rows = [row for row in input_day5.strip().split("\n")]

rule_3 = [['ab'],['cd'],['pq'],['xy']]
count = 0
for row in rows:
    valid = True
    for rule in rule_3:
        if rule[0] in row:
            valid = False
    found_double = False
    for i in range(len(row)-1):
        if row[i] == row[i+1]:
            found_double = True
    vowels = ['a','e','i','o','u']
    vowel_count = 0
    for char in row:
        if char in vowels:
            vowel_count +=1
    if valid and found_double and vowel_count >= 3:
        count += 1
print(f"Solution: {count}")

valid_row = 0
for row in rows:
    double_valid = False
    repeat_valid = False
    for index, char in enumerate(row[:-2]):
        double = char + row[index+1]
        if double in row[index+2:]:
            double_valid = True
        if char == row[index+2]:
            repeat_valid = True
        if repeat_valid and double_valid:
            valid_row +=1
            break

print(f"Solution 2: {valid_row}")