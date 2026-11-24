a = [1,2,3,4,5,7,8,9,10,98,85,63,54,87,25]

# sum =0
# a = a.sort()
# for i in range (len(a)):
#     if sum == a[i]:
#         sum +=1
#         continue
#     else:
#         print(i)
#         break
# a =[1,2,3,4,5]
# n = len(arr)
# og_n = n+1
# og_sum = ((og_n)*(og_n+1)//2)

# # for i in range(1,og_n+1):
# real_sum =0
# for elem in arr:
#     real_sum += elem
# missing_nimber = og_sum-real_sum
# print(missing_nimber)
for i in range(1,len(a)):
    previous = a[i-1]
    next =a[i]
    if a[i-1]>a[i]:
        a[i]=previous
        a[i-1]=next

print(f"list is sorted: {a}")
