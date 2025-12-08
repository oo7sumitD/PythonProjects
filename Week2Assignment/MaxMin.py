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
