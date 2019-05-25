from random import randint
def gera_numeros(numeros_emuso):
    num_ok = False
    while (num_ok==False):
        numero_gerado = str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
        if (numero_gerado != numeros_emuso):
            return numero_gerado