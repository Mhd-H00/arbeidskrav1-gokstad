"""Oppgave 2.6
Konverter datasettet fra Oppgave 2.2 til en liste av dictionaries med formatet:
{"navn": "Cecilie", "alder": 28}
4"""

"""Forklaring: zip kompinere to lister, [] lager liste dictionaries"""



navn = ['Cecilie', 'Bjørn', 'Tor', 'Anna']
alder = [28, 30, 24, 25]


liste_dict = [{"navn": n, "alder": a} for n, a in zip(navn, alder)]
print(liste_dict)
