from inputs import input_day25
rows = [row.strip() for row in input_day25.strip().split("\n")]

keys, locks = [], []
for index, row in enumerate(rows):
    if index % 8 == 1 and row == ".....":
        new_key = [0, 0, 0, 0, 0]
        for i in range(1,6):
            for y in range(5):
                if rows[index+i][y] == "#":
                    if 0 <= y < len(new_key):
                        new_key[y] += 1
        keys.append(new_key)
    elif index % 8 == 1 and row == "#####":
        new_lock = [0, 0, 0, 0, 0]
        for i in range(1,6):
            for y in range(5):
                if rows[index+i][y] == "#":
                    if 0 <= y < len(new_lock):
                        new_lock[y] += 1
        locks.append(new_lock)

count = 0
for lock in locks:
    for key in keys:
        res = [(a+b)<6 for a, b in zip(key, lock)]
        if all(res):
            count += 1

print(count)
