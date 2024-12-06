from inputs import input_day2

rows = [list(map(int, row.split())) for row in input_day2.strip().split("\n")]

def is_safe(row: list) -> bool:
    inc = all(1 <= row[i + 1] - row[i] <= 3 for i in range(len(row) - 1))
    dec = all(1 <= row[i] - row[i + 1] <= 3 for i in range(len(row) - 1))
    return inc or dec

def count_safe_rows(rows: list, dampener: bool) -> int:
    safe_rows = 0
    for row in rows:
        if dampener:
            if is_safe_with_dampener(row):
                safe_rows += 1
        else:
            if is_safe(row):
                safe_rows += 1
    return safe_rows

def is_safe_with_dampener(row):
    if is_safe(row):
        return True
    for i in range(len(row)):
        modified_row = row[:i] + row[i + 1:]
        if is_safe(modified_row):
            return True
    return False

safe = count_safe_rows(rows, dampener=True)
print(safe)