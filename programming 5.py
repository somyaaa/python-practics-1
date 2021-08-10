# tuple unpacking with functions
stock_prices = [('tata', 500), ('hdfc', 1000), ('maruti', 200)]
for stock_name, price in stock_prices:
    print(stock_name)
    print(price)

# find the employee whose working hour is more
working_hour = [('sam', 1000), ('tom', 950), ('ron', 999)]


#
# *args & *kwargs
# arguments and keyword arguments
def sum_number(x, y):
    return sum((x, y))
sum_number(20, 72)
# *kwargs
def kw_example(**kwargs):
    if 'food' in kwargs:
        print(kwargs['food'])
    else:
        print('no food in the list')
kw_example(fruit = 'orange', food = 'potato')

# three cup monte game
# list of cups
# shuffle the cups
# ask the person to guess where is the ball
# check whether the guess is correct or not
list_cups = ['', '0', '']
from random import shuffle
shuffle(list_cups)
print(list_cups)
# shuffle the cups
def shuffle_list(list_cups):
    shuffle(list_cups)
    return list_cups
result = shuffle_list(list_cups)
print(result)
# ask the guess
def get_guess():
    guess = ''
    guess = input("pick the cup 0,1 or 2")
    return int(guess) # guess should be integer
guess = get_guess()
# check the guess whether its correct or not
def check_guess(list_cups, guess):
    if list_cups[guess] == '0':
        print("correct guess")
    else:
        print("wrong guess")

check_guess(list_cups,guess)
print(list_cups)
result = shuffle_list(list_cups)

# lambda function is a small anonymous function.
# example add 10 to argument a and return the result
x = lambda a : a + 10
print(x(5))

# multiply argument
x = lambda a, b : a * b
print(x(4, 10))

map(function, iterables)









