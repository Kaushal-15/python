
def print_diamond(n):
    # Top half of the diamond
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    
    # Bottom half of the diamond
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

rows = int(input("Enter the number of rows for the diamond pattern: "))
print_diamond(rows)