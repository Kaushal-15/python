def main():
    num_subjects = int(input("Enter the number of subjects: "))

    marks = []
    total_sum = 0

    
    print("Enter the marks for each subject:")
    for i in range(num_subjects):
        mark = int(input(f"Subject {i + 1}: "))
        marks.append(mark)
        total_sum += mark

    # Calculate average
    average = total_sum / num_subjects

    
    print(f"\nTotal Marks: {total_sum}")
    print(f"Average Marks: {average:.2f}")

if __name__ == "__main__":
    main()
