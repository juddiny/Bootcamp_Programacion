# bienvenida
BIENVENIDA="BIENVENIDO \n SELECCIONA LA OPCION QUE MEJOR TE ACOMODE: \n 1. EJERCICIO NOMBRES. \n 2. EJERCICIO EDAD. \n 3. EJERCICIO OPERACIONES MATEMÁTICAS. \n 4. EJERCICIO CALCULO NOTAS. \n 5. EJERCICIO INTERCAMBIO DE VARIABLES. \n 6. EJERCICIO INTERCAMBIO DE VARIABLES SIN VARIABLE DE APOYO. \n 7. EJERCICIO DE RAIZ CUADRADA. \n 8. EJERCICIO CONVERTIR CARACTER A ASCII. \n 9. EJERCICIO CONVERTIR DE VALOR A CARACTER ASCII. \n 10. PROGRAMA PERSONAL."
DESPEDIDA="GRACIAS"

# menu
SELECCION="selecciona un número correspondiente al ejercicio: "
# Ejercicio 1
INGRESA_NOMBRE="INGRESA TU NOMBRE: "
INGRESA_APELLIDO="INGRESA TU APELLIDO: "
NOMBRE_COMPLETO="tu nombre completo es: {apellido} {nombres} "
# separadores
SEPARADOR = "="*50
# Ejercicio 2

INGRESA_ANIO="INGRESA TU AÑO DE NACIMIENTO: "
EDAD_ACTUAL="Tu edad actual es {edad} años"

# Ejercicio 3 
NUMERO1="INGRESA EL PRIMER NUMERO A CALCULAR: "
NUMERO2="INGRESA EL SEGUNDO NUMERO A CALCULAR: "
SUMATORIA="la suma de los numeros es {num1} + {num2} = "
RESTA="la resta de los numeros es {num1} - {num2} = "
PRODUCTO="el producto de los numeros es {num1} * {num2} = "
COCIENTE="el cociente de los numeros es {num1} / {num2} ="
ERR_COCIENTE="NO SE MUESTRA EL COCIENTE YA QUE NO ES POSIBLE LA DIVISION POR 0"

# Ejercicio 4
"""
Leer las tres notas de los parciales y mostrar su definitiva aplicando los respectivos
porcentajes: Primer y Segundo Parcial 25%, Final del 20% y los Talleres 30% (tres talleres por
separado)
"""
NOTA="POR FAVOR INGRESA LA NOTA"
TALLERES="POR FAVOR INGRESA LA NOTA DE LOS EXAMENES: "
NOTAFINAL="su nota es: {notafinal}"

# Ejercicio 5 y 6
NUM_ORIGIANES="SUS NÚMEROS INICIALES SON: num1= {num1} y num2= {num2}"
NUM_FINALES="SUS NÚMEROS FINALES SON: num1= {num1} y num2= {num2}"

# Ejercicio 7
ING_VALORES="INGRESE EL VALOR DE {valor}: "
RESULTADO_ECUACION="EL RESULTADO DE LA ECUACION"
FORMULAX1="(-B+math.sqrt(B**2-(4*A*C)))/2*A"
FORMULAX2="(-B-math.sqrt(B**2-(4*A*C)))/2*A"

# Ejercicio 8 

VARASCII="Ingresa un carácter: "
RESULT_ASCII="El código ASCII de '{caracter}' es: {codigo_ascii}"
ERR_ASCII="Error: Debes ingresar exactamente un carácter para calcular su codigo ASCII."

# Ejercicio 9 
VALORNUM="Ingresa el numero a convertir a ASCII numeros entre 0 y 255: "
VALOR_ASCII="El valor {valor} corresponde al simbolo {simbol}"
ERR_VALOR_ASCII="El valor ingresado no corresponde a un número entre 0 y 255"

# Ejercicio 10 
PROG_PROPIO="PARA CONOCER UN PROGRAMA BÁSICO DE MI AUTORIA TE INVITO A DAR CLICK \n \033]8;;{url}\033\\Haz clic aquí\033]8;;\033\\"
