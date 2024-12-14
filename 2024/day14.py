from inputs import input_day14

def func_(n):
    rows = [row for row in input_day14.strip().split("\n")]

    bath_width = 101
    bath_height = 103
    bathroom = [[" " for _ in range(bath_width)] for _ in range(bath_height)]

    robots = []
    for row in rows:
        first_split = row.strip().split(" ")
        second_split = first_split[0].strip().split("=")
        third_split = second_split[1].strip().split(",")
        position = (int(third_split[0]), int(third_split[1]))

        second_split_2 = first_split[1].strip().split("=")
        third_split_2 = second_split_2[1].strip().split(",")
        velocity = (int(third_split_2[0]), int(third_split_2[1]))

        new_position = position
        for i in range(n):
            x,y = new_position
            vx, vy = velocity
            new_position = (x+vx, y+vy)
        x,y = new_position
        final_position = (x % bath_width, y % bath_height)
        robots.append(final_position)

    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        x,y = robot
        if 0 <= x <= 49 and 0<= y <= 50:
            q1 +=1
        elif 51 <= x <= 100 and 0 <= y <= 50:
            q2 +=1
        elif 0 <= x <= 49 and 52 <= y <= 103:
            q3 += 1
        elif 51 <= x <= 100 and 52 <= y <= 103:
            q4 += 1

    for robot in robots:
        x,y = robot
        bathroom[y][x] = "+"

    for row in bathroom:
        print(row)

    sf = q1*q2*q3*q4
    print(sf)
    return robots

for n in [7383]:
    robots = func_(n)
    distance = 0
    for i in range(len(robots)-1):
        x = abs(robots[i+1][0] - robots[i][0])
        y = abs(robots[i + 1][1] - robots[i][1])
        distance += x
        distance += y
    #if distance < 27000:
    #    print(n)
    #    print(distance)