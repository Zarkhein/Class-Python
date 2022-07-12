from dis import dis
from random import*
import this
from turtle import distance

class voiture:
    "Def d'une voiture"
    def __init__(self, moteur, roue, prix, kilometre, reservoirActuel, reservoirMax):
        self.moteur = moteur
        self.roue =  roue
        self.prix = prix
        self.kilometre = kilometre
        self.reservoirActuel = reservoirActuel
        self.reservoirMax = reservoirMax

    def setReservoirActuel(self, reservoirActuel):
        self.reservoirActuel = reservoirActuel
    def getReservoirActuel(self):
        return self.reservoirActuel
    
    def setKilometre(self, kilometre):
        self.kilometre = kilometre
    def getKilometre(self):
        return self.kilometre

    def deplacement2(self, kilo1, kilo2):
        distanceParcouru = randint(kilo1, kilo2)
        essencePerdu = distanceParcouru * 10
        print("Vroom vroom la voiture se deplace de: ", distanceParcouru, "Km")
        self.kilometre += distanceParcouru
        self.reservoirActuel -= essencePerdu
        if(self.reservoirActuel <= 0):
            print("Oups vous avez plus d'essence...")
        print("Vous avez maintenant au compteur: ", self.kilometre, "Km")
        print("Il vous reste: ", self.reservoirMax, "L /", self.reservoirActuel, "L")


    def deplacement(self, val1, val2):
        test = randint(val1, val2)
        print("Vroom vroom la voiture se deplace de: ", test, "Km")
        self.kilometre += test
        print("Vous avez maintenant au compteur: ",self.kilometre, "Km")
        

audi = voiture("500v", 4, 25000, 0, 100,100)
audi.setKilometre(500)
audi.deplacement2(0,100)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

alice = User("Alice", " alice@exmaple.com")
alice.email = "contact@alice.com"
        