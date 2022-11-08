
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

#e
    def __str__(self):
        return f'{self.title}, {self.sted}, {self.starttidspunkt}, {self.varighet},{self.id}'

#f
def ny_avtale():
    while True:
        try:
            ny_title = input('skriv inn title for  avtalen: ')
            ny_sted = input('i hvilket by tok avtalen sted : ')
            ny_starttidspunkt = datetime.fromisoformat(input('Starttid (ÅÅÅÅ-MM_DD TT:MM:SS ):'))
            ny_varighet = int(input('skrive in varighet: '))
            ny_id = int(input('skrive din id: '))

            avtale2 = Avtale(ny_title, ny_sted, ny_starttidspunkt, ny_varighet,ny_id)
            break
        except ValueError:
            print('feil input. prøv igjen')
    return avtale2



#g
def skriveut_liste(lister):
    for i in range(len(lister)):
        print(i, lister[i])



#h
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


#i
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
        lister.append(Avtale(title,sted.id,starttidspunkt,varighet))
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
    meny_valg = List
    while True:
        print(' Velg en av de alternativer:\n a.lese inn avtaler fra fil\n b.Skrive avtalene til fil\n c.Skrive inn en ny avtale\n d.Skrive ut alle avtalene\n e.slett en avtale\n f.rediger en avtale\n g.Avslutt')
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

        else:
            if brukeren_valg == 'g':
                print('avsluet')
                break


#n
def rediger_avtale():
    skriveut_liste(List)
    valg = int(input("Velg avtale å redigere"))
    List[valg] = ny_avtale()
    return skriveut_liste(List)


meny_system()



#################### :ØVING 10  #######################

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



#################################################


#g
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




#k
def legge_til_kategori(katliste):
    kategori_liste=[]






















#if __name__== '__main__':
    #avtale = Avtale('saiksbiko', 'London', data_objekt , 50 )
    #print(avtale)
    #print(ny_avtale())
    #enListe = [Avtale('Gineve', 'Italy', data_objekt, 59)]
    #toList = [Avtale('Oavtale', 'Oslo', data_objekt1, 40)]
    #treListe = [Avtale('Belfor', 'Britin', data_objekt2, 89)]
    #fireListe = [Avtale('Saiksbiko', 'USA', data_objekt, 120)]
    #List = enListe+toList+treListe+fireListe
    #skriveut_liste(List)
    #lager_liste(List)
    #lese_filliste()
    #sjekkdato(enListe, data_objekt)
    #sjekkstring(enListe,'Gineve')

#l#m#n
