# -----------------------------------------------------------
# 1. For loop: Check if input number is even or odd
# -----------------------------------------------------------

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")


# -----------------------------------------------------------
# 2. Reverse a string using for loop and check palindrome
#    Strings = “civic”, “hello”
# -----------------------------------------------------------

s = input("Enter a string: ")

reversed_s = ""
for ch in s:
    reversed_s = ch + reversed_s

print("Reversed string is -", reversed_s)

if s == reversed_s:
    print("It is a palindrome")
else:
    print("Not a palindrome")


# -----------------------------------------------------------
# 3. Generate first N Fibonacci numbers
# -----------------------------------------------------------

n = int(input("Enter how many Fibonacci numbers to generate: "))

a, b = 0, 1
print("Fibonacci sequence:")

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b


# -----------------------------------------------------------
# 4. From list [1,2,3,4,5], find values whose sum is 9
#    Expected output: [4, 5]
# -----------------------------------------------------------

nums = [1, 2, 3, 4, 5]
target = 9

result = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            result = [nums[i], nums[j]]
            break

print("Pair with sum 9 is -", result)


# -----------------------------------------------------------
# WHILE LOOP
# -----------------------------------------------------------
# 5. Print all even numbers between 1 and 20
# -----------------------------------------------------------

i = 1
print("Even numbers from 1 to 20:")
while i <= 20:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1

print("\n")


# -----------------------------------------------------------
# BREAK
# 6. Find first occurrence of a number in list and stop
# -----------------------------------------------------------

numbers = [10, 20, 30, 40, 50]
search_for = 30

for num in numbers:
    if num == search_for:
        print("Found:", num)
        break


# -----------------------------------------------------------
# CONTINUE
# 7. Print only odd numbers from 1 to 10
# -----------------------------------------------------------

print("\nOdd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")


# -----------------------------------------------------------
# PASS
# 8. What will be the output?
# -----------------------------------------------------------

print("Output of pass example:")
for i in range(5):
    if i == 3:
        pass
    print(i)


# -----------------------------------------------------------
# MATCH
# 9. Day of week -> weekday/weekend
# -----------------------------------------------------------

day = input("\nEnter day of week: ").lower()

match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("It's a Weekday")
    case "saturday" | "sunday":
        print("It's a Weekend")
    case _:
        print("Invalid day entered")
