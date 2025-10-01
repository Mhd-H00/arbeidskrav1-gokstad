"""Oppgave 4.1
Lag en funksjon som oppretter en mappe kalt Files og genererer 30 tilfeldige
filer med følgende filtyper i denne mappen: .txt, .csv, og .log. Hver fil
skal ha:
• Et tilfeldig navn med mellom 5 og 10 tegn.
• En tilfeldig filtype valgt fra de tre typene.
• Innhold i disse filen er ikke viktig—lag gjerne disse filene uten innhold
Files
|-- G5zLehz4 .txt
|-- iTwTrTkU .txt
|-- vPcaO7jR .csv
|-- 1 Vgi2jbe .log
‘-- 7 NMaq7aa .csv
0 directories , 5 files"""


"""Forklaring:1- Importere viktig bibbiotekene (OS) gir tilgang til windos funksjoenr. (random) generere tilfeldig tall og bokstave. (string) hjelper med tekst-konstanter bokstaver og tall.
  -2 definere oppretelse funksjon (den som opprette 40 filer), mappe navn sjekker hvis den finnes fra før, exit_ok kode krasje ikke hvis mappe med samme navn finnes fra før 3- Definere filtyper.
   4- For løkke genererer filer navn fra 5-10 bokstav og tall 5- filtype.random velge tilfeldig type på de filene som skal oppretes. 6- Kombinere mappenavn filnavn og full filsti(full path).
   7- Åpne filen for skriving (with open(full_filbane, 'w') as f: pass) lukken den uten å skrive noe. 8- Siste sterg kjøre funksjon."""





import os
import random
import string

def opprett_tilfeldige_filer():
    mappe_navn = "Mohammad Hoori"
    os.makedirs(mappe_navn, exist_ok=True)


    filtyper = ['.txt', '.csv', '.log']

    for _ in range(30):
        lengde = random.randint(5, 10)
        filnavn = ''.join(random.choices(string.ascii_letters + string.digits, k=lengde))


        filtype = random.choice(filtyper)
        full_filbane = os.path.join(mappe_navn, filnavn + filtype)

        with open(full_filbane, 'w') as f:
            f.write("Denne filen er for test og er ikke viktig.")
            pass


opprett_tilfeldige_filer()

