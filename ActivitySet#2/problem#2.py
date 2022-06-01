def add(a,b):
    return  a+b


def enter():
    a = int(input("enter the 1st Number?"))
    b = int(input("enter the 2nd number?"))
    return a,b
def output(c):
    print("sum of a and b is:",c)
def main():
    a,b=enter()
    c=add(a,b)
    output(c)

if __name__=="__main__":
    main()