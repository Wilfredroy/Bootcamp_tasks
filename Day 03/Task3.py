class Dog :
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(f"{self.name} is barking")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
class Puppy(Dog):
    def play(self):
        print(f"{self.name} is playing")
        
my_puppy = Puppy("Harry Potter", 5)

my_puppy.bark()
my_puppy.sleep()
my_puppy.play()