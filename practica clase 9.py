
#1)cree una funcion que calcule el promedio de N notas

def promediar(acu,contador):
    if(contador)==0:
        return 0
    promedio= acu/contador
    return promedio

contador=0
acu=0

while True:
    nota = int(input("Ingrese la nota (o un número negativo para terminar): "))
    if nota<0:
        break
    acu+= nota
    contador += 1
    
if contador ==0:
    print("No se ingresaron notas validas")
else:
 print(f"el promedio es:{promediar(acu,contador):.2f}")
#########################################################
#2)Cree una funcion que determine si un color es primario o no, se debe imprimir por
#pantalla la leyenda “el color X es primero “ o “el color X no es primario”

def es_color_primario(color):
   
    if color.lower() == "amarillo" or color.lower() == "rojo" or color.lower() =="azul":
     return True
    else:
     return False
     
color = input("Ingrese el color que quiere averiguar: ")
if es_color_primario(color):
    print(f"El color que ha consultado :{color} es primario")
else:
    print(f"El color que ha consultado :{color} no es primario")  
################################################################
#3)Cree una funcion que determine que numero de una serie de N numeros es mayor

def encontrar_maximo():
    maximo = None 
    
    while True:
        numero = int(input("Ingrese un numero (o un numero negativo para terminar): "))
        if numero < 0:
            break  
        
        if maximo is None or numero > maximo:
            maximo = numero
    
    if maximo is None:
        print("No se ingresaron numeros validos.")
    else:
        print(f"El numero mayor de la serie es: {maximo}")

# Llamo a la funcion
encontrar_maximo()

############################################################################
#4)Cree una funcion que dibuje un rectangulo de X filas y X columnas determinadas por el
#usuario

def dibujar_rectangulo():
    while True:
        filas = int(input("Ingrese un numero de filas(o un cero para terminar): "))
        if filas == 0:
            break 
        columnas = int(input("Ingrese un numero de columnas(o un cero para terminar): "))
        if columnas == 0:
            break  
        for i in range(filas):
            print("*" * columnas)
        print()  
#llamado a la funcion
dibujar_rectangulo()
          
######################################################################      
#Cree una funcion que calcule el Factorial de un numero entero positivo

def factorial():
     while True:
        numero = int(input("Ingrese un numero entero positivo(o un cero para terminar): "))
        if numero == 0 or numero<0:
            break 
        acu=1
        for i in range(1,numero+1):#para que multiplique por 1,2,etc
            
             acu=acu* i
        print(f"El factorial de {numero} es:{acu}")

#llamado a la funcion
factorial()
