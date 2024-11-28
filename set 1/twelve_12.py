columns = 5

# Upper half
for i in range(1, columns + 1):
    print('*' * i)

# Lower half
for i in range(columns - 1, 0, -1):
    print('*' * i)
