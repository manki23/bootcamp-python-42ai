class Book:
    name = ""
    last_update = 0  # datetime
    creation_date = 0  # datetime
    recipes_list = {} # a dictionnary with 3 keys: "starter", "lunch", "dessert"

    def check_input(self, name, last_update, creation_date, recipes_list):
        should_exit = False
        if not isinstance(name, str) or len(name) < 1:
            print("InputError: <name> must be a string (cannot be empty)")
            should_exit = True
        if not isinstance(last_update, str) or len(ingredients) < 1:
            print("InputError: <last_update> must be a datetime")
            should_exit = True
        if not isinstance(creation_date, str):
            print("InputError: <creation_date> must be a datetime")
            should_exit = True
        if not isinstance(recipes_list, dict):
            print("InputError: <recipes_list> must be a dictionary")
            should_exit = True
        if should_exit:
            sys.exit()

    def __init__(self, name, last_update, creation_date, recipes_list):
        self.check_input(name, last_update, creation_date, recipes_list)
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        pass
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        pass
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass