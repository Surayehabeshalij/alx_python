def no_c(my_string):
    # Initialize an empty string to store the new string
    new_string = ""
    
    # Iterate over each character in the original string
    for char in my_string:
        # Check if the character is not "c" or "C"
        if char != "c" and char != "C":
            # If it's not "c" or "C", add it to the new string
            new_string += char
    
    # Return the new string
    return new_string#
# Call the no_c function with a string
result = no_c("This is a test string with c and C characters")
print(result) # Output: "This is a test string with  and  haraters"