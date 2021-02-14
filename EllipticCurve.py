import random as rn

pE = [] #one point in E

def GenCurve(p):
    #p : prime
    #Generate elliptic curve E : y^3 = x^2 + ax + b (mod p)
    #Return Elliptic Curve EC = [a,b,p]
    a=rn.randint(0,p-1)
    x=rn.randint(0,p-1)
    y=rn.randint(1,p-1)
    b=(y**2-x**3-a*x)%p    
    D=(4*a**3+27*b**2)%p
    
    while D==0:
        x=rn.randint(0,p)
        y=rn.randint(0,p)
        b=(y**2-x**3-a*x)%p    
        D=(4*a**3+27*b**2)%p
    
    global pE
    pE = [x,y]
    return [a,b,p]

def addEC(P, Q, E):
    #Elliptic curve E : y^3 = x^2 + ax + b (mod p)
    # E = [a,b,p] 
    # P=[x1,y1] , Q=[x2,y2]
    
    O = ['Inf','Inf'] #Infinity Point
    p=E[2]
    a=E[0]
    x1=P[0]
    y1=P[1]
    x2=Q[0]
    y2=Q[1]
    
    if x1=='Inf' or x2=='Inf':
        if x1=='Inf':
            return Q
        else:
            return P    
    
    elif x1==x2 and (y1!=y2 or y1==0 or y2==0):
        return O
    
    else:
        if x1!=x2:
            u=pow(x2-x1,-1,p)
            s=((y2-y1)*u)%p
        else:
            u=pow(2*y1,-1,p)
            s=((3*x1**2+a)*u)%p
        x3=(s**2-x1-x2)%p
        y3=(s*(x1-x3)-y1)%p
        return [x3,y3]
        
def mulEC(k,P,E):
    #k*P = P + P + ... + P (k times addition) on E
    bink=bin(k)[3:]
    T=P
    for t in bink:
        T=addEC(T,T,E)
        if t=='1':
            T=addEC(T,P,E)
    return T
    
#Main Program

#Generate Curve
p=281 #set p as a prime number
E=GenCurve(p)
print("\nElliptic Curve E : y^2 = x^3 + {}x + {} (mod {})".format(E[0],E[1],E[2]))

#One point in E
P=pE
print("\nOne point in E = ",P)

#Addition and Multiplication on E
Q = addEC(P,P,E)
print("\n"+str(Q))
print(mulEC(2,P,E))
