import numpy as np
from matplotlib import pyplot as plt
from ColorFilter import ColorFilter

cf = ColorFilter()
array = plt.imread("../../resources/module03/ex03/elon_musk.png")
array2 = plt.imread("../../resources/module03/ex01/42AI.png")

for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert]:
    # array = plt.imread("../../resources/module03/ex01/42AI.png")
    array = plt.imread("../../resources/module03/ex03/elon_musk.png")
    plt.imshow(f(array))
    plt.show()

im = cf.to_grayscale(array, "m")
plt.imshow(im, cmap="gray")
plt.show()

im = cf.to_grayscale(array, "w", weights = [0.2126, 0.7152, 0.0722])
plt.imshow(im, cmap="gray")
plt.show()

# lignes utiles pour tester en ligne de commande :
# import numpy as np ; from matplotlib import pyplot as plt ; from ColorFilter import ColorFilter ; cf = ColorFilter(); array = plt.imread("../../resources/module03/ex03/elon_musk.png") ; array2 = plt.imread("../../resources/module03/ex01/42AI.png")
# c = cf.to_grayscale(array, "mean")
# plt.imshow(c) ; plt.show()