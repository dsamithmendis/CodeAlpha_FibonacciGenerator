def fibonacci_generator(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Loop 'n' times to generate the sequence
    for _ in range(n):
        print(a, end=' ')  # Print the current number and stay on the same line
        a, b = b, a + b     # Update 'a' to the next number, and 'b' to the sum of current 'a' and 'b'

# Example: Generate and print the first 10 Fibonacci numbers
fibonacci_generator(10)
