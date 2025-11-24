def factorial(n):
    """Calculates n! using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)
# Example usage
print(f"5! = {factorial(5)}")
print(f"0! = {factorial(0)}")

output:
5! = 120
0! = 1


