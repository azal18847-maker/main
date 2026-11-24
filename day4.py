#list has a hetrogenious nature thats why be called it multiple data eg:-
#  a=["azal",28,True,12.2,print()]
# special power -same as string it also has indexing   ||
#  mutable nature - you can change any value of your list
l=[10,20,30,40,5]                         #    |
# l="hello"#you can change the name of list  #    |
                                           #    v
# l[0]=100000 #output: [100000,20,30,40,50] -you can change the value
#loop in values 
for i in l:
    if i%2==0:
        print(i)