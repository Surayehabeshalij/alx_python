def update_dictionary(a_dictionary, key, value):
    # Check if the key already exists in the dictionary
    if key in a_dictionary:
        # If the key exists, update its value
        a_dictionary[key] = value
    else:
        # If the key does not exist, add it to the dictionary with its value
        a_dictionary[key] = value
    
    return a_dictionary