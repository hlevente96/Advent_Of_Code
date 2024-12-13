from inputs import input_day7
rows = [row for row in input_day7.strip().split("\n")]
mapping = {'c': 0, 'b': 956}
stack = rows
while stack:
    for row in rows:
        first_split = row.strip().split("->")
        equation_result = first_split[1].strip()
        second_split = first_split[0].strip().split(" ")
        if len(second_split) == 1 and second_split[0] != "lx":
            mapping[equation_result] = int(second_split[0])
            stack.remove(row)
        elif len(second_split) == 2 and second_split[1].strip() in mapping.keys():
            mapping[equation_result] = ~mapping[second_split[1]] & 0xFFFF
            stack.remove(row)
        elif len(second_split) == 3 and second_split[2].isdigit() and second_split[0].strip() in mapping.keys():
            shift = int(second_split[2])
            if second_split[1] == 'LSHIFT':
                mapping[equation_result] = mapping[second_split[0]] << shift & 0xFFFF
                stack.remove(row)
            elif second_split[1] == 'RSHIFT':
                mapping[equation_result] = mapping[second_split[0]] >> shift & 0xFFFF
                stack.remove(row)
        elif len(second_split) == 3:
            if second_split[1] == 'AND' and second_split[0].strip() in mapping.keys() and second_split[2].strip() in mapping.keys():
                mapping[equation_result] = mapping[second_split[0]] & mapping[second_split[2]] & 0xFFFF
                stack.remove(row)
            elif second_split[1] == 'OR' and second_split[0].strip() in mapping.keys() and second_split[2].strip() in mapping.keys():
                mapping[equation_result] = mapping[second_split[0]] | mapping[second_split[2]] & 0xFFFF
                stack.remove(row)
            elif second_split[1] == 'AND' and second_split[0].strip() == '1' and second_split[2].strip() in mapping.keys():
                mapping[equation_result] = 1 & mapping[second_split[2]] & 0xFFFF
                stack.remove(row)

print(f"Solution of a = {mapping['lx']}")
