# Function to sum all elements in a list
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage
my_list = [1, 2, 3, 4, 5]
print("Sum of list:", sum_list(my_list))