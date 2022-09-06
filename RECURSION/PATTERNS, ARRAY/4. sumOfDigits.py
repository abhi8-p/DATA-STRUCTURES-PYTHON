def sod(n):
    if n == 0 :
    # if n < 10:
    #     return n
        return 0

    return n%10 + sod(n//10)

print(sod(984))