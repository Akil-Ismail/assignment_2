
#First Dictionary:
dict1=[]
while True:
    key=input("enter a new key for first dictionary : ")
    if key=="stop":
        break
    value=input("enter value for the key : ")
    dictionary1={
        key:value
    }
    dict1.append(dictionary1)

print("First Dictionary : ",dict1)

#Second Dictionary:
dict2=[]
while True:
    key_2=input("enter a new key for second dictionary : ")
    if key_2=="stop":
        break
    value_2=input("enter value for the key : ")
    dictionary2={
        key_2:value_2
    }
    dict2.append(dictionary2)

print("Second Dictionary : ",dict2)

#Merge function:
def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

dict1_combined = {k: v for d in dict1 for k, v in d.items()}
dict2_combined = {k: v for d in dict2 for k, v in d.items()}

merged_result = merge_dictionaries(dict1_combined, dict2_combined)

print("Merged Dictionary : ",merged_result)
