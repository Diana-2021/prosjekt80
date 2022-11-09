from DAT_120.Oving10.sted import *
from DAT_120.Oving10.kategori import *


from datetime import datetime


#d
data_objekt = datetime.fromisoformat('1950-04-26')
data_objekt1 = datetime.fromisoformat('1960-05-30')
data_objekt2 = datetime.fromisoformat('1970-09-14')


class Avtale:

    def __init__(self, title, sted, starttidspunkt,varighet, id):
        self.title = str(title)
        self.sted = str(sted)
        self.starttidspunkt = starttidspunkt
        self.varighet = int(varighet)
        self.id=id
        self.kategori_liste=()

#e
    def __str__(self):
        return f'{self.title}, {self.sted}, {self.starttidspunkt}, {self.varighet},{self.id}'


#k    >> øving 10
    def legge_til_kategori(self,kategori):
        return self.kategori_liste.append(kategori)



def legg_kat_til_avtale(index_k):
    kategori_lista=()
    for i in range (kategori_lista):
        index_k=int(input("hvilken kategori vil du legge inn?"))
        if index_k !=kategori_lista:
            kategori_lista.append(index_k)




#f            # n  øving 10
def ny_avtale():

    while True:
        try:
            ny_title = input('skriv inn title for  avtalen: ')
            ny_starttidspunkt = datetime.fromisoformat(input('Starttid (ÅÅÅÅ-MM_DD TT:MM:SS ):'))
            ny_varighet = int(input('skrive in varighet: '))
            ny_id = int(input('skrive din id: '))
            print("velg stedet fra listen under ")
            sted_liste=skriveut_liste_steder()
            if.......
            avtale2 = Avtale(ny_title,sted_liste,ny_starttidspunkt, ny_varighet,ny_id)
            break
        except ValueError:
            print('feil input. prøv igjen')
    return avtale2



#g
def skriveut_liste(lister):
    for i in range(len(lister)):
        print(i, lister[i])



#h       #l >>> øving 10
def write_liste(lister, navn ="text.txt"):
    with open(navn, mode="w")as fila:
        fila.write("title ; sted ;starttidspunkt ; varighet ; id" )
        for avtale_id in lister:
            avtale = lister[avtale_id]
            streng = fila.write(f"\n{avtale.id};{avtale.title};{avtale.sted.id};{avtale.starttidspunkt};{avtale.varighet}")
            for kategori in avtale.kategorier:
                streng+=str(kategori.id)+ ","
            streng= streng.strip(",")
            streng += "/n"
            fila.write(streng)



#i           #l >>> øving 10
def read_file():
    lister = []
    fila = open ("text.txt", "r")
    next(fila)
    for linje in fila:
        linje = linje.strip()
        linje = linje.split(";")
        title = linje[0]
        sted = linje[1]
        starttidspunkt = datetime.fromisoformat(linje[2])
        varighet = linje[3]
        lister.append(Avtale(title,sted,starttidspunkt,varighet))
        #print(linje)
    fila.close()
    return lister



#j
def sjekkdato(liste,dato):
    avtaler_på_sammedato =[]
    for avtaler in liste:
        if avtaler.starttidspunkt == dato:
            avtaler_på_sammedato.append(avtaler)
        return avtaler_på_sammedato



#k
def sjekkstring(liste, string1) :
    avtaler_tittle_str = []
    for avtaler in liste:
        if avtaler.title.find(string1) != -1:
            avtaler_tittle_str.append(avtaler)
    return avtaler_tittle_str

List = []



def meny_system():
    global List
    kategori_liste=list()        #m øving10
    sted_liste=list()            #m Øving10
    meny_valg = List
    while True:
        print(' Velg en av de alternativer:\n a.lese inn avtaler fra fil\n'
              ' b.Skrive avtalene til fil\n c.Skrive inn en ny avtale\n'
              ' d.Skrive ut alle avtalene\n e.slett en avtale\n '
              'f.rediger en avtale\n g.legge til kategori til systemet\n'
              'h.legge til sted til systemet \n i.Avslutt')

        brukeren_valg = input('velg en av de alternativer:')
        if brukeren_valg == 'a':
            print('du har valgt a')
            List = read_file()
        elif brukeren_valg == 'b':
            print('du har valgt b')
            write_liste(List)
        elif brukeren_valg == 'c':
            print('du har valgt c')
            List.append(ny_avtale())
        elif brukeren_valg == 'd':
            print('du har valgt d')
            skriveut_liste(List)
        elif brukeren_valg == 'e':
            skriveut_liste(List)
            valg_slett = int(input('hvilken avtalen har du lyst å slette.Skriv indexen til avtale:'))
            List.pop(valg_slett)
            print(meny_valg)
        elif brukeren_valg =='f':
            print('du har valgt f')
            rediger_avtale()
        elif brukeren_valg== 'g':              # m  øving10
            print('du har valgt g')
            kategori_liste.append(leser_ny_kategori())
        elif brukeren_valg== 'h':             #m Øving 10
            print('du har valgt h')
            sted_liste.append(les_nyt_sted())
        else:
            if brukeren_valg == 'i':
                print('avsluet')
                break


#n
def rediger_avtale():
    skriveut_liste(List)
    valg = int(input("Velg avtale å redigere"))
    List[valg] = ny_avtale()
    return skriveut_liste(List)


meny_system()

