"""Oppgave 1.5
Utvid Oppgave 1.3 slik at brukeren kan angi et intervall [m, n] i stedet for
1-10, og programmet skriver ut en pent formatert tabell for tallet i hele
intervallet.
| 1 | 2 | 3 |
|---|---|---|
| 1 | 2 | 3 |
| 2 | 4 | 6 |
| 3 | 6 | 9 |


## Forklaring: Kilde er oppgave hjelp 01.09.2025."""

m = int(input("Skriv starttall: "))
n = int(input("Skriv sluttall: "))


def get_len(v):
    return len(str(v))


header = "|"

for i in range(m, n + 1):
    if get_len(i) >= 2:
        header += f"  {i} |"
    else:
        header += f"   {i} |"
print(header)

split = "|"
for i in range(m, n + 1):
    split += f"-----|"
print(split)

for i in range(m, n + 1):
    rad = "|"
    for j in range(m, n + 1):
        v = j + i
        if get_len(v) >= 2:
            rad += f"  {v} |"
        else:
            rad += f"   {v} |"
    print(rad)
