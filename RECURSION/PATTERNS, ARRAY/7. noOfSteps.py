"""
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
"""
def numberOfSteps(num):
    if num == 0:
        return 0
    # if num == 1:
    #     return 1
    # if num %2 == 0 :
    #     # print("even: 1")
    #     return 1 + numberOfSteps(num//2)
    # else:
    #     # print("odd: 2")
    #     return 2 + numberOfSteps((num -1 )//2)
    if num % 2 == 0:
        return 1 + numberOfSteps(num//2)
    return 1 + numberOfSteps(num -1)

print(numberOfSteps(123))