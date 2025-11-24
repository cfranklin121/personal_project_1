pantry_test = [
    {"eggs": 12, "milk": 1, "flower": 5, "pasta": 1, "tomatoes": 2, "shrimp": 1, "pasta": 1, "butter": 3, "olive oil": 3, "red pepper flake": 0.5, "garlic": 4, "white wine": 0.5, "parsley": 3, "lemon": 1}
    ]

recipies_test = [
    ["cake", {"eggs": 1, "milk": 1, "flower": 5}],
    ["spagetti", {"pasta": 1, "tomatoes": 2}],
    ["shrimp scampi", {"shrimp": 1, "pasta": 1, "butter": 3, "olive oil": 3, "red pepper flake": 0.5, "garlic": 4, "white wine": 0.5, "parsley": 3, "lemon": 1}],
    ["meatloaf", {"ground beef": 1, "eggs": 1, "oats": 0.5, "beefy onion soup mix": 1}]
]


results = [
    "['eggs', 'milk', 'flower', 'pasta', 'tomatoes', 'shrimp', 'butter', 'olive oil', 'red pepper flake', 'garlic', 'white wine', 'parsley', 'lemon']",
    "['Cake', 'Spagetti', 'Shrimp scampi', 'Meatloaf']",
    "['ground beef', 'eggs', 'oats', 'beefy onion soup mix']",
    "['shrimp scampi']",
    "['cake', 'spagetti', 'shrimp scampi']",
]