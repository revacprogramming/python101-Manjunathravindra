inp=input("Enter file name:")
lol=open(inp,"r")
count=0
for x in lol: 
    if x[0:4]=="From":
        mylist=x.split()
        print(mylist[1])
        count+=1
print("total email address are:",count)
        
