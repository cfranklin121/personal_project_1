from recipies import *
from help import *
import os

def formatted_recipie_names(recipies):
    names = []
    for recipie in recipies:
        names.append(recipie[0].capitalize())

    return names

def get_recipie(recipies, name):
    print(f"Searching for {name}...")
    for recipie in recipies:
        if recipie[0] == name.lower():
            for dict in recipie[1:]:
                ingredients = []
                for key in dict:
                    ingredients.append(key)
                                     
            return ingredients
    return "No recipie found"

def search_by_ingredient(recipies, name):
    result = [] 
    for recipie in recipies:
        for dict in recipie[1:]:
            for key in dict:
                if key == name.lower():
                    result.append(recipie[0])
    if len(result) > 0:
        return result
    return "No result found"

def get_pantry(pantry):
    result = []
    for item in pantry:
        for key in item:
            result.append(key)
    if len(result) > 0:
        return result
    return "Your pantry is empty."

def recipies_that_can_be_made(recipies, pantry):
    result = []
    for recipie in recipies:
        can_make = True
        for dict in recipie[1:]:
            for key in dict:
                for dict2 in pantry:
                    if key in dict2:
                        can_make = True
                    else:
                        can_make = False                            

        if can_make:
            result.append(recipie[0])
    return result

def main():
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

if __name__ == "__main__":
    main()