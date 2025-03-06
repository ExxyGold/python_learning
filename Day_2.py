print("Welcome to Tip Calculator")
bill = int(input("How much is your total bill? $"))
percent= int(input("What percentage tip will you like to give? 10, 12 or 15? "))
person= int(input("How many people to split the bill? "))

tot_bill= float (bill + (bill * 0.01 * percent))
each = round(tot_bill / person, 2)
print(f"Each person is to pay ${each}")