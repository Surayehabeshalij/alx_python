def print_matrix_integer(matrix=[[]]):
    # Iterate over each row in the matrix
    for row in matrix:
        # Iterate over each element in the row and print it
        for element in row:
            # Use str.format() to print the integer with a width of 2 characters
            print("{:d}".format(element), end=" ")
        # Print a newline character after each row
        print()