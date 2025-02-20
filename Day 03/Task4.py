class dog:
    def bark(self):
        print("Dog is barking")
        
    def sleep(self):
        print("Dog is sleeping")
        
class cat:
    def meow(self):
        print("cat is meowing")
        
    def purr(self):
        print("cat is purring")
        
class hybrid(dog, cat):
    def show_traits(self):
        print("I have both dog and cat traits")
        
hybrid_pet = hybrid()

hybrid_pet.bark()
hybrid_pet.sleep()
hybrid_pet.meow()
hybrid_pet.purr()