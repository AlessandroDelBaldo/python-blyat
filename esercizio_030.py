import random


def genera_cartella(id: int)->dict:
    cartella = [[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]
    cont_riga = 0
    for i in range(3):
        n1 = random.randint(1,9)
        n2 = random.randint(10,19)
        n3 = random.randint(20,29)
        n4 = random.randint(30,39)
        n5 = random.randint(40,49)
        n6 = random.randint(50,59)
        n7 = random.randint(60,69)
        n8 = random.randint(70,79)
        n9 = random.randint(80,90)
        cartella[cont_riga][0]=n1
        cartella[cont_riga][1]=n2
        cartella[cont_riga][2]=n3
        cartella[cont_riga][3]=n4
        cartella[cont_riga][4]=n5
        cartella[cont_riga][5]=n6
        cartella[cont_riga][6]=n7
        cartella[cont_riga][7]=n8
        cartella[cont_riga][8]=n9
        cont_riga += 1
    
    print(cartella)

genera_cartella(2)

