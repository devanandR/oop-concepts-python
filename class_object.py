class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} says woof!"

if __name__ == "__main__":
    dog = Dog("Buddy", 5)
    print(dog.speak())
