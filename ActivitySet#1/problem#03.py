largest=None
x=0
while True:
    num=input("enter the number")
    if num=="done":
        break
    if type(num)==float:
        y=num
    else:
        print("invalid input")    
    if x<y:
        largest=y
    else:    
        x=num
print(largest)        





