#d

from datetime import datetime
data_objekt = datetime.fromisoformat('1950-04-26')
data_objekt1 = datetime.fromisoformat('1960-05-30')
data_objekt2 = datetime.fromisoformat('1970-09-14')
class Avtale:

    def __init__(self, title, sted, starttidspunkt,varighet):
        self.title = str(title)
        self.sted = str(sted)
        self.starttidspunkt = starttidspunkt
        self.varighet = int(varighet)

#e
    def __str__(self):
        return f'avtalen title er: {self.title} \navtalen sted er: {self.sted} \navtelen satrtpunkt er: {self.starttidspunkt} \navtalen varighet er: {self.varighet} '

#f
def ny_avtale():
    while True:
        try:
            ny_title = input('skriv inn title for  avtalen: ')
            ny_sted = input('i hvilket by tok avtalen sted : ')
            ny_starttidspunkt = datetime.fromisoformat(input('Starttid (ÅÅÅÅ-MM_DD TT:MM:SS ):'))
            ny_varighet = int(input('skrive in varighet: '))
            avtale2 = Avtale(ny_title, ny_sted, ny_starttidspunkt, ny_varighet)
            break
        except ValueError:
            print('feil input. prøv igjen')
    return avtale2

#g
def skriveut_liste(lister):
    for i in range(len(lister)):
        print(i, lister[i])

#h
def lager_liste(lister):
    with open("text.txt", mode="w")as fila:
        fila.write("title ; sted ; starttidspunkt ; varighet ")
        for avtale in lister:
            fila.write(f"\n{avtale.title} ; {avtale.sted}; {avtale.starttidspunkt}; {avtale.varighet}")

#i
def lese_filliste():
    lister = []
    fila = open ("text.txt", "r")
    for linje in fila:
        linje = linje.strip()
        linje = linje.split(";")
        title = linje[0]
        sted = linje[1]
        starttidspunkt = linje[2]
        varighet = linje[3]
        lister.append(title)
        lister.append(sted)
        lister.append(starttidspunkt)
        lister.append(varighet)
        print(linje)
    fila.close()
    return lister

#j
def sjekkdato(liste, dato) :
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


if __name__== '__main__':
    avtale = Avtale('saiksbiko', 'London', data_objekt , 50 )
    print(avtale)
    print(ny_avtale())
    enListe = [Avtale('Gineve', 'Italy', data_objekt, 59)]
    toList = [Avtale('Oavtale', 'Oslo', data_objekt1, 40)]
    treListe = [Avtale('Belfor', 'Britin', data_objekt2, 89)]
    fireListe = [Avtale('Saiksbiko', 'USA', data_objekt, 120)]
    List = enListe+toList+treListe+fireListe
    skriveut_liste(List)
    lager_liste(List)
    lese_filliste()
    sjekkdato(enListe, data_objekt)
    sjekkstring(enListe,'Gineve')

