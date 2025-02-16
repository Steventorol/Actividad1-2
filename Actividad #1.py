#1
# def calcular_distancia(velocidad, tiempo):
#     distancia = velocidad * tiempo
#     return distancia

# velocidad = float(input("Ingrese la velocidad del automóvil en m/s: "))
# tiempo = float(input("Ingrese el tiempo en segundos: "))

# distancia = calcular_distancia(velocidad, tiempo)

# print(f"La distancia recorrida es: {distancia} metros.")

#______________________________________________________________________________________________
# //2.Se necesita obtener el promedio de un estudiante a partir de sus tres notas parciales. El
# estudiante debe digitar sus tres notas y el sistema deberá darle el promedio del semestre. 
#//

# nota1 = float(input("Ingrese nota 1: "))
# nota2 = float(input("Ingrese nota 2: "))
# nota3 = float(input("Ingrese nota 3: "))

# def calcular_promedio(nota1,nota2,nota3): 
#   promedio = (nota1 + nota2 +nota3) /3
#   return promedio

# print(f" su promedio {calcular_promedio(nota1, nota2,nota3)} es.")

#______________________________________________________________________________________________
# nota1 = input("Ingrese nota 1: ")
# nota2 = input("Ingrese nota 2: ")
# nota3 = input("Ingrese nota 3: ")

# promedio = (int(nota1) + int(nota2) +int(nota3)) /3

# print(" su promedio es:", promedio)

#3______________________________________________________________________________________________
# #3-Elaborar un algoritmo que permita ingresar el número de partidos ganados, perdidos y
# #empatados, de un equipo en un torneo de futbol. Se debe de imprimir el puntaje total del
# equipo, tenga en cuenta que:
# a. Por cada partido ganado obtendrá 3 puntos.
# b. Por cada partido empatado 1 punto.
# c. Por cada partido perdido 0 puntos.
# Se desea imprimir la cantidad de partidos ganados, perdidos, empatados y el cálculo
# completo de la cantidad de puntos obtenidos del equipo de futbol. 


# partidos_ganados = int(input("Ingrese el número de partidos ganados: "))
# partidos_perdidos = int(input("Ingrese el número de partidos perdidos: "))
# partidos_empatados = int(input("Ingrese el número de partidos empatados: "))


# puntaje_total = (partidos_ganados * 3) + (partidos_empatados * 1)

# print(f"Partidos ganados: {partidos_ganados}")
# print(f"Partidos perdidos: {partidos_perdidos}")
# print(f"Partidos empatados: {partidos_empatados}")
# print(f"Puntaje total: {puntaje_total}")

#4______________________________________________________________________________________________
# Se requiere el algoritmo para elaborar la planilla de un empleado. Para ello se debe digitar:
# nombre del empleado, la cantidad de horas laboradas en el mes y la tarifa por hora. Se debe
# calcular el total devengado por el empleado en el mes e imprimir: Nombre del empleado,
# cantidad de horas laboradas y total devengado.

# NombreE = input("Ingrese el nombre del empleado: ")
# CantidadH = int(input("Ingrese la cantidad de horas laboradas: "))
# TotalD = int(input("Ingrese la tarifa por hora: "))

# Calculo = CantidadH * TotalD

# # f-strings mejora la legibilidad en la impresión.
# print(f"\nNombre: {NombreE} \nHoras Laboradas: {CantidadH} \nTotal Devengado: {Calculo}")

# 5
# Se tiene un triángulo rectángulo cuyos lados deberán ser digitados por el usuario. Se debe
# hallar la hipotenusa teniendo en cuenta la formula: H = raíz cuadrada (a**2 + b**2) 

# import math

# a = int(input("Ingrese el valor del cateto a: "))
# b = int(input("Ingrese el valor del cateto b: "))

# h = math.sqrt(a**2 + b**2)

# print(f"\nLa hipotenusa del triángulo es: {h}")


# # 6 Se tiene un horno en casa con temperaturas en grados Celsius centígrado), requiere
# transformar la temperatura de 70°C a grados Fahrenheit. Para ello tenga en cuenta la
# siguiente fórmula # F = (C * 1.8) + 32 



# C = int(input("ingrese los grados de temperatura: "))  # Temperatura en grados Celsius
# F = (C * 1.8) + 32  # Conversión a Fahrenheit

# print(f"{C}°C equivalen a {F}°F")














#Segunda actividad 

# 1. Desarrolle un algoritmo que lea un número, en caso de ser negativo lo
# imprima junto con su positivo.

# numero = int(input("Ingrese un número: "))
# if numero < 0:
#     print("Número negativo:", numero)
#     print("Número positivo:", -numero)

# 2. desarrollar un programa que, dado una calificación de un alumno en un
# parcial, escribe aprobado si la calificación es superior a 3.

# calificacion = float(input("Ingrese la calificación del alumno: "))
# if calificacion > 3:
#     print("Aprobado")
# else:
#     print("Reprobado")

# 3. desarrollar el algoritmo dado como dato el sueldo de un trabajador, le aplica
# un aumento del 15% si su sueldo es inferior a $300.000.

# sueldo = float(input("Ingrese el sueldo del trabajador: "))
# if sueldo < 300000:
#     sueldo += sueldo * 0.15
#     print("Sueldo con aumento:", sueldo)
# else:
#     print("Sueldo no requiere aumento:", sueldo)

# 4. desarrollar un algoritmo que asigne el sueldo a cinco empleados, teniendo
# en cuenta su categoría.
categoria = input("Ingrese la categoría del empleado (A, B, C): ").upper()
if categoria == "A":
    sueldo = 350000
elif categoria == "B":
    sueldo = 250000
else:
    sueldo = 150000
print("Sueldo asignado:", sueldo)

# 5. desarrollar un programa que capture tres números e imprima por pantalla
# cual es el número mayor, el menor, cuales son iguales, si los tres
# diferentes.

# a = int(input("Ingrese el primer número: "))
# b = int(input("Ingrese el segundo número: "))
# c = int(input("Ingrese el tercer número: "))

# if a > b and a > c:
#     mayor = a
# elif b > a and b > c:
#     mayor = b
# else:
#     mayor = c

# if a < b and a < c:
#     menor = a
# elif b < a and b < c:
#     menor = b
# else:
#     menor = c

# print(f"Mayor: {mayor}, Menor: {menor}")

# if a == b == c:
#     print("Los tres números son iguales.")
# elif a == b or a == c or b == c:
#     print("Hay dos números iguales.")
# else:
#     print("Los tres números son diferentes.")

# 6. Escriba el algoritmo que al capturar un numero entero convierta grados
# centígrados a kelvin, si captura un numero flotante diga si es mayor a 10.5,
# y si captura un carácter escriba su nombre.

# entrada = input("Ingrese un número o carácter: ")

# if entrada.isdigit():
#     grados = int(entrada)
#     kelvin = grados + 273.15
#     print(f"Temperatura en Kelvin: {kelvin}")
# elif '.' in entrada:
#     num_flotante = float(entrada)
#     if num_flotante > 10.5:
#         print("El número es mayor a 10.5")
# else:
#     print(f"El carácter es: {entrada}")

# 7. Desarrolle un algoritmo que lea de un registro: el nombre, la edad, el sexo,
# el estado civil de cualquier persona e imprima el nombre de la persona, si
# corresponde a un hombre casado mayor de 40 años o a una mujer soltera
# menor de 50 años.

# nombre = input("Ingrese el nombre: ")
# edad = int(input("Ingrese la edad: "))
# sexo = input("Ingrese el sexo (H/M): ").upper()
# estado_civil = input("Ingrese el estado civil (casado/soltero): ").lower()

# if (sexo == "H" and estado_civil == "casado" and edad > 40) or (sexo == "M" and estado_civil == "soltero" and edad < 50):
#     print(f"{nombre} cumple con los requisitos.")


# 8. Prepare un algoritmo que identifique e imprima el número medio de un
# conjunto de tres números únicos. El número medio es aquel que no es el
# menor ni el mayor.

# a = int(input("Ingrese el primer número: "))
# b = int(input("Ingrese el segundo número: "))
# c = int(input("Ingrese el tercer número: "))

# if (a > b and a < c) or (a < b and a > c):
#     medio = a
# elif (b > a and b < c) or (b < a and b > c):
#     medio = b
# else:
#     medio = c

# print(f"El número medio es: {medio}")

# 9. Dados tres números enteros únicos, a, b y c. Elabore un algoritmo que los
# ordene de mayor a menor e imprímalos.

# a = int(input("Ingrese el primer número: "))
# b = int(input("Ingrese el segundo número: "))
# c = int(input("Ingrese el tercer número: "))

# numeros = [a, b, c]
# numeros.sort(reverse=True)
# print("Números ordenados de mayor a menor:", numeros)

# 10.A ciertos estudiantes se les dice que su calificación final será el promedio
# de las dos calificaciones más altas de entre las tres que se han obtenido en
# el curso. Haga un algoritmo que permita a un estudiante efectuar el cálculo
# correspondiente a su nota final.

# cal1 = float(input("Ingrese la primera calificación: "))
# cal2 = float(input("Ingrese la segunda calificación: "))
# cal3 = float(input("Ingrese la tercera calificación: "))

# calificaciones = [cal1, cal2, cal3]
# calificaciones.sort(reverse=True)
# promedio = (calificaciones[0] + calificaciones[1]) / 2
# print("El promedio de las dos mejores calificaciones es:", promedio)


# 11.Escriba un algoritmo que acepte o rechace una pieza en forma de varilla,
# para una empresa de acuerdo a los siguientes criterios:

# longitud = float(input("Ingrese la longitud de la varilla (cm): "))
# diametro = float(input("Ingrese el diámetro de la varilla (cm): "))
# masa = diametro * longitud / 3.5  # Densidad = 3.5 Gr/cm

# if 7.5 < longitud <= 9 and 0.5 <= diametro <= 1.3 and masa <= 5.8:
#     print("La pieza ha sido aceptada.")
# else:
#     print("La pieza ha sido rechazada.")

# 12.Un vendedor desea calcular su comisión total sobre las ventas de varios
# artículos. Al vendedor le corresponde el 3% de comisión sobre artículos
# cuyo precio es menor de $2.000.oo y el 5% de comisión sobre artículos
# cuyo precio es de $2000.oo o más. El vendedor hizo 50 ventas y desea
# saber también cuántas ventas hizo menores de 2000 y cuantas mayores o
# iguales a 2000.

# ventas_menores = 0
# ventas_mayores = 0
# comision_total = 0

# for i in range(50):
#     precio = float(input(f"Ingrese el precio de la venta {i+1}: "))
#     if precio < 2000:
#         comision_total += precio * 0.03
#         ventas_menores += 1
#     else:
#         comision_total += precio * 0.05
#         ventas_mayores += 1

# print("Comisión total:", comision_total)
# print("Ventas menores de 2000:", ventas_menores)
# print("Ventas mayores o iguales a 2000:", ventas_mayores)

# 13.desarrollar un algoritmo que halle la nota total de una materia en el SENA, y
# determine si la gano o la reprobó

# nota1 = float(input("Ingrese la primera nota: "))
# nota2 = float(input("Ingrese la segunda nota: "))
# nota3 = float(input("Ingrese la tercera nota: "))

# promedio = (nota1 + nota2 + nota3 - min(nota1, nota2, nota3)) / 2
# print(f"Nota final: {promedio}")

# if promedio >= 3:
#     print("Aprobado")
# else:
#     print("Reprobado")

# 14. Desarrollar un algoritmo que evalué la siguiente expresión aritmética 1/n.

# n = int(input("Ingrese un número n: "))
# if n != 0:
#     resultado = 1 / n
#     print(f"El resultado de 1/{n} es: {resultado}")
# else:
#     print("No se puede dividir entre cero.")

# 15. desarrollar el algoritmo que evalué la formula cuadrática o general.

# import math

# a = float(input("Ingrese el valor de a: "))
# b = float(input("Ingrese el valor de b: "))
# c = float(input("Ingrese el valor de c: "))

# discriminante = b**2 - 4*a*c

# if discriminante >= 0:
#     raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
#     raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
#     print(f"Las raíces son: {raiz1} y {raiz2}")
# else:
#     print("No tiene raíces reales.")

# 16.desarrollar un algoritmo que capture un número y diga si es par o impar.

# numero = int(input("Ingrese un número: "))
# if numero % 2 == 0:
#     print("El número es par.")
# else:
#     print("El número es impar.")

# 17.desarrollar el algoritmo que lea tres números y diga si uno es divisible del
# otro.

# a = int(input("Ingrese el primer número: "))
# b = int(input("Ingrese el segundo número: "))
# c = int(input("Ingrese el tercer número: "))

# if a % b == 0:
#     print(f"{a} es divisible por {b}")
# if b % a == 0:
#     print(f"{b} es divisible por {a}")
# if c % a == 0:
#     print(f"{c} es divisible por {a}")

# 18.Desarrollar un algoritmo que capture un número y diga si negativo o
# positivo.

# numero = int(input("Ingrese un número: "))
# if numero < 0:
#     print("El número es negativo.")
# else:
#     print("El número es positivo.")

