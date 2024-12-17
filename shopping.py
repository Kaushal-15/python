#shopping cart
prices=[]
foods=[]
total=0

while True:
    food = input("Enter the food or press(q to quit): ")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"Enter the price of the food {food}:$ "))
        foods.append(food)
        prices.append(price)
    
print("-----YOUR CART!-----")
for food in foods:
    print(food)

for price in prices:
    total+=price

print()
print(f"The total of the cart is:${total}")
