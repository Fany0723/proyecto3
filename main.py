import os
from  readchar import readkey, key

def limpiarPantalla():
    os.system('cls' if os.name=='nt' else 'clear')

numero = 0
while   numero <= 50:
    print(numero)
    k = readkey()
    if( k == "n" or k == "N" ):
        limpiarPantalla()
        numero += 1
    

