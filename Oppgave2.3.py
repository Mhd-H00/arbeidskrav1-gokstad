"""Oppgave 2.3
Ta utgangspunkt i listene fra Oppgave 2.2 og lag en dictionary der tekstverdier
fra listen med navn blir nøkler og tallverdiene fra listen med alder blir
verdier. Skriv ut innholdet av denne dictionary p˚a formatet:
"Cecilie er 25 ˚ar"
"Bjørn er 30 ˚ar"""

"""forklaring: AI .Hva kan ZIP som innbygd funksjon kan gjøre? ZIP kan koble sammen
 elementer fra to eller mer lister og spurt også om forklaring om personer.items(metode som
 retunerer alle verdi nøkkel parene som en liste"""




navn_alder = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

navn = navn_alder[::2]
alder = navn_alder[1::2]


personer = dict(zip(navn, alder))

for n, a in personer.items():
    print(f"{n} er {a} år")
