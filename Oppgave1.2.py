"""Skriv et program som ber brukeren skrive inn to setninger. Programmet
skal deretter sammenligne lengden p˚a de to setningene og skrive ut hvilken
som er lengst og antall karakterer det er i denne setningen."""

"""Forklaring:

Jeg brukt ai for å finne riktig funksjon som jeg kan bruke: Prompt(Hvilken funksjon i python hjelper med å telle bokstav?) isalpha
 (innebygd funksjon som sjekker om tegn er bokstav eller ikke).
Vi brukte 1 i sum i for løkke for å fortelle koden at du skal telle en hvergang du ser en bokstav."""


setning1 = input("Skriv inn første setning:")
setning2 = input("SKriv inn andre setning:")

antall_bokstav1 = sum(1 for tegn in setning1 if tegn.isalpha())
antall_bokstav2 = sum(1 for tegn in setning2 if tegn.isalpha())

if antall_bokstav1 > antall_bokstav2:
    print(f"Setning 1 har flere bokstaver ({antall_bokstav1}) enn setning 2 ({antall_bokstav2})")
elif antall_bokstav1 < antall_bokstav2:
    print(f"Setning 2 har flere bokstaver ({antall_bokstav2}) enn setning 1 ({antall_bokstav1})")
else:
    print(f"Begge setningene har like mange bokstaver ({antall_bokstav1})")