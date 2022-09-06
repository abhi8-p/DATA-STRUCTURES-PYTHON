import time
def helper(arr,index):
    if len(arr) - 2 == index :
        return arr[index] < arr[index + 1]
    # if len(arr) -1 == index :
    #     return True
    return (arr[index] < arr[index+1]) and helper(arr,index+1) 

def sortedArray(arr):
    # if len(arr) == 2:
    #     return (arr[0] < arr[1])

    # return (arr[0] < arr[1])& sortedArray(arr[1:])
    return helper(arr,0)

start = time.time()
arr = [1,3,4,5]
print(sortedArray(arr))
end = time.time()
print("Time = {}".format(end - start))

