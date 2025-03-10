# from turtle import Turtle, Screen

# timmy = Turtle()


# my_screen = Screen()




# while True:
#     print(timmy)
#     timmy.shape("turtle")
#     timmy.color("blue")

#     timmy.forward(100)
#     timmy.right(120)

#     print(my_screen.canvheight)
    
from prettytable import PrettyTable

table = PrettyTable()



table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])

table.align = "l"


print(table)




    
    


   