rows = 5
columns = 5

for i in range(rows):
    if i % 2 == 0:
        for j in range(1, columns + 1):
            print(j, end='')
    else:
        for j in range(columns, 0, -1):
            print(j, end='')
    print()
