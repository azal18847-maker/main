l=2
r=6

result ={}

for i in range(l,r+1):
    num =""
    for j in range(1,i+1):
        if i%j ==0:
            num= num + str(j)+ " "
    result[i]=num

for i,j in result.items():
    print(i , ": ", j)