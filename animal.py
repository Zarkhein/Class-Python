from unicodedata import name


class Animal:
    def __init__(self, name):
        self.name = name
    
    def showInfo(self):
        print("Je suis: " + self.name)
    
    def move(self):
        print(self.name + ":  chasse...")
    

class Cat(Animal):
    def __init__(self, voix, name):
        super().__init__(name)
        self.voix = voix
    
    def miole(self):
        print("Attention! "+ self.voix)
    
    def jump(self):
        print("Attention!" + self.name + " a encore sauter!")
    
class Dog(Animal):
    def __init__(self, name, voix):
        super().__init__(name)
        self.voix = voix

    def Aboie(self):
        print("Attention! " + self.voix)

    def sleep(self):
        print(self.name + " dors toujours...")
        

Maurice = Cat("Miaou", "Maurice")
Maurice.jump()
Maurice.showInfo()
Maurice.miole()

Albert = Dog("Albert", "Waouf")
Albert.showInfo()
Albert.Aboie()
Albert.move()
Albert.sleep()
        