# a=[10,-5,20,-3,0,8]
# for i in range(len(a)):
#     if a[i]>0:
#         print("positive : ",a[i])
# for i in range(len(a)):
#     if a[i]<0:
#         print("negative : ",a[i])
# a = [10,20,30,40]
# sum = 0
# for i in range(len(a)):
#     sum =sum+ a[i]
# d= sum /len(a);
# print(d)
# a = [10,548,20,30,40,5,60,100,6,87,94,11]
# sum = a[0]
# index =0
# for i in range(len(a)):
#     if(a[i]>sum):
#         sum = a[i]
#         index =i
# print(sum," found at ",index , " index ")
# a = [10,548,20,30,40,5,60,100,6,87,94,11]
# sum = a[0]
# index =0
# for i in range(len(a)):
#     if(a[i]<sum):
#         sum = a[i]
#         index =i
# print(f"min is {sum} at index {index}")
a = [2,3,15,15,3,2]
number =0
for i in range(len(a)-1,-1,-1):
    number += a[i]+(10**i)
    print(number)
print(number)
