"""Lag et program som ber brukeren om a skrive inn et positivt heltall (int)
og finner summen av alle tall f ra 1 til dette tallet (inkluder ogs˚a tallet i
summen). Summen skal beregnes ved hjelp av en for-løkke."""

"""Forkalring: or å kunne løse denne har jeg lest denne artikkel : https://www.uvm.edu/~cbcafier/cs1210/book/11_loops/loops_and_summation.html#:~:text=Calculating%20a%20sum%20in%20a%20loop,-While%20we%20have&text=Since%20the%20elements%20of%20t,We%20call%20this%2C%20sum_%20.&text=Then%2C%20we%20iterate%20over%20all,element%20to%20the%20variable%20sum_%20.

Fikk feil resultat på grunn av inrykk i print. Har brukt AI for mulig feil i koden: Jeg fikk svar på at det er et alternativ å bruke en annen variablenavn enn 'sum' fordi den er innbygd funksjon"""


tallet =int(input("Skriv ett tall så finner jeg summen fra 1 til dette tallet: "))
summen = 0
for i in range (1, tallet + 1):
    summen += i
print(summen)
