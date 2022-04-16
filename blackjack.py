from random import *
from re import S
print()
print("*"*50 + " inicia el juego "+"*"*50)
# Entradas
palos = ('♠', '🖤', '🍀', '💎')
numeros = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A')

#PRIMER MANO USUARIO
carta1_usuario = choice(palos), choice(numeros)
carta2_usuario = choice(palos), choice(numeros)

#PRIMER MANO CRUPIER
carta1_crupier = choice(palos), choice(numeros)
carta2_crupier = choice(palos), choice(numeros)

#SUMAMOS LAS CARTAS DE CADA MANO
carta1_usuario_valor = carta1_usuario[1]
carta2_usuario_valor = carta2_usuario[1]
carta1_crupier_valor = carta1_crupier[1]
carta2_crupier_valor = carta2_crupier[1]

if carta1_usuario_valor == "J" or \
    carta1_usuario_valor == "K" or \
    carta1_usuario_valor == "Q":

    carta1_usuario_valor = 10 
elif carta1_usuario_valor == "A":
    carta1_usuario_valor = 11

if carta2_usuario_valor == "J" or \
    carta2_usuario_valor == "K" or \
    carta2_usuario_valor == "Q":

    carta2_usuario_valor = 10 
elif carta2_usuario_valor == "As":
    carta2_usuario_valor = 11

if carta1_crupier_valor == "J" or \
    carta1_crupier_valor == "K" or \
    carta1_crupier_valor == "Q":

    carta1_crupier_valor = 10 
elif carta1_crupier_valor == "As":
    carta1_crupier_valor = 11

if carta2_crupier_valor == "J" or \
    carta2_crupier_valor == "K" or \
    carta2_crupier_valor == "Q":

    carta2_crupier_valor = 10 
elif carta2_crupier_valor == "As":
    carta2_crupier_valor = 11    

suma_usuario = carta2_usuario_valor + carta1_usuario_valor
suma_crupier = carta1_crupier_valor + carta2_crupier_valor

print("el usuario sacó:", carta1_usuario , carta2_usuario)
print("la mano del usuario es:", suma_usuario)
print()
print("el crupier sacó:", carta1_crupier , carta2_crupier)
print("la mano del crupier es:", suma_crupier)



#SI EL CRUPIER NO LLEGA A SUMAR 17, HACEMOS QUE JUNTE OTRA CARTA
if suma_crupier < 17: 
    carta3_crupier = choice(palos), choice(numeros)
    carta3_crupier_valor = carta3_crupier[1]

    if carta3_crupier_valor == "J" or \
        carta3_crupier_valor == "K" or \
        carta3_crupier_valor == "Q":

        carta3_crupier_valor = 10 

    elif carta3_crupier_valor == "As" and (11 + suma_crupier) > 21 and (1 + suma_crupier) <= 21 :
        carta3_crupier_valor = 1 

    elif carta3_crupier_valor == "As":
        carta3_crupier_valor = 11   

    

    suma_crupier += carta3_crupier_valor
    print("el crupier sacó otra carta con el valor", carta3_crupier)
    print("ahora la mano del crupier es:", suma_crupier)



#SI EL USUARIO NO LLEGA A SUMAR 21, HACEMOS QUE JUNTE OTRA CARTA
if suma_usuario < 21:
    usuario_otracarta = input("Desea el usuario sacar otra carta? \n [y] para aceptar o \n [cualquier otra tecla] para continuar:\n").lower()
    if usuario_otracarta == "y":  
        carta3_usuario = choice(palos), choice(numeros)
        carta3_usuario_valor = carta3_usuario[1]

        if carta3_usuario_valor == "J" or \
            carta3_usuario_valor == "K" or \
            carta3_usuario_valor == "Q":

            carta3_usuario_valor = 10 

        elif carta3_usuario_valor == "As" and (11 + suma_usuario) > 21 and (1 + suma_usuario) <= 21 :
            carta3_usuario_valor = 1 

        elif carta3_usuario_valor == "As":
            carta3_usuario_valor = 11   

        suma_usuario += carta3_usuario_valor

        print("el usuario sacó otra carta con el valor", carta3_usuario)

print("ahora la mano del usuario es de:",suma_usuario)


#BUSCAMOS EL GANADOR 

if (suma_usuario > suma_crupier and suma_usuario <= 21) or (suma_crupier > 21 and suma_usuario <= 21): 
    resultado = "el usuario gana" 
elif (suma_usuario < suma_crupier and suma_crupier <= 21) or (suma_usuario > 21 and suma_crupier <= 21): 
    resultado = "la casa gana"
elif suma_usuario == suma_crupier and suma_usuario <= 21:
    resultado = "hay empate"
else: 
    resultado = "ambos pierden"
    

#SALIDAS
if carta1_usuario[0] == carta1_crupier[0]:
    print("el palo de la primera carta de usuario, crupier es:" , carta1_usuario[0])
    if carta1_usuario[1] == carta1_crupier[1]:
        print("el valor de la primera carta de usuario, crupier:" , carta1_usuario[1])
print()
print("/////",resultado)

print("*"*50 + " finalizó el juego "+"*"*50)



# falta la consigna de determinar si salió al menos una figura, mostrar el puntaje parcial que se obtiene en cada mano 