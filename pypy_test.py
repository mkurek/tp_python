import timeit
result = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(result)
