
def fibonacci(x):
    return 1 if x <= 2 else fibonacci(x-1) + fibonacci(x-2)

if __name__ == '__main__':
    import timeit
    result = timeit.timeit('fibonacci(30)', setup='from __main__ import fibonacci', number=50)
    print(result)
