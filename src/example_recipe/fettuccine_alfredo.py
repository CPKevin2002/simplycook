from src.recipe import Ingredient, Recipe, Step

"""
Example recipe for fettuccine alfredo, source: https://www.allrecipes.com/recipe/23431/to-die-for-fettuccine-alfredo/
"""

# TODO: fix print error when ingredients are labeled as "some" -- set default value of ingredients
def fettuccine_alfredo():
    r = Recipe(dish_name="fettuccine alfredo")
    r.add_ingredient(Ingredient("fettuccine pasta", 24, "ounces"))
    r.add_ingredient(Ingredient("butter", 1, "cup"))
    r.add_ingredient(Ingredient("heavy cream", .75, "pint"))
    r.add_ingredient(Ingredient("salt", 1, "some"))

