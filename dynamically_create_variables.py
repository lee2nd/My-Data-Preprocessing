# https://stackoverflow.com/questions/5036700/how-can-you-dynamically-create-variables
    
item_lst = ["x","y","z"]

for i in range(len(item_lst)):
    globals()[f"v{i+1}"] = item_lst[i]
    
print(v1)
# x
print(v2)
# y
print(v3)
# z
