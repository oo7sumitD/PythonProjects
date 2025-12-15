# MAX() MIN()
"""
1) Find the Maximum and Minimum Values in a List
   numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
   Expected Output:
       Max = 79
       Min = 1
"""
numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
maximum = max(numbers)
minimum = min(numbers)
print("Max value:", maximum)
print("Min value:", minimum)


"""
2) Given a set of numbers, find the maximum and minimum values.
   setn = {5, 10, 3, 15, 2, 20}
   Expected Output:
       Max = 20
       Min = 2
"""
setn = {5, 10, 3, 15, 2, 20}
set_max = max(setn)
set_min = min(setn)
print("Max value in set:", set_max)
print("Min value in set:", set_min)


"""
3) Write a Python function that takes a list of strings and returns a tuple  
   (shortest_word, longest_word).
   If multiple words tie, return the first occurrences.

   Input:  words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
   Output: ('kiwi', 'grapefruit')
"""
def shortest_and_longest(words):
    shortest = min(words, key=len)
    longest = max(words, key=len)
    return (shortest, longest)

words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
result = shortest_and_longest(words)
print("Shortest and Longest words:", result)



######## LAMBDA, MAP, FILTER, REDUCE ########
"""
1) Given a list let's see how to double each element of the given list using map()
   a = [1, 2, 3, 4]
   Expected Output: [2, 4, 6, 8]
"""
a = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, a))
print("Doubled List:", doubled)


"""
2) Use filter() and lambda to extract all even numbers from a list of integers.
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   Expected Output: [2, 4, 6, 8, 10]
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_nums)


"""
3) Use reduce() and lambda to find the longest word in a list of strings.
   words = ["apple", "banana", "cherry", "date"]
   Expected Output: 'banana'
"""
from functools import reduce

words = ["apple", "banana", "cherry", "date"]
longest_word = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print("Longest Word:", longest_word)


"""
4) Use map() to square each number in the list and round the result 
   to one decimal place.
   my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
   Expected Output: [18.9, 37.1, 10.6, 95.5, 4.7, 78.9, 21.1]
"""
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
squared_rounded = list(map(lambda x: round(x * x, 1), my_floats))
print("Squared & Rounded:", squared_rounded)


"""
5) Use filter() to select names with 7 or fewer characters from the list.
   my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
   Expected Output: ['olumide', 'josiah', 'omoseun']
"""
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
names_upto_7 = list(filter(lambda x: len(x) <= 7, my_names))
print("Names with <= 7 chars:", names_upto_7)


"""
6) Use reduce() to calculate the sum of all numbers in a list.
   [1, 2, 3, 4, 5]
"""
nums = [1, 2, 3, 4, 5]
total_sum = reduce(lambda a, b: a + b, nums)
print("Sum of numbers:", total_sum)

######## ALL & ANY ########
"""
1) Check if All Numbers are Positive using all()
   Input : numbers = [1, 2, 3, 4, 5]
   Expected Output : True
"""
numbers = [1, 2, 3, 4, 5]
all_positive = all(num > 0 for num in numbers)
print("All numbers are positive:", all_positive)


"""
2) Check if Any Number is Even using any()
   Input: numbers = [1, 3, 5, 7, 8]
   Expected Output: True
"""
numbers = [1, 3, 5, 7, 8]
any_even = any(num % 2 == 0 for num in numbers)
print("Any number is even:", any_even)


"""
3) Determine if any number in a list is divisible by 5 and print
   Input: numbers = [3, 11, 20, 7, 25]
   (Example Input — you can replace)
   Expected Output:
       20
       25
"""
numbers = [3, 11, 20, 7, 25]

divisible_by_5 = list(filter(lambda x: x % 5 == 0, numbers))
print("Numbers divisible by 5:", divisible_by_5)


##### CLASS LEARNING ############

"""
1) Define a class Person with attributes name and age.
   Create an instance and print its attributes.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Sumit", 25)
print(p.name)
print(p.age)


"""
2) Write a Python class BankAccount with attributes:
   account_number, balance, customer_name
   Methods: deposit(), withdraw(), check_balance()
"""
class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def check_balance(self):
        print("Current balance:", self.balance)

acc = BankAccount("12345", "Sumit", 5000)
acc.deposit(1000)
acc.withdraw(2000)
acc.check_balance()


"""
3) Create a class Book with class method from_string() 
   that creates a Book instance from a string.
   book = Book.from_string("Python Programming, John Doe")
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split(",")
        return cls(title.strip(), author.strip())

book = Book.from_string("Python Programming, John Doe")
print(book.title)
print(book.author)


"""
4) Create a base class Animal with method sound().
   Create subclasses Dog and Cat that override the sound() method.
"""
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()
d.sound()
c.sound()


"""
5) Write code to perform multiple inheritance.
"""
class Father:
    def father_feature(self):
        print("Feature from Father")

class Mother:
    def mother_feature(self):
        print("Feature from Mother")

class Child(Father, Mother):
    def child_feature(self):
        print("Feature from Child")

baby = Child()
baby.father_feature()
baby.mother_feature()
baby.child_feature()


##### EXCEPTION HANDLING #####

"""
1) Write a Python program that attempts to divide two numbers
   a = 10, b = 0
   Handle ZeroDivisionError and print the error.
"""
a = 10
b = 0

try:
    result = a / b
    print("Result:", result)
except ZeroDivisionError as e:
    print("Error:", e)


"""
2) Apply exception handling to the code and handle an exception 
   if the index is out of range.

   my_list = [1, 2, 3]
   print(my_list[5])
"""
my_list = [1, 2, 3]

try:
    print(my_list[5])
except IndexError as e:
    print("Index Error:", e)


"""
3) Correct the below code with appropriate exception handling.
   Finally print “Execution completed”

   def safe_divide(a,b):
         result = a / b
         print(f"Result: {result}")

   safe_divide(1,0)
   safe_divide(1,"a")
"""
def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)
    except TypeError as e:
        print("TypeError:", e)
    except Exception as e:
        print("Unexpected Error:", e)
    finally:
        print("Execution completed")


safe_divide(1, 0)
safe_divide(1, "a")


#### GENERATORS ####

"""
1) Write a generator to produce the first 10 Fibonacci numbers.

Output:
0
1
1
2
3
5
8
13
21
34
"""
def fibonacci_generator():
    a, b = 0, 1
    while True:  # infinite generator, but we will take first 10
        yield a
        a, b = b, a + b

fib = fibonacci_generator()

for _ in range(10):
    print(next(fib))


"""
2) Write a generator infinite_multiples(n) that yields multiples of the given base value indefinitely.

Input: n = 3
Output:
3
6
9
12
15
...
"""
def infinite_multiples(n):
    multiple = n
    while True:
        yield multiple
        multiple += n

gen_mult = infinite_multiples(3)

# Print first 10 multiples for demonstration
for _ in range(10):
    print(next(gen_mult))


"""
3) Write a generator repeat_word(word, times) that yields the word the given number of times.

word = "hello"
times = 5
"""
def repeat_word(word, times):
    for _ in range(times):
        yield word

gen_repeat = repeat_word("hello", 5)

for w in gen_repeat:
    print(w)


##### MODULES LEARNING ####

"""
1) Using datetime, add a week and 12 hours to a date.
   Given date: March 22, 2020, at 10:00 AM.
   Print original and new datetime.
"""
from datetime import datetime, timedelta

original_date = datetime(2020, 3, 22, 10, 0)
new_date = original_date + timedelta(weeks=1, hours=12)

print("Original Date:", original_date)
print("New Date:", new_date)


"""
2) Code to get the dates of yesterday, today, and tomorrow.
"""
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


"""
3) Write a code snippet using os module:
   - Get current working directory
   - Create a folder “test”
   - List files/folders
   - Remove the folder “test”
"""
import os

cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Create folder
os.makedirs("test", exist_ok=True)
print("Folder 'test' created.")

# List items
print("Files & Folders in CWD:", os.listdir(cwd))

# Remove folder
os.rmdir("test")
print("Folder 'test' removed.")


"""
4) Python program to rename a file from old_name.txt to new_name.txt.
"""
try:
    os.rename("old_name.txt", "new_name.txt")
    print("File renamed successfully.")
except FileNotFoundError:
    print("File old_name.txt not found!")


"""
5) Create a file and write content, then get the size of example.txt.
"""
# Create file example.txt
with open("example.txt", "w") as f:
    f.write("This is an example file.")

# Get file size
size = os.path.getsize("example.txt")
print("Size of example.txt:", size, "bytes")


"""
6) Convert string "Feb 25 2020 4:20PM" into a Python datetime object.
   Output: 2020-02-25 16:20:00
"""
date_str = "Feb 25 2020 4:20PM"
dt_object = datetime.strptime(date_str, "%b %d %Y %I:%M%p")
print("Converted datetime:", dt_object)


"""
7) Subtract 7 days from date 2025-02-25.
   Output: New date: 2025-02-18
"""
given_date = datetime(2025, 2, 25)
new_date = given_date - timedelta(days=7)

print("New date:", new_date.date())


"""
8) Format the date 2020-02-25 as "Tuesday 25 February 2020"
"""
date_to_format = datetime(2020, 2, 25)
formatted = date_to_format.strftime("%A %d %B %Y")
print("Formatted Date:", formatted)
