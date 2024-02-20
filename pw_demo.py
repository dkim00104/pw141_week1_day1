# write a function that says "Welcome to CT NAME_HERE!"

print("Welcome to CT David!")

name = "David"

print("Welcome to CT " + name + "!")

print(f"Welcome to CT {name}!")

# my solution 

def greeting(name):
    print("Welcome to CT " + name + "!")

greeting("David")

# alternative solution

def greeting(name):
    print(f"Welcome to CT {name}!")
    return 3

greeting("David")

print(greeting("David") + greeting("Tom"))
print(greeting("David") == 3)

# example

def adder(num1, num2):
    return num1 + num2

print(adder(5,6))