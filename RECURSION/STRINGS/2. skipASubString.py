def helper2(string,sub,index = 0):
    ch = ''
    new_ch = ''
    if len(string) == index:
        return ch
    if string[index:len(sub)+1] == sub:
        helper2(string,sub,index+len(sub)+1)
    else:
        new_ch = string[index] 
    new_ch = new_ch + helper2(string,sub,index+1)
    ch = ch + new_ch
    return ch

def skipSubstring(string,sub):
    return helper2(string,sub)

print(skipSubstring('pineapple','in'))