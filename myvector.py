
class MyVector:

    def __init__(self, name_id, colour, typee, values):
        if not isinstance(name_id, str):
            raise ValueError("'name_id' should be a string.")
        valid_colours = {"r", "g", "b", "y", "m"}
        if colour not in valid_colours:
            raise ValueError("'colour' should be one of the possible values: 'r', 'g', 'b', 'y', 'm'.")
        if not (isinstance(typee, int) and typee >= 1):
            raise ValueError("'type' should be a positive integer greater or equal to 1.")
        if not (isinstance(values, list) and len(values) == 3 and all(isinstance(val,float) for val in values)):
            raise ValueError("'values' should be a list of 3 floats.")

        self.name_id = name_id
        self.colour = colour
        self.typee = typee
        self.values = values

    def get_name_id(self):
        return self.name_id

    def set_name_id(self, name_id):
        self.name_id = name_id

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour

    def get_type(self):
        return self.typee

    def set_type(self, typee):
        self.typee = typee

    def get_values(self):
        return self.values

    def set_values(self, values):
        self.values = values

    def add_scalar(self, scalar):
        self.values[0] += scalar
        self.values[1] += scalar
        self.values[2] += scalar

    def add_two_vectors(self, values1, values2):
        res_vector = []
        x = values1[0] + values2[0]
        y = values1[1] + values2[1]
        z = values1[2] + values2[2]
        res_vector.append(x)
        res_vector.append(y)
        res_vector.append(z)
        return res_vector

    def substract_two_vectors(self, values1, values2):
        res_vector = []
        x = values1[0] - values2[0]
        y = values1[1] - values2[1]
        z = values1[2] - values2[2]
        res_vector.append(x)
        res_vector.append(y)
        res_vector.append(z)
        return res_vector

    def multiplicate_two_vectors(self, values1, values2):
        result = values1[0] * values2[0] + values1[1] * values2[1] + values1[2] * values2[2]
        return result

    def sum_elements_vector(self, values):
        result = values[0] + values[1] + values[2]
        return result

    def product_elements_vector(self, values):
        result = values[0] * values[1] * values[2]
        return result

    def avg_elements_vector(self, values):
        result = (values[0] + values[1] + values[2]) / 3
        return result

    def min_elements_vector(self, values):
        return min(values[0], values[1], values[2])

    def max_elements_vector(self, values):
        return max(values[0], values[1], values[2])

    def __str__(self):
        return f"Vector '{self.name_id}' of type '{self.typee}', colour '{self.colour}' and coordinates {self.values}"
