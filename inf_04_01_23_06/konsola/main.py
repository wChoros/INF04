from math import sqrt


def eratosthenes_sieve(arr: list):
    arr[0] = False
    arr[1] = False
    n = len(arr)
    for i in range(2, int(sqrt(n)) + 1):
        if arr[i]:
            for j in range(2, n):
                if i * j > n - 1:
                    break
                arr[i * j] = False


arr = [True for _ in range(100)]
eratosthenes_sieve(arr)
print(', '.join([str(number) for number, is_prime in enumerate(arr) if is_prime]))