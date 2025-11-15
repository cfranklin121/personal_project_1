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

def main():
    print("Program Start...")
    print("Recipies:")
    print(formatted_recipie_names(recipies))
    name = "cake"
    print(f"ingredients for {name}: {get_recipie(recipies, name)}")
    print("Exit...")

if __name__ == "__main__":
    main()