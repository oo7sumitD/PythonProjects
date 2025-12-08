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
