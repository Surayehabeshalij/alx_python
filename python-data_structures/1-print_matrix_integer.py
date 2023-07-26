def print_matrix_integer(matrix=[[]]):
    # Iterate over each row in the matrix
    for i, row in enumerate(matrix):
        # Iterate over each element in the row and print it with a space character at the end
         for j, element in enumerate(row):
            print("{:d}".format(element), end="")
            if j < len(row) - 1:
                print(" ", end="")
       
