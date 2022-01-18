# Hassan Mohamed Hassan
#2440105785
#Final Exam


import numpy as np
import math
import matplotlib.pyplot as plt

# Question 1

def f(x):
    f = lambda x :1 /(x+5)
    return f(x)

def a(x):
    a = lambda x : np.log(abs(x+5))
    return a(x)

def Simpsons(a,b,x):
    n= (a-b)/x
    pionts = list()
    ans=0
    pionts.append(b)
    y=b
    for i in range(x):
      y=y+n
      pionts.append(y)
    for i in pionts:
      if i==a or i==b:
        ans=ans+f(i)
      else:
          k = 2 if pionts.index(i)%2 == 0 else 4
          ans+=(f(i)*k)
    ans =ans *(n/3)
    return ans
    
print("Answers for Question 1\n")

Q1 = Simpsons(5,1,10)
print("a) ",Q1)


Q2=0
# 1 /(x+5) --> ln(x+5)+C

Q2 = a(5)-a(1)     
print("b) ",Q2)   

Q3 = (abs(Q1-Q2)/Q2)*100
print("c) ",Q3) 
     


# Question 2
x1=[]
y1=[]
def Q2f(x,y):
     f = lambda x,y: (y*(x**3))-(1.5*y)
     return f(x,y)
 
def RK5O():#for sloling for solution
    h = 0.1
    x,y = 0,1;
    while(x<2):
        y1.append(y)
        x1.append(x)
        k1 = Q2f(x,y)
        k2 = Q2f((x+((1/4)*h)),(y+((1/4)*k1*h)))
        k3 = Q2f((x+((1/4)*h)),(y+((1/8)*k1*h)+((1/8)*k2*h)))
        k4 = Q2f((x+((1/2)*h)),(y+((1/2)*k2*h)+(k3*h)))
        k5 = Q2f((x+((3/4)*h)),(y+((3/16)*k1*h)+((9/16)*k4*h)))
        k6 = Q2f((x+h),(y-((3/7)*k1*h)+((2/7)*k2*h)+((12/7)*k3*h)-((12/7)*k4*h)+((8/7)*k5*h)))
        y= y+(((1/90)*h)*((7*k1)+(32*k3)+(12*k4)+(32*k5)+(7*k6)))
        x=x+h
        
    return y



print("\n\nQuestion 2\n\n")
# dy/dx = y*(x^3) -(1.5*y) --> dy/dx = y(x^3-1.5) --> 1/ydy = x^3-1.5dx
#1/ydy ->> ln(y)
#x^3-1.5dx --> x^3 --> x^4/4, 1.5-->1.5x  --> 1/4(x^4)-1.5x+C
# ln(y) = 1/4(x^4)-1.5x+C
#   y = e(1/4(x^4)-1.5x+C)
#

p=1;
q=0
x2=[]
y2=[]
Q2af= lambda x: np.exp(((1/4)*(x**4))-(1.5*x))
while(q<2):#used the calqualte the pionts for the qraph
    x2.append(q)
    y2.append(p)
    q+=0.1
    p=Q2af(q)
    
Q2a = Q2af(2)-Q2af(0)   
print("a) ",Q2a)

Q2b = RK5O()
print("b)", Q2b)

plt.plot(x2,y2, label = "analytical")
plt.plot(x1,y1, label = "Runge-Kutta")

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.legend()
plt.show()
Q2c = (abs(Q2b-Q2a)/Q2a)*100
print("c)", Q2c)



# Question 3




   

def parabolic(x,x1,x2):
    f = lambda x: (2*math.sin(x))-((x**2)/10)

    top = ((x1**2-x2**2)*f(x))+((x2**2-x**2)*f(x1))+((x**2-x1**2)*f(x2))
    bottom = (2*f(x)*(x1-x2))+(2*f(x1)*(x2-x))+(2*f(x2)*(x-x1))
    x3= top/bottom
    return x3

print("\n\nQuestion 3\n\n")

x3 = parabolic(0,1,4)
print("a) ",x3)
# f = 2*sin(X)-x^2/10 --> f'(x) = cos(x)-2x/10
df = lambda x: math.cos(x)-((2*x)/10)
print("b) ",df(x3))
q=0
x4=[]
y4=[]
Q3f = lambda x: (2*math.sin(x))-((x**2)/10)
while(q<4.1):#used the calqualte the pionts for the qraph
    x4.append(q)
    p=Q3f(q)
    y4.append(p)
    q+=0.1
    

plt.figure(2)
plt.plot(x4,y4, label = "parabolic")

  
plt.plot(x3,Q3f(x3),"go", label="optimum")
plt.plot(0,Q3f(0),"ob",label="starting")
plt.plot(1,Q3f(1),"ob")
plt.plot(4,Q3f(4),"ob")
plt.plot(4,Q3f(4),"ob")
plt.legend()
plt.show()




# Question 4


def Q4f(x,y):
     f = lambda x,y: -x+y-(2*(x**2))-(2*x*y)-(y**2)
     return f(x,y)
# -x+y-(2*(x**2))-(2*x*y)-(y**2)/x


z= [2,3]
def steepac(x,y):
    z1 = [2,3]
    while(z[0]!=0 and z[1]!=0):
        z[0]= z[0]+(0.1*z1[0])
        z[1]= z[1]+(0.1*z1[0])
    





