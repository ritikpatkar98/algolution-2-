rows = 5
columns = 5

for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
            print("1", end='')
        else:
            print("0", end='')
    print()
