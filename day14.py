s ="eat sleep code and repeat code and eat clean"
c=s.split()
c =c.toLowerCase()
d ={}
for i in c:
    l=len(i)
    temp = []
    for j in c:
        if j == l and not j in temp:
            temp.append(j)
    d[l]=temp

print(d)