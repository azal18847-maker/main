"""
DICTIONARY 
1. ANNOTED BY {CURRY BRACKETS}
2. DICTIONARY IS COMBINATONS MULTIPLE
KEYS:VALUES
3 . dictionary are mutable.
4. dictionary are hetrogenous.
5. dictionary are ordered
6. in dict keys will always be unique but values can be duplicated.
"""
#D {} #EMPTY DICTIONARY
d ={1:10,2:20,3:30}
# d[5] =50#assignment
# print(d[5],d)
#agar hum direct loop run krte hai dictionary pe toh we will get KEYS.
# for i in d:
"""METHODS"""
#1 .keys()
d = {"a":1.0,"b":20,"c": 3.0,"d":40}
# print(d.keys())



#2. .values()
#will give all the values from the dictionary
# print(d.values())



#it will give both keys and values from the dictionary
#3. .items()
# print(d.items())
# for key,value in d.items():
#     print(key,value)

#4. .pop()
#remove the key and value from the dict.
# d.pop("d")
# print(d)

#5. .get()
#get func takes keys if key sexists return the value otherwise return the default i.e. none we can also give the value of default like"not found"
# print(d.get(5,"not found"))
#6. .update()
# #to merge two dictionaries
# a.update(b)
# print(a)
#7. len()
# length of dictionaryd(total number of keys.)
# d ={1:10,2:20,3:30,4:40}
# print(len(d))

# print(d.keys())
# for keys in d:
#     print(keys)
# sum =0
# for keys,values in d.items():
#     sum = sum +values
# print(sum)
# greatest =0
# name =0
# print(type(name))
d ={"ravi":80,"rohan":33,"chirag":22,"devraj":100}
for values in d:
    
        d[values ]=d[values]+5
print(d)


# print(name,greatest)
# d ={}
# for i in range(1,6):
#     d[i]=i*i
# print(d)
    

