from myvector import MyVector
from vectorrepo import VectorRepository

def main():

    repository = VectorRepository()
    vector1 = MyVector("vector1", "r", 1, [1.0,1.0,1.0])
    vector2 = MyVector("vector2", "y", 2, [1.0,2.0,1.0])
    vector3 = MyVector("vector3", "g", 3, [2.0,2.0,1.0])
    vector4 = MyVector("vector4", "b", 3, [4.0,2.0,2.0])
    vector_list = [vector1, vector2, vector3, vector4]
    repository.set_list_of_vectors(vector_list)

    while True:
        print("\nMenu")
        print("1. Add a vector to the repository")
        print("2. Get all vectors")
        print("3. Get a vector at a given index")
        print("4. Update a vector at a given index")
        print("5. Update a vector identified by name_id")
        print("6. Delete a vector by index")
        print("7. Delete a vector by name_id")
        print("8. Plot all vectors in a chart")
        print("9. Extra")
        print("10. Exit")
        print(repository)

        try:

            choice = int(input("Enter your choice: "))

            if choice == 1:
                name_id = input("Enter 'name_id': ")
                colour = input("Enter 'colour': ")
                try:
                    typee = int(input("Enter 'type': "))
                    try:
                        coord_x = float(input("Enter 'coord_x': "))
                        coord_y = float(input("Enter 'coord_y': "))
                        coord_z = float(input("Enter 'coord_z': "))
                        values = [coord_x, coord_y, coord_z]
                        try:
                            vector = MyVector(name_id, colour, typee, values)
                            repository.add_vector(vector)
                            print("Vector succesfully added to the repository!")
                        except ValueError as e:
                            print(f"Error: {e}")
                    except ValueError:
                        print("Error: 'values' should be a list of 3 floats.")
                except ValueError:
                    print("Error: 'type' should be a positive integer greater or equal to 1.")

            if choice == 2:
                print(repository)

            if choice == 3:
                try:
                    index = int(input("Enter an index: "))
                    if 0 <= index < len(repository.get_list_of_vectors()):
                        print(f"The vector found at index '{index}' is:\n{repository.get_vector_at_index(index)}")
                    else:
                        print("Error: 'index' out of range")
                except ValueError:
                    print("Error: 'index' should be an integer.")

            if choice == 4:
                try:
                    index = int(input("Enter an index: "))
                    if 0 <= index < len(repository.get_list_of_vectors()):
                        name_id = input("Enter updated 'name_id': ")
                        colour = input("Enter updated 'colour': ")
                        try:
                            typee = int(input("Enter updated 'type': "))
                            try:
                                coord_x = float(input("Enter updated 'coord_x': "))
                                coord_y = float(input("Enter updated 'coord_y': "))
                                coord_z = float(input("Enter updated 'coord_z': "))
                                values = [coord_x, coord_y, coord_z]
                                try:
                                    repository.update_vector_at_index(index, name_id, colour, typee, values)
                                except ValueError as e:
                                    print(f"Error: {e}")
                            except:
                                print("Error: 'values' should be a list of 3 floats.")
                        except ValueError:
                            print("Error: 'type' should be a positive integer greater or equal to 1.")

                    else:
                        print("Error: 'index' out of range")
                except ValueError:
                    print("Error: 'index' should be an integer.")

            if choice == 5:
                try:
                    name_id = input("Enter the 'name_id': ")
                    index = repository.find_vector_by_name_id(name_id)
                    up_name_id = input("Enter updated 'name_id': ")
                    colour = input("Enter updated 'colour': ")
                    try:
                        typee = int(input("Enter updated 'type': "))
                        try:
                            coord_x = float(input("Enter updated 'coord_x': "))
                            coord_y = float(input("Enter updated 'coord_y': "))
                            coord_z = float(input("Enter updated 'coord_z': "))
                            values = [coord_x, coord_y, coord_z]
                            try:
                                repository.update_vector_at_index(index, up_name_id, colour, typee, values)
                            except ValueError as e:
                                print(f"Error: {e}")
                        except:
                            print("Error: 'values' should be a list of 3 floats.")
                    except ValueError:
                        print("Error: 'type' should be a positive integer greater or equal to 1.")
                except ValueError as e:
                    print(f"Error: {e}")

            if choice == 6:
                try:
                    index = int(input("Enter an index: "))
                    if 0 <= index < len(repository.get_list_of_vectors()):
                        repository.delete_vector_by_index(index)
                    else:
                        print("Error: 'index' out of range.")
                except ValueError:
                    print("Error: 'index' should be an integer.")

            if choice == 7:
                try:
                    name_id = input("Enter the 'name_id': ")
                    index = repository.find_vector_by_name_id(name_id)
                    repository.delete_vector_by_name_id(index)
                except ValueError as e:
                    print(f"Error: {e}")

            if choice == 8:
                repository.plot_vectors()

            if choice == 9:
                print("1. Get a list of values representing the multiplication of consecutive vectors in the repository")
                print("2. Delete all vectors for which the max value is equal to a given value")
                print("3. Update the colour of a vector identified by 'name_id'")

                try:

                    choice1 = int(input("Enter your choice: "))

                    if choice1 == 1:
                        try:
                            multiplication_result = repository.extra_16()
                            print("List of values representing the multiplication of consecutive vectors:")
                            print(multiplication_result)
                        except ValueError as e:
                            print(f"Error: {e}")

                    if choice1 == 2:
                        try:
                            value = float(input("Enter a value: "))
                            try:
                                repository.extra_20(value)
                            except ValueError as e:
                                print(f"Error: {e}")
                        except ValueError:
                            print("Error: 'value' should be a positive float/int.")

                    if choice1 == 3:
                        try:
                            name_id = input("Enter the 'name_id': ")
                            index = repository.find_vector_by_name_id(name_id)
                            try:
                                colour = input("Enter 'colour': ")
                                repository.extra_22(index, colour)
                            except ValueError as c:
                                print(f"Error: {c}")
                        except ValueError as e:
                            print(f"Error: {e}")


                except ValueError:
                    print("Error: 'choice' should be a positive integer (1-3)")

            if choice == 10:
                break

        except ValueError:
            print("Error: 'choice' should be a positive integer (1-10)")

if __name__ == "__main__":
    main()







