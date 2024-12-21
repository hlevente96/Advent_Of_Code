from itertools import product
input_num =[869,180,596,965,973]

def generate_combinations(input_dict, total):
    key_order = list(input_dict.keys())
    value_lists = [input_dict[key] for key in key_order]
    combinations = product(*value_lists)
    return [''.join(combo) for combo in combinations] if not total else [combo for combo in combinations]

first_input = {8:['A<^^^A', 'A^^^<A'],6:['v>A', '>vA'],9:['^A'],"A":['vvvA']}
second_input = {1:['A^<<A'],8:['^^>A', '>^^A'],0:['vvvA'],"A":['>A']}
third_input = {5:['A<^^A','A^^<A'],9:['^>A','>^A'],6:['vA'],"A":['vvA']}
fourth_input = {9:['A^^^A'],6:['vA'],5:['<A'],"A":['vv>A','>vvA']}
fifth_input = {9:['A^^^A'],7:['<<A'],3:['vv>>A','>>vvA'],"A":['vA']}

total_first_combinations = {
    0: generate_combinations(first_input, False),
    1: generate_combinations(second_input, False),
    2: generate_combinations(third_input, False),
    3: generate_combinations(fourth_input, False),
    4: generate_combinations(fifth_input, False)
}
input_data = generate_combinations(total_first_combinations, True)

total_count = {"A<": 0,"Av": 0,"A^": 0,"A>": 0,"AA": 0,"<<": 0,"<v": 0,"<^": 0,"<>": 0,"<A": 0,"v<": 0,"vv": 0,"v^": 0,
               "v>": 0,"vA": 0,"><": 0,">v": 0,">^": 0,">>": 0,">A": 0,"^<": 0,"^v": 0,"^^": 0,"^>": 0,"^A": 0}
total_map = {
    "A<": ["Av","v<","<<","<A"],"Av": ["A<","<v","vA"],"A^": ["A<","<A"],"A>": ["Av","vA"],"AA": ["AA"],
    "<<": ["AA"],"<v": ["A>",">A"],"<^": ["A>",">^","^A"],"<>": ["A>",">>",">A"],"<A": ["A>",">>",">^","^A"],
    "v<": ["A<","<A"],"vv": ["AA"],"v^": ["A^","^A"],"v>": ["A>",">A"],"vA": ["A^","^>",">A"],
    "><": ["A<","<<","<A"],">v": ["A<","<A"],">^": ["A<","<^","^A"],">>": ["AA"],">A": ["A^","^A"],
    "^<": ["Av", "v<", "<A"],"^v": ["Av", "vA"],"^^": ["AA"],"^>": ["Av","v>",">A"],"^A": ["A>", ">A"],
}
map_variations = {
    "Av": [["A<","<v","vA"], ["Av","v<","<A"]],
    "vA": [["A^","^>",">A"], ["A>",">^","^A"]],
    "^>": [["Av","v>",">A"], ["A>",">v","vA"]],
    ">^": [["A<","<^","^A"], ["A^","^<","<A"]]
}

def generate_all_maps(key_variations,map_):
    all_maps = []
    for av_values in key_variations["Av"]:
        for va_values in key_variations["vA"]:
            for up_left_values in key_variations["^>"]:
                for left_up_values in key_variations[">^"]:
                    map_copy = map_.copy()
                    map_copy["Av"] = av_values
                    map_copy["vA"] = va_values
                    map_copy["^>"] = up_left_values
                    map_copy[">^"] = left_up_values
                    all_maps.append(map_copy)
    return all_maps

all_maps = generate_all_maps(map_variations,total_map)

def create_initial_dict(input_data):
    first_round = []
    for item in input_data:
        new_dict = {key: 0 for key in total_count}
        for i in range(len(item) - 1):
            new_dict[item[i:i+2]] += 1
        first_round.append(new_dict)
    return first_round

def next_robot(input_data, grid_map):
    result = []
    for item in input_data:
        new_dict = {key: 0 for key in total_count}
        for pair, value in item.items():
            if value != 0:
                mappings = grid_map[pair]
                for map_ in mappings:
                    new_dict[map_] += value
        result.append(new_dict)
    return result

def sequence(input_data, sequence, grid_map):
    result = input_data
    for _ in range(sequence):
        result = next_robot(result, grid_map)
    return result

sum_count = []
for input_ in input_data:
    for map_ in all_maps:
        initialized_input = create_initial_dict(input_)
        robots = sequence(initialized_input, 25, map_)
        count = 0
        for index, row in enumerate(robots):
            count += sum(row.values()) * input_num[index]
        sum_count.append(count)

print(min(sum_count))
