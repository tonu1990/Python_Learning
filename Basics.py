# this is a way to add comment using #

''' This is another way to add comments using Triple quotes- string literal comment'''

string_a = "This is sample string"
print(string_a)

string_b = """This is multiple line string .
This is second line of string.
String ends at third line"""
print(string_b)

# Assigning multiple values to multiple variables
a, b, c , d = 5, 3.2, 'Hello' , "Tonu"
print(a)
print(b)
print(c)
print(d)

# concatenate two different non compatiable data types and error handling 

try :
    print (a+c)

     
except Exception as e:
    print(e)

#immutability 

print(id(a))
i= 7
print (id(i))
i= i+1 
a= a+3

 
print(id(a))
print (id(i))

# adding numbers of different types 
a = 14 + 4j
b= True
c= 3.14
d = 7

print(a+b)
print(a+c)
print(a+d)
print(b+c)
print(b+d)
print(c+d)

# Check cached integer range
for i in range(-10, 10):
    obj_id = id(i)
    print(f"Value: {i}, Address: {obj_id}")

#size of int
import sys
print(sys.getsizeof(d))
