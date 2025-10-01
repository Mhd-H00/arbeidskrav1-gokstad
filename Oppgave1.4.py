"""Lag et program som bytter plass p˚a to elementer i en gitt liste. Programmet
skal ta utgangspunkt i følgende liste:
fruits = ["eple", "banan", "appelsin", "drue", "kiwi"]
1. Be brukeren om ˚a skrive inn to indekser (input) som angir hvilke
elementer i listen som skal bytte plass
2. Bytt plass p˚a elementene som ligger p˚a de angitte indeksene
3. Skriv ut den oppdaterte listen
Hvis en eller begge indeksene er ugyldige (ikke i listen), skal programmet gi
en passende feilmelding

## Forklaring: 1- Vi prine ut liste før oppdatering. 2- Vi skrive input som sjekker første og andre indekse.
3- Første if sjekker om begge er et tall med isdigit innbygd funksjon. 4- Den andre if sjekker om tallene er innenfor 0-4.
"""

fruits = ["eple", "banan", "appelsin", "drue", "kiwi"]
print("Liste før oppdatering:", fruits)


indeks1 = input("Skriv inn første indeks (0-4): ")

indeks2 = input("Skriv inn andre indeks (0-4): ")


if indeks1.isdigit() and indeks2.isdigit():
    indeks1 = int(indeks1)
    indeks2 = int(indeks2)


    if 0 <= indeks1 < len(fruits) and 0 <= indeks2 < len(fruits):
        fruits[indeks1], fruits[indeks2] = fruits[indeks2], fruits[indeks1]
        print(" Oppdatert liste:", fruits)
    else:
        print("Indeksene må være mellom 0 og 4.")
else:
    print("Du må skrive inn gyldige tall.")


