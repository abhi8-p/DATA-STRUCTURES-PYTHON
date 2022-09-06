import math
def reverseNum(n):
    if n == 0 :
        return n

    power = int(math.log(n,10))         #find the number of digits -1 here # base paramter is 2nd parameter
    return (n%10) *int(math.pow(10,power)) + reverseNum(n//10)

print(reverseNum(1232)) 
