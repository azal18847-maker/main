a= [10, 25, 15, 40, 30]
# lar=a[0]
# sec=a[0]
# for i in range(0,len(a)):
#     if a[i]>lar:
#         sec=lar
#         lar=a[i]
#     elif a[i]>sec and a[i]!=lar:
#         sec=a[i]
# print(sec)
sum=0;
for i in range(0,len(a)):
    sum=sum+a[i]
print(sum/len(a))