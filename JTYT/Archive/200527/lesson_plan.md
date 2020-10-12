# Repetition and Control Flow Exercises

1. Write a program that counts the number of items in a list greater than 30:

```
count = 0
for n in numbers:
    if n>30:
        count+=1
```

1. Write a Python program to convert a list of temperatures from fahrenheit to celcius

```
f_temps = [30, 100, 130]
c_temps = []
for temp in f_temps:
  C = (5/9) * (temp - 32)
  c_temps.append(C)
```

1. Write a program that prints out the fibonacci sequence

```
n=50
x,y=0,1

while y<n:
    print(y)
    x,y = y,x+y
```

1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

```
nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))

print (','.join(nl))
```

# Functions

1. A function wraps a chunk of code inside a name - it is a way of abstracting logic
1. Instead of writing

```
x,y=0,1

while y<n:
    print(y)
    x,y = y,x+y
```

I can write `up_to_n = fibonacci(n)`

1. Anatomy of a function

```
  _ define a function: "def"
 |
 |    ___the function name: "add_xy"
 |   |
 |   |        ___the arguments/parameters: "x, y"
 |   |       |
def add_xy(x, y):
  z = x + y ----- indent denotes the function body
  return z  ----- what the function returns
```

Example run:

    ```
    def add_xy(x, y):
      z = x + y
      return z

    add_xy(1, 2) //3
    ```

EXTRA EXERCISES (not used):

1.  Write a program to reverse a string.
    ```
    Sample String : "1234abcd"
    Expected Output : "dcba4321"
    ```
1.  Write a function that accepts a string and calculate the number of upper case letters and lower case letters.

```
Sample String : 'The quick Brow Fox'
Expected Output :
 No. of Upper case characters : 3
 No. of Lower case Characters : 12
```

1.  Write a function to print the even numbers from a given list.

```
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
```

1.  Write a function that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically

```
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
```

1. Answers:

   ```
   def max_of_two( x, y ):
       if x > y:
           return x
       return y
   def max_of_three( x, y, z ):
       return max_of_two( x, max_of_two( y, z ) )
   print(max_of_three(3, 6, -5))

   def string_reverse(str1):
       rstr1 = ''
       index = len(str1)
       while index > 0:
           rstr1 += str1[index - 1]
           index = index - 1
       return rstr1
   print(string_reverse('1234abcd'))

   def string_test(s):
       d={"UPPER_CASE":0, "LOWER_CASE":0}
       for c in s:
           if c.isupper():
             d["UPPER_CASE"]+=1
           elif c.islower():
             d["LOWER_CASE"]+=1
           else:
             pass
       print ("Original String : ", s)
       print ("No. of Upper case characters : ", d["UPPER_CASE"])
       print ("No. of Lower case Characters : ", d["LOWER_CASE"])
   string_test('The quick Brown Fox')

   def is_even_num(l):
       enum = []
       for n in l:
           if n % 2 == 0:
               enum.append(n)
       return enum
   print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

   def reverse_hyphen(input_list):
     items=[n for n in input_list.split('-')]
     items.sort()
     return items
   reverse_hyphen("green-red-black-white")
   ```
