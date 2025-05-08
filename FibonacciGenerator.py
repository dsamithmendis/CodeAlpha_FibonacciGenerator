# Define a function to generate a Fibonacci-like sequence
def fibonacci_generator(a, b, n):
    for _ in range(n):  # Loop n times to generate the required number of terms
        print(a, end=' ')  # Print the current term without a newline
        a, b = b, a + b  # Update a and b to the next two terms in the sequence

# Use a try-except block to handle invalid inputs (e.g., non-integer input)
try:
    # Get the first term from the user
    a = int(input("Enter the first term (a): "))
    # Get the second term from the user
    b = int(input("Enter the second term (b): "))
    # Get the number of terms to generate
    n = int(input("Enter the number of terms to generate: "))

    # Check if the number of terms is positive
    if n <= 0:
        print("Please enter a positive number of terms.")
    else:
        print("Generated sequence:")
        # Call the function to generate the sequence
        fibonacci_generator(a, b, n)

# Handle invalid inputs such as strings or special characters
except ValueError:
    print("Invalid input! Please enter valid integers.")
