class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

# Create an object of the Person class
person1 = Person("Alice", 30)

# Access attributes and call methods
print(person1.name)  # Output: Alice
person1.greet()      # Output: Hello, my name is Alice