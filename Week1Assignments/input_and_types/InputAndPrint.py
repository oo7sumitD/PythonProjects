'''Write a program that asks the user for their name and then prints a greeting   message using their name. '''

str_ip  = input("enter your name: ")
print(f"Hello Coder {str_ip}, Welcome to different world.")

'''Ask the user to enter two numbers from the user and print their sum, multiplication, and division. '''
num_ip1  = input("enter first number: ")
num_ip2  = input("enter second number: ")
print(f"Sum of two numbers: {int(num_ip1)+int(num_ip2)}")
print(f"Multiplication of two numbers: {int(num_ip1)*int(num_ip2)}")
print(f"Division of two numbers: {int(num_ip1)/int(num_ip2)}")

'''Ask the user to enter input names separated by commas, split the string from comma and copy to a list and print'''
names_ip = input("Enter names separated by commas: ")
names_lst = names_ip.split(",")
print(f"Names list - {names_lst}")

'''Ask the user to enter their age and check if they are eligible to vote based on their age.'''
age_ip  = input("enter your age: ")

if int(age_ip) >= 18:
    print("Eligible for voting")
else:
    print("Not eligible.")

'''For value = 3.14159, Using f-string print output for only up to 2 decimal places.'''
value = 3.14159
print(f"Value up to 2 decimal places is - {value:.2f}")