# Dictionary 'key' : value
# Dictionaries are not based on index
# There is no particular order in dictionary
myExample = {'someItem': 2, 'otherItem': 20}

# similar to tables in other language
print(myExample['otherItem'])

myExample['newItem'] = 400

for a in myExample:
    print(a)
    
print();

for a in myExample:
    print(a, myExample[a])
    
# you can use function get() which is more secure

print(myExample.get('nonExisting'));