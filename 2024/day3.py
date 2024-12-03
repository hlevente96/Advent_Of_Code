from day3_input import input_data
import re

sum_ = 0
multiply_ = True
matched_lists = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)",input_data)
for mul in matched_lists:
    if mul == "do()":
        multiply_ = True
    elif mul == "don't()":
        multiply_ = False
    if multiply_ and mul != "do()" and mul != "don't()":
        numbers = re.findall(r"\d+", mul)
        sum_ += (int(numbers[0]) * int(numbers[1]))

print(sum_)

