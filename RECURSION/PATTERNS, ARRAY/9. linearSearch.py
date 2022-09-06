new_arr = []
def helper(arr,val,index):
    if len(arr)  == index:
        return False 
    if arr[index] == val:
        return True 
    return helper(arr,val,index+1)
    
def linearSearch(arr,val):
    return helper(arr,val,0)


arr = [ 1,3,4,5,6,3,35]
print(linearSearch(arr,45))
