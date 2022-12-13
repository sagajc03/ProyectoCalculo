def newtonrhapson(a,n):
    x = 0
    fx = 0
    dfx = 0
    y = 0
    for l in range(-1000,1000):
        for i in range(0,n):
            fx = a[n-i-1]*(x+i)**(n-i) + fx
        for i in range(0,n-1):
            if i != n:
                dfx = a[n-1-i]*(n-i)*(x+i)**(n-i-1) + dfx
        y = x-(fx/dfx)
        rel = abs((x-y)/y)
        if rel <= 10**(-10):
            return y
        x = y

a = [5/4,-(7/3),1,0,0]
n = len(a) 
y = newtonrhapson(a,n)
print(y)