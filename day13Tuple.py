"""
TUPLE
A tuple is an ordered ,immutabe collection.
Once you create it, you can not change ,add or remove items.
1. Annoted by (paranthesis).
2. Ordered -> their are indexes
3. hetrogenous -> mixed types values are allowed 
4. duplicate elements are allowed
5. immutable
6. we can do slicing in tuple
t = (1,2,3,3,4,5,6,6)
t = () #empty tuple
print(type(t))
print (t)
print(t[1:5])
print(t[::])

"""
"""
METHODS
1.count() -> count the occurence of any value
2.index() -> show the index locaation of the first occuring element.

3.
4.
5.

t = (1,2,1,2,1)

print(t.count(1))
print(t.index(2))

"""




"""
OPERATIONS
+ -> two tuples can concatenate

print(t1 + t2)
print(t1 *10)
"""
t1= (1,2,[2,3,4])
a = t1[2]

a.append(100)
print(t1)