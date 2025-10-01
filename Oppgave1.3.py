"""#%% md
## Oppgave 1.3
Oppgave 1.3
Lag et program som ber brukeren skrive inn et tall og genererer multiplikasjonstabellen
for dette tallet (fra 1 til 10). Eksempel:
Input: 3
Output:
3 * 1
3 * 2
3 * 3
Osv..
## Forklaring:
Vi be brukeren å skrive tallet med int(input fordi det er ett tall og ikke bokstave. i for løkke skriver vi fra 1 til 11 og ikke til 10 dan den funksjon (range) inkludere start men ikke stopp."""




tall = int(input("Skriv inn ett tall så finner jeg muktiplikasjonstabellen til tallet:"))
for i in range(1, 11):
    print(f"{tall} X {i} = {tall * i}")
