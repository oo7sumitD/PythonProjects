"""1. Task: Convert the following values to the specified types and print the results"""

# 1.Convert 3.75 to an integer and print the value

num_float = 3.75
print(f"Integer value: {int(num_float)}")


# 2.Convert "123" to a float and print the value
string = "123"
print(f"Float value: {float(string)}")


# 3.Convert 0 to a boolean and print the value
num = 0
print(f"Boolean value: {bool(num)}")

# 4.Convert False to a string and print the value
flag = False
print(f"String value: {str(flag)}")


"""2. Convert all characters in the string to uppercase. x = "hello" """
string = "hello"
print(f"Uppercase String: {string.upper()}")

"""3. Given x = 5 and y = 3.14, calculate z = x + y and determine the data type of z. And convert it to integer. """
int_num = 5
float_num = 3.14
z = int_num+float_num
print(f"Type of Z: {type(z)}")
print(f"Converting Z to Integer: {int(z)}")

"""4. Given the string s = 'hello', perform the following operations:"""
s = "hello"

# 1.Convert the string to uppercase.
print(f"Uppercase String: {s.upper()}")

# 2.Replace 'e' with 'a'.
print(f"Replaced 'e' with 'a': {s.replace("e","a")}")

# 3.Check if the string starts with 'he'.
print(f"If String starts with 'he': {s.startswith("he")}")

# Check if the string ends with 'lo'.
print(f"If String ends with 'lo': {s.endswith("lo")}")

