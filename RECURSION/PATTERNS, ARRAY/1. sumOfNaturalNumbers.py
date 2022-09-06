def snn(n):
    if n == 1:
        return 1
    return n + snn(n-1)

print(snn(100))

'''
we can directly use n*(n+1)/2
'''