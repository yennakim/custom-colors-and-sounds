class Vehicle:
  def __init__(self, color, make, model, year):
    self.color = color
    self.make = make
    self.model = model
    self.year = year
    
  def drive(self):
    print(f'The {self.color} {self.year} {self.make} {self.model} went "Vrooooooom!"')
  def turn(self, direction):
    print(f'Making a {self.direction} turn')
  def stop(self):
    print(f'Screech!')
  
class Car(Vehicle):
  def __init__(self, color, make, model, year):
    super().__init__(color, make, model, year)
  def drive(self):
    print(f'The old {self.color} {self.model} drives past. RRrrrrrummbbble!"')
  def turn(self, direction):
    print(f"The {self.color} {self.make} {self.model} smoothly turns {direction}.")
  def stop(self):
    print(f'Screech!')
    
    
class Bus(Vehicle):
  def __init__(self, color, make, model, year):
    super().__init__(color, make, model, year)
  def drive(self):
    print(f'The {self.color} {self.model} drives past. Honk honk!"')
  def turn(self, direction):
    print(f"The {self.color} {self.make} {self.model} turns {direction}.")
  def stop(self):
    print(f'The {self.model} abruptly stops')
    
class Truck(Vehicle):
  def __init__(self, color, make, model, year):
    super().__init__(color, make, model, year)
  def drive(self):
    print(f'The {self.color} {self.model} drives past. Revvvvvvvvv!"')
  def turn(self, direction):
    print(f"The {self.color} {self.make} {self.model} smoothly turns {direction}.")
  def stop(self):
    print(f'The {self.model} loudly stops')
        
class Boat(Vehicle):
  def __init__(self, color, make, model, year):
    super().__init__(color, make, model, year)
  def drive(self):
    print(f'The {self.color} {self.model} drives past. Purrrrrrrr!"')
  def turn(self, direction):
    print(f"The {self.color} {self.make} {self.model} struggles to turn {direction}.")
  def stop(self):
    print(f'The {self.make} {self.model} boat stops')
      
class Moped(Vehicle):
  def __init__(self, color, make, model, year):
    super().__init__(color, make, model, year)
  def drive(self):
    print(f'The {self.color} moped drives past. Beep beep!"')
  def turn(self, direction):
    print(f"The {self.color} moped sharply turns {direction}.")
  def stop(self):
    print(f'The {self.make} {self.model} moped slowly stops')


# Car
car = Car("yellow","Toyota", "Camry", "2021")
print(car.make)
print(car.drive())
print(car.turn("left"))
print(car.stop())

# Bus
bus = Bus("black", "Volvo", "9700 Double Decker", "2024")
print(f'{bus.make} {bus.model}')
print(bus.drive())
print(bus.turn("right"))
print(bus.stop())

# Truck
truck = Truck("grey", "Ford", "F-150", "2024")
print(f'{truck.make} {truck.model}')
print(truck.drive())
print(truck.turn("right"))
print(truck.stop())

# Boat
boat = Boat("white", "Beneteau", "Oceanis 46.1", "2023")
print(f'{boat.make} {boat.model}')
print(boat.drive())
print(boat.turn("right"))
print(boat.stop())

# Moped
moped = Moped("teal", "Buddy", "50", "2010")
print(f'{moped.make} {moped.model}')
print(moped.drive())
print(moped.turn("right"))
print(moped.stop())
