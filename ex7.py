def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List must contain at least two distinct numbers."
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    
    if len(unique_numbers) < 2:
        return "No second largest number exists."
    return unique_numbers[-2]

numbers1 = [10, 20, 4, 45, 99]
numbers2 = [1, 1, 1, 2]

print("Second largest in list 1:", find_second_largest(numbers1))
print("Second largest in list 2:", find_second_largest(numbers2))
