import sys


class Vector:
    def is_column_vector(self, values):
        if (
            isinstance(values, list) and
            all(isinstance(value, list) for value in values) and
            not any(
                not isinstance(value, list) or
                len(value) != 1 or
                not isinstance(value[0], float)
                for value in values
            )
        ):
            return True
        else:
            return False

    def is_raw_vector(self, values):
        if (
            isinstance(values, list) and
            all(isinstance(value, float) for value in values)
        ):
            return True
        else:
            return False

    def is_tuple(self, values):
        if (
            isinstance(values, tuple) and
            len(values) == 2 and
            isinstance(value[0], int) and
            isinstance(value[1], int) and
            values[0] < value[1] and
            values[0] > 0
        ):
            return True
        else:
            return False
    
    def print_usage(self):
        print("Vector can be initialized with:")
        print("-> a list of floats: Vector([0.0, 1.0, 2.0, 3.0]),")
        print("-> a list of list of floats: Vector([[0.0], [1.0], [2.0],",
              " [3.0]]),")
        print("-> a size: Vector(3) -> the vector will have values = ",
              "[[0.0], [1.0], [2.0]],")
        print("-> a range: Vector((10,15)) -> the vector will have values",
              " = [[10.0], [11.0], [12.0], [13.0], [14.0]]")

    def __init__(self, values):
        if self.is_column_vector(values):
            self.shape = (len(values), 1)
            self.values = values
        elif self.is_raw_vector(values):
            self.shape = (1, len(values))
            self.values = values
        elif isinstance(values, int) and values > 0:
            self.shape = (values, 1)
            self.values = [[float(elem)] for elem in range(0, values - 1)]
        elif self.is_tuple(values):
            self.shape = (values[1] - values[0], 1)
            values_range = range(values[0], values[1] - 1)
            self.values = [[float(elem)] for elem in values_range]
        else:
            print("InputError: ", end="")
            self.print_usage()
            sys.exit()

    def check_vector(self, vector):
        return self.is_column_vector(vector) or self.is_raw_vector(vector)

    def __add__(self, other):
        if (
            self.is_column_vector(self.values) and
            self.is_column_vector(other) and
            self.shape[0] == len(other)
        ):
            return [[x[0] + y[0]] for x, y in zip(self.values, other)]
        elif (
            self.is_raw_vector(self.values) and
            self.is_raw_vector(other) and
            self.shape[1] == len(other)
        ):
            return [x + y for x, y in zip(self.values, other)]
        else:
           raise ValueError("") 

    def __radd__(self, other):
        pass

    # add : only vectors of same dimensions.
    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        pass

    # sub : only vectors of same dimensions.
    def __truediv__(self, other):
        pass

    def __rtruediv__(self, other):
        pass

    # div : only scalars.
    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    # mul : only scalars.
    def __str__(self):
        pass

    def __repr__(self):
        pass
    
    def dot(self, other):
        pass

    def T(self):
        pass
