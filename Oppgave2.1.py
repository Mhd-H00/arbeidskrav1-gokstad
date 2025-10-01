"""Datastrukturer
Oppgave 2.1
Skriv et program som leser inn en dato i formatet “dd/mm/yyyy” fra
brukeren. Programmet skal deretter sjekke om datoen er gyldig. Hvis datoen
er ugyldig, skal programmet skrive en passende feilmelding.

## Forklaring Spurt ai om dato og tid metoder i python. Den som har brukt er strptime det finnes
andre metoder og muligheter også
1-Vi importere datetime.
2-Skrive input
3-Vi bruker try og except som en lettelse for feil håndtering"""

from datetime import datetime

dato_str = input("Skriv inn dato (dd/mm/yyyy):")
try:
    datetime.strptime(dato_str, "%d/%m/%Y")
    print("Datoen er gyldig.")
except ValueError:
    print("Ugyldig dato eller format. Bruk dd/mm/yyyy.")
