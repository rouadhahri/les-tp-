


import matplotlib.pyplot as plt
from numpy import linspace
f=lambda x: x**3+x**2-3*x-3
T=linspace(-2,2,41)
plt.title("solution dans [-2:2] ");
plt.xlabel("x")
plt.ylabel ("f(x)")
plt.grid(True)
plt.plot(T,f(T))





def dicho(a,b,f,tol):
    m=(a+b)/2
    err=abs(b-a)
    while err>tol:
        if f(m)==0 :
            break
        elif f(a)*f(m)<0 :
            b=m
        else :
            a=m
        m=(a+b)/2
        err=abs(b-a)
    return m




f=lambda x: x**3+x**2-3*x-3
x3=dicho(-2,-1.5,f,10)
x10=dicho(-2,-1.5,f,10)
x20=dicho(-2,-1.5,f,20)
print(x3,x10,x20)
#print(x3)




print('f(x10)={},f(x20)={}'.format(f(x10),f(x20)))




def dichow (a ,b,f,eps):

    g,d = min (a,b),max(a,b)
    gau,dor = f(g),f(d)
    n = 0
    while d-g > eps :
        n += 1
        m = ( g + d )/2
        valm = f ( m )
        if gau * valm < 0 :
            d = m
            dor = valm
        else :
            g = m
            gau = valm
    
    return (g+d)/2,n



dichow(-2,-1.5,f,0.0001)







