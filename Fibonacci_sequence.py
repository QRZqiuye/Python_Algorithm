def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# 예시: 처음 10개 출력
for i in range(10):
    print(fibonacci_recursive(i), end=" ")
