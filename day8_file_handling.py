
file = open("student.txt", "w")
file.write("Name: Harsha\n")
file.write("Course: AIML\n")
file.write("Age: 19")
file.close()

print("Data written successfully!")


file = open("student.txt", "r")
print(file.read())
file.close()


file = open("student.txt", "a")
file.write("\nCollege: SRM")
file.close()

file = open("student.txt", "r")
print(file.read())
file.close()