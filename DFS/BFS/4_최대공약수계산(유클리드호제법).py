def GCD(a,b):
    temp=a%b
    a=b
    b=temp
    print(a,b)
    if a%b==0:
        return b 
    else:
        print("1")
        return GCD(a,b)
        

print(GCD(192,162))
