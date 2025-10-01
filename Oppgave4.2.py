"""Oppgave 4.2
Lag en funksjon som leser filene i Files og sorterer dem i undermapper
basert p˚a filtype:
• Opprett en ny mappe kalt SortedFiles
• Opprett undermapper kalt txt-files, csv-files, og log-files inne
i denne mappen kalt SortedFiles.
• Flytt filene fra Files til riktig undermappe i SortedFiles basert p˚a
deres filtype.
SortedFiles
|-- csv
| |-- vPcaO7jR .csv
| ‘-- 7 NMaq7aa .csv
|-- log
| ‘-- 1 Vgi2jbe .log
‘-- txt
|-- G5zLehz4 .txt
‘-- iTwTrTkU .txt
3 directories , 5 files"""

"""Forklaring: 1- Denne koden er storsett samme som forrige oppgave koden.2- De som ble lagt til er shutil bibioteket som sortere filer, definere kildemappe og lage undermappe. 3- Opprettlse av hovedmappe og kildemappe.
  4- Går gjennom alle filer i hovedmappe, flytt filene til riktig undermappe i sortertefiler 5- Kjører koden og skrive en bekreftelse. """



import os
import random
import string
import shutil

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

def sorter_filer_etter_filtype():
    kilde_mappe = "Mohammad Hoori"
    sortert_mappe = "sortertfiler"

    undermapper = {
        '.txt': 'txt-filer',
        '.csv': 'csv-filer',
        '.log': 'log-filer'
    }

    os.makedirs(sortert_mappe, exist_ok=True)

    for undermappe in undermapper.values():
        os.makedirs(os.path.join(sortert_mappe, undermappe), exist_ok=True)

    for filnavn in os.listdir(kilde_mappe):
        full_kildebane = os.path.join(kilde_mappe, filnavn)
        if os.path.isfile(full_kildebane):
            _, filtype = os.path.splitext(filnavn)
            if filtype in undermapper:
                destinasjonsmappe = os.path.join(sortert_mappe, undermapper[filtype])
                full_destinasjonsbane = os.path.join(destinasjonsmappe, filnavn)
                shutil.move(full_kildebane, full_destinasjonsbane)


opprett_tilfeldige_filer()
sorter_filer_etter_filtype()
print("Filer er opprettet og sortert i 'sortertfiler'.")
