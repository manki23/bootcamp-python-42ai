import sys

class Recipe:
    def check_input(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        should_exit = False
        if not isinstance(name, str) or len(name) < 1:
            print("InputError: <name> must be a string (cannot be empty)")
            should_exit = True
        if not isinstance(cooking_lvl, int) or int(cooking_lvl) < 1 or int(cooking_lvl) > 5:
            print("InputError: <cooking_lvl> must be an integer between 1 and 5")
            should_exit = True
        if not isinstance(cooking_time, int) or int(cooking_time) < 0:
            print("InputError: <cooking_time> must be an integer (no negative numbers)")
            should_exit = True
        if not isinstance(ingredients, list) or len(ingredients) < 1:
            print("InputError: <ingredients> must be a list (cannot be empty)")
            should_exit = True
        if not isinstance(description, str):
            print("InputError: <description> must be a string")
            should_exit = True
        if not isinstance(recipe_type, str) or recipe_type not in ["starter", "lunch", "dessert"]:
            print("InputError: <recipe_type> must be one of 'starter', 'lunch' or 'dessert'")
            should_exit = True
        if should_exit:
            sys.exit()


    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.check_input(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
        self.name = name
        self.cooking_lvl = cooking_lvl  # range from 1 to 5
        self.cooking_time = cooking_time  # in minutes (no negative numbers)
        self.ingredients = ingredients  # list of all ingredients each represented by a string
        self.description = description  # description of the recipe
        self.recipe_type = recipe_type  # can be "starter", "lunch" or "dessert"


    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"Recipe name: {self.name}\n"
        txt += f"Level: {self.cooking_lvl}\n"
        txt += f"Cooking time: {self.cooking_time}\n"
        txt += f"Ingredients: {', '.join(self.ingredients)}\n"
        txt += f"Description: {self.description}\n"
        txt += f"Recipe type: {self.recipe_type}\n"
        return txt

