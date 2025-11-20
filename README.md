# personal_project_1
Boot.dev personal project 1

Initial Idea:
A program that will store different recipies. Each recipie is stored with all of its ingredients, and they will be compared to the pantry. When compared, a list will be printed with what can be made, and if it can't, what items are missing.

Ideas:
Functions needed
Get all recipies
    print_formatted_recipie_names
    should return a list of all the recipies in the data base
        input; recpies list
        output; prints the recipie name, formatted

Search for recipie
    get_recipie
    returns the ingredients list of a recipie
        input; recipie list, name
        output; returns the list that matches the name

Search for ingredient
    search_by_ingredient
    returns a list of recipies that share that ingredient

Get all items in pantry
    get_pantry
    returns a list of all items in the pantry

Get all recipies that can curretnly be made
    recipies_that_can_be_made
    return a list of all the recipies that can be made with what is currently in the pantry
        input: pantry and all recipies
        output:
            All recipies that can currently be made
            All recipies that can be partially made, with a list of what ingredients are currently missing
        function:
            take one recipie, search each ingrediant over the pantry and see if it's there. If they are all there it can be made. If one or more are missing, note the issing ingredient and add to the list if missing ingredients.
