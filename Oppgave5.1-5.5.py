import csv
from collections import Counter

# Les inn CSV-filen og filtrer gyldige rader
gyldige_rader = []
with open('bokutlaan.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for rad in reader:
        try:
            rad['Forlenget'] = int(rad['Forlenget'])
            rad['Låneperiode'] = int(rad['Låneperiode'])
            gyldige_rader.append(rad)
        except (ValueError, KeyError):
            # Hopp over rader med ugyldige eller manglende data
            continue

# ...existing code until feilmeldinger...

# Oppgave 5.1: Summen av forlenget dager..
total_forlenget = sum(rad['Forlenget'] for rad in gyldige_rader)
print(f"\nOppgave 5.1:")
print(f"Totalt antall dager lånene ble forlenget: {total_forlenget}")


# Oppgave 5.2: bøker per sjanger...
def tell_boker_per_sjanger():
    sjanger_dict = {}
    for rad in gyldige_rader:
        sjanger = rad['Sjanger']
        sjanger_dict[sjanger] = sjanger_dict.get(sjanger, 0) + 1
    return sjanger_dict


print(f"\nOppgave 5.2:")
for sjanger, antall in tell_boker_per_sjanger().items():
    print(f"{sjanger}: {antall}")


# Oppgave 5.3: gjenneomsnittlig av låneperioden....
def beregn_gjennomsnitt_laneperiode():
    total_dager = sum(rad['Låneperiode'] + rad['Forlenget'] for rad in gyldige_rader)
    return total_dager // len(gyldige_rader) if gyldige_rader else 0


print(f"\nOppgave 5.3:")
print(f"Gjennomsnittlig låneperiode: {beregn_gjennomsnitt_laneperiode()} dager")


# Oppgave 5.4: Bøker som ble ikke retunert...
def finn_ikke_returnerte_boker():
    ikke_returnert = []
    for rad in gyldige_rader:
        if rad['Tilbakelevert'].strip().lower() == 'nei':
            ikke_returnert.append({
                'bok': rad['Boktittel'],
                'låner': f"{rad['Fornavn']} {rad['Etternavn']}"
            })
    return ikke_returnert


print(f"\nOppgave 5.4:")
for bok in finn_ikke_returnerte_boker():
    print(f"Bok: {bok['bok']}, Låner: {bok['låner']}")


# Oppgave 5.5: Mest lånte bøker...
def finn_mest_lante_boker():
    bok_teller = Counter()
    for rad in gyldige_rader:
        bok_teller[rad['Boktittel']] += 1


    max_count = max(bok_teller.values())

    # Finner alle bøker som maks lånet ut....
    mest_lante = [(bok, antall) for bok, antall in bok_teller.items()
                  if antall == max_count]

    # Sortere alfabetisk
    return sorted(mest_lante, key=lambda x: x[0])


print(f"\nOppgave 5.5:")
mest_lante = finn_mest_lante_boker()
for bok, antall in mest_lante:
    print(f"Bok: {bok}, Antall utlån: {antall}")