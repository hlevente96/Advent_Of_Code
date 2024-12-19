from inputs import input_day19_tow, input_day19_des
towels_input = [t.strip() for t in input_day19_tow.strip().split(",")]
designs_input = [des.strip() for des in input_day19_des.strip().split("\n")]

def can_construct_design(design, towels):
    length = len(design)
    design_patterns = [1]+[0]*length
    for index in range(1, length+1):
        for towel in towels:
            if index >= len(towel) and design[index - len(towel):index] == towel:
                design_patterns[index] += design_patterns[index - len(towel)]
    return design_patterns[length]

counter = 0
for design in designs_input:
    result = can_construct_design(design, towels_input)
    if result:
        counter += result

print(counter)