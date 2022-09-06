"""
in this program we are trying to skip the character 'a' and print the rest
here in helper we are using  a 2nd parameter 
while in helper2 we are using a another string variable to store the value
"""
def helper2(string,index):
    ch = ''
    if len(string) == index:
        return ch 
    
    new_ch = ''
    
    if string[index] != 'a':
        new_ch = new_ch + string[index]
    
    new_ch = new_ch + helper2(string, index +1)
    ch = ch + new_ch 
    return ch
# def helper(string,index,ch = ''):
#     if len(string) == index:
#         return ch 
#     if string[index] != 'a':
#         ch = ch + string[index]
#     return helper(string,index +1 ,ch)
def skipCharacter(string):
    # return helper(string,0)
    a = helper2(string,0)
    return a


print(skipCharacter('bacd'))
