from day1_input import input_data

rows = input_data.strip().split("\n")

column1 = []
column2 = []
for row in rows:
    col1, col2 = row.split(",")
    column1.append(int(col1))
    column2.append(int(col2))

column1 = sorted(column1)
column2 = sorted(column2)

distance = 0
for i in range(len(column1)):
    distance += abs(column1[i] - column2[i])

new_list = []
for i in column1:
    similarity = 0
    for j in column2:
        if i == j:
            similarity +=1
    new_list.append(i*similarity)

print(sum(new_list))