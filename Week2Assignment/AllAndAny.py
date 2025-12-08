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
