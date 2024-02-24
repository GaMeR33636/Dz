class Animal:
  def __init__(self, name):
      self.name = name

  def speak(self):
      return f"{self.name} makes a sound."

class Bird:
  def __init__(self, name):
      self.name = name

  def fly(self):
      return f"{self.name} can fly."

class Parrot(Animal, Bird):
  def __init__(self, name, color):
      super().__init__(name)
      self.color = color

  def speak(self):
      return f"{self.name} says '{self.name} wants a cracker!'"

parrot1 = Parrot(input("Введіть ім'я птаха: "),"green")

print(parrot1.speak())
print(parrot1.fly())   

