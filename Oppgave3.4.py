"""Lag en funksjon som tar en annen funksjon som parameter, noen argumenter
og et forventet resultat, og som returnerer sant hvis det faktiske resultatet
stemmer overens med det forventede resultatet, ellers usant."""

"""Forklaring 1- importere pyautogui for å har kontroll på mus og tastatur og
 tid gir mulighet til ventetid. random for å velge tilfeldig karakter."""



import pyautogui
import time
import random

def robotlærer():
    pyautogui.alert(" Velkommen til ukvalifisert Robotlærer 3000!")
    time.sleep(1)

    navn = pyautogui.prompt("Hva heter du, elev?")
    time.sleep(1)

    pyautogui.write(f"Analyserer prestasjonene til {navn}...", interval=0.1)
    time.sleep(2)

    karakter = random.choice(["A", "B", "C", "D", "E", "F", "Z"])
    kommentar = random.choice([
        "Strålende innsats!",
        "Du har potensiale... kanskje.",
        "Robotlæreren er forvirret. Prøv igjen.",
        "Dette var... kreativt.",
        "Du får Z for Zzzzz...",
        "Fantastisk! Du er en kode-ninja!",
        "Hmm... du har trykket på knapper, i hvert fall."
    ])

    pyautogui.alert(f"{navn}, du får karakter: {karakter}\nKommentar: {kommentar}")
    pyautogui.moveTo(300, 300, duration=1)
    pyautogui.click()
    pyautogui.alert("Robotlærer 3000 logger av. Husk å gjøre leksene dine!")

robotlærer()
