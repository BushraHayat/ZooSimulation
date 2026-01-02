import random
from abc import ABC,abstractmethod
from enum_mod import State

class Animal(ABC):  
    _play_cost=30
    _walk_cost=20
    _hunt_cost=40
    _run_fly_cost=50
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__energy_level=100  #when animal walks energy level drops 20%, plays-30% ,runs-50%   
        self._state=State.awake
    @abstractmethod
    def speak(self):    #each animal will have its own implementation of speak
        pass
    @abstractmethod
    def eat(self):     #each animal will have its own implementation of eat
        pass
    def play(self):    # this method will be inherited as it is
        if self.is_tired(self._play_cost):
          print(f"{self.name} is tired, hence can't play anymore")
        else:
          self._state=State.playing
          self.reduce_energy(self._play_cost)
          print(f"{self.name} is playing")

    def sleep(self):
        if self.is_energized() and self._state==State.sleeping:
          print(f"{self.name} is already sleeping")
        else:
          self._state=State.sleeping
          self.restore_energy()
          print(f"{self.name} is sleeping") 
    
    def walk(self):     
        if self.is_tired(self._walk_cost):
          print(f"{self.name} is tired, hence can't walk anymore")
        else:
          self._state=State.walking
          self.reduce_energy(self._walk_cost)
          print(f"{self.name} is walking")

    def is_tired(self,value):
        if self.__energy_level-value<0:
            self._state=State.tired
            return True
        else:     
            return False
    def is_energized(self):
        if self.__energy_level==100:
            return True
        else:            
            return False
    def restore_energy(self):
        self.__energy_level=100
    def reduce_energy(self,cost):
       self.__energy_level-=cost 

    def __str__(self):
        return f"{self.name} with age {self.age} is {self._state.name}, has energy level {self.__energy_level}%"
        
               
class Carnivore(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def eat(self):       #this method is implemented with its own functionality 
        if  self.is_energized() and self._state==State.eating:
            print(f"{self.name} is already full")
        else:
           self._state=State.eating
           self.restore_energy()
           print(f"{self.name} is eating meat")
    def hunt(self,animal_list,animal_to_hunt):
       if self.is_tired(self._hunt_cost):
          print(f"{self.name} is tired, hence can't hunt now")
       else: 
          print(f"{self.name} is hunting {animal_to_hunt.name}") 
          animal_list.remove(animal_to_hunt)   
          self._state=State.hunting
          self.reduce_energy(self._hunt_cost)
          
    def __str__(self):
        return super().__str__()+" and is a Carnivore"

class Herbivore(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def eat(self):     #this method is implemented with its own functionality 
        if self.is_energized() and self._state==State.eating:
            print(f"{self.name} is already full")
        else:
           self._state=State.eating
           self.restore_energy()
           print(f"{self.name} is eating plants/seeds")
    
    def __str__(self):
        return super().__str__()+f" and is a Herbivore"
  
class Lion(Carnivore):
    def __init__(self, name, age):
       super().__init__(name, age)

    def speak(self):
        self._state=State.speaking
        print("Roar")
    def run(self):
        if self.is_tired(self._run_fly_cost):
          print(f"{self.name} is tired, hence can't run now")
        else:
          self._state=State.running
          self.reduce_energy(self._run_fly_cost)
          print(f"{self.name} is running")

class Horse(Herbivore):
    def __init__(self, name, age):
       super().__init__(name, age)

    def speak(self):
        self._state=State.speaking
        print("Neigh")
    def run(self):
        if self.is_tired(self._run_fly_cost):
          print(f"{self.name} is tired, hence can't run now")
        else:
          self._state=State.running
          self.reduce_energy(self._run_fly_cost)
          print(f"{self.name} is running")
    

class Parrot(Herbivore):
    __sounds=["gurgle","whistle","squawk"]

    def __init__(self, name, age):
       super().__init__(name, age)       
    def speak(self):
        self._state=State.speaking
        chosen_sound=random.choice(self.__sounds)
        print(chosen_sound)
    def fly(self):  
        if self.is_tired(self._run_fly_cost):
          print(f"{self.name} is tired, hence can't fly now")
        else:
          self._state=State.flying
          self.reduce_energy(self._run_fly_cost)
          print(f"{self.name} is flying")

# class Eagle(Carnivore):
#     def speak(self):
#         print("Ee")  
#     def fly(self):
#         if self.is_tired(50):
#           print(f"{self.name} is tired, hence can't fly now")
#         else:
#           print(f"{self.name} is flying")