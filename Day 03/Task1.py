class Dog :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} is barking")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
    
my_dog = Dog("Tommy", 5)

my_dog.bark()
my_dog.sleep()