cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10  # time in minutes
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60  # time in minutes
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15  # time in minutes
    }
}

# 1.
# print(cookbook.keys()) # print dictionary keys
# print(cookbook.values()) # print dictionary values
# print(cookbook.items()) # print dictonary items


# 2.
def print_recipe(name):
    if name in cookbook:
        print(f"Recipe for {name}:")
        print("Ingredients list: {}".format(cookbook[name]['ingredients']))
        print("To be eaten for {}.".format(cookbook[name]['meal']))
        print(f"Takes {cookbook[name]['prep_time']} minutes of cooking.")
    else:
        print(f"Recipe {name} doesn't exist in the cookbook.")
    print("\n--------------------------------------------------------------\n")


# 3.
def del_recipe(name):
    del cookbook[name]


# 4.
def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time  # time in minutes
    }


# 5.
def print_recipe_names():
    print("The recipies in the cookbook are:\n-", "\n- ".join(cookbook.keys()))


# 6.
def print_menu():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")


def add_recipe_action():
    name = str(input("Enter recipe\'s name:\n>> "))
    n = int(input("Enter number of ingredients :\n>> "))
    print(f"Enter {str(name)}\'s list of ingredients:")
    ingredients = []
    for i in range(0, n):
        ingredients.append(str(input(f"ingredient {i + 1} >> ")))
    meal = str(input("Enter the type of meal:\n>> "))
    prep_time = int(input("Enter the preparation time in minutes:\n>> "))
    add_recipe(name, ingredients, meal, prep_time)
    print(name + "\'s recipe successfully added.\n")


def del_recipe_action():
    print("Please enter the name of the recipe you wish to delete:")
    name = str(input(">> "))
    if name in cookbook:
        del_recipe(name)
        print(name + "\'s recipe successfully deleted.")
    else:
        print(f"Recipe {name} doesn't exist in the cookbook.")
    print("\n--------------------------------------------------------------\n")


def print_recipe_action():
    print("Please enter the recipe's name to get its details:")
    name = str(input(">> "))
    print()
    print_recipe(name)


def print_cookbook_action():
    print("---------------------------COOKBOOK---------------------------\n")
    for elem in cookbook.keys():
        print_recipe(elem)
    if len(cookbook) == 0:
        print("The cookbook is empty.\n")


keep_going = True
show_menu = True

while keep_going:
    if show_menu:
        print_menu()
    choice = input(">> ")
    print()
    if choice == "1":
        add_recipe_action()
        show_menu = True
    elif choice == "2":
        del_recipe_action()
        show_menu = True
    elif choice == "3":
        print_recipe_action()
        show_menu = True
    elif choice == "4":
        print_cookbook_action()
        show_menu = True
    elif choice == "5":
        print("Cookbook closed.")
        keep_going = False
    else:
        print("This option does not exist, " +
              "please type the corresponding number.")
        print("To exit, enter 5.")
        show_menu = False
