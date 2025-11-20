from recipies import *

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
    name = "Meatloaf"
    ingredient = "White wine"
    print("Program Start...")
    print("Pantry:")
    print(get_pantry(pantry))
    print("Recipies:")
    print(formatted_recipie_names(recipies))
    
    print(f"Ingredients for {name}: {get_recipie(recipies, name)}")
    print(f"Serching for recipies with {ingredient}:")
    print(search_by_ingredient(recipies, ingredient))
    print(f"Can make: {recipies_that_can_be_made(recipies, pantry)}")
    print("Exit...")

if __name__ == "__main__":
    main()