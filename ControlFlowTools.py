# If statements

age = 19

if age < 18:
    print("You are underage")
elif age >= 55:
    print("Consuming alcohol at old age may worsen health issues")
else:
    print("You may purchase")

# And, Or statements

white_blood_cell = 5000
red_blood_cell = 5
platelet = 0.35

if red_blood_cell < 3.90 or white_blood_cell < 3500 or platelet < 0.15:
    print("Recommended Medical Attention")
elif red_blood_cell < 3.90 and white_blood_cell < 3500 and platelet < 0.15:
    print("Urgent Medical Attention")
else:
    print("Healthy")

# Loops

i = 0
while i <= 10:
    print(i)
    i += 1

fruit_list = ["Apple", "Banana", "Orange", "Pear", "Mango"]
for fruit in fruit_list:
    print(fruit)

for x in range(0, 10, 1):
    print(x)

for y in range(10, 0, -1):
    print(y)

for index in range(0, 3, 1):
    fruit = fruit_list[index]
    print(fruit)

# Control Statements

for x in range(0, 10, 1):
    if x == 3:
        break
    print(x)

for x in range(0, 4, 1):
    if x == 2:
        continue
    print(x)

for x in range(1, 6, 1):
    print(x)
    if x == 5:
        pass
for x in range(1, 6, 1):
    print(x)
    if x == 5:
        print("End of list")

# Functions

def print_hello():
    print("Hello")

print_hello()
print_hello()

def square(n):
    result = n * n
    print(result)

square(2)

def add(a, b):
    result = a + b
    print(result)

add(5, 4)

def square_V2(n):
    result = n * n
    return result

square_5 = square_V2(5)
print(square_5)

def cube(n):
    result = n * n * n
    return result

cube_3 = cube(3)
print(cube_3)

run = True
def print_status():
    global run
    if run == True:
        text = "Running"
    else:
        text = "Not Running"
    print(text)

print_status()