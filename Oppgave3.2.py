"""Oppgave 3.2
Lag en funksjon som tar inn to datoer som strenger p˚a formatet “dd/mm/yyyy”
og returnerer antall dager mellom dem. Hvis den første datoen er senere enn
den andre, skal funksjonen fortsatt returnere antall dager (positivt tall).
Eksempel:
Input: "21/11/2024", "01/01/2024" → Output: 325 dager"""

"""Forklaring:!- 1- Vi importere først datetime module. 2- Vi definere funksjon. 3- Definere dato format.4- strptime konvertere teksten til dato format. 4- Retutn abs trekker en dato fra andre dato.
 5- Gir beskjed til brukeren når brukeren skrive inn en feil dato eller feil format. 6- 
 Spurte AI om forskjellen mellom type[int]: og int | None: Svarer at det er mer riktig og vanlig
 å breuke INT | NONE: typehint som sier at funksjonen kan retunere enten et helltal eller ingenting"""


from datetime import datetime


def antall_dager_mellom(dato1: str, dato2: str) -> int | None:
    format = "%d/%m/%Y"
    try:
        d1 = datetime.strptime(dato1, format)
        d2 = datetime.strptime(dato2, format)
        return abs((d1 - d2).days)
    except ValueError:
        print("Feil: Datoene må være på formatet 'dd/mm/yyyy' og være gyldige.")
        return int


# Brukeren input og funksjon kalling
if __name__ == "__main__":
    dato1 = input("Skriv inn første dato (dd/mm/yyyy): ")
    dato2 = input("Skriv inn andre dato (dd/mm/yyyy): ")

    dager = antall_dager_mellom(dato1, dato2)
    if dager is not int:
        print(f"Antall dager mellom {dato1} og {dato2} er: {dager} dager.")





