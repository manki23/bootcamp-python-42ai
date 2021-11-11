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

    def is_row_vector(self, values):
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
        elif self.is_row_vector(values):
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
        return self.is_column_vector(vector) or self.is_row_vector(vector)

    def add(self, v1, v2):
        if self.check_column_vector(v1, v2):
            return [[x[0] + y[0]] for x, y in zip(v1, v2)]
        elif self.check_row_vector(v1, v2):
            return [x + y for x, y in zip(v1, v2)]
        else:
            raise ValueError("Cannot add vectors with different sizes")

    # add : only vectors of same dimensions.
    def __add__(self, other):
        self.add(self.values, other)

    def __radd__(self, other):
        self.add(other, self.values)

    # sub : only vectors of same dimensions.
    def sub(self, v1, v2):
        if self.check_column_vector(v1, v2):
            return [[x[0] - y[0]] for x, y in zip(v1, v2)]
        elif self.check_row_vector(v1, v2):
            return [x - y for x, y in zip(v1, v2)]
        else:
            raise ValueError("Cannot substract vectors with different sizes")

    def __sub__(self, other):
        self.sub(self.values, other)

    def __rsub__(self, other):
        self.sub(other, self.values)

    def check_row_vector(self, v1, v2, check_zero=False):
        return (
            self.is_row_vector(v1) and
            self.is_row_vector(v2) and
            len(v1) == len(v2) and
            not (check_zero and any(y == 0 for y in v2))
        )

    def check_column_vector(self, v1, v2, check_zero=False):
        return (
            self.is_column_vector(v1) and
            self.is_column_vector(v2) and
            len(v1) == len(v2) and
            not (check_zero and any(y == 0 for y in v2))
        )

    # div : only scalars.
    def __truediv__(self, other):
        if (
            self.is_column_vector(self.values) and
            (isinstance(other, float) or isinstance(other, int)) and
            float(other) != 0.0
        ):
            return [[x[0] / other] for x in self.values]
        elif (
            self.is_row_vector(self.values) and
            (isinstance(other, float) or isinstance(other, int)) and
            float(other) != 0.0
        ):
            return [x / other for x in self.values]
        elif self.check_column_vector(self.values, other, True):
            return [[x[0] / y[0]] for x, y in zip(self.values, other)]
        elif self.check_row_vector(self.values, other, True):
            return [x / y for x, y in zip(self.values, other)]
        else:
            raise ValueError("__truediv__ can only be used with "
                             + "a scalar different from zero")

    def __rtruediv__(self, other):
        if (
            self.is_column_vector(self.values) and
            (isinstance(other, float) or isinstance(other, int)) and
            all(y != 0 for y in self.values)
        ):
            return [[other / y[0]] for y in self.values]
        elif (
            self.is_row_vector(self.values) and
            (isinstance(other, float) or isinstance(other, int)) and
            all(y != 0 for y in self.values)
        ):
            return [other / y for y in self.values]
        elif self.check_column_vector(other, self.values, True):
            return [[x[0] / y[0]] for x, y in zip(other, self.values)]
        elif self.check_row_vector(other, self.values, True):
            return [x / y for y in zip(other, self.values)]
        else:
            raise ValueError("__rtruediv__ can only be used with "
                             + "a scalar different from zero")

    def mul(self, v1, v2, mul_type):
        if (
            self.is_column_vector(v1) and
            (isinstance(v2, float) or isinstance(v2, int))
        ):
            return [[x[0] * v2] for x in v1]
        elif (
            self.is_row_vector(v1) and
            (isinstance(v2, float) or isinstance(v2, int))
        ):
            return [x * v2 for x in v1]
        elif self.check_column_vector(v1, v2):
            return [[x[0] * y[0]] for x, y in zip(v1, v2)]
        elif self.check_row_vector(v1, v2):
            return [x * y for x, y in zip(v1, v2)]
        else:
            raise ValueError(f"{mul_type} can only be used with "
                             + "a scalar different from zero")

    # mul : only scalars.
    def __mul__(self, other):
        self.mul(self.values, other, "__mul__")

    def __rmul__(self, other):
        self.mul(other, self.values, "__rmul__")

    def __str__(self):
        return f"Values: {self.values}\nShape: {self.shape}"

    def __repr__(self):
        return f"Vector({self.values})"

    def dot(self, other):
        if self.check_column_vector(self.values, other):
            return sum([x[0] * y[0] for x, y in zip(v1, v2)])
        elif self.check_row_vector(v1, v2):
            return sum([x * y for x, y in zip(v1, v2)])
        else:
            raise ValueError(f".dot() can only be used with "
                             + "two vectors of same dimension m")

    def T(self):
        if self.is_column_vector(self.values):
            self.values = [x[0] for x in self.values]
            self.shape = (self.shape[1], self.shape[0])
            return self
        elif self.is_row_vector(self.values):
            self.values = [[x] for x in self.values]
            self.shape = (self.shape[1], self.shape[0])
            return self
        else:
            raise ValueError(f".T() failed, vector data corrupted")
