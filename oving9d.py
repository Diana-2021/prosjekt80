#d
from datetime import datetime
data_objekt = datetime.fromisoformat('1950-05-26')


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
            ny_title = input('skriv inn title for avtalen: ')
            ny_sted = input('i hvilket by tok avtalen sted : ')
            ny_starttidspunkt = datetime.fromisoformat(input('Srarttid (ÅÅÅÅ-MM_DD TT:MM:SS ):'))
            ny_varighet = int(input('skrive in varighet: '))
            avtale2 = Avtale(ny_title, ny_sted, ny_starttidspunkt, ny_varighet)
            break
        except ValueError:
            print('feil input. prøv igjen')
    return avtale2



avtale = Avtale('saiksbiko', 'London', data_objekt , 50 )
print(avtale)
print(ny_avtale())


