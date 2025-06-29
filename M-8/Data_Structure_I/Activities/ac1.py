items = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("Total items:", len(items))
print("First item:", items[0])
print("Final item:", items[-1])

items.append('Papaya')
print("After appending:", items)

items.remove('Guava')
print("After removal:", items)

items.sort()
print("Sorted items:", items)

items.pop(1)
print("After popping index 1:", items)

items.reverse()
print("Reversed order:", items)

print("Repeated List:", items * 2)

items = items[:4]
print("Trimmed list:", items)

items.clear()
print("List after clearing:", items)
