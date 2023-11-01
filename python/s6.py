# Ways to use "f" strings in Python

# 1 - Align strings with f-strings:
print('# 1 - Align strings with f-strings:')
name = "Lynn"
age = 43
print(f"|\t{name:<10}\t|\t{age:^5}\t|")

print("_" * 30)  # this is only a separate line

# 2 - Use f-strings with dictionary variables:
print('2 - Use f-strings with dictionary variables:')
person = {"name": "Lynn", "age": 43}
print(f"My name is {person['name']} and I'm {person['age']} years old.")

print("_" * 30)

# 3 - Use f-strings to format binary and hexadecimal numbers:
print('3 - Use f-strings to format binary and hexadecimal numbers:')
x = 100
print(f"x = {x:b}")
print(f"x = {x:x}")

print("_" * 30)

# 4 - Use f-strings to format dates and times:
print('4 - Use f-strings to format dates and times:')

import datetime

now = datetime.datetime.now()
print(f"Today is {now:%B %d, %Y}")

print("_" * 30)

# 5 - Use f-strings to format currency values:
print('5 - Use f-strings to format currency values:')

salary = 82000
print(f"My salary is ${salary:,}")

print("_" * 30)

# 6 - Use f-strings with formatted strings:
print('6 - Use f-strings with formatted strings:')

name = "Lynn"
age = 43
message = f"My name is {name} and I'm {age} years old."
print(f"Message length: {len(message):<10}, Message: '{message:^20}'")

print("_" * 30)

# 7 - Use f-strings to format scientific notation:
print('7 - Use f-strings to format scientific notation:')

x = 1234567890.123456789
print(f"x = {x:e}")


