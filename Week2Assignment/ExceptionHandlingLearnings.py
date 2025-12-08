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
