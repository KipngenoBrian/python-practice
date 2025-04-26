# Function to calculate factorial recursively
def factorial_recursive(n):
    if n == 1 or n == 0:  # Base case
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage
n = 5
print("Factorial of", n, "is", factorial_recursive(n))