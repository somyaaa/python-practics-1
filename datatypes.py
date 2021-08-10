print("hello world")
#arithmetic problems
#addition
print( 2+ 2)
#subtraction
print(10 - 12)
#multiplication
print( 10 * 9)
#division
print(90 / 2)
print(38//7) # // used to get a integer number instead of floating number
#modulo opertaion
print(78 % 3)
print(61 % 9) #it is not completely divisible
#power
print(59 ** 2)
print ((10 +20) * (2 + 10))
#variables
a = 90
b = 23
sum = a+ b
print(sum)
print(a) #this shows the value of 'a' assign by user before
print(b) #this shows the value of 'b' assign by user before
#numeric types
#integers
num = 20
print(type(num))
a = 10
print(type(a)) #shows the type of data that we entered

#variable_name
name = "somya"
print(name)
name = "somya"
#2name = "sinha" this wont work
#shouldn't start with number
#even (name last = "sinha" ) this doesnt work
#should not have spaces
# dynamic typing
name_last = "sinha"
print("my last name is" + name_last)
#logical operation
salary = 8000
tax_percentage = 0.2
taxes = salary * tax_percentage
print(taxes)
#strings
#single quotes or double quotes
#strings are immutable
name = "sanya"
last_name = "sinha"
print(last_name)
# string slicing
b = "hello, world!"
print(b[2:5])
#Get the characters from the start to position 5 (not included)
b = "Hello, everyone!"
print(b[:5])
#Get the characters from position 2, and all the way to the end
b = "Good morning!"
print(b[4:])
#to get the character
#from 'o' in world! (positon -5)
#to, but not included 'd' in world! (position -2)
b = "Hello, World!"
print(b[-5:-2])
#string modify strings
#upper case
a = "Hello, World!"
print(a.upper())
#lower case
a= "Hello, World!"
print(a.lower())
#removing whitespace
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space
a = "good, morning!"
print(a.strip()) #returns "good, morning!"
#split string
#The split() method returns a list where the text between the specified separator becomes the list items.
a = "Hello, World!"
print(a.split(",")) # returns ['hello' , 'world!']
#String Concatenation
#To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)
#Use the format() method to insert numbers into strings
age = 27
txt = "my name is sanya, and I am {}"
print(txt.format(age))
#another example
quantity = 5
itemno = 670
price = 60
myorder = "i want {} pieces of item {} for {} rupee."
print(myorder.format(quantity, itemno, price))
#modifing the strings
name = "sinha"
print(name[1:5])
modified_name = "t" + name[1:5]
print(modified_name)
#boolean operations using (if else)
a = 100
b = 89
if b > a:
    print ("b is greater tha a")
else:
    print("b is not greater than a")
#for two variable
x = "good"
y = 8
print(bool(x))
print(bool(y))
