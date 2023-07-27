def best_score(a_dictionary):
    # Initialize the best key and value to None
    best_key = None
    best_value = None 
    # Return the best key
    if a_dictionary is None:
           return None
    best_key = None
    for key, value in a_dictionary.items():
        if best_key is None or value > a_dictionary[best_key]:
            best_key = key
    return best_key
