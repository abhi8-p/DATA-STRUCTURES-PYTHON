"""
Here helper2 another list to append the values but helper 2 is not much optimized so helper1
is generally preffered
"""

# new_arr = []
# def helper(arr,val,index):
#     if len(arr)  == index:
#         return new_arr 
#     if arr[index] == val:
#         new_arr.append(index) 
#     return helper(arr,val,index+1)
    
def linearSearch(arr,val):
    # return helper(arr,val,0)
    return helper2(arr,val,0)

def helper2(arr,val,index):
    li = []
    if len(arr) == index:
        return li 

    if (arr[index] == val):
        li.append(index)

    new_li = helper2(arr,val,index +1)
    li.extend(new_li)
    return li


arr = [ 1,3,4,5,6,3,35]
print(linearSearch(arr,3))
