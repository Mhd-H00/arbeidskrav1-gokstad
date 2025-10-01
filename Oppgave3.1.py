"""Oppgave 3.1
Lag en funksjon som tar inn en streng og sjekker om det er en gyldig
IPv4-adresse. En gyldig IPv4-adresse har fire deler atskilt med punktum
(_), der hver del er et heltall mellom 0 og 255. Funksjonen skal returnere
True hvis det er en gyldig adresse, og False ellers. Eksempel:
Input: "192.168.0.1" → Output: True
Input: "256.100.50.0" → Output: False"""

"""Forklaeing

1- Funksjon som tar bare en parameter"""

def ipv4_adresse_sjekker(ip_adresse):
    #2-split ip i deler.
    deler = ip_adresse.split(".")
#3- Sjekker nøyaktig lengden på delene.
    if len(deler) != 4:
        return False
#4- for løkke går i hver del i deler listen. isdigit og startswith sjekker om det er
    #ledende null.
    for del_ in deler:
        if not del_.isdigit() or (del_ != '0' and del_.startswith('0')):
            return False
#-5 Konvertering til helttall og sjekker om tallene er mellom 0 og 225
        tall = int(del_)
        if tall < 0 or tall > 255:
            return False

    return True


print(ipv4_adresse_sjekker("192.168.0.1"))
print(ipv4_adresse_sjekker("256.100.50.0"))
print(ipv4_adresse_sjekker("192.168.01.1"))

# mulig ekstra løsning denne delen hva er mulig for meg å løse uten AI. Jeg har spurt om
#mulig input løsning til min kode#

if __name__ == "__main__":
    ip_adresse = input("Skriv en ip adresse:")
    if ipv4_adresse_sjekker(ip_adresse):
        print("Ip adresse er gyldig")
    else:
        print("Ip adresse er ugyldig")








