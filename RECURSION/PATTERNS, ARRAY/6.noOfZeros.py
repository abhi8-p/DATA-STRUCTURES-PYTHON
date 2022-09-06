def noOfZeros(n):
    if n == 0:
        return 0

    if n%10 == 0:
        return 1 + noOfZeros(n//10)
    else:
        return noOfZeros(n//10)

print(noOfZeros(2030))