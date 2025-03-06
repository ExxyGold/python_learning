# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400== 0:
#                 return "Leap Year"
#             else:
#                 return "Not Leap Year"
#         else:
#             return "Leap Year"
#     else:
#         return "Not Leap year"
    
# def days_in_month(Y, M):
#     """Gives the numbers of days in a year"""
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#     if is_leap(Y) == "Leap Year":
#         month_days[1] +=1
#         return month_days[M-1]
#     elif is_leap(Y)== "Not Leap Year":
#         return month_days[M-1]



# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days= days_in_month(year, month)
# print(days)


from pi_art import calc_logo, clear
#Calculator
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1- n2

def multiply(n1, n2):
    return n1 * n2

def divide( n1, n2):
    return n1/n2



operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    clear()
    print(calc_logo)
    num1= float(input("What's the first number?: "))

    for symbols in operations:
        print (symbols)

    while True:
        operation_symbol = input("Pick an operation from the  line above: ")
        num2 = float(input("What's the next number?: "))

        chosen = operations [operation_symbol]

        answer = chosen(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")


        ride_on = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start afresh: ").lower()

        if ride_on == "y":
            num1 = answer
        else:
            calculator()
calculator()
