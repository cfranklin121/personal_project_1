from recipies import *

def print_formatted_recipie_names(recipies):
    for recipie in recipies:
        for dict in recipie:
            for key in dict:
                if dict[key] == "*":
                    print(key.capitalize())

def get_recipie(recipies, name):
    print(f"Searching for {name}...")
    for recipie in recipies:
        #print(f"layer 1 {recipie}")
        for dict in recipie:
            #print(f"    layer 2 {dict}")
            for key in dict:
                #print(f"        layer 3 {key}")
                if dict[key] == "*":
                    if key == name.lower():
                        return recipie[1:]
    return "No recipie found"

def main():
    print("Program Start...")
    print_formatted_recipie_names(recipies)
    print(get_recipie(recipies, "spagetti"))
    print("Exit...")

if __name__ == "__main__":
    main()