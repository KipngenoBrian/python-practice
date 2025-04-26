# Function to sum the digits of a number
def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10    # Get the last digit
        total += digit
        number = number // 10  # Remove the last digit
    return total

# Example usage
num = 1234
print("Sum of digits:", sum_of_digits(num))