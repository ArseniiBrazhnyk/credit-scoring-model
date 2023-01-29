import random

class Sklep:
    def __init__(self, nazwa, towary):
        self.nazwa = nazwa
        self.towary = towary

    def randomTowar(self):
        return self.towary[random.randrange(0, len(self.towary) - 1)]

    def randomIlosc(self, day):
        if day == 'Niedziela':
            return
        elif day == 'Sobota':
            return 70
        else: 
            return 55
    
    def createLine(self, day):
        tableOfGoods = []
        ilosc = random.randrange(15, self.randomIlosc(day))
        for x in range(0, ilosc):
            tableOfGoods.append(self.randomTowar())
        return tableOfGoods