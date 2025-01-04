rows = int(input("Enter the number of rows (for the upper half): "))

# Upper half 
for i in range(1, rows + 1):
    print(' ' * (rows - i), end='')
    print('*' * (2 * i - 1))

# Lower half 
for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i), end='')
    print('*' * (2 * i - 1))
