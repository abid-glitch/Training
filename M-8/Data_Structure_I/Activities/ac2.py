# blank dictionary
d = {}

# integer key dictionary
d = {1: 'apple', 2: 'ball'}

# keys mixed
d = {'name': 'John', 1: [2, 4, 3]}

d = {'name': 'Jack', 'age': 26}

# access values
print(d['name'])
print(d.get('age'))

# modify value
d['age'] = 27
print(d)

# insert item
d['address'] = 'Downtown'
print(d)

# delete specific key
d.pop('age')
print(d)

# fetch specific value
print("Address is:", d.get('address'))

# erase all data
d.clear()
print(d)
