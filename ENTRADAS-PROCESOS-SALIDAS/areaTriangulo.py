#1. inicializacion de variables y reservar espacios de memoria
base=0
altura=0
area=0

#2. Entrada por teclado con imput
base= float(input("BASE : "))
altura= float(input("ALTURA : "))

#3. procesos

area= base * altura /2

#4. salida con print
print("\n\n")
print("BASE ALTURA AREA")
print('='*50)
print(f"{base}\t{altura}\t{area}")
print('='*50)