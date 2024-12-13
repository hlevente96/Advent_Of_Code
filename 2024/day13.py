from inputs import input_day13
machines_input = [row for row in input_day13.strip().split("\n")]

machines, machine = [], []
iteration = 0
for row in machines_input:
    if iteration == 0 or iteration == 1:
        first_split = row.strip().split(":")
        second_split = first_split[1].strip().split(",")
        third_split = second_split[0].strip().split("+")
        fourth_split = second_split[1].strip().split("+")
        machine.append((int(third_split[1]),int(fourth_split[1])))
        iteration+=1
    elif iteration == 2:
        first_split = row.strip().split(":")
        second_split = first_split[1].strip().split(",")
        third_split = second_split[0].strip().split("=")
        fourth_split = second_split[1].strip().split("=")
        machine.append((int(third_split[1]), int(fourth_split[1])))
        iteration += 1
    elif iteration == 3:
        iteration = 0
        machines.append(machine)
        machine = []

def calculate_token(machines: list, add: int) -> int:
    total_tokens = 0
    for mac in machines:
        token = 0
        x1, y1 = mac[0]
        x2, y2 = mac[1]
        X = mac[2][0] + add
        Y = mac[2][1] + add
        A = ((Y*x2)-(X*y2))/((y1*x2)-(y2*x1))
        B = (X-(x1*A))/x2
        if A.is_integer() and B.is_integer():
            token = int(A)*3 + int(B)*1
        total_tokens += token
    return total_tokens

print(f"First solution: {calculate_token(machines,0)}")
print(f"Second solution: {calculate_token(machines, 10000000000000)}")



