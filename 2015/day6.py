from inputs import input_day6

rows = [row for row in input_day6.strip().split("\n")]

for row in rows:
    first_split = row.strip().split("through")
    second_split = first_split[0].strip().split(" ")
    first_coord = (int(second_split[-1].split(",")[0]), int(second_split[-1].split(",")[1]))
    second_coord = (int(first_split[1].strip().split(",")[0]),int(first_split[1].strip().split(",")[1]))
    if len(second_split) == 3:
        rule = second_split[0] + " " + second_split[1]
    else:
        rule = second_split[0]
