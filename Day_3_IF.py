print("Welcome to Python Pizza Delivery")

size = input("What size of pizza do you want?: ").lower()
pepperoni = input("Do you wish for pepperoni?: ").lower()
extra_cheese = input("Do you want extra cheese?: ").lower()


if size == "s":
    amount = 15
elif size == "m":
    amount = 20
elif size == "l":
    amount = 25

if pepperoni == "yes":
    if size == "s":
        amount += 2
    else:
        amount += 3

if extra_cheese == "yes":
    amount += 1

print(f"Your total bill is ${amount}")
