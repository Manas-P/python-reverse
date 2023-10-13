def reverse_string(s):
    # Log the input at each recursion level
    print(f"Called with: {s}")
    
    # Base case: if the string is empty or has one character, return it
    if len(s) <= 1:
        print("Base case reached")
        return s
    
    # Recursive case: 
    else:
        # Extract the first character
        first_character = s[0]
        print(f"First character: {first_character}")
        
        # Extract the rest of the string
        rest_of_string = s[1:]
        print(f"Rest of string: {rest_of_string}")
        
        # Call the function recursively for the rest of the string
        reversed_rest_of_string = reverse_string(rest_of_string)
        print(f"Reversed rest of string: {reversed_rest_of_string}")
        
        # Concatenate the first character to the end of the reversed rest of string
        reversed_string = reversed_rest_of_string + first_character
        print(f"Reversed string: {reversed_string}")
        
        return reversed_string

# Example usage:
original_string = "Hello, World!"
reversed_string = reverse_string(original_string)

print("\nResults:")
print("Original String: ", original_string)
print("Reversed String: ", reversed_string)
