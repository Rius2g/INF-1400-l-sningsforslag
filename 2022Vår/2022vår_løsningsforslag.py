import random


'''
Hadde ikke noe prekode, så vi anntok at varebil = x2 personbil størrelse og at alle biler til enhver tid (utenom skapelse) skal tilhøre en garasje
Dermed flytter vi bilen til en annen garasje hvis den ikke har en garasje
Bruker arv ved å lage bil, eneste forskjell mellom person og varebil er størrelsen (x2)
Bruker ikke polymorfi ettersom 0 prekode og aner ikke hva vi egentlig endrer på
'''
class Bil:
    def __init__(self, Størrelse, Garasje):
        self.Størrelse = Størrelse
        self.Garasje = Garasje

    
    def FlyttBil(self, Garasjer):
        if self.Garasje != None:  
            self.Garasje.KjørUt(self)
        for garasje in Garasjer:
            if garasje == self.Garasje:
                continue
            elif garasje.parker(self):
                self.Garasje = garasje
        if self.Garasje != None:
            self.Garasje.parker(self)
        else:
            print("Ingen ledige garasjer")



class Garasje:
    def __init__(self, størrelse ):
        self.GjenståendePlass = størrelse
        self.BilerIGarasjen = []


    def parker(self, bil):
        if self.GjenståendePlass >= bil.Størrelse:
            self.BilerIGarasjen.append(bil)
            self.GjenståendePlass -= bil.Størrelse
            print(f"Garasjen har nå {self.GjenståendePlass} plass igjen")
            return True


    def KjørUt(self, bil):
        self.BilerIGarasjen.remove(bil)
        self.GjenståendePlass += bil.Størrelse




class Personbil(Bil):
    def __init__(self):
        super().__init__(4, None)




class Varebil(Bil):
    def __init__(self):
        super().__init__(8, None)




if __name__ == "__main__":
    garasjer = []
    for _ in range(5):
        garasjer.append(Garasje(random.randint(45, 75)))

    for _ in range(30):
        bil = None
        if random.randint(0, 1):
            bil = Personbil()
        else:
            bil = Varebil()
        for garasje in garasjer:
                if garasje.parker(bil):
                    bil.Garasje = garasje
                    break


    




