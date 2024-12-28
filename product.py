//here the product of the two numbers is done without the multiplication operator//
def multiply(a,b):
    result=0
    for _ in range(b):
        result=result+a
    return result

num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
if (num1 < 0 or num2 < 0):
    print("Numbers should be positive only")
else:
    product=multiply(num1,num2)
    print(f"The reuslt of the numbers {num1} and {num2} is {product}")

