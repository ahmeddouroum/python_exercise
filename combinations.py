def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

def n_choose_k(n, k):
    if k < 0 or k > n:
        return 0
    return fact(n) // (fact(k) * fact(n - k))

print(n_choose_k(n, k))
