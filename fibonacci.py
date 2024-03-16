# Function to generate Fibonacci sequence up to nth term
def fibonacci(n):
  sequence = [0, 1]
  for i in range(2, n):
    sequence.append(sequence[i-1] + sequence[i-2])
  return sequence[:n]

# Get user input for n
n = int(input("Enter the value of n: "))

# Generate and print Fibonacci sequence up to nth term
print(fibonacci(n))