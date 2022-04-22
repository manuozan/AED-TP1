from random import *

print()
print("*" * 50 + " inicia el juego " + "*" * 50)

# Entradas
palos = ('♠', '🖤', '🍀', '💎')
numeros = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A')

# Primer mano usuario
carta1_usuario = choice(palos), choice(numeros)
carta2_usuario = choice(palos), choice(numeros)

# Primer mano crupier
carta1_crupier = choice(palos), choice(numeros)
carta2_crupier = choice(palos), choice(numeros)

# Sumamos las cartas de cada mano
carta1_usuario_valor = carta1_usuario[1]
carta2_usuario_valor = carta2_usuario[1]
carta1_crupier_valor = carta1_crupier[1]
carta2_crupier_valor = carta2_crupier[1]

# Deteminacion del valor de las figuras del usuario
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
elif carta2_usuario_valor == "A":
    if carta1_usuario_valor == "A":
        carta2_usuario_valor = 1
    else:
        carta2_usuario_valor = 11

# Deteminacion del valor de las figuras del crupier
if carta1_crupier_valor == "J" or \
        carta1_crupier_valor == "K" or \
        carta1_crupier_valor == "Q":

    carta1_crupier_valor = 10
elif carta1_crupier_valor == "A":
    carta1_crupier_valor = 11

if carta2_crupier_valor == "J" or \
        carta2_crupier_valor == "K" or \
        carta2_crupier_valor == "Q":

    carta2_crupier_valor = 10
elif carta2_crupier_valor == "A":
    if carta1_crupier_valor == "A":
        carta2_crupier_valor = 1
    else:
        carta2_crupier_valor = 11

# determinar puntaje cada uno
suma_usuario = carta2_usuario_valor + carta1_usuario_valor
suma_crupier = carta1_crupier_valor + carta2_crupier_valor

# mostrar cartas y puntaje parcial
print("\nEl usuario sacó:", carta1_usuario, carta2_usuario)
print("La mano del usuario es:", suma_usuario)
print()
print("El crupier sacó:", carta1_crupier, carta2_crupier)
print("La mano del crupier es:", suma_crupier)

# si el crupier no llega a sumar 17, hacemos que junte otra carta
if suma_crupier < 17:
    carta3_crupier = choice(palos), choice(numeros)
    carta3_crupier_valor = carta3_crupier[1]

    if carta3_crupier_valor == "J" or \
            carta3_crupier_valor == "K" or \
            carta3_crupier_valor == "Q":

        carta3_crupier_valor = 10

    elif carta3_crupier_valor == "A" and (11 + suma_crupier) > 21:
        carta3_crupier_valor = 1

    elif carta3_crupier_valor == "A":
        carta3_crupier_valor = 11

    suma_crupier += carta3_crupier_valor
    print()
    print("El crupier sacó otra carta con el valor", carta3_crupier)
    print("Ahora la mano del crupier es:", suma_crupier)

# si el usuario no llega a sumar 21, hacemos que junte otra carta
if suma_usuario < 21:

    carta3_usuario = choice(palos), choice(numeros)
    carta3_usuario_valor = carta3_usuario[1]

    if carta3_usuario_valor == "J" or \
            carta3_usuario_valor == "K" or \
            carta3_usuario_valor == "Q":
        carta3_usuario_valor = 10

    elif carta3_usuario_valor == "A" and (11 + suma_usuario) > 21:
        carta3_usuario_valor = 1

    elif carta3_usuario_valor == "A":
        carta3_usuario_valor = 11

    suma_usuario += carta3_usuario_valor
    print()
    print("El usuario sacó una tercera carta con el valor", carta3_usuario)
    print("Ahora la mano del usuario es de:", suma_usuario)

# determinacion del resultado final
if (suma_crupier < suma_usuario <= 21) or (suma_crupier > 21 >= suma_usuario):
    resultado = "El usuario gana"
elif (suma_usuario < suma_crupier <= 21) or (suma_usuario > 21 >= suma_crupier):
    resultado = "La casa gana"
elif suma_usuario == suma_crupier and suma_usuario <= 21:
    resultado = "Hay empate"
else:
    resultado = "Ambos pierden"

# salidas
if carta1_usuario[0] == carta1_crupier[0]:
    print(f'Ambos jugadores obtuvieron {carta1_usuario[0]} en la primera carta')
    if carta1_usuario[1] == carta1_crupier[1]:
        print(f'Ademas ambos obtuvieron {carta1_usuario[1]} en la primera carta')
print()
print("El resultado final de la partida es:", resultado)

print("*" * 50 + " Finalizó el juego " + "*" * 50)
