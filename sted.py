from DAT_120.Oving10.avtale import *
from DAT_120.Oving10.kategori import *


class Sted:
    def __init__(self,id,navn,addresse=None,gateadrs=None,postnm=None,poststed=None):
        self.id=id
        self.navn=navn
        self.addresse=addresse
        self.gateadrs=gateadrs
        self.postnm=postnm
        self.poststed=poststed


    def __str__(self):
        return f'{self.id},{self.navn},{self.addresse},{self.gateadrs},{self.postnm},{self.poststed}'


#h
def les_nyt_sted():
    user_id=input("Skriv inn id:")
    user_navn=input("skriv inn ditt navn:")
    user_addresse=input("skriv inn hele addressen din: ")

    ny_sted=Sted(user_id,user_navn,user_addresse)
    return ny_sted



#i
def write_sted(lister):
    with open("sted.txt", mode="w")as fila:
        fila.write("id ; navn; addresse")
        for sted in lister:
            fila.write(f"\n{sted.id};{sted.sted};{sted.addresse}")



def lese_sted_fil():
    lister = []
    fila = open("sted.txt", "r")
    next(fila)
    for linje in fila:
        linje = linje.strip()
        linje = linje.split(";")
        id = linje[0].strip()
        navn = linje[1].strip()
        addresse = linje[3].strip()
        lister.append(Sted(id,navn,addresse))
    fila.close()
    return lister




#j
def skriveut_liste_steder(lister):
    for i in range(len(lister)):
        print(i, lister[i])



