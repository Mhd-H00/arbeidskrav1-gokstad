"""Ta utgangspunkt i en liste der tekst og tall er plassert parvis med navn og
alder slik:
["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]
Skriv et program som splitter denne listen i to separert lister, en liste for
navn og en liste for alder.

forklaring: Dette er et eksempel på data slicing. [::2] går gjennom hele listen
0 og hver andre elemet [1::2] starte fra første inddex og gjennom hele listen hver andre element også """

navn_alder = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

navn = navn_alder[::2]
alder = navn_alder[1::2]

print(navn)
print(alder)