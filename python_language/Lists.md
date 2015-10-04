# Python Snippets For Data Science
Quick and dirty python reference

Cut and paste as needed


### LISTS
```python



list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = ['a','b','c','d','e','f','g','h','i','j']

print list1[0]
print list1[1:]
print list1[2:5]
print list1[:-1]
print list1[1:-1]


# Length
print len(list1)


# Concatenation
list3 = list1 + list2


# Repetition
print list3 * 2


# Membership
print 1 in list1


# Iteration
for number in list1:
	print number


# Comparision
print cmp(list1,list2)


# Maxium element
max(list1)


# Minimun element
min(list2)


# Convert tuple into list
mytuple = ('a',1)
list4 = seq(mytuple)


# Combining Lists
list3 = zip(list1,list2)


# Separating List Tuples
list4 = zip(*list3)


# Getting index when iterating
for index, document in list3:
	print index ," ", document

for index, _ in list3:
	print index 


# List Comprehensions

print [ x for x in list1 ]
print [ (x, x < 5) for x in list1 if x % 2 == 0 ]
print [ i if i%2==0 else 0 for i in list1 ]


# append()
list1.append(11)



```


