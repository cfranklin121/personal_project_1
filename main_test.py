from main import *
from recipies import *
from test_cases import *

name = "chicken"
ingredient = "yogurt"
print("Program Start...")
print("Print pantry:")
print(get_pantry(pantry))

print("Recipies:")
print(formatted_recipie_names(recipies))

print(f"Ingredients for {name}: {get_recipie(recipies, name)}")
print(f"Serching for recipies with {ingredient}:")
print(search_by_ingredient(recipies, ingredient))
print(f"Can make: {recipies_that_can_be_made(recipies, pantry)}")
print("Exit...")