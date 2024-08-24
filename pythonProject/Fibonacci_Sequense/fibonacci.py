def fibonacci(n):
    # Edge case for n = 0
    if n == 0:
        return 0

    # Edge case for n = 1
    if n == 1:
        return 1

    # Create an array to store Fibonacci numbers up to n
    fib = [0] * (n + 1)

    # Initialize the first two Fibonacci numbers
    fib[0] = 0
    fib[1] = 1

    # Fill the array with Fibonacci numbers
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    # Return the nth Fibonacci number
    return fib[n]


# Example usage:
n = 10
print(f"Fibonacci number at index {n} is: {fibonacci(n)}")

