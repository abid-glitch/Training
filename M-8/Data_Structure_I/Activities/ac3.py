def convert(data):
    res = {}
    for entry in data:
        res[entry[0]] = entry[1:]
    return res

people = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

print("\nInitial nested list:")
print(people)
print("\nList transformed to dictionary:")
print(convert(people))
