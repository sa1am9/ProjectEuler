def Fibonachi():
    x_1=1
    x_0=1
    sum=0
    while x_1<=4*10**6:
        x_n=x_1+x_0
        x_1,x_0=x_n,x_1
        if x_n%2==0:
            sum+=x_n
    return sum
print(Fibonachi())

