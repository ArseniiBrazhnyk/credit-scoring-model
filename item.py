class Item:
    def __init__(self, nazwa, cena_zakupu, cena_brutto, vat):
        self.nazwa = nazwa
        self.cena_zakupu = cena_zakupu
        self.cena_brutto = cena_brutto
        self.vat_procent = vat
        self.vat_zlotych = round(cena_brutto / (1 + self.vat_procent/100), 2)

    def __str__(self):
        return self.nazwa + ";" + str(self.cena_zakupu) + ";" + str(self.cena_brutto) + ";" + str(self.vat_zlotych)

    def toString(self):
        return self.nazwa + ";" + str(self.cena_zakupu) + ";" + str(self.cena_brutto) + ";" + str(self.vat_zlotych)