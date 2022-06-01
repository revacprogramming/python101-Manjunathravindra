'''
1.take a input form user.
2.
3.
'''

def userinput():
    x=int(input("enter the hour:"))
    y=float(input("enter the rate per hour:"))
    return x,y
def grosspay( hours,rate_per_hour):
    gpay=hours*rate_per_hour
    return gpay
def prin(gpay):
     print("gross pay is :",gpay)
def main():
    x,y=userinput()
    gpay=grosspay(x,y)
    prin(gpay)
if __name__=="__main__":
    main()




