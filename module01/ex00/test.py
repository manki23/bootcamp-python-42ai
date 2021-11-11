from book import Book
from recipe import Recipe
import time

tourte = Recipe(
    'tourte',
    1,
    30,
    ['eggs', 'flour', 'sugar'],
    "",
    "dessert"
)
pizza = Recipe(
    'pizza',
    1,
    30,
    ['tomatoes', 'flour', 'cheese', 'water', 'salt'],
    "",
    "lunch"
)
pizza2 = Recipe(
    'pizza2',
    1,
    30,
    ['tomatoes', 'flour', 'cheese', 'water', 'salt'],
    "",
    "lunch"
)
print("===================TEST RECIPE ERROR MANAGEMENT=====================")
try:
    print(">>> TEST1 <<<")
    Recipe(None, None, None, None, None, None)
except SystemExit:
    pass
try:
    print(">>> TEST2 <<<")
    Recipe('', '', '', '', '', '')
except SystemExit:
    pass
try:
    print(">>> TEST3 <<<")
    Recipe('test', 0, -10, [], '', 'brrr')
except SystemExit:
    pass

print("===================TEST BOOK ERROR MANAGEMENT=====================")
try:
    print(">>> TEST1 <<<")
    Book(None, None)
except SystemExit:
    pass
try:
    print(">>> TEST2 <<<")
    Book('', '')
except SystemExit:
    pass
try:
    print(">>> TEST3 <<<")
    Book('test', {'lunch': [], 'dessert': 0})
except SystemExit:
    pass
try:
    print(">>> TEST4 <<<")
    Book('test', {'lunch': [], 'dessert': 0, 'starter': 4.2})
except SystemExit:
    pass
print("===================TEST RECIPE CORRECT BEHAVIOR===================")
print(">>> TEST str(recipe) <<<")
print(str(pizza))
print("===================TEST BOOK CORRECT BEHAVIOR=====================")
book = Book("Book1", {'lunch': [], 'dessert': [], 'starter': []})
print(">>> TEST creation_date and last_update have the same value <<<")
print(
    book.creation_date.strftime("%y/%m/%d %H:%M:%S")
    == book.last_update.strftime("%y/%m/%d %H:%M:%S")
)
print(book.creation_date.strftime("creation_date: %y/%m/%d %H:%M:%S"))
print(book.last_update.strftime("last_update: %y/%m/%d %H:%M:%S"))
print(">>> TEST adding recipes <<<")
time.sleep(1)
book.add_recipe(pizza)
book.add_recipe(pizza2)
book.add_recipe(tourte)
print(">>> CHECK last_update and creation_date <<<")
print(book.creation_date.strftime("creation_date: %y/%m/%d %H:%M:%S"))
print(book.last_update.strftime("last_update: %y/%m/%d %H:%M:%S"))
print(">>> TEST print_recipe_list <<<")
book.print_recipe_list()
print(">>> TEST get_recipes_by_types('lunch') <<<")
print(book.get_recipes_by_types('lunch'))
print(">>> TEST get_recipe_by_name('pizza') <<<")
book.get_recipe_by_name('pizza')

print("===================TEST BOOK FUNCTIONS ERROR MANAGEMENT===========")
try:
    print(">>> get_recipes_by_types(None) <<<")
    print(book.get_recipes_by_types(None))
except SystemExit:
    pass
try:
    print(">>> get_recipe_by_name(None) <<<")
    book.get_recipe_by_name(None)
except SystemExit:
    pass
print("===========================OVER AND OUT===========================")
