from func_globales import numero_valido, operador_valido, operacion

def pedir_fracc()->tuple:
    """
        Pide el numerador y denominador 
        Verifica que ambos sean numeros validos, si no lo son los vuelve a pedir 

        Luego toma el largo del numero con mas digitos y lo guarda para el ancho de la barra 
        
        Retorna una tupla con el siguiente orden:
        (numerador, denominador, ancho de barra)  
    """
    numerador= input("Ingrese el numerador: ")
    numerador= numero_valido(numerador)

    while numerador==0:
        print("Ingrese un denominador diferente, no vaya a sumar un 0")
        numerador= input("Reingrese el numerador: ")
        numerador= numero_valido(numerador)
            
    denominador= input("Ingrese el denominador: ")
    denominador=numero_valido(denominador)
        
    while denominador==0:
        print("Error, division por 0")
        denominador= input("Reingrese el denominador: ")
        denominador=numero_valido(denominador)

    return (numerador, denominador)


def simplificado(tupla):
    numerador, denominador= tupla
    resultado=0

    if denominador > numerador:
        grande= denominador
        chico= numerador

    else:
        grande=numerador
        chico=denominador

    #cociente= grande//chico
    resto= grande%chico

    #  grande== chico*cociente + resto
    divisor=chico

    nuevo_grande=chico
    nuevo_chico=resto

    while resto!=0:
        #cociente= nuevo_grande//nuevo_chico
        resto= nuevo_grande%nuevo_chico
        
    # nuevo_grande == nuevo_chico*cociente + resto
        divisor=nuevo_chico

        nuevo_grande=nuevo_chico
        nuevo_chico=resto
    
    resultado= ( int(tupla[0]/divisor), int(tupla[1]/divisor) )
    
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

    else: # Si no suma, resta ni divide Multiplica 
        numer_final= operacion(numer1, operador, numer2)
        denom_final= operacion(denom1, operador, denom2)

    signo= numer_final<0 and denom_final<0
    if signo:
        numer_final= abs(numer_final)
        denom_final= abs(denom_final)

    return (numer_final, denom_final)


   
def fracc_imprimible(fraccion):
    """
        Recibe una fraccion con numerador y denominador

        Los separa en 3 renglones que tienen la misma longitud de caracteres 
        Para quedar con el mismo tamaño añade espacios a los 2 renglones mas chicos  

        Los renglones
                        1 es el numerador                                   num
                        2 es la barra que va en medio de la fraccion        ───
                        3 es el el denominador                              den
    
        Devuelve una tupla con los 3 renglones, que dan facilidad para imprimir fracciones

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
        Recibe tuplas con fracciones, de la forma (numerador, denominador), 
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

        print(f"""Esta operando con: numerador: {fracc1[0]}
                 denominador: {fracc1[1]}                  """)

        operador= input("Ingrese el operador: ")
        operador= operador_valido(operador)

    UI_fraccion(fracc1, " ", ("", ""), simplificado(fracc1))

