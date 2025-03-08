from pi_art import MENU, resources

#Print Report of the machines resources



def order_made (type):
    drink  = MENU[type]
    ingredients = drink ["ingredients"]
    water = ingredients["water"]

    if "milk" in ingredients:
        milk = ingredients["milk"]
    else:
        milk= 0
    coffee = ingredients["coffee"]
    cost = drink ["cost"]
    drink_ingredients = [ water,milk, coffee, cost ]
    return drink_ingredients

def money():
    print("Please insert coins.")
    quater = int(input("How many quaters?: "))
    dime = int(input("How many dimes? "))
    nickle = int(input("How many Nickles?: "))
    penny = int(input("How many pennies?: "))

    amount = (quater * 0.25) +(dime * 0.1) + (nickle * 0.05) + (penny * 0.01)
    return amount
account = 0
done_ordering = False

while not done_ordering:
    order = input("What would you like? (espresso is $1.5/latte is $2.5/ cappuccino is $3.0): ").lower()

    water_available = resources["water"]
    milk_available = resources["milk"]
    coffee_available = resources["coffee"]


    if order == "report":
        print (f" Water: {water_available}ml \n Milk: {milk_available}ml \n Coffee: {coffee_available}g\n Money: ${account}")
    elif order not in MENU:
        print(f"Sorry, {order} is not in our menu.")
    else:
        order_details = order_made(order)
        water_needed = order_details[0]
        milk_needed = order_details[1]
        coffee_needed = order_details[2]
        cost = order_details[3]
        payment = money()

        if payment >= cost:
            
            account += cost
            change =  round(payment - cost, 2)
    
            if payment == cost:
                print(f"Here is your {order} ☕ Enjoy!")
            else:
                print (f"Here is ${change} in change.\n Here is your {order} ☕ Enjoy!")

        else:
            print("Sorry, that's not enough money. Money refunded")
