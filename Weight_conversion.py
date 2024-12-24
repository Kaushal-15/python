print("Weight Conversion Tool")
print("1.Kg to lbs")
print("2.lbs to kg")
print("Enter the choice below:")
choice=int(input("Choice:"))
if(choice==1):
    print("Enter in kilograms(kg):")
    kg=float(input())
    kg_lb=kg*2.20462
    print(f"The {kg} is equivalent to {kg_lb}lbs.")
else:
    print("Enter in pounds(lbs):")
    lb=float(input())
    lb_kg=lb/2.20462
    print(f"The {lb} is equivalent to {lb_kg}kg.")


