# Function to calculate factorial using a loop
def factorial_loop(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Example usage
n = 5
print("Factorial of", n, "is", factorial_loop(n))