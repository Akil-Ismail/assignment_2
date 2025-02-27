
#First Dictionary:
dict1={}
while True:
    key=input("enter a new key for first dictionary : ")
    if key=="stop":
        break
    value=input("enter value for the key : ")
    dict1[key]=value

print("First Dictionary : ",dict1)

#Second Dictionary:
dict2={}
while True:
    key_2=input("enter a new key for second dictionary : ")
    if key_2=="stop":
        break
    value_2=input("enter value for the key : ")
    dict2[key_2]=value_2

print("Second Dictionary : ",dict2)

#Merge function:
def merge_dictionaries(dict1,dict2):
    dict3={}
    for key,value in dict1.items():
        dict3[key]=value
    for key_2,value_2 in dict2.items():
        dict3[key_2]=value_2        
    print("Merged Dictionary : ",dict3)

merge_dictionaries(dict1,dict2)
