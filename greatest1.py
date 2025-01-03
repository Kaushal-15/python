
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Nested if-else to find the greatest number
if a > b:
    if a > c:
        greatest = a
    else:
        greatest = c
else:
    if b > c:
        greatest = b
    else:
        greatest = c

print(f"The greatest number is: {greatest}")
