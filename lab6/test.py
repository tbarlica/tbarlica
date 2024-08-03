from student import Student

# Creates an instance of the Student class, it will be separate from all other objects created with the Student class:
student1 = Student('John', '013454900')
print(student1.name)
print(student1.number)
print(student1.courses)
student1.displayStudent()

student2 = Student('Jessica', '023384103')
print(student2.name)
print(student2.number)
print(student2.courses)
student2.displayStudent()

# Add new courses for student1
student1.addGrade('uli101', 4.0)
student1.addGrade('ops245', 3.5)
student1.addGrade('ops445', 3.0)

# Add new courses for student2
student2.addGrade('ipc144', 4.0)
student2.addGrade('cpp244', 4.0)

print(student1.name)
print(student1.courses)
print(student2.name)
print(student2.courses)


