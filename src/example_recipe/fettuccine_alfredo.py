from src.recipe import Ingredient, Recipe, Step
from datetime import timedelta

"""
Example recipe for fettuccine alfredo, source: https://www.allrecipes.com/recipe/23431/to-die-for-fettuccine-alfredo/
"""

def fettuccine_alfredo() -> Recipe:
    r = Recipe(dish_name="fettuccine alfredo")
    r.add_ingredient(Ingredient("fettuccine pasta", 24, "ounces"))
    r.add_ingredient(Ingredient("butter", 1, "cup"))
    r.add_ingredient(Ingredient("heavy cream", .75, "pint"))
    r.add_ingredient(Ingredient("salt", 1, "some"))
    r.add_ingredient(Ingredient("pepper", 1, "some"))
    r.add_ingredient(Ingredient("garlic salt", 1, "dash"))
    r.add_ingredient(Ingredient("Romano cheese", .75, "cup"))
    r.add_ingredient(Ingredient("grated Parmesan cheese", .5, "cup"))

    r.add_step(Step(
        "Bring a large pot of lightly salted water to a boil. \
        Add fettuccine and cook for 8 to 10 minutes or until al dente; drain.",
        timedelta(minutes=15), "pot", True))

    r.add_step(Step("Melt butter into cream in a large saucepan over low heat \
    add salt, pepper, and garlic salt. Increase the heat to medium \
    stir in grated Romano and Parmesan cheese until melted and sauce has thickened.", timedelta(minutes=7), "pot", False))

    r.add_step(Step("Add cooked pasta to sauce and toss until thoroughly coated; serve immediately.", timedelta(minutes=5), "pot", False))

    return r

