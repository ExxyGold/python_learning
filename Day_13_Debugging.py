# def my_function():
#     for i in range(1, 21):
#         if i== 20:
#             print("You Got it")
# my_function()

# from random import randint

# dice_imgs = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣" ]
# dice_num = randint(0,5)
# print(dice_imgs[dice_num])

# year = int(input("What is your year of Birth?: "))
# if year >= 1980 and year <= 1994:
#     print("You are a millenial")
# elif year >1994:
#     print("You are a Gen Z")

# age = int(input("What is your age? "))
# if age> 18:
#     print(f"You can drive at age {age}")


# pages = 0
# word_per_page = 0

# print(pages)

# pages= int(input("Number of Pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages* word_per_page
# print(total_words)

# def mutate(a_list):
#     b_list = []
#     for items in a_list:
#         new_item = 2 * items
#         b_list.append(new_item)
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])


# number = int(input("Which number do you want to check? "))

# if number % 2 == 0:
#     print(" THis is an even number.")
# else:
#     print("This is an odd number.")

# year = input("Which year do you want to check? ")

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 ==0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap Year")
# else:
#     print("Not leap year.")


for number in range(1, 101):
    if number % 3 ==0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)