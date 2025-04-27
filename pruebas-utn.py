# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# Aplicamos una estuctura repetitiva FOR, imprimiendo los numeros del 0 al 100 inclusive

# for x in range (0,101):

# Aqui aplicamos la tecnica de cimino, que es poner un end ( un salto de linea) y que lo que se escriba siga en la misma linea

#     print(x,"",end="") 





# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

#creamos la estructura while pero primero diciendole al usuario que ponga un numero entero
# numero=int(input("Ingrese un numero entero: "))
# contador = 0

#En caso de poner numero negativo, lo transformamos al numero en un valor absoluto, ignorando asi el signo
# numero= abs(numero)

#Para evitar errores catastroficos evitamos la entrada de 0 al bucle
# if numero == 0 :
#     print("Su numero tiene 1 digito")

 #Indicamos que si el numero no es 0    
#else:
    # while numero > 0:
    #     numero = numero // 10
    #     contador +=1
    # print(f"Su numero tiene {contador} cantidad de digitos")        





# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

#Pedimos los valores al usuario
# numero_1= int(input("Ingrese el primer valor: "))
# numero_2= int(input("Ingrese el segundo valor: "))
#Igualamos la variable suma a 0
# suma = 0
#Preguntamos si numero 1 es mayor o igual a numero 2
# if numero_1 >= numero_2:
#     print("El numero primer numero debe ser mayor que el segundo: ")
# else:
  #Estructura for 
    # for x in range(numero_1+1,numero_2):
    #     suma = suma + x
    #     print(suma)





# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
#Indicaciones al usuario
# usuario= int(input("Escriba un numero entero que se ira sumando periodicamente. [Para finalizar la operacion pulse '0']: "))
#Acumulador de los numeros que se van a ir sumando
# acumulador = 0
#Estructura repetitiva que indica que se va a repetir hasta que el usuario marque 0
# while usuario != 0:
#     acumulador += usuario
#     usuario=int(input("Escriba un numero entero que se ira sumando periodicamente. [Para finalizar la operacion pulse '0']: "))


#Mensaje final
# print(f"La sumatoria total de tus numeros ingresados es:{acumulador} ")





# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#Importar  la funcion random
# import random

#Indicaciones al usuario
# numero_usuario=int(input(f"Ingrese un numero del 0 al 9 que aleatoriamente debera adivinar: "))

#Variables que contendran los valores maximos y minimos del random
# a=0
# b=9
# rango_random= random.randint(a,b)

#Intentos del usuario
# intentos = 1

#Creacion de estructura repetitiva con sus preguntas if, else
# while rango_random != numero_usuario:
#     intentos+=1
#     if numero_usuario == rango_random:
#         print("Felicidades, adivinaste el numero al primer intento!")

    # numero_usuario=int(input("Ingrese un numero del 0 al 9 que aleatoriamente debera adivinar: "))
    # if numero_usuario < rango_random:
    #     print("El numero elegido es bajo!")
    # else:   
    #     print("El numero elegido es alto!")
     
#Mensaje final    
# print(f"Felicidades! adivinaste el numero!, tus intentos fueron: {intentos}")






# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

#Variables que contendran los valores
# a= -2
# b=100

#Creacion de la estructura repetitiva
# for x in range(b,a,-2):
#  print(x)






# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

#Indicaciones al usuario
# numero_usuario= int(input("Escriba un numero entero positivo: "))

#Contenido igualado a cero, ideal para que se empiece a llenar de informacion a medida que el for hace su trabajo
# contenido=0

#Creacion de la estructura repetitiva
# for x in range(0,numero_usuario+1):
#     contenido= contenido + x

#Mensaje final
# print(f"El resultado de la suma entre todos los numeros enteros positivos entre 0 y {numero_usuario} es: {contenido}")






# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio)

#Esta variable es la que se puede modificar para que el numero maximo de numeros que tirara el usuario sean igual  a la misma:
# contador_numeros=4

#Aca metemos unas variables las cuales van a servir como almacen de informacion 
# contador = 1
# contador_par=0
# contador_impar=0
# contador_positivo= 0
# contador_negativo=0

#Creacion del ciclo while:
#while contador <= contador_numeros:   
#Pedimos al usuario que ingrese un valor     
#    usuario=int(input("Ingrese un numero: "))
#    contador = contador + 1
#Si el numero es par..  
#    if usuario %2==0:
#        contador_par = contador_par +1
#Si el numero es impar...
#    elif usuario %2 != 0:
#        contador_impar= contador_impar+1
#Si el numero es mayor que 0...
#    if usuario >0:
#        contador_positivo= contador_positivo + 1
#Si el numero es menor que 0 ...
#    elif usuario <0:
#        contador_negativo= contador_negativo + 1

#Mensaje final con los respectivos datos acumulados en las variables del comienzo..
#print(f"NUMEROS PAR: {contador_par}, NUMEROS IMPAR: {contador_impar}, NUMEROS NEGATIVOS: {contador_negativo}, NUMEROS POSITIVOS: {contador_positivo}")







# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

#Creacion del contador de numeros que esto puede ser 4, o 100,
# contador_numeros = 4
#Creacion del almacen de numeros que va lanzando el usuario
# almacen_numeros= 0
# promedio = 0
#Bucle for
# for i in range(contador_numeros):
#     usuario=int(input("Ingrese un numero, y le calcularemos el promedio de los mismos: "))
#     almacen_numeros = almacen_numeros + usuario
#     promedio = almacen_numeros / contador_numeros
#Mensaje final
# print(f"El promedio de todos los numeros que usted ha enviado es de : {promedio}")









# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.


#Indicaciones al usuario
# numero=int(input("Ingrese un numero que desee invertir: "))
#Pasamos el numero a cadena  ( modificamos el tipo de variable)
# cadena_numero=str(numero)
#Invertimos los valores de esa cadena 
# invertir_cadena=cadena_numero[::-1]
#una vez invertidos ese string, lo volvemos a transformar en int ( entero o numero)
# numero_de_nuevo=int(invertir_cadena)

#mensaje final con el resultado
# print(f"El numero: {numero} ,invertido quedaria: {numero_de_nuevo}")



