from func_globales import numero_valido, operador_valido, operacion


#
# ----------- LOGICA ----------------
#

def pedir_fracc()->tuple:
    """
        Pide el numerador y denominador 

        Verifica que sean diferentes de 0 y que sean enteros
        si no lo son los vuelve a pedir  hasta que sean validos
        
        Retorna una fracc con el siguiente orden:
            (numerador, denominador)  
    """
    def es_cero_float(nro, parte="numerador"):
        """
            Verifica si el numero es 0 o float y lo vuelve a pedir hasta que no lo sean
            parte es para cambiar el mensaje de error, debe ser: numerador o denominador 
        """
        
        error_es_cero={ "numerador": "Error, esta sumando 0",
                       "denominador": "Error, division por 0"}

        error_es_float={"numerador": "Ingrese un numerador diferente, debe ser entero",
                        "denominador": "Ingrese un denominador diferente, debe ser entero"}

        nro_no_valido=True
        while nro_no_valido:

            if nro==0:
                print(f"\n {error_es_cero[parte]} \n")
                nro= numero_valido( input(f"Reingrese el {parte}: ") )
            
            elif type(nro) == float:
                print(f"\n {error_es_float[parte]} \n")
                nro= numero_valido( input(f"Reingrese el {parte}: ") )
            
            else:
                nro_no_valido= False
        
        return nro

    numerador= input("Ingrese el numerador: ")
    numerador= numero_valido(numerador)

    numerador= es_cero_float(numerador, "numerador")
            
    denominador= input("Ingrese el denominador: ")
    denominador= numero_valido(denominador)
        
    denominador= es_cero_float(denominador, "denominador")

    return (numerador, denominador)


def simplificado(fracc):
    numerador, denominador= fracc
    resultado=0

    if denominador > numerador:
        grande= denominador
        chico= numerador

    else:
        grande=numerador
        chico=denominador

    if chico !=0:
        resto= grande%chico 
        divisor=chico 
    else:
        resto=0
        divisor=grande

    nuevo_grande=chico
    nuevo_chico=resto

    while resto!=0:

        resto= nuevo_grande%nuevo_chico
        
        divisor=nuevo_chico

        nuevo_grande=nuevo_chico
        nuevo_chico=resto
    
    resultado= ( int(fracc[0]/divisor), int(fracc[1]/divisor) )
    
    return resultado
    

def operar_fracciones(fracc1, operador, fracc2):
    """
    """

    numer_final=0
    denom_final=0

    numer1, denom1=fracc1
    numer2, denom2=fracc2

    suma_resta=operador=="+" or operador=="-"
    divide=operador=="/"

    if suma_resta:
        denom_final= denom1*denom2
        numer1= numer1*denom2
        numer2= numer2*denom1

        numer_final= operacion(numer1, operador, numer2)
    
    elif divide:
        numer_final= numer1 * denom2  
        denom_final= denom1 * numer2  

    else: # Si no suma, resta o divide Multiplica 
        numer_final= operacion(numer1, operador, numer2)
        denom_final= operacion(denom1, operador, denom2)

    signo= numer_final<0 and denom_final<0
    if signo:
        numer_final= abs(numer_final)
        denom_final= abs(denom_final)

    return (numer_final, denom_final)


#
# --------------- Termina la Logica -------------------------
#

# 
# --------------- INTERFAZ USUARIO --------------------------
#  

def fracc_imprimible(fraccion):
    """
        Recibe una fraccion con numerador y denominador

        Los separa en 3 renglones que tienen la misma longitud de caracteres 
        Para quedar con el mismo tamaño añade espacios a los 2 renglones mas chicos  

        Los renglones
                        1 es el numerador                                   num
                        2 es la barra que va en medio de la fraccion        ───
                        3 es el el denominador                              den
    
        Devuelve una fracc con los 3 renglones, que dan facilidad para imprimir fracciones

    """
    
    numerador, denominador=fraccion

    largo_numer= len(str(numerador))
    largo_denom= len(str(denominador))
    
    renglon1=""
    renglon2= "─"
    renglon3=""

    espacios_diferencia= abs( largo_numer - largo_denom )

    if largo_numer > largo_denom:

        renglon1=str(numerador)
        renglon2= "─" * largo_numer
        renglon3=str(denominador) + " "*espacios_diferencia

    elif largo_numer < largo_denom:

        renglon1=str(numerador) + " "*espacios_diferencia
        renglon2= "─" * largo_denom
        renglon3=str(denominador)
    
    else:   # Si no es mayor ni menor es =

        renglon1=str(numerador)
        renglon2= "─" * largo_numer
        renglon3=str(denominador)
    
    return (renglon1, renglon2, renglon3) 

 
def UI_fraccion(fracc1=("num", "den"), oper="=", fracc2=("x","y"), result=("", "")):
    """
        Recibe fraccs con fracciones, de la forma (numerador, denominador), 
        Result debe ser fraccion, oper es un operador, meramente decorativo
        
        Imprime en pantalla la calculadora, las fracciones deberian verse:

                    num1     num2       resultado
                    ────  +  ────   =   ─────────
                    den1     den2       resultado

    """

    fracc1=fracc_imprimible(fracc1)
    fracc2=fracc_imprimible(fracc2)
    result=fracc_imprimible(result)
    
    numer1, barra1, denom1 = fracc1
    numer2, barra2, denom2 = fracc2
    numer_res, barra_res, denom_res = result

    print(f"""
        Casio
        --- Calculadora de FRACCIONES ---               
          
          {numer1}     {numer2}     {numer_res}           
          {barra1}  {oper}  {barra2}  =  {barra_res} 
          {denom1}     {denom2}     {denom_res} 

        |1| |2| |3|      |+| |-| 

        |4| |5| |6|      |x| |/|

        |7| |8| |9|      |=|  

        |.| |0|
    """)
# --------------- Terminan los procesos de Interfaz --------------


#-----------------------------------------------------------------
#                          CALCULADORA
#-----------------------------------------------------------------


def Calculadora_fracciones():
    resultado=(0, 0)

    UI_fraccion()

    fracc1=pedir_fracc()

    operador= input("Ingrese el operador: ")
    operador= operador_valido(operador)

    while operador != "=":

        fracc2=pedir_fracc()

        resultado= operar_fracciones(fracc1, operador, fracc2)
        resultado= simplificado(resultado)

        UI_fraccion(fracc1, operador, fracc2, resultado)

        fracc1=resultado

        print(f"""Esta operando con:    numerador: {fracc1[0]}
                     denominador: {fracc1[1]}
            """)

        operador= input("Ingrese el operador: ")
        operador= operador_valido(operador)

    UI_fraccion(fracc1, " ", ("", ""), simplificado(fracc1))
