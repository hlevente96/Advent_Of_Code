input_data = [872027,227, 18, 9760, 0, 4, 67716, 9245696]

def rules(input_list: list):
    new_list = []
    for number in input_list:
        number_length = len(str(number))
        if number == 0:
            new_list.append(1)
        elif number_length % 2 == 0:
            middle = number_length // 2
            first_half = int(str(number)[:middle])
            second_half = int(str(number)[middle:])
            new_list.append(first_half)
            new_list.append(second_half)
        else:
            num = number * 2024
            new_list.append(num)
    return new_list

def repeat(input_, iteration):
    current_list = input_
    for i in range(iteration):
        current_list = rules(current_list)
    return current_list

solution = repeat(input_data, 25)
print(f"First Solution: {len(solution)}")

def dict_update(dict_: dict, key, value):
    if key in dict_.keys():
        dict_[key] += value
    else:
        dict_.update({key:value})

def rules_2(input_list, iteration):
    input_dict = {key: 1 for key in input_list}
    for _ in range(iteration):
        new_dict = {}
        for number, value in input_dict.items():
            if number == 0:
                dict_update(new_dict,1,value)
            elif len(str(number)) % 2 == 0:
                middle = len(str(number)) // 2
                dict_update(new_dict,int(str(number)[:middle]),value)
                dict_update(new_dict,int(str(number)[middle:]),value)
            else:
                key = number * 2024
                dict_update(new_dict,key,value)
        input_dict = new_dict
    return sum(input_dict.values())

refined_result = rules_2(input_data, 75)
print(f"Second Solution: {refined_result}")

