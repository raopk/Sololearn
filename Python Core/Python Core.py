"""
Going back to the basis of python
"""


print('Hello World')

print('Hello world!')

print('Spam and eggs')

print (2 + 2)

print(5 + 4 - 3)

print(3/4)

print(0.42)

print(8/2)

print(6 * 7.0)

print(4 + 1.65)

print(1 + 2 + 3 + 4.0 + 5)

#Exponents

print( 2**5)

print( 8 ** (1/3))

#Quotients
print(20 // 6)
print(20 % 6 )

print(10//4)

#modulo

print(20 % 6)

print(1.25 % 0.5)

print(76 % (37 * 2))

print(7 %(5//2))

print(1 + 4 *3)

print(0.01 * (2 ** 30))

print(1 * (2 ** 30))

print('Python is fun!')

print('Always look on the bright side of life')

print('Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!')

print('One\nTwo\nThree')

print("""This is
a MULTILINE
text""")

print("Spam" + 'eggs')

print("2" + "2")

print("spam" * 3)

print(4 * '2')

user = 'James'

this_is_a_normal_name = 7
#123abc = 7

x = 7
print(x)

print(x + 3)
print(x)

x = 123.456
print(x)

x = "This is a string"
print(x + "!")

x = input("John")
print(x)

#In-place operators

a = 2
print(a)

a += 3
print(a)



x = 'spam' + 'eggs'
print(x)

#Walrus Operator
num = int(input())
print(num)

print(num:=int(input()))

my_boolean = True
print(my_boolean)

print(2 == 3)

print(True)

print(False)

print('eleven' != 'seven')

print(2 != 10)
print(7 > 5)
print(10 < 10)

if 10 > 5:
    print("10 is greater than 5")

print("Program ended")

num = 12
if num > 5:
    print("Bigger than 5")
if num <= 47:
    print("Between 5 and 47")


x = 4
if x == 5:
    print('Yes')
else:
    print('No')

num = 3
if num == 1:
    print('one')
elif num == 2:
    print('two')
elif num == 3:
    print('Three')
else:
    print("something else")


##Boolean Logic

print(True and True)

print(not True)

grade = 88
if (grade >= 70 and grade <= 100):
    print("Passed")

x = 4
y = 2

if 1 + 1 != y or x == 4 and 7 == 8:
    print("Yes")
elif x > y:
    print("No")

#List are used to store items
words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])


empty_list = []
print(empty_list)

number = 3
things = ['string', 0, [1,2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])


m = [[1,2,3],
    [4,5,6]
    ]

print(m[1][2])

strg = "Hello world!"
print(strg[6])

nums = [7,7,7,7,7]
nums[2] = 5
print(nums)

#List operation
nums = [1,2,3]
print(nums + [4,5,6])

nums = [1,2,3]
print(nums + [4,5,6])
print(nums * 3)

words = ['spam', "eggs", "spam", "sausage"]
print("spam" in words)
print("tomato" in words)

nums = [1,2,3]
print(4 not in nums)
print(4 not in nums)
print(3 not in nums)
print(3 not in nums)

nums.append(4)
print(nums)

print(len(nums))

words = ["Python", "fun"]
index = 1
words.insert(index, 'is')
print(words)

letter = ['p', 'q', 'r', 's', 'p', 'u']
print(letter.index('r'))
letter.count('p')

#WHILE LOOP
i = 1
while i <= 5:
    print(i)
    i += 1
print('Finished')

i = 3
while i >= 0:
    print(i)
    i -=1


x = 1
while x < 10:
    if x%2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")
    x += 1

i = 0
while True:
    print(i)
    i +=1
    if i >= 5:
        print("Breaking")
        break
print ("Finished")

i = 0
while i < 5:
    i += 1
    if i == 3:
        print('Skipping 3')
        continue
    print(i)

i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Skipping three")
        continue
    print(i)

#For LOOP
words = ['hello', 'worlds', 'spam', 'eggs']
for word in words:
    print(word + '!')
#
strg = "testing for loops"
count = strg.count('t')

print(count)



strg = "for testing and teaching"
count = 0

for t in strg:
    if(t == 't'):
        count += 1

print(count)

lst = [2,3,4,5,6,7]

for x in lst:
    if(x%2 == 1 and x > 4):
        print(x)
        break
#Range
numbers = list(range(10))
print(numbers)

numbers = list(range(3,8))
print(numbers)

print(range(20) == range(20))

numbers = list(range(5, 20, 2))
print(numbers)

numbers = list(range(3,15, 3))
print(numbers[2])

for _ in range(5):
    print("Hello")


lst = [1, 1, 2, 3, 5, 8, 13]
print(lst[lst[4]])

for i in range(10):
    if i % 2 != 0:
        print(i + 1)


lst = [1,2,3,4]
if len(lst) % 2 == 0:
    print(lst[0])
#
#The Fizzbuzz iteration
    n = int(input())

for x in range(1, n):
    if x % 2 == 0:
        continue
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)

#Custom Functions
def my_func():
    print("spam")
    print("spam")
    print("spam")
    print("spam")

my_func()


def print_with_exclamation(wordd):
    print(wordd + '!')

print_with_exclamation("spam")


def print_sum_twice(x, y):
    print(x + y)
    print(x + y)
print_sum_twice(5, 8)

def maxx(x,y):
    if x >= y:
        return x
    else:
        return y

print(maxx(4,7))
z = maxx(8,5)
print(z)

def add_num(x,y):
    total = x + y
    return total
    print("This wont be printed")

print(add_num(4,5))

def shout(word):
    """print a word with an
    exclamation mark following it.
    """
    print(word + "!")

shout('spam')


#Modules
import random

for i in range(5):
    value = random.randint(1,6)
    print(value)
#
from math import pi
print(pi)

#import some_module

def print_nums(x):
    for i in range(x):
        print(i)

    return

print_nums(10)

def func(x):
    return sum(range(x))

try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print("Done Calculation")
except ZeroDivisionError:
    print("An error occured")
    print("due to zero division")

try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")

try:
    word = "spam"
    print(word / 0)
except:
    print('An error occured')


pin = input()
try:
	#your code goes here
    pin = int(pin)
    print("PIN code is created")
except ValueError:
	#and here
    print("Please enter a number")


'''finally
To ensure some code runs no matter what
errors occur, you can use a finally statement.
The finally statement is placed at the bottom
of a try/except statement. Code within a finally
statement always runs after execution of the
code in the try, and possibly in the except, blocks.'''

try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("THis code will run no matter what")

try:
    print(1)
except:
    print(2)
finally:
    print(3)