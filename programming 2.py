# list
# create a list (basic one)
list = ["onion", "potato", "chilly"]
print(list)
# list_length
this_list = ["ram", "sham", "mohan"]
print(len(this_list))
# mixed lists
list_mixed = [100, 12.0, 'hey']
print(list_mixed)
# indexing and slicing
print(list_mixed[2])
print(this_list[0:2])
print(this_list[0::3])
# for individual fetching data from the list
# concatenation
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = list_1 + list_2
print(list_3)
# list are mutable
# strings are not mutable
list_4 = ['c', 'A', 't']
list_4[0] = 'C'
print(list_4)
print(type(list_2))
# add elements to the list
list_5 = [10, 60, 100]
list_5.append(2)
print(list_5)
# for removing the element from the list
list_5.pop()
print(list_5)
# for removing a specific number from the list
list_5.pop(1)
print(list_5)
# for sorting the list
list_sort = [20, 90, 89, 200, 4]
list_sort.sort()
print(list_sort)

# you cant sort the old list by using new list
list_sort_1 =[90, 1, 89, 23, 0]
list_new = list_sort_1.sort()
print(list_new)

# reversing the list
list_6 = [2, 3, 4, 5, 6, 7]
print(len(list_6))
list_6.reverse()
print(list_6)

# dictionaries
# unordered mapping for sorting elements
# key value pairs
my_dict_syntax = {'key1':'value1','key2':'value2'}
my_dict = {'name': 'somya', 'age': '21'}
print(my_dict)
scores = {'sanya': 90, 'raj': 20, 'sham': 88}
print(scores)
# to print the specific score of individuals
print(scores['sanya'])

# add new key value pair
# how to reassign existing key value
# how to get only values
# how to get the entire dict

dict_new = {'name': 'sam', 'scores': [80, 90, 20, 30]}
print(dict_new['scores'][2])

# tuple are used to store multiple items in a single variable.
# tuple is collection which is ordered and unchangeable
# tuples are similar to lists
# create a tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# tuple length
print(len(thistuple))

# indexing and slicing of tuple
tuple_1 = [2, 4, 6, 8, 10]
print(tuple_1[0])
print(tuple_1[0:3])
print(tuple_1[2:])
print(tuple_1.count(2))
print(tuple_1.index(2))

# mixed tuples
tuple_mixed = (1, 'hello', 10.2)
print(tuple_mixed)
print(type(tuple_mixed))

# sets in python
set_new = {'hello', 'how', 'are', 'you'}
print(set_new)

# do not do repeat the values
list_7 = [1, 2, 3, 1, 1, 2, 2, 4, 3, 3]
print(set(list_7))
set_num = {1, 2, 3, 4, 5}
set_num.add(6)
print(set_num)
set_num.add(5)
print(set_num)

# booleans (true/false)
print(10 > 9)
print(10 == -10)
print(10 < 9)

# control flow
# if else
# indention
if 1 < 0:
    print("the condition is true")
else:
    print("the condition is false")

# elif
name = 'sanya'
if name == 'ram':
    print("login as ram")
elif name == 'sam':
    print("login as sam")
else:
    print("check the user")

# if elif else
# while loop
x = 0
while x < 10:
    print(x)
    x += 1

print("break statement")
# break statement
a = 1
while a < 6:
    print(a)
    if a == 3:
        break
    a += 1

# else statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")










