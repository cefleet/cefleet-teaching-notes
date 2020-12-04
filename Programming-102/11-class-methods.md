# Class Methods

## Objectives
- Defining Class methods
- Using Class methods
- Modifying attributes with class methods
- Exercises

## Defining class methods
- ```python
    #in game terms mob stands for mobile. It can be anything that moves including enemies, npc, and the player's characters.
    class Mob:
        def __init__(self, name, health = 10):
            self.name = name
            self.health = health
        
        # The first argument of every method is self.
        def get_hit(self, power):
            print('I, %s, have been hit for %s!' % (self.name, power))

    hero = Mob("Sir Galahand", 20)
    #self is not placed here. The class handles that itself
    hero.get_hit(2)
## Modifying attributes with class methods
- ```python
    ... #previous code
        def get_hit(self, power):
            #Health is now lowered
            self.health = self.health - power
            print('I, %s, have been hit for %s and now have %s health' % (self.name, power, self.health))

    hero = Mob("Sir Galahand", 20)
    hero.get_hit(4)
    hero.get_hit(6)
- ```python
    class Mob:
        def __init__(self, name, health = 10, attack_power = 2):
            self.name = name
            self.health = health
            self.attack_power = attack_power #added

        ...#get_hit from previous examples

        def attack(self, enemy):
            #using another class instances methods
            print("I am attacking %s for %s power" % (enemy.name, self.attack_power))
            enemy.get_hit(self.attack_power)
            
    hero = Mob("Sir Galahand", 20,3)
    bad_guy = Mob('Evil McEvil', 10)

    hero.attack(bad_guy)
    bad_guy.attack(hero)
## Exercise
1. Using our vehicle class from the previous lesson, add a speed, top_speed, position, and acceleration attribute.
    - speed and position should start at 0, top_speed and acceleration are numbers.
    - add a class method called move. When the move method is called have the position increase by the speed of the car.
    - add a class method called accelerate and using the very simplified equation to have the vehicle accelerate when the accelerate method is called on that instance:
    ```
     speed = speed + acceleration
    ```
    - In the accelerate method, do not allow the vehicle to pass the top speed.
    - modify the instances of the vehicles to include acceleration and top speed when you instance the vehicles.
    - using a while loop and assuming each iteration of the loop is a 'second' have the vehicles 'race' by accelerating as much as possible on a drag strip for 20, 40, and 60 seconds to see who wins.
    - (challange) instead of racing for a timeframe, make the race different distances. Position can be considered in meters. 