def print_pattern(rows):
    for i in range(rows):
        for j in range(rows):
            if j <= i:
                print(i + 1, end='')
            else:
                print(rows, end='')
        print()

print_pattern(5)
