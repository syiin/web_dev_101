# Functions (continued)

1. Scope

   1. What will this return?

   ```
   x = 3

   def add_xy(x, y):
     z = x + y
     return z

   add_xy(1, 2)
   ```

1. Currying:

   1. When a function returns a function

   ```
   def BMI_weight(height):
    def h(weight):
        return weight / height**2
    return h
   ```

1. Recursion:

   1. When a function calls itself - why would you do this?
   1. Example

      ```
      def factorial_recursive(n):
        # Base case: 1! = 1
        if n == 1:
            return 1

        # Recursive case: n! = n * (n-1)!
        else:
            return n * factorial_recursive(n-1)
      ```

## Classes

1. The simplest class:

```
  _ define a class
 |
 |       ___the name of the class: notice capital letter
 |      |
 |      |     ___the parent class: a class this inherits from
 |      |    |
class Vehicle():
  def honk(self):
    #honk is a function inside the class, we call these "methods"
    print("HONK HONK!")

company_vehicle = Vehicle() #define an instance of the class
company_vehicle.honk()  #call the method inside the class
```

1. Init is a special method that initialises an instance of the class

```
class Vehicle():
  def __init__(self, max_speed):
    self.max_speed = max_speed #this is called an "attribute"

  def honk(self):
    print("HONK HONK!") #honk is a function inside the class, we call these "methods"

company_vehicle = Vehicle(60) #init is called here
print(company_vehicle.max_speed) #we access attribute values by using the 'class_instance.attribute_name'
```

1. A feature of classes is inheritance - it allows us to write DRY-er code

```
class Vehicle():
  def __init__(self, max_speed):
    self.max_speed = max_speed #this is called an "attribute"

  def honk(self):
    print("HONK HONK!") #honk is a function inside the class, we call these "methods"

class Car(Vehicle):
  def __init__(self, max_speed):
    self.max_speed = max_speed
    self.wheels = 4

  def set_car_brand(self, brand):
    self.brand = brand

company_car = Car(60)
company_car.honk() #we get this for free because we inherited from Vehicle
company_car.set_car_brand("Toyota")
print(company_car.brand)
```

1. The code above is slightly inefficient, because we're not inheriting properly from Vehicle. This is better:

```
Class Car(Vehicle):
  def __init__(self, max_speed):
    super.__init__(max_speed) #super refers to the parent class ("Vehicle")
    self.wheels = 4

  def set_car_brand(self, brand):
    self.brand = brand
```

1. Why are classes important? Checkout the example code in the scikit learn documentation for linear regression: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

```
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3

reg = LinearRegression()
reg.fit(X, y)
reg.score(X, y)
```
