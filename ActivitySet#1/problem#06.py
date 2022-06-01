def userinput():
    x=int(input("enter the hour:"))
    y=float(input("enter the rate per hour:"))
    return x,y
def computepay(hours,rate_per_hour):
    if hours<=40:
        gpay=hours*rate_per_hour
        return gpay
    else:
        gpay=40*rate_per_hour+(hours-40)*((rate_per_hour/2)+rate_per_hour)
        return gpay
def prin(gpay):
     print("gross pay is :",gpay)
def main():
    x,y=userinput()
    gpay=computepay(x,y)
    prin(gpay)
if __name__=="__main__":
    main()