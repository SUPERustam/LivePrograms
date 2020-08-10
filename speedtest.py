from timeit import timeit

code = """
def rec_fib(n):
    if 0 < n <= 2:
        return 1
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)



print(rec_fib(6))
"""
print(timeit(code, number=10) / 10, code.__sizeof__())

