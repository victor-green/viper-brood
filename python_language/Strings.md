# Python Snippets For Data Science
Quick and dirty python reference

Cut and paste as needed


### STRINGS
```python



# Declaration
value1 = "First String"
value2 = "Second String"

print "Charater 0: ", value[0]
print "Range 1:5", value2[1:5]

value3 = "Hello World"
value3[:6] + 'Team'
print value3

print "Hello" in value1


# Operators
value1 = "Hello"
value2 = "World"

### Concatenation
value3 = value1 + value2

### Repitition
print = value3 * 2

### Slice
print value3[1]

### Range Slice
print value3[1:3]

### Membership
has_l = 'l' in value3
print has_l

no_z = 'z' not in value3
print no_z

### Format
print "My name is %s and age is %d", ('Jim',30)


# Builtin Methods

# capitalize()
print "lower case sentence".capitalize()


# count()
print "theodore".count("eo")
print "theodore".count("eo",0,len("theodore"))


# endswith()
print "theodore".endswith("ore")
print "theodore".endswith("ore",0,len(name))


# find()
print "theodore".find("eodz")
print "theodore".find("eodz",0,len(name))


# index()
try:
	subname = "theodore".index("eodz",0,len("theodore"))
except ValueError:
	print "Substring not found"
else:
	print subname


# isalnum()
print "theodore".isalnum()


# isalpha()
print "theodore".isalpha()


# isdigit()
print "theodore".isdigit()


# isspace()
print ' '.isspace()


# istitle()
print "theodore".istitle()


# join()
import urllib2
print '\n############\n'.join(urllib2.urlopen('http://data.stackexchange.com/users/7095'))


# len()
print len("theodore")


# lower()
print "THEODORE".lower()


# lstrip()
print "   Theodore".lstrip()


# rfind()
print "theodore".rfind("eodz")
print "theodore".rfind("eodz",0,len(name))


# rindex()
try:
	subname = "theodore".rindex("eodz",0,len("theodore"))
except ValueError:
	print "Substring not found"
else:
	print subname


# rstrip()
print "Theodore    ".rstrip()


# split()
print "Theodore Roos".split(" ")


# splitlines()
print "Theodore\nRoos".splitlines()


# startswith()
print fullname.startswith("You")


# strip()
print fullname.strip()


# swapcase()
print "theodore".swapcase()


# title()
print "theodore".title()


# upper()
print "theodore".upper()


# isdecimal()
print "theodore".isdecimal()



```

