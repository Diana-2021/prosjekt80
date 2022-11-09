from DAT_120.Oving10.avtale import *
from DAT_120.Oving10.sted import *

#c

class Kategori:
    def __init__(self,id,navn,prioritet=1):
        self.id=id
        self.navn=navn
        self.prioritet = prioritet


#c
    def __str__(self):
        return f"{self.id}, {self.navn},{self.prioritet}"


#d
def leser_ny_kategori():
    user_id=input("Skriv inn id:")
    user_navn=input("skriv inn ditt navn:")
    user_perioritet=input("skriv inn prioritet for kategorien: ")

    ny_kategori=Kategori(user_id,user_navn,user_perioritet)
    return ny_kategori


#e
def write_kategori(lister):
    with open("kategori.txt", mode="w")as fila:
        fila.write("id ; navn; perioritet")
        for k in lister:
            fila.write(f"\n{k.id};{k.navn};{k.prioritet}")


def lese_fila():
    lister = []
    fila = open ("kategori.txt", "r")
    next(fila)
    for linje in fila:
        linje = linje.strip()
        linje = linje.split(";")
        id = linje[0].strip()
        navn= linje[1].strip()
        prioritet=linje[2].strip()
        lister.append(Kategori(id,navn,prioritet))
        #print(linje)
    fila.close()
    return lister



#f
def skriveut_kat_liste(lister,tittel = "avtaleliste"):
    print(tittel)
    for i in lister:
        objekt = lister[i]
        print(f"{i},{objekt}")

