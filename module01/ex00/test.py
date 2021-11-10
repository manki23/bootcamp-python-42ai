from book import Book
from recipe import Recipe

tourte = Recipe('tourte', 1, 30, ['eggs', 'flour', 'sugar'], "", "dessert")
pizza = Recipe('pizza', 1, 30, ['tomatoes', 'flour', 'cheese', 'water', 'salt'], "", "lunch")
to_print = str(tourte)
print(to_print)