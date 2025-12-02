# -----------------------------------------------------------
# 1. Convert list of numeric strings → integers (List Comprehension)
#    strings = ["1", "2", "3", "4", "5"]
#    Expected output: [1, 2, 3, 4, 5]
# -----------------------------------------------------------
strings = ["1", "2", "3", "4", "5"]
int_list = [int(x) for x in strings]
print("1)", int_list)


# -----------------------------------------------------------
# 2. Extract integers > 10 from list (List Comprehension)
#    numbers = [1, 5, 13, 4, 16, 7]
#    Expected output: [13,16]
# -----------------------------------------------------------
numbers = [1, 5, 13, 4, 16, 7]
greater_than_10 = [num for num in numbers if num > 10]
print("2)", greater_than_10)


# -----------------------------------------------------------
# 3. List of squares from 1 to 5 (List Comprehension)
#    Expected output: [1,4,9,16,25]
# -----------------------------------------------------------
squares = [x*x for x in range(1, 6)]
print("3)", squares)


# -----------------------------------------------------------
# 4. Convert 2D list → 1D list (List Comprehension)
#    matrix = [[1,3,4], [23,32,56,74], [-2,-6,-9]]
#    Expected output: [1,3,4,23,32,56,74,-2,-6,-9]
# -----------------------------------------------------------
matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
flattened = [item for sublist in matrix for item in sublist]
print("4)", flattened)


# -----------------------------------------------------------
# 5. Dictionary comprehension from keys & values
#    keys = ['a','b','c'], values = [1,2,3]
#    Expected output: {'a':1,'b':2,'c':3}
# -----------------------------------------------------------
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {keys[i]: values[i] for i in range(len(keys))}
print("5)", my_dict)


# -----------------------------------------------------------
# 6. Filter dictionary where scores > 80 (Dict Comprehension)
#    scores = {'Alice':85,'Bob':70,'Charlie':90}
#    Expected: {'Alice':85,'Charlie':90}
# -----------------------------------------------------------
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
filtered_scores = {name: score for name, score in scores.items() if score > 80}
print("6)", filtered_scores)
