#CONVERSIONES (3)
from func_globales import numero_valido
# --------- Func. Conversiones ---------
def a_octal():
    # --------- Decimal --> Octal ---------  
    
    num1 = (input("ingrese decimal: "))
    num1 = numero_valido(num1) # Validar numero.(Caracteres)
    
    while not ent_pos(num1): # Validar numero. (Entero positivo)
        num1 = input("Ingrese numero entero positivo: ")
        num1 = numero_valido(num1)
     
    n_interfaz = num1 # Variable para interfaz.     
    
    octal = "" # Asignar valor (UnboundLocalError). 
    
    while num1 >= 8: # Verificacion.
        resto = num1 % 8 # Sacar resto.
        num1 = num1 // 8 # Sacar cociente.
        octal += str(resto) # Agregar resto a octal. (str)
    
    octal += str(num1) # Agregar decimal a octal. (str)
    octal = octal [::-1] #Invertir cadena.
    
    # Mostrar conversion.    
    print(f"""
          
        --- DECIMAL [{n_interfaz}] ---> OCTAL [{octal}] ---
                 
        """)

def a_binario():
    # --------- Decimal --> Binario ---------

    num1 = (input("Ingrese decimal: "))
    num1 = numero_valido(num1) # Validar numero.(Caracteres)
    
    while not ent_pos(num1):# Validar numero. (Entero positivo)
        num1 = input("Ingrese numero entero positivo: ")
        num1 = numero_valido(num1) 
    
    n_interfaz = num1 # Variable para interfaz.
    
    binario = "" # Asignar valor (UnboundLocalError). 
    
    while num1 >= 2: # Verificacion.
        resto = num1 % 2 # Sacar resto.
        num1 = num1 // 2 # Sacar cociente.
        binario += str(resto) # Agregar resto a binario. (str)
        
    binario += str(num1) # Agregar decimal a binario. (str)
    binario = binario [::-1] #Invertir cadena.
    
    # Mostrar conversion.    
    print(f"""
          
        --- DECIMAL [{n_interfaz}] ---> BINARIO [{binario}] ---
                 
        """)

def a_hexa():
    # --------- Decimal --> Hexadecimal ---------
    
    #Diccionario de valores hexadecimales.
    valores_hexa = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 
                    8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"} 

    num1 = input("ingrese decimal: ") # Ingresar decimal.
    num1 = numero_valido(num1) # Validar numero.(Caracteres)
    
    while not ent_pos(num1):# Validar numero. (Entero positivo)
        num1 = input("Ingrese numero entero positivo: ")
        num1 = numero_valido(num1) 
    
    n_interfaz = num1 # Variable para interfaz.    
    
    restos = [] # Lista para restos
    
    hexadecimales = "" # Guardar valores hexa.
    
    while num1 >= 16: # Verificacion
        
        resto = num1 % 16 # Sacar resto. 
        
        num1 = num1 // 16 # Sacar cociente.
        
        restos.append(resto) # Agregar el resto a lista restos.
        
    restos.append(num1) # Agrega cociente a restos
    
    for r in (restos): # Leer lista residuos.
        hexadecimales += valores_hexa[r]
           
    num_hexa = hexadecimales [::-1] # Invertir cadena.
    
    # Mostrar conversion.    
    print(f"""
          
        --- DECIMAL [{n_interfaz}] ---> HEXADECIMAL [{num_hexa}] ---
                 
        """)

# --------- Menú de Conversiones ---------

def Calculadora_Conversion():
    print("""
          
          ----- MENÚ DE CONVERSIONES -----
          
                1. Decimal A Octal.
                2. Decimal A Binario.
                3. Decimal A Hexadecimal.
                
                
        """)
    
    opcion= numero_valido(input("Ingrese conversión: "))
    while opcion != 1 and opcion != 2 and opcion != 3:
        print("Opcíón no válida, ingrese nuevamente.")
        opcion= numero_valido(input("Ingrese conversión: "))
    
    if opcion == 1:
            a_octal()
              
    elif opcion == 2:
            a_binario()
              
    elif opcion == 3:
            a_hexa()
   

# --------- Validar numero entero positivo ---------           
def ent_pos(num1):
    if type(num1) == int and num1 >= 0:
        return True
    else:
        return False