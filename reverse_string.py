# Function to reverse a string manually
def reverse_string(s):
    reversed_s = ""  # Start with an empty string
    for char in s:
        reversed_s = char + reversed_s  # Add each character to the beginning
    return reversed_s

# Example usage
text = "brian"
print("Reversed string:", reverse_string(text))
