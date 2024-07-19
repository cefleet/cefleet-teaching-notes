class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
  
  def greet(self, message):
    print('Greetings from ' + self.first_name + ' ' + self.last_name)
    print(message)
  
if __name__ == "__main__":
  instructor = Person('Clint', 'Fleetwood')
  instructor.greet('Welcome to your first day of class.')