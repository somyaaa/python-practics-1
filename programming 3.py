# for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# looping through a string
for x in "banana":
    print(x)

# the break statement
name = ["sham", "ram", "mohan", "sam"]
for x in name:
    print(x)
    if x =="mohan":
        break

print("hello") # just to identify next output
# continue statement
for x in name:
    print(x)
    if x == "ram":
        continue
    print(x)

# the range() function
for x in range(6):
    print(x)

# print whether the number is even or odd
num = [1, 2, 3, 4, 5, 6, 7, 8]
for number in num:
    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')

print("hello")

# sum of the numbers in the list 1
n = [1, 2, 3, 4]
sum_n = 0
for num in n:
    sum_n = sum_n + num

    print(sum_n)

my_msg = 'hello world'
for _ in my_msg:
    print("hi")
    print(len(my_msg))

print("hey")

list_tup = [(1, 2), (3, 4), (5, 6)]
for item in list_tup:
    print(item)


for a, b in list_tup:
    print(a)
    print(b)

# dict
dict_val = {'key1': 1, 'key2': 2}
for item in dict_val.values():
    print(item)

# break continue pass
list_num =[1, 2, 3, 4, 5, 6, 7]
for num in list_num:
    if num == 3:
        break
    print(num)

# break in while loop
n = 0
while (n < 5):
    print(n)
    n += 1

# range
# enumerate
string_msg = 'hello'
index_count = 0
for char in string_msg:
    print(f'at index {index_count} is {char}')
    index_count += 1

# enumerate
str_msg = 'whats up'
for index,char in enumerate(str_msg):
    print(index)
    print(char)
    print('\n')

# zip function
list_1 = ['sam', 'ram', 'sham']
list_2 = [10, 20, 30]
list_3 = [80, 100, 20]
for a, b, c in zip(list_1, list_2, list_3):
    print(a)
    print(b)
    print(c)
print('\n')
# min and max function
list_n = [ 23, 5, 78, 200, -2, 90]
print(max(list_n))

# random library
from random import shuffle
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(my_list)
print(my_list)

# input function
input("what is the weather?")









