for i in range(1,11):
    print(i)
for i in range(1,11):
    if i == 6:
        break
    print(i)
    for i in range(1,11):
        if i == 5:
            continue
        print(i)
for i in range(3):
    for j in range(3):
        print(i,j)
def greet():
    print("Welcome ti ML Internship")
greet()
def greet(name):
    print("Hello",name)
greet("Harsha")
def add(a,b):
    return a + b
print(add(25, 35))
def square(num):
    return num * num
print(square(8))