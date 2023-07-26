def print_matrix_integer(matrix=[[]]):
    # Iterate over each row in the matrix
    for i, row in enumerate(matrix):
        # Iterate over each element in the row and print it with a space character at the end
        print (row.join(" "))
        # If this is not the last row, print a newline character
        if i < len(matrix) - 1:
            print()
