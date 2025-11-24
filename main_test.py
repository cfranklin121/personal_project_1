from main import *
from recipies import *
from test_cases import *

print("-------------------------------")
passed = 0
failed = 0
i = 0

name = "Meatloaf"
ingredient = "White wine"

print("Program Start...")
print("Test get_pantry():")
print("Expected: ", results[0])
print("Result:   ", get_pantry(pantry_test))
if str(get_pantry(pantry_test)) == results[0]:
    passed += 1
    print("=====PASS=====")
else:
    failed += 1
    print("=====FAIL=====")

print()

print("Test formatted_recipie_names():")
print("Expected: ", results[1])
print("Result: ", formatted_recipie_names(recipies))
if str(formatted_recipie_names(recipies)) == results[1]:
    passed += 1
    print("=====PASS=====")
else:
    failed += 1
    print("=====FAIL=====")

print()

print("Test get_recipie():")
print("Expected: ", results[2])
print(f"Result for {name}: {get_recipie(recipies, name)}")
if str(get_recipie(recipies, name)) == results[2]:
    passed += 1
    print("=====PASS=====")
else:
    failed += 1
    print("=====FAIL=====")

print()

print("Test search_by_ingredient():")
print("Expected: ", results[3])
print(f"Result for {ingredient}:", search_by_ingredient(recipies, ingredient))
if str(search_by_ingredient(recipies, ingredient)) == results[3]:
    passed += 1
    print("=====PASS=====")
else:
    failed += 1
    print("=====FAIL=====")

print()

print("Test recipies_that_can_be_made():")
print("Expected: ", results[4])
print(f"Result: {recipies_that_can_be_made(recipies, pantry_test)}")
if str(recipies_that_can_be_made(recipies, pantry_test)) == results[4]:
    passed += 1
    print("=====PASS=====")
else:
    failed += 1
    print("=====FAIL=====")

print(f"Passed: {passed}, Failed: {failed}")
print("Exit...")
    
    
    
    
    
    
    
    

'''
    print("Input")
    for t in test:
        print(f"{t}")
    result = fix_the_networks(test)
    print(f"Expected: {expected[i]}")
    print(f"Actual: {result}")

    if expected[i] == result:
        passed += 1
        print("=====PASS=====")
    else:
        failed += 1
        print("=====FAIL=====")
    i += 1
    print("-------------------------------")
print(f"Passed: {passed}, Failed: {failed}")
'''