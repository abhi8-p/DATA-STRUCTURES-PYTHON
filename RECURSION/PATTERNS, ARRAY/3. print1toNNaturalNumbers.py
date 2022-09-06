def n1(n):
    if n < 1 :
        return  
        
    n1(n-1)
    print(n)

n1(6)