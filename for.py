# Read the value of n from the user
n = int(input("Enter the number of terms: "))
total_sum = 0

print("The first", n, "natural numbers are:")
for i in range(1, n + 1):
    print(i, end=" ") 
    total_sum += i  
print("\nThe sum of the first", n, "natural numbers is:", total_sum)
