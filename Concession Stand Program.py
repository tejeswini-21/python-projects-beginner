#Concession Stand Program

menu = {
    "pizza": 3.66,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "soda": 2.00
}
cart = []
total = 0

print("=======CONCESSION STAND=========")
for item, price in menu.items():
    print(f"{item:<8} : ${price:.2f}")

print("===============================")
while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break

    if food in menu:
        cart.append(food)
        print(f"{food.capitalize()} added to cart.")

    else:
        food = input("Item not found.Please select an item from the menu.")


print("==========YOUR ORDER=========")
if len(cart) == 0:
    print("Your cart is empty.")
else:
    for food in cart:
        price = menu[food]
        total += price
        print(f"{food:<8} ${price:.2f}")

    print("------------------------------------")

    print(f"Total:  ${total:.2f}")
print("========================================")
print("Thank you for your purchase!")