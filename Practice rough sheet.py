# a =[1,2,3,4,5]
# n =len(a)
# b=[20,30,40]
# m = len(b)
# for i in range (0,n-m+1):
#     if a[i:m+i] == b:
#         print("sublist found")
#         break
# else:
#     print("not found")

# n =len(a)
# k=2
# for i in range(k%n):
#     last  = a.pop()
#     a.insert(0,last)
# print(a)

# a =[1,2,2,3,4,4,5]
# dup=[]
# for i in range (len(a)):
#     count =1
#     for j in range(i+1,len(a)):
#         if ( a[i]==a[j]):
#             count+=1
#     if count>=2:
#         dop.append(i)
arr1 =[1 ,4 ,5 ,7 ]
arr2 =[2 ,3 ,6 ,8 ]
n1=len(arr1)
n2=len(arr2)
i=0
j=0
arr =[]
while i<n1 and j<n2:
    if arr1[i]<arr2[j]:
        arr.append(arr1[i])
        i+=1
    else:
        arr.append(arr2[j])
        j+=1

while i<n1:
    arr.append(arr1[i])
    i+=1
while j<n2:
    arr.append(arr2[j])
    j+=1
print(arr)