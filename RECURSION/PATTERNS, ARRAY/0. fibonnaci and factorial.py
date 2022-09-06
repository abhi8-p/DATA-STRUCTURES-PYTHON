def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)
      
      
print(fact(4)) 

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 :
        return 1
    
    
    return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(4))