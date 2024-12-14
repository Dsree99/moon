MOD = 10**9 + 7

def matrix_multiply(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
         (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
         (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
    ]

def matrix_exponentiation(matrix, power):
    result = [[1, 0], [0, 1]]  # Identity matrix
    while power:
        if power % 2 == 1:
            result = matrix_multiply(result, matrix)
        matrix = matrix_multiply(matrix, matrix)
        power //= 2
    return result
#random test

def fibonacci_matrix(n):
    if n == 1 or n == 2:
        return 1
    F = [[1, 1], [1, 0]]
    result = matrix_exponentiation(F, n - 1)
    return result[0][0]

# Test
n = int(input("Enter the position of the Fibonacci number: "))
print(f"The {n}th Fibonacci number is {fibonacci_matrix(n)}")