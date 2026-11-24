a= [1, 2, 3, 2, 4, 1, 5]
c=0
a1 = ""
for i in range (0,len(a)):
    c=0
    val = a[i]
    for j in range (len(a)):
        if(val == a[j]):
            c=c+1
    if(c>1):
        continue
    else:
        a1 += str (val)  
print(a1)