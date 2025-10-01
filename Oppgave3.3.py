"""I dataprogrammering brukes fargekoder ofte for˚a representere farger i brukergrensesnitt
og grafikk. To vanlige m˚ater ˚a representere farger p˚a er:
1. Hex-kode: En fargekode som starter med # og best˚ar av seks tegn
som representerer de røde, grønne og bl˚a komponentene i fargen (for
eksempel #CD5C5C). Hver komponent har to tegn (heksadesimalt),
hvor:
• CD representerer rødt (r),
• 5C representerer rødt (g), og
• 5C representerer bl˚att (b),
2. RGB-kode: En fargekode representert som tre heltall, ´en for hver
fargekomponent (rød, grønn, bl˚a). For eksempel: rgb(205, 92, 92).
Lag en funksjon rgb to hex som tar inn tre heltall (for eksempel red=205,
green=92, blue=92) og returnerer tilsvarende Hex-kode som en streng (for
eksempel "#CD5C5C"). Legg ogs˚a til passende feilmelding om red, blue eller
green parametere har ugyldig verdi."""

"""Forklaring:1- Definere funksjon. 2- zip kombinere verdiene med navn. 3- Isinstance sjekker at verdin er et heltall. 4-  """



def rgb_to_hex(rødt, grønn, blått):

    for verdi, navn in zip((rødt, grønn, blått), ("rødt", "grønn", "blått")):
        if not isinstance(verdi, int) or not (0 <= verdi <= 255): # 4- sikre at verdien er innen gyldig rgb område. Ved fiel retunere feilmelding.
            return f"Ugyldig verdi for {navn}: {verdi}. Må være et heltall mellom 0 og 255."

#4- formater to sifre hexadecimal.
    return "#{:02X}{:02X}{:02X}".format(rødt, grønn, blått)

# print ut resultat.
print(rgb_to_hex(205, 92, 92))  # Output: #CD5C5C
print(rgb_to_hex(300, 92, 92))  # Output: Ugyldig verdi for red: 300. Må være et heltall mellom 0 og 255.

