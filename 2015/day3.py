from inputs import input_day3
position_santa = [0,0]
position_robo = [0,0]
houses = set()
houses.add(tuple(position_santa))
santa_options = (True, False)
start = 0
for char in input_day3:
    santa = santa_options[start%2]
    if char == "^":
        if santa:
            position_santa[1] += 1
        else:
            position_robo[1] += 1
    elif char == "v":
        if santa:
            position_santa[1] -= 1
        else:
            position_robo[1] -= 1
    elif char == ">":
        if santa:
            position_santa[0] += 1
        else:
            position_robo[0] += 1
    elif char == "<":
        if santa:
            position_santa[0] -= 1
        else:
            position_robo[0] -= 1
    houses.add(tuple(position_santa))
    houses.add(tuple(position_robo))
    start += 1

print(f"Second Solution: {len(houses)}")