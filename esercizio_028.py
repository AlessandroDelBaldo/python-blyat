#Scrivere una funzione che passati come parametro la classe ambientale (euro 0, euro1,...., euro6), i kW e gli anni passati dall'immatricolazione di un autoveicolo, calcoli il bollo auto e l'eventuale superbollo. Nel caso non sia previsto il superbollo si scelga se restituire 0 oppure None. Utilizzare la funzione in un programma di esempio.
#
#N.B.
#Creare una funzione specifica per il superbollo da usare nella funzione principale.
#es.
#def calcola_superbollo (kW:int, immatricolazione: int) ->float: ....
#
#Signature metodo principale:
#def calcola_bollo (classe_ambientale:int, kW:int, immatricolazione:int) ->list[float] | None: ....
#N.B.
#La funzione può eseguire un controllo sui dati inseriti in ingresso e in caso di dati non validi (es. negativi) restituisce None
#
#
#utilizzo:
#bollo, superbollo = calcola_bollo (.......................................
#
#Calcolo bollo:
#Euro 0 fino a 100 kW pagano 3 euro a kW e 4,50 euro per ogni kW oltre i 100
#Euro 1 fino a 100 kW pagano 2,9 euro a kW e 4,35 euro per ogni kW oltre i 100
#Euro 2 fino a 100 kW pagano 2,8 euro a kW e 4,20 euro per ogni kW oltre i 100
#Euro 3 fino a 100 kW pagano 2,7 euro a kW e 4,05 euro per ogni kW oltre i 100
#Euro 4 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
#Euro 5 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
#Euro 6 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
#Calcolo superbollo:
#Auto nuove e fino a 5 anni pagano 20 euro per ogni kW oltre i 185
#Dopo i primi 5 anni pagano 12 euro per ogni kW oltre i 185
#Dopo i 10 anni pagano 6 euro per ogni kW oltre i 185
#Dopo i 15 anni pagano 3 euro per ogni kW oltre i 185
#Dopo i 20 anni non pagano il superbollo

import os

auto = {}

def scheda_tecnica(x):
    cont = True
    while cont is True:
        os.system('cls'if os.name == 'nt' else 'clear')
        classe_ambientale = int(input("Inserire la classe ambientale del veicolo (0-6):"))
        if classe_ambientale >= 0 and classe_ambientale <= 6:
            kW = int(input("Inserire i kW del veicolo:"))
            immatricolazione = int(input("Immatricolazione del veicolo:"))
            x["Classe ambientale"] = classe_ambientale
            x["kW del veicolo"] = kW
            x["Anni passati dall'immatricolazione del veicolo"] = immatricolazione
            cont = False
            os.system('cls'if os.name == 'nt' else 'clear')
        else:
            print("Inserire una classe ambientale idonea")
            input("PREMI INVIO PER CONTINUARE...")
        os.system('cls'if os.name == 'nt' else 'clear')

def calcola_bollo (classe_ambientale:int, kW:int, auto:dict) ->list[float]:
    if classe_ambientale == 0:
        if kW <= 100:
            prezzo_bollo = kW*3
        else:
            kW_eccesso = kW - 100
            prezzo_bollo = 100*3 + kW_eccesso*4.5
    elif classe_ambientale == 1:
        if kW <= 100:
            prezzo_bollo = 100*2.9
        else:
            kW_eccesso = kW - 100
            prezzo_bollo = 100*2.9 + kW_eccesso*4.35
    elif classe_ambientale == 2:
        if kW <= 100:
            prezzo_bollo = kW*2.8
        else:
            kW_eccesso = kW - 100
            prezzo_bollo = 100*2.8 + kW_eccesso*4.20
    elif classe_ambientale == 3:
        if kW <= 100:
            prezzo_bollo = kW*2.7
        else:
            kW_eccesso = kW - 100
            prezzo_bollo = 100*2.7 + kW_eccesso*4.05
    elif classe_ambientale == 4:
        if kW <= 100:
            prezzo_bollo = kW*2.58
        else:
            kW_eccesso = kW - 100
            prezzo_bollo = 100*2.58 + kW_eccesso*3.87
    elif classe_ambientale == 5:
        if kW <= 100:
            prezzo_bollo = kW*2.58
        else:
            kW_eccesso = kW - 100
            prezzo_bollo = 100*2.58 + kW_eccesso*3.87
    elif classe_ambientale == 6:
        if kW <= 100:
            prezzo_bollo = kW*2.58
        else:
            kW_eccesso = kW - 100
            prezzo_bollo = kW*2.58 + kW_eccesso*3.87
    auto["Bollo del veicolo"] = prezzo_bollo

def calcola_superbollo (kW:int, immatricolazione: int) ->float:
    if kW > 185:
        if immatricolazione >= 0 and immatricolazione <= 5:
            costo_superbollo = (kW - 185)*20
        elif immatricolazione > 5 and immatricolazione <= 10:
            costo_superbollo = (kW - 185)*12
        elif immatricolazione > 10 and immatricolazione <= 15:
            costo_superbollo = (kW - 185)*6
        elif immatricolazione > 15 and immatricolazione <= 20:
            costo_superbollo = (kW - 185)*3
        elif immatricolazione > 20:
            costo_superbollo = 0
    auto["Superbollo del veicolo"] = costo_superbollo



scheda_tecnica(auto)

calcola_superbollo(auto["kW del veicolo"],auto["Anni passati dall'immatricolazione del veicolo"])

calcola_bollo(auto["Classe ambientale"],auto["kW del veicolo"],auto)

for i,t in auto.items():
    print(i,":",t)