def reverse_string(s):
    # Base case: if the string is empty or has one character, return it
    if len(s) <= 1:
        return s
    # Recursive case: reverse the substring s[1:] and append s[0] at the end
    return s[0] + reverse_string(s[1:])

# Example usage:
original_string = "Hello, World!"
reversed_string = reverse_string(original_string)

print("Original String: ", original_string)
print("Reversed String: ", reversed_string)
