class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
dog1 = Dog("Tommy", 4)
dog2 = Dog("Timmy", 3)
dog3 = Dog("Tonny", 2)
dog4 = Dog("Tummy", 1)

print(f"my first dog name is {dog1.name} and is {dog1.age} years old ")
print(f"my second dog name is {dog2.name} and is {dog2.age} years old ")
print(f"my third dog name is {dog3.name} and is {dog3.age} years old ")
print(f"my fourth dog name is {dog4.name} and is {dog4.age} years old ")
