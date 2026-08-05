
fruits = ["Apple", "Banana", "Mango"]

print("Original List:", fruits)

fruits.append("Orange")
print("After Append:", fruits)

fruits.remove("Banana")
print("After Remove:", fruits)

fruits.insert(1, "Grapes")
print("After Insert:", fruits)

print("First Fruit:", fruits[0])

print()



colors = ("Red", "Green", "Blue")

print("Tuple:", colors)

print("First Color:", colors[0])

print()




numbers = {10,20,30,20,10}

print("Set:", numbers)

numbers.add(40)

print("After Add:", numbers)

print()



student = {
    "name":"Harsha",
    "age":19,
    "course":"AIML"
}

print(student)

print(student["name"])

student["city"] = "Chennai"

print(student)