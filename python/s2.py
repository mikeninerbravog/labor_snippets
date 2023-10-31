# How to convert two lists into a dictionary

# Method 1: Using a Dictionary Comprehension

keys = ["name", "age", "city"]
values = ["Mike", 38, "Rio de Janeiro"]

# Create a dictionary using a dictionary comprehension
my_dict = {keys[i]: values[i] for i in range(len(keys))}

print("Method 1 result:")
print(my_dict)


# Method 2: Using the zip() Function

keys = ["name", "age", "city"]
values = ["Mike", 38, "Rio de Janeiro"]

# Create a dictionary using zip
my_dict = dict(zip(keys, values))

print("Method 2 result:")
print(my_dict)
