from func_globales import numero_valido as num_val
from clasica import Calculadora_Clasica 
from fraccion import Calculadora_fracciones
from conversion import Calculadora_Conversion

print("""
    Para una mejor experiencia le sugerimos 
        expandir el tamaño de la terminal
    """)
opcion= 0


while opcion !=4:


    print("""   
        ---- MENU CALCULADORAS ----

                1 - Clasica
                2 - Fracciones 
                3 - Conversiones
                4 - Salir / off
        """)

    opcion= num_val( input("     Ingrese el numero de calculadora:  ") )

    while opcion<=0 or opcion>=5:
        print("\n    Opción no válida, ingrese nuevamente. \n")
        opcion= num_val( input("     Ingrese el numero de calculadora:  ") )

    if opcion == 1:
        Calculadora_Clasica()

    elif opcion == 2:
        Calculadora_fracciones()
        
    elif opcion == 3:
        Calculadora_Conversion()
        
    



print("""
        ----- OFF -----
        """)