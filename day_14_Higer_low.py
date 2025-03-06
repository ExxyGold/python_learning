from pi_art import higher_logo, vs, clear, higher_data
import random

print (higher_logo)

first_data = random.choice(higher_data)

def getting_B():
    second_data = random.choice(higher_data)
    while True:
        if second_data == first_data:
            second_data = random.choice(higher_data)
        else:
            break
    return second_data



def compare(data):
    for keys in data:
        if keys == "follower_count":
            follower = data[keys]
    return follower

def personality(data):
    for keys in data:
        if keys == "name":
            name = data[keys]
        elif keys == "description":
            description = data[keys]
        elif keys == "country":
            country = data[keys]
    detail_1 = f" {name}, a {description}, from {country}"
    return detail_1

game = False

print(f"Compare A {personality(first_data)}" )

score = 0

while not game:
    print(vs)
    second_data = getting_B()

    print(f"Compare B: {personality(second_data)}")

    follower1 = compare(first_data)
    follower2 = compare(second_data)

    choice = input("Who has more followers? Type 'A' or 'B': ")

    comparison = {
        "A" : follower1,
        "B": follower2
    }

    if choice == "A":
        if comparison["A"]> comparison ["B"]:
            score += 1
            clear()
            print(higher_logo)
            print(f"You're right, current score is {score}")
            print(f"Compare A {personality(first_data)}" )
        else:
            print(f"Sorry that's wrong, final score is {score}")
            game = True
    elif choice == "B":
        if comparison[choice]> comparison ["A"]:
            first_data = second_data
            score += 1
            clear()
            print(higher_logo)
            print(f"You're right, current score is {score}")
            print(f"Compare A {personality(second_data)}" )
        else:
            print(f"Sorry that's wrong, final score is {score}")
            game= True