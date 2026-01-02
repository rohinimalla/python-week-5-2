# Fibonacci series without recursion (iteration)
print("Fibonacci series with iteration:")

def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Fibonacci series with recursion
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


n = int(input("Enter a number: "))

fibonacci_iterative(n)

print("Fibonacci series with recursion:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")
