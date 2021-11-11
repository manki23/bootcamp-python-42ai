from recipe import Recipe
from datetime import datetime
import sys


class Book:
    name = ""
    last_update = 0  # datetime
    creation_date = 0  # datetime
    # a dictionnary with 3 keys: "starter", "lunch", "dessert"
    recipes_list = {}

    def check_input(self, name, recipes_list):
        should_exit = False
        if not isinstance(name, str) or len(name) < 1:
            print("InputError: <name> must be a string (cannot be empty)")
            should_exit = True
        if not isinstance(recipes_list, dict):
            print("InputError: <recipes_list> must be a dictionary")
            should_exit = True
        meals = ['starter', 'lunch', 'dessert']
        if (
            isinstance(recipes_list, dict) and
            set(recipes_list.keys()) != set(meals)
        ):
            print(f"InputError: recipes_list must have 3 keys: {meals}")
            should_exit = True
        elif (
            isinstance(recipes_list, dict) and
            set(recipes_list.keys()) == set(meals)
        ):
            for key, value in recipes_list.items():
                if not isinstance(value, list):
                    print(f"InputTypeError: <{key}> must contain "
                          + "a list of recipe")
                    should_exit = True
        if should_exit:
            sys.exit()

    def __init__(self, name, recipes_list):
        self.check_input(name, recipes_list)
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name and returns the instance"""
        if not isinstance(name, str) or len(name) < 1:
            print("InputError: name must be a valid string")
        else:
            for rec_type, rec_list in self.recipes_list.items():
                for elem in rec_list:
                    if elem.name == name:
                        print(str(elem))
                        return elem

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        meals = ['starter', 'lunch', 'dessert']
        if recipe_type not in meals:
            print(f"InputError: recipe_type must be one of {meals}")
        else:
            recipes = self.recipes_list[recipe_type]
            rec_names = [elem.name for elem in recipes]
            return rec_names

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        recipe_set = [
            'name',
            'cooking_lvl',
            'cooking_time',
            'ingredients',
            'description',
            'recipe_type'
        ]
        if not isinstance(recipe, Recipe):
            print(f"InputError: object {recipe} is not an instance of Recipe")
        elif set(recipe.__dict__.keys()) != set(recipe_set):
            print(f"InputError: object recipe corrupted, "
                  + "it should contain the following keys : {recipe_set}")
        else:
            recipe_type = recipe.__dict__['recipe_type']
            self.recipes_list[recipe_type].append(recipe)
            self.last_update = datetime.now()

    def print_recipe_list(self):
        print("-----------------RECIPE LIST-----------------")
        for rec_type, value in self.recipes_list.items():
            print(f"================ {rec_type} ================")
            for recipe in value:
                print(str(recipe))
                print("========================================\n")
        print("---------------------------------------------\n")
