from main import *
from recipies import *
from help import *
import os

run = True

while run:
    os.system('clear')
    selection = 0
    print("============WELCOME============")
    print("View pantry:                  1")
    print("View all recipies:            2")
    print("Search recipies:              3")
    print("Search by ingredient          4")
    print("View makeable recipies:       5")
    print("Help                          6")
    print("Exit:                         7")
    selection = int(input())

    match selection:
        case 1:
            print(get_pantry(pantry)) 
        case 2:
            print(formatted_recipie_names(recipies))
        case 3:
            name = input("Enter name: ")
            print(get_recipie(recipies, name))
        case 4:
            name = input("Enter ingredient: ")
            print(search_by_ingredient(recipies, name))
        case 5:
            print(recipies_that_can_be_made(recipies, pantry))
        case 6:
            help()
        case 7:
            run = False
        case _:
            print("Invalid Selection")
        
    input("Press any key to continue...")


