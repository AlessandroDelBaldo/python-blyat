import random

cartella = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]
def genera_cartella(id: int)->dict:
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
    
    cont_riga = 0
    libero1 = [0,1,2,3,4,5,6,7,8]
    libero2 = [0,1,2,3,4,5,6,7,8]
    libero3 = [0,1,2,3,4,5,6,7,8]
    for i in range(3):
        vuoto1 = random.choice(libero1)
        vuoto2 = random.choice(libero2)
        vuoto3 = random.choice(libero3)
        cartella[0][vuoto1] = "-"
        cartella[1][vuoto2] = "-"
        cartella[2][vuoto3] = "-"
        libero1.remove(vuoto1)
        libero2.remove(vuoto2)
        libero3.remove(vuoto3)

    
    print(cartella[0])
    print(cartella[1])
    print(cartella[2])
    return cartella

genera_cartella(2)
