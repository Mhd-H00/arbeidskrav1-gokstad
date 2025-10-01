"""Oppgave 2.5
Ta utgangspunktet i dictionary som er sortert p˚a navn i Oppgave 2.4 og
lag en ny liste med disse verdiene slik at listen f˚ar samme format som den i
Oppgave 2.2, men sortert p˚a navn.
["Anna", 25, "Bjørn", 30, "Cecilie", 28, "Tor", 24]"""
"""Forklaring sorted som innbygd funksjon i python hjelpe med å sortere elementer i dict"""



navn_alder = {
    "Bjørn": 30,
    "Cecilie": 28,
    "Anna": 25,
    "Tor": 24
}


sortert_liste = sorted(navn_alder.items())

print(sortert_liste)