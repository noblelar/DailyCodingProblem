

def fibonacci(n):
   """Return the nth Fibonacci number."""
   if n < 0:
      raise ValueError("Input should be a non-negative integer.")
   elif n == 0:
      return 0
   elif n == 1:
      return 1
   else:
      a, b = 0, 1
      for _ in range(2, n + 1):
            a, b = b, a + b
      return b
      

# Test cases
print(fibonacci(8))  # Output: 0

print(fibonacci(9))  # Output: 1


