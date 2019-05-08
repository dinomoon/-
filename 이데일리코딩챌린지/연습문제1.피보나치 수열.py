# 자연수 N( 1 <= N <= 35 )이 주어졌을 때 N번 째 피보나치 수를 출력한다.
# 1 1 2 3 5 8 13 21 34

def Fibonacci(N):
    if N < 2:
        return N
    return Fibonacci(N-1) + Fibonacci(N-2)

print(Fibonacci(30))

# Fibonacci(5) = Fibonacci(4) + Fibonacci(3)
# Fibonacci(4) = Fibonacci(3) + Fibonacci(2)
# Fibonacci(3) = Fibonacci(2) + Fibonacci(1)
# Fibonacci(2) = Fibonacci(1) + Fibonacci(0)
