from pi_art import higer_logo, vs
import random

higher_data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    }]

# print (higer_logo)

first_data = random.choice(higher_data)

second_data = random.choice(higher_data)

while True:
    if second_data == first_data:
        second_data = random.choice(higher_data)
    else:
        break


def compare(data):
    for keys in data:
        if keys == "follower_count":
            follower = data[keys]
    return follower

print(f"{first_data} \n {compare(first_data)}")

print(f"{second_data} \n {compare(second_data)}")

# def personality(data):
#     for keys in data:
#         if keys == "name":
#             name = data[keys]
#         elif keys == "description":
#             description = data[keys]
#         elif keys == "country":
#             country = data[keys]
#     detail_1 = f" {name}, a {description}, from {country}"
#     return detail_1


# game = False

# print(f"Compare A {personality(first_data)}" )


# while not game:
#     print(vs)

#     print(f"Compare B: {personality(second_data)}")

#     choice = input("Who has more followers? Type 'A' or 'B': ")

#     score = 0

#     comparison = {
#         "A" : compare(first_data),
#         "B": compare(second_data)
#     }

#     score = comparison[choice]
#     print(score)

#     print(comparison["A"])
#     print(comparison["B"])

#     # if choice == "A":
#     #     if comparison["A"]> comparison ["B"]:
#     #         score += 1
#     #         print(f"You're right, current score is {score}")
#     #         print(f"Compare A {personality(first_data)}" )
#     #     else:
#     #         print(f"Sorry that's wrong, final score is {score}")
#     #         game = True
#     # elif choice == "B":
#     #     if comparison[choice]> comparison ["A"]:
#     #         score += 1
#     #         print(f"Compare A {personality(second_data)}" )
#     #     else:
#     #         print(f"Sorry that's wrong, final score is {score}")
#     #         game= True