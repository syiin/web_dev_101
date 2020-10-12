# Python Basics

1. Variables
   1. assigning and instantiation
   1. data types
1. Operators
   1. things that act on variables
   1. `+`, `-`, `*`, `//`, `%`
1. Basic IO
1. String interpolation
1. E: Add 2 int variables together, add 2 string variables together, print "Hello World"

```
x = 3
y = 2

x + y //5

x = "Hello "
y = "World."

x + y // "Hello World."

print("Hello World!")

```

1. Data structures
   1. Lists
   1. Dictionaries
   1. E: Instantiate a list, add something to it, alter a value in it
   1. E: Instiate a dictionary, add something to it, alter a value in it

```
listOfNums = [1, 2, 3]
listOfNums.append(4)
listOfNums[2] = 8

productListing = {'id': 0, 'name': 'orange', type: 'fruit', 'price per kg': 10}
productListing['supplier'] = "Radiant"
productListing['price per kg'] = 12

// when would we use one over the other?
// how do you think matrices are represented here?
```

1. Logic
   1. `if`, `else`
   1. Control flow
   1. E: Write an if else statement that checks if a number is greater than 3 and prints a message proclaiming whether or not it is

```
x = 8
if (x > 3)
  print("x is greater than 3")
else (x < 3)
  print("x is less than 3")
```

1. Repetition
   1. `for`, `while`
   1. E: Write a loop that checks if a list of numbers is divisible by 3

```
list_nums = [2, 3, 6, 9, 12, 13, 15]
div_by_3 = []

for num in list_nums:
    if num % 3 == 0:
      div_by_3.append(num)
```

1. Functions
   1. E: Write a function that adds 2 numbers to gether
   1. E: Write a function that checks if a number is larger 2
   1. E: Write a function that takes a list of ints and returns another list containing the numbers in it that are divisible by 3

```
def filter_div_3(list_nums):
  div_by_3 = []
  for num in list_nums:
      if num % 3 == 0:
        div_by_3.append(num)
  return div_by_3
```

1. Classes

   1. E: Define a class
   1. E: Create an instance of a class
   1. E: Get an attribute from a class, set an attribute
   1. E: Call a method on a class
   1. When would it make sense to pass an instance attribute rather than an external argument to a method?
   1. E: Inherit from a class

1. Numpy

```
mDimList = [[1, 2], [3, 4]]
mDimArr = np.array([[1, 2], [3, 4]])
```

Code Share platform: https://codeshare.io/5Npdym
On Skype: {code} {code}
