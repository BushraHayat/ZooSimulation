from AnimalMod import *
class Visitor:
    def __init__(self,name):
        self.name=name
    
    def feed_animal(self,animal):      
        print(f"Visitor {self.name} wants to feed {animal.name}")
        animal.eat()
       
    def play_with_animal(self,animal):       
        print(f"Visitor {self.name} wants to play with {animal.name}")
        animal.play()
      