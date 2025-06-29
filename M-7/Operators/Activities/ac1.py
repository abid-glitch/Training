name_val = "Penguin"
person_age = 15
student_status = True
person_weight = 38.5

print("Name :", name_val)
print("Data Type of Name is", type(name_val))
print("Age :", person_age)
print("Data Type of Age is", type(person_age))
print("is_student :", student_status)
print("Data Type of is_student is", type(student_status))
print("Weight :", person_weight)
print("Data Type of weight is", type(person_weight))

print("\nAfter Type Conversion....")
person_age = str(person_age)
print(person_age)
print("Data Type of age is", type(person_age))
person_weight = int(person_weight)
print(person_weight)
print("Data Type of Weight is", type(person_weight))
