class Human:
  def __init__(self, name, age):
      self.name = name
      self.age = age

  def drive_car(self, car):
      print(f"{self.name} is driving {car.make}.")

class Car:
  def __init__(self, make, year):
      self.make = make
      self.year = year

  def honk(self):
      print("Beep! Beep!")


john = Human(input("Введіть ім'я  "),input("Введіть вік  "))
car = Car(input("Введіть марку авто  "), 2022)

john.drive_car(car)  
car.honk()          
