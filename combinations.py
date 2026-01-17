def fact(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def n_choose_k(n, k):
    if k < 0 or k > n:
        return 0
    return fact(n) // (fact(k) * fact(n - k))

print(n_choose_k(n, k))
