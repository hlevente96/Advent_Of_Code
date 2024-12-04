from day4_input import input_data

data = [row for row in input_data.strip().split("\n")]
rows_number = len(data)
columns_number = len(data[0])
target = "XMAS"
directions = [(0, 1),(0, -1),(1, 0),(-1, 0),(1, 1),(-1, -1),(1, -1),(-1, 1)]

def count_word(grid_data: list, rows: int, columns: int, xmas: str) -> int:
    length = len(xmas)
    count = 0
    for row in range(rows):
        for col in range(columns):
            for dr, dc in directions:
                if 0 <= row + dr * (length - 1) < rows and 0 <= col + dc * (length - 1) < columns:
                    word = "".join(grid_data[row + dr * i][col + dc * i] for i in range(length))
                    if word == xmas:
                        count += 1
    return count

def count_x_mas(grid_data: list, rows: int, columns: int) -> int:
    count = 0
    letter_options = [('M', 'S'), ('S', 'M')]
    for row in range(1, rows - 1):
        for col in range(1, columns - 1):
            if (grid_data[row][col] == 'A' and (grid_data[row - 1][col - 1], grid_data[row + 1][col + 1]) in letter_options
                    and (grid_data[row - 1][col + 1], grid_data[row + 1][col - 1]) in letter_options):
                count += 1
    return count

word_count = count_word(data, rows_number, columns_number, target)
print(word_count)

xmas_count = count_x_mas(data, rows_number, columns_number)
print(xmas_count)
