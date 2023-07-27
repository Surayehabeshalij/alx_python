def best_score(a_dictionary):
    # Initialize the best key and value to None
    best_key = None
    best_value = None  
    # Loop through each key-value pair in the dictionary
    for key, value in a_dictionary.items():
        # If the value is greater than the current best value, update the best key and value
        if best_value is None or value > best_value:
            best_key = key
            best_value = value
    # Return the best key
    return best_key
     if a_dictionary is None:
        return None
    best_key = None
    for key, value in a_dictionary.items():
        if best_key is None or value > a_dictionary[best_key]:
            best_key = key
    return best_key
    
