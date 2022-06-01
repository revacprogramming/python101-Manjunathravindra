enter=input("enter the file name:")
f=open(enter,"r")
count=0
sum=0
for x in f:
  if x[0:19]=="X-DSPAM-Confidence:":
      count+=1
      sum+=float(x[20:28])
      
print(sum/count)