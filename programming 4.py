# using range function
for num in range(0, 10, 2):
    print(num)

# list comprehension
# unique way to create a list
my_msg = 'helloo'
list = [char for char in my_msg]
print(list)

print('\n')
# only even number
for n in range(0, 15):
    if n % 2 == 0:
        print(n)

# list comprehension with nested for loop
for a in [5, 6, 7]:
    for b in [11, 23, 43]:
        print(a * b)

print('\n')
# getting the output in single line
my_nested_list = [a * b for a in [3, 6, 9] for b in [11, 10, 14]]
print(my_nested_list)

# functions (built- in function)
my_nested_list.append(200)
print(my_nested_list)
print('\n')
my_nested_list.insert(4, 70)
print(my_nested_list)

print('\n')


# creating function
# syntax
def my_function():
    print("hello from a function")


my_function()


def print_name():
    print("hello everyone")


print_name()


# define a method using def keyword
# pass parameters or arguments to a method
def s_num(a, b):
    print(a + b)


s_num(20, 34)


# print whether a number is even or not
def even(num):
    if num % 2 == 0:
        print(f'{num}is even')
    else:
        print(f'{num}is odd')


even(9)
even(6)
print('\n')

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# its not working
#def check_even(n_list):
 #   for num in n_list:
  #      if num % 2 == 0:
   #         return True
  #      else:
   #         return False
    #check_even(n_list)

    

