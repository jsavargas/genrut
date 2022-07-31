#!/usr/bin/python3
#_*_ coding: utf8 _*_

#--------------------------------------------------------------------
# ----            GENERADOR DICCIONARIOS CON RUTs CHILENOS      ----|
# ----            Gohanckz                                      ----|
# ----            Contact : gohanckz@gmail.cl                   ----|
# ----            Version : 2.1                                 ----|
#--------------------------------------------------------------------


try:
    import argparse, re
except ImportError as error:
    print("Falta instalar algunas librerías")
    print(error)



parser = argparse.ArgumentParser(description="RUT CHILE V2.1 by @Gohanckz")
parser.add_argument('-f','--full', action='store_true', help="Generar RUTs con puntos, guión y dígito verificador Ej: 12.345.678-9")
parser.add_argument('-d','--digit', action='store_true', help="Generar RUTs solo con dígito verificador Ej: 12345678-9")
parser.add_argument('-l','--list', action='store_true', help="Generar RUTs sin puntos ni guión con dígito verificador Ej: 123456789")
parser.add_argument('-m','--miss', action='store_true', help="Generar solo RUTs sin dígito verificador Ej: 12345678")

parser.add_argument('-b','--begin', type=str, required=True, help="Indique el RUT inicial de 8 dígitos Ej: 12345678")
parser.add_argument('-e','--end', type=str, required=True, help="Indique el RUT inicial de 8 dígitos Ej: 12345678")
parser = parser.parse_args()




def calculaDV(rut):
    # Calcula el dígito verificador válido para un RUT
    rut_str=str(rut)[::-1]  # Invierte el string! Ver http://stackoverflow.com/questions/931092/reverse-a-string-in-python
    
    # Variables para el cálculo
    multiplicador=2
    suma=0
    
    for c in rut_str:
        # Iteramos sobre todos los caracteres del RUT ya invertido, sumando los dígitos * el multiplicador
        suma+=int(c)*multiplicador
        multiplicador+=1
        if multiplicador>7:
            multiplicador=2
        
    dv=str(11-(suma%11))  # 11 - Módulo
    
    # Excepciones
    if dv=='11':
        dv='0'
    if dv=='10':
        dv='K'
        
    return dv


def main():


    for i in range(int(parser.begin),int(parser.end)+1):
        rut = str(i)

        rut_str=str(rut)[::-1]  # Invierte el string! Ver http://stackoverflow.com/questions/931092/reverse-a-string-in-python
        
        # Variables para el cálculo
        multiplicador=2
        suma=0
        
        for c in rut_str:
            # Iteramos sobre todos los caracteres del RUT ya invertido, sumando los dígitos * el multiplicador
            suma+=int(c)*multiplicador
            multiplicador+=1
            if multiplicador>7:
                multiplicador=2
            
        digito=str(11-(suma%11))  # 11 - Módulo

        if digito == "11":
            digito = "0"
        elif digito == "10":
            digito = "k"
        
        if parser.full:
            result = re.sub(r"(\d{1,2})(\d{3})(\d{3})", r"\1.\2.\3", rut)
            print(f"{result}-{digito}")
        
        elif parser.digit: print(f"{rut}-{digito}")
        elif parser.list: print(f"{rut}{digito}")
        elif parser.miss: print(f"{rut}")





if __name__ == '__main__':
    main()
    