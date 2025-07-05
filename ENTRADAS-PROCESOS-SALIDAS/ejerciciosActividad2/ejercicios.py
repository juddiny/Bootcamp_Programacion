from strings import *
from datetime import datetime
import math
import os
class ejercicios (object):
    """Ingresar por teclado y por separado en dos variables, sus nombres y apellidos respectivamente,
    mostrar en orden contrario al que se ingresaron, es decir apellidos y nombres, Ejm;
    ENTRADA: JHON JAIRO
    OROZCO DAVILA
    SALIDA => OROZCO DAVILA JHON JAIRO"""
    def __init__(self):
        self.menu()
        pass

    def menu(self):
        while True:
            os.system('clear')
            print(BIENVENIDA)
            var=input(SELECCION)
            if (int(var)>=1 and int(var)<=10):        
                if var=="1":
                    self.ejercicio1()
                if var=="2":
                    self.ejercicio2()
                if var=="3":
                    self.ejercicio3()
                if var=="4":
                    self.ejercicio4()
                if var=="5":
                    self.ejercicio5()
                if var=="6":
                    self.ejercicio6()
                if var=="7":
                    self.ejercicio7()
                if var=="8":
                    self.ejercicio8()
                if var=="9":
                    self.ejercicio9()
                if var=="10":
                    self.ejercicio10()
            else:
                print(DESPEDIDA)
                break      
            input("\nPresiona ENTER para continuar...")  # El mensaje es opcional
    def ejercicio1(self):
        nombres=input(INGRESA_NOMBRE)
        apellido=input(INGRESA_APELLIDO)
        print(SEPARADOR)
        print(NOMBRE_COMPLETO.format(nombres=nombres,  apellido=apellido))       
    def ejercicio2(self):
        """
        Hallar la edad de una persona, conociendo su año de nacimiento; declarar una CONSTANTE
        con el año actual.
        """
        anio_actual = datetime.now().year
        edad=anio_actual - int(input(INGRESA_ANIO))
        print(EDAD_ACTUAL.format(edad=edad))
    def ejercicio3(self):
        """
        Leer dos números y hallar: la sumatoria, su diferencia, su producto, su cociente y su residuo,
        NO usar funciones.
        """
        num1=float(input(NUMERO1))
        num2=float(input(NUMERO2))
        print(SUMATORIA.format(num1=num1, num2=num2), num1+num2)
        print(RESTA.format(num1=num1, num2=num2), num1-num2)
        print(PRODUCTO.format(num1=num1, num2=num2), num1*num2)
        if(num2!=0):
            print(COCIENTE.format(num1=num1, num2=num2), num1/num2)
        else:
            print(ERR_COCIENTE)
    def ejercicio4(self):
        listaNotas=[]
        listaPorcentajes=[0.25,0.25,0.20,0.3]
        cont=1
        while cont<=3:
            num=float(input(f"{NOTA} {cont}: "))
            listaNotas.append(num)
            cont+=1
        listaNotas.append(float(input(TALLERES)))
        nota=listaNotas[0]*listaPorcentajes[0]+listaNotas[1]*listaPorcentajes[1]+listaNotas[2]*listaPorcentajes[2]+listaNotas[3]*listaPorcentajes[3]
        print(NOTAFINAL.format(notafinal=nota))
    def ejercicio5(self):
        """
        Ingresar dos valores diferentes, almacenarlos en dos variables, pero al momento de mostrarlos,
        sus valores internamente (en la R.A.M.) han sido intercambiados. Se pueden utilizar otras
        variables auxiliares. Ejm: x = 10; y = 20 al final x = 20 ; y = 10 (nota no es intercambiarlos
        al imprimir)
        """
        num1=float(input(NUMERO1))
        num2=float(input(NUMERO2))
        print(NUM_ORIGIANES.format(num1=num1,num2=num2))
        temp=num1
        num1=num2
        num2=temp
        print(NUM_FINALES.format(num1=num1,num2=num2))
    
    def ejercicio6(self):
        """
        El mismo ejercicio anterior, pero utilizando solamente dos variables (en la R.A.M.) durante
        toda la operación. Ayuda, utilizar operaciones matemáticas.
        """
        num1=float(input(NUMERO1))
        num2=float(input(NUMERO2))
        print(NUM_ORIGIANES.format(num1=num1,num2=num2))
        num1=num1+num2
        num2=num1-num2
        num1=num2-num1
        print(NUM_FINALES.format(num1=num1,num2=num2))
    def ejercicio7(self):
        """La Función calcula algebraicamente la ecuación de segundo grado, tanto en sus componente Positivo como Negativo.
        
        Esta función pide 3 valores A,B,C y calcula su ecuación de segundo grado.
        
        Args:
            self: hace Referencia a la instancia de la clase.
            
        Returns:
            None: La función solo imprime el valor
        
        """
        A=float(input(ING_VALORES.format(valor="A")))
        B=float(input(ING_VALORES.format(valor="B")))
        C=float(input(ING_VALORES.format(valor="C")))
        X1= (-B+math.sqrt(B**2-(4*A*C)))/(2*A)
        X2= (-B-math.sqrt(B**2-(4*A*C)))/(2*A)
        print(RESULTADO_ECUACION," \n" ,FORMULAX1," = ", X1 )
        print(RESULTADO_ECUACION," \n" ,FORMULAX2," = ", X2 )
        
    def ejercicio8 (self):
        """Lee un carácter y mostrar su código ASCII, por ejemplo, al ingresar @ debe mostrar 64
        
        Esta funcion pide un caracter y si el largo de lo introducido por teclado es de un solo digito calcula y muestra su valor en ASCII.
        
        Args:
            self: hace Referencia a la instancia de la clase.
        
        Returns:
            None: La función solo imprime en pantalla el valor correspondiente al caracter ASCII, sin retornar valores.
        
        """
        caracter = input(VARASCII)
        if len(caracter) == 1:
            codigo_ascii = ord(caracter)
            print(RESULT_ASCII.format(caracter=caracter,codigo_ascii=codigo_ascii))
        else:
            print(ERR_ASCII)
    def ejercicio9 (self):
        """Solicita un valor y determina su caracter ASCII.
        
        Esta funcion pide un valor y si este se encuentra entre 0 y 255 muestra su simbolo ASCII.
        
        Args:
            self: hace Referencia a la instanacia de la clase.
        
        Returns: 
            None: La función solo imprime en pantalla el caracter ASCII, sin retornar valores.
        """
        valor= int(input(VALORNUM))
        if valor >=0 and valor <=255:
            simbol= chr(valor)
            print(VALOR_ASCII.format(valor=valor,simbol=simbol))
        else:
            print(ERR_VALOR_ASCII)
    
    def ejercicio10(self):
        """Muestra un enlace al programa propio en Google Colab.
        
        Esta función imprime un mensaje formateado que contiene una URL clickeable
        (o texto plano, dependiendo de la terminal) donde los usuarios pueden acceder
        al código del programa en Google Colab.

        Args:
            self: Referencia a la instancia de la clase.

        Returns:
            None: La función solo imprime en pantalla, no retorna valores.

        """
        url = "https://colab.research.google.com/drive/1YuALK4wBQOryq-YFLqV0PVCkG2V_wizB?usp=sharing"
        print(PROG_PROPIO.format(url=url))