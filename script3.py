# Initialize an empty dictionary
dict = {}

# Collect key-value pairs from the user
while True:
    key = input("Enter a new key for dictionary: ")
    if key.lower() == "stop":
        break
    value = input("Enter value for the key: ")
    dict[key] = value

print(dict)

# Create a new dictionary to group keys by values
dict2 = {}

# Populate dict2 by reversing the key-value relationships
for key, value in dict.items():
    if value not in dict2:
        dict2[value] = [key]
    else:
        dict2[value].append(key)

print(dict2)
