import os


os.system('clear')

#1. inicializacion de variables y reservar espacios de memoria
lado1=0
lado2=0
lado2=0
perimetro=0

#2. Entrada por teclado con imput
lado1= float(input("LADO1 : "))
lado2= float(input("LADO2 : "))
lado3= float(input("LADO3 : "))

#3. procesos

perimetro= lado1+lado2+lado3

#4. salida con print
print("\n\n")
print("PERIMETRO DEL TRIANGULO")
print('='*50)
print(f"{lado1}\t+{lado2}\t+{lado3}\t={perimetro}")
print('='*50)