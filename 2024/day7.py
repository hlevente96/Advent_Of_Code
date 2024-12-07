from inputs import input_day7
from itertools import product

equations = [row for row in input_day7.strip().split("\n")]
operators = ["+", "*", "||"]
counter = 0

def evaluate(numbers_, ops):
    result_ = numbers_[0]  # Start with the first number
    for i, op_ in enumerate(ops):
        if op_ == "+":
            result_ += numbers_[i + 1]
        elif op_ == "*":
            result_ *= numbers_[i + 1]
        elif op_ == "||":
            result_ = int(str(result_) + str(numbers_[i + 1]))
    return result_

for equation in equations:
    split_equation = equation.strip().split(":")
    result = int(split_equation[0])
    numbers = [int(num) for num in split_equation[1].strip().split(" ")]
    operator_combinations = product(operators, repeat=len(numbers)-1)
    for option in operator_combinations:
        res = evaluate(numbers, option)
        if res == result:
            counter += result
            break

print(f"Second Solution: {counter}")

