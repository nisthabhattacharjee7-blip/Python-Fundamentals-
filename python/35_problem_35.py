a = 7
b = 10
c = 15

def greatest( a , b , c ): 
    if(a>b and a>c):
        return a 
    elif (b>a and b>c):
        return b 
    elif(c>b and c>a): 
        return c    
    
print(greatest( a , b , c ))    