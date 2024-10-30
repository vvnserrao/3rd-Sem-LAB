dict1 = dict()
print("Initialized empty dictionary:", dict1) 

dict2 = {1: 'vivian', 2: 'serrao', 3: 'mca'}
print("Initialized dictionary with key-value pairs:", dict2) 

dict1 = dict2.copy()
print("Copied dict2 into dict1:", dict1)

dict1.clear()
print("Cleared all items from dict1:", dict1)  

print("Value for key 1 in dict2:", dict2.get(1))  

print("All key-value pairs in dict2:", dict2.items()) 

print("All keys in dict2:", dict2.keys())  

dict2.pop(3)
print("Removed item with key 3 from dict2:", dict2) 

dict2.popitem()
print("Removed and returned an arbitrary (key, value) pair from dict2:", dict2)  

dict3 = {4: 'student'}
dict2.update(dict3)
print("Updated dict2 with dict3:", dict2)  

print("All values in dict2:", dict2.values())
