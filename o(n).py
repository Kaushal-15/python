n = int(input("N: "))
def addup(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

#order of n complexity = o(n)
result = addup(n)
print("Sum of numbers from 1 to", n, "is:", result)
