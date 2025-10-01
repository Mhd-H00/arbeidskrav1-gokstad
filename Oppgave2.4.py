"""Skriv et program som sorterer denne dictionary etter alder hvor den eldste
skal være først. Skriv ut resultatet

forklaring kilde er oppgavene uke 35 veiledere har forklart"""



navn_alder = {
    "Cecilie": 28,
    "Bjørn": 30,
    "Tor": 24,
    "Anna": 25
}


sortert = dict(sorted(navn_alder.items(), key=lambda x: x[1], reverse=True))
for navn, alder in sortert.items():
    print(f"{navn} er {alder} år")
