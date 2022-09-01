def Balanced(expr):
    stack = []
    for i in expr:
        if i in ('(','{','['):
            stack.append(i)
        else:
            if not stack:
                return False
            elif isMatching(stack[-1],i) == False:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True
        
def isMatching(a,b):
    if (a=='(' and b ==')') or \
        (a=='[' and b == ']') or \
            (a == '{' and b == '}'):
        return True
    else:
        return False
    
expr = '{{[()]}}'
print(Balanced(expr))


