# Shopping Cart

foods = []
prices = []
quantities = []
total = 0

while True:
    food = input("Enter a food item (or 'q' to quit): ")

    if food.lower() == "q":
        break

    price = float(input("Enter the price ($): "))
    quantity = int(input("Enter quantity: "))

    foods.append(food)
    prices.append(price)
    quantities.append(quantity)

print("\n========== SHOPPING CART ==========")

for i in range(len(foods)):
    subtotal = prices[i] * quantities[i]
    total += subtotal

    print(
        f"{foods[i]:<15} "
        f"${prices[i]:>6.2f} x {quantities[i]} = ${subtotal:.2f}"
    )

print("===================================")
print(f"Total Amount: ${total:.2f}")
