

def greet(name, location):
    print("Hello " + name)
    print("Hello " + name + " I see you live in " + location)
    print(location + "is a good place to live.")


nameInput = input("Insert name here \n")
locationInput = input("Where do you live? \n")
greet(nameInput, locationInput)
