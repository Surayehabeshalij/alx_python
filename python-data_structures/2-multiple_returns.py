def multiple_returns(sentence):
    # Check if the sentence is empty
    if len(sentence) == 0:
        # If it's empty, return a tuple with length 0 and None as the first character
        return (0, None)
    else:
        # If it's not empty, return a tuple with the length of the sentence and its first character
        return (len(sentence), sentence[0])