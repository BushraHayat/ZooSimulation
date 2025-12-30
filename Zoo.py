from AnimalMod import *
from VisitorMod import *
    
def run_simulation():
    print("***** WELCOME TO THE ZOO SIMULATION *****")
    days=int(input("Enter number of days to run the simulation for:"))  #Allowing the simulation to run for a configurable number of days. 
    
    #initializing animals and visitor
    lion=Lion("Lion",8)   
    parrot=Parrot("Parrot",3)
    horse=Horse("Horse",10)
    visitor=Visitor("John")
    lion_actions=[lion.walk,lion.play,lion.speak,lion.eat,lion.sleep,lion.run]
    horse_actions=[horse.walk,horse.play,horse.speak,horse.eat,horse.sleep,horse.run]
    parrot_actions=[parrot.walk,parrot.play,parrot.speak,parrot.eat,parrot.sleep,parrot.fly]
    visitor_actions=[visitor.feed_animal,visitor.play_with_animal]
    animals=[lion,horse,parrot]

    for day in range(1,days+1):  #running simulation for x number of days
        print(f"------------DAY {day}-----------\nWe have the following animals in our zoo:")      
        print(lion)
        print(parrot)
        print(horse)
        
        for i in range(1,4):
            lion_c_action=random.choice(lion_actions)
            lion_c_action()
            print(lion)
        for i in range(1,4):
            horse_c_action=random.choice(horse_actions)
            horse_c_action()
            print(horse)
        for i in range(1,4):
            parrot_c_action=random.choice(parrot_actions)
            parrot_c_action()
            print(parrot)

        print("Visitor has arrived")
        for i in range(1,4):          
            visitor_c_action=random.choice(visitor_actions)
            chosen_animal=random.choice(animals)
            visitor_c_action(chosen_animal)
        
        print(lion)
        print(parrot)
        print(horse)
        #At the end of the day all animals must go to sleep
        print("It's the end of the day hence:")
        lion.sleep()
        horse.sleep()
        parrot.sleep()
       
run_simulation()