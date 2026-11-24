a =[10,20,30,40,50]
temp=len(a)-1
for i in range(0,(len(a)-1)//2):
    a[i],a[temp]=a[temp],a[i]
    temp =temp-1
print(a)
# method 2
a =[10,20,30,40,50,60]
n= len(a)
for i in range(0,len(a)//2):
    a[i],a[n-i-1]=a[n-i-1],a[i]
print (a)