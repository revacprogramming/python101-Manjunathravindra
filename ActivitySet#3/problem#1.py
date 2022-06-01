import math

def data():
    x=float(input("enter the x coordinate:"))
    y=float(input("enter the y coordinate:"))
    return x,y
def len(x,y,a,b):
    num1=pow(a-x)
    num2=pow(b-y)
    sqr=num1+num2
    final=math.sqrt(sqr)
    return final


x1,y1=data()
x2,y2=data()
x3,y3=data()
len1=len(x1,y1,x2,y2)
len2=len(x1,y1,x3,y3)
len3=len(x3,y3,x2,y2)
print(max(len1,len2,len3))


