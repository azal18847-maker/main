"""sets"""
# 1. sets are annoted by {} or set()
# 2. Sets are collection of Unique items.
# empty {} -> dict but {1,2,3,4} -> set.
#3. Sets are hetrogenous.
#4. Sets are unordered.
#5. as sets don't have indexing we cannot replace anyvalue
#6. No duplicate elements are allowed

# s = {1,2,3,4}
# s = set()
# print(s)
# s1= {1,2,3,4,5,True, 80.2,"Sample"}
# print(s1)


"""METHOD OF SETS
.add() to add any element inside the set.
s ={1,2,3}
s.add(4)
.remove() to remove any element from set.

.discard() if element is not present inside of the set so it will not raise any error.
s.discard(6)
print(s)


"""
"""
SET OPERATIONS...
1. Union - merge both the sets
2. intersection - common elements 
3. difference - ese element jo ek set n=but dusre mai nhi.
4. symmeetric difference - common element remove krke deta hai.

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s2.difference(s1))
print(s1.difference(s2))
print(s1.symmeetric_difference(s2))
print(f"UNION -> {s1 | s2}")
print(f"INTERSECTION -> {s1 & s2}")
print(f"DIFFERENCE -> {s1 - s2}")
print(f"DIFFERENCE -> {s2 - s1}")
"""
#whenever we want to create a set like this in which be don't have to add and remove element from like restricted
#so, we make an frozenset()
s={1,2,3,4}
s= frozenset()
s.add(4)
s.remove(4)
print(s)