def GCD(a,b):
    temp=a%b
    a=b
    b=temp
    if a%b==0:
        return a,b 
    else:
        GCD(a,b)

print(GCD(192,162))
