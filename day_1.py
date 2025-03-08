# print("Welcome to Band name Generator.")
# city= input("What's the name of the city you grew up in?\n")
# pet= input("What's your pet's name?\n")
# print("Your band name could be "+ city + " " + pet)

sequence = int(input("How many numbers would you like to have in your sequence: "))

def highest(maximum):
    number = [0, 1]

    for numbers in range(2, maximum):

        value = number[numbers - 1] + number[numbers - 2]

        number.append(value)

    if maximum == 1:
        return [number[0]]
    else:
        return number

output = highest(sequence)

print(output)

# lets say we have a sequence of 8 numbers
# the next number should be the addition of last number and second to last 