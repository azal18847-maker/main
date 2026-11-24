# a=[1,2,3,6,5,4,7,8,9]
a = [100,2,3,4,5,7,8,9,1,2]

n =len(a)
sum =0
for i in range(n):
    sum =0
    for j in range(1,n-i):
        sum+=1
        if a[j-1]>a[j] :
            a[j],a[j-1] = a[j-1],a[j]
print(a)

# lar = a[0]
# while n>0:
#     for i in range(n):
#         if a[i] > lar:
#             lar = a[i]
#     a[n-1]=lar
#     n -=1
#     print(n)
# print()