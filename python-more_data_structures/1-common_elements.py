def common_elements(set_1, set_2):
    # Create an empty set to hold the common elements
    common = set()
    # Loop through each element in set_1
    for elem in set_1:
        # If the element is also in set_2, add it to the common set
        if elem in set_2:
            common.add(elem)
    return common