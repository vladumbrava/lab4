import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
class VectorRepository:

    def __init__(self):
        """
           Initializes an empty VectorRepository.

           Input:
           - None

           Output:
           - None

           Description:
           This constructor initializes an empty list to store vectors.
        """
        self.vectors_list = []

    def get_list_of_vectors(self):
        """
            Get the list of vectors in the repository.

            Input:
            - None

            Output:
            - List of MyVector objects

            Description:
            Returns the list of vectors stored in the repository.
        """
        return self.vectors_list

    def set_list_of_vectors(self, vectors_list):
        """
            Set the list of vectors in the repository.

            Input:
            - vectors_list: List of MyVector objects

            Output:
            - None

            Description:
            Sets the list of vectors in the repository with the provided list.
        """
        self.vectors_list = vectors_list

    def add_vector(self, vector):
        """
            Add a vector to the repository.

            Input:
            - vector: MyVector object

            Output:
            - None

            Description:
            Adds the given vector to the repository. Checks if the 'name_id' of the vector
            doesn't already exist in the repository to avoid duplicates.
        """
        for v in self.vectors_list:
            if v.name_id == vector.name_id:
                raise ValueError("chosen 'name_id' already exists in the repository.")
        self.vectors_list.append(vector)

    def get_vector_at_index(self, index):
        """
            Get a vector at a specified index in the repository.

            Input:
            - index: Integer index

            Output:
            - MyVector object or None

            Description:
            Returns the vector at the specified index in the repository.
            Returns None if the index is out of range.
        """
        if not isinstance(index, int):
            raise ValueError("'index' should be an integer.")
        if 0 <= index < len(self.vectors_list):
            return self.vectors_list[index]

    def update_vector_at_index(self, index, name_id, colour, typee, values):
        """
            Update a vector at a specified index in the repository.

            Input:
            - index: Integer index
            - name_id: String
            - colour: String ('r', 'g', 'b', 'y', 'm')
            - typee: Integer (greater or equal to 1)
            - values: List of 3 floats

            Output:
            - MyVector object or None

            Description:
            Updates the vector at the specified index in the repository with the provided
            'name_id', 'colour', 'typee', and 'values'. Validates input types and conditions
            (e.g., 'typee' should be a positive integer greater or equal to 1).
            Returns the updated vector or None if the index is out of range.
        """
        if 0 <= index < len(self.vectors_list):
            if not isinstance(name_id, str):
                raise ValueError("'name_id' should be a string.")
            valid_colours = {"r", "g", "b", "y", "m"}
            if colour not in valid_colours:
                raise ValueError("'colour' should be one of the possible values: 'r', 'g', 'b', 'y', 'm'.")
            if not (isinstance(typee, int) and typee >= 1):
                raise ValueError("'type' should be a positive integer greater or equal to 1.")
            if not (isinstance(values, list) and len(values) == 3 and all(isinstance(val, float or int) for val in values)):
                raise ValueError("'values' should be a list of 3 floats.")

            self.vectors_list[index].name_id = name_id
            self.vectors_list[index].colour = colour
            self.vectors_list[index].typee = typee
            self.vectors_list[index].values = values
            return self.vectors_list[index]
        else:
            return None

    def find_vector_by_name_id(self, name_id):
        """
            Find the index of a vector with a specified 'name_id'.

            Input:
            - name_id: String

            Output:
            - Integer index or None

            Description:
            Searches for the vector with the provided 'name_id' in the repository.
            Returns the index of the vector if found, otherwise returns None.
        """
        index = -1
        for i in range(len(self.vectors_list)):
            if self.vectors_list[i].name_id == name_id:
                index = i
        if index == -1:
            raise ValueError("there exists no vector with chosen 'name_id'.")
        return index

    def update_vector_found_by_name_id(self, index, name_id, colour, typee, values):
        """
           Update a vector identified by 'name_id' in the repository.

           Input:
           - index: Integer index
           - name_id: String
           - colour: String ('r', 'g', 'b', 'y', 'm')
           - typee: Integer (greater or equal to 1)
           - values: List of 3 floats

           Output:
           - MyVector object

           Description:
           Updates the vector identified by 'name_id' in the repository with the provided
           'name_id', 'colour', 'typee', and 'values'. Validates input types and conditions
           (e.g., 'typee' should be a positive integer greater or equal to 1).
        """
        if not isinstance(name_id, str):
            raise ValueError("'name_id' should be a string.")
        valid_colours = {"r", "g", "b", "y", "m"}
        if colour not in valid_colours:
            raise ValueError("'colour' should be one of the possible values: 'r', 'g', 'b', 'y', 'm'.")
        if not (isinstance(typee, int) and typee >= 1):
            raise ValueError("'type' should be a positive integer greater or equal to 1.")
        if not (isinstance(values, list) and len(values) == 3 and all(isinstance(val,float) for val in values)):
            raise ValueError("'values' should be a list of 3 floats.")
        self.vectors_list[index].name_id = name_id
        self.vectors_list[index].colour = colour
        self.vectors_list[index].typee = typee
        self.vectors_list[index].values = values
        return self.vectors_list[index]

    def delete_vector_by_index(self, index):
        """
            Delete a vector at a specified index in the repository.

            Input:
            - index: Integer index

            Output:
            - None

            Description:
            Deletes the vector at the specified index in the repository.
        """
        if 0 <= index < len(self.vectors_list):
            self.vectors_list.pop(index)

    def delete_vector_by_name_id(self, index):
        """
            Delete a vector identified by 'name_id' in the repository.

            Input:
            - index: Integer index

            Output:
            - None

            Description:
            Deletes the vector identified by 'name_id' in the repository.
        """
        self.vectors_list.pop(index)

    def extra_16(self):
        """
            Perform vector multiplication for consecutive vectors.

            Input:
            - None

            Output:
            - List of multiplication results

            Description:
            Performs vector multiplication for consecutive vectors in the repository.
            Raises an error if there are not enough vectors in the repository to perform multiplication.
        """
        mul_list = []
        if len(self.vectors_list) < 2:
            raise ValueError("there are not enough vectors in the repository to perform multiplication.")
        for i in range(len(self.vectors_list) - 1):
            vector1 = self.vectors_list[i].get_values()
            vector2 = self.vectors_list[i+1].get_values()
            mul_value = self.vectors_list[i].multiplicate_two_vectors(vector1, vector2)
            mul_list.append(mul_value)
        return mul_list

    def extra_20(self, value):
        """
            Delete vectors with the maximum element equal to a specified value.

            Input:
            - value: Float

            Output:
            - None

            Description:
            Deletes vectors in the repository whose maximum element is equal to the specified value.
            Raises an error if there are no vectors in the repository.
        """
        if self.vectors_list == []:
            raise ValueError("no vectors in the repository.")
        for i in range(len(self.vectors_list)):
            vector_value = self.vectors_list[i].get_values()
            max_value = self.vectors_list[i].max_elements_vector(vector_value)
            if max_value == value:
                self.vectors_list.pop(i)

    def extra_22(self, index, colour):
        """
            Update the colour of a vector at a specified index.

            Input:
            - index: Integer index
            - colour: String ('r', 'g', 'b', 'y', 'm')

            Output:
            - None

            Description:
            Updates the colour of the vector at the specified index with the provided colour.
            Raises an error if the specified colour is not one of the possible values: 'r', 'g', 'b', 'y', 'm'.
        """
        valid_colours = {"r", "g", "b", "y", "m"}
        if colour not in valid_colours:
            raise ValueError("'colour' should be one of the possible values: 'r', 'g', 'b', 'y', 'm'.")
        self.vectors_list[index].set_colour(colour)

    def plot_vectors(self):
        """
            Plot vectors in a 3D chart.

            Input:
            - None

            Output:
            - None

            Description:
            Plots vectors in a 3D chart using the Matplotlib library.
            Each vector is represented by a point in the chart with different colours and markers based on type and colour.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        colors = {'r': 'red', 'g': 'green', 'b': 'blue', 'y': 'yellow', 'm': 'magenta'}
        markers = {1: 'o', 2: 's', 3: '^'}

        for vector in self.vectors_list:
            x, y, z = vector.get_values()
            color = colors.get(vector.get_colour(), 'black')
            marker = markers.get(vector.get_type(), 'D')

            ax.scatter(x, y, z, c=color, marker=marker, label=f'{vector.get_name_id()}')

        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        ax.set_title('Vectors 3D Plot')
        ax.legend()

        plt.show()

    def __str__(self):
        """
            String representation of the VectorRepository.

            Input:
            - None

            Output:
            - String

            Description:
            Returns a string representation of the VectorRepository, including information about each vector.
        """
        result = "Vector repository:"
        for vector in self.vectors_list:
            result += f"\n{vector}"
        return result
