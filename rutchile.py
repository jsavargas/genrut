#!/usr/bin/python3
#_*_ coding: utf8 _*_



try:
    import argparse, re, random
except ImportError as error:
    print("Falta instalar algunas librerías")
    print(error)

data = []

parser = argparse.ArgumentParser(description="Generador de RUTs Chilenos válidos")
parser.add_argument('-f','--full', action='store_true', default=True, help="Generar RUTs con puntos, guión y dígito verificador Ej: 12.345.678-9")
parser.add_argument('-d','--digit', action='store_true', help="Generar RUTs solo con dígito verificador Ej: 12345678-9")
parser.add_argument('-l','--list', action='store_true', help="Generar RUTs sin puntos ni guión con dígito verificador Ej: 123456789")
parser.add_argument('-m','--miss', action='store_true', help="Generar solo RUTs sin dígito verificador Ej: 12345678")

parser.add_argument('-r','--random', action='store_true', help="Generar solo RUTs sin dígito verificador Ej: 12345678")
parser.add_argument('-c','--count', type=int, default=10, help="Opcional. Especifica la cantidad de RUTs a generar (10 por default).")

parser.add_argument('-b','--begin', type=str, required=True, help="Indique el RUT inicial  Ej: 12345678")
parser.add_argument('-e','--end', type=str, required=True, help="Indique el RUT inicial  Ej: 12345678")
parser = parser.parse_args()




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
        
        if parser.random:
            if parser.digit: data.append(f"{rut}-{digito}")
            elif parser.list: data.append(f"{rut}{digito}")
            elif parser.miss: data.append(f"{rut}")
            elif parser.full: 
                result = re.sub(r"(\d{1,2})(\d{3})(\d{3})", r"\1.\2.\3", rut)
                data.append(f"{result}-{digito}")


        elif parser.digit: print(f"{rut}-{digito}")
        elif parser.list: print(f"{rut}{digito}")
        elif parser.miss: print(f"{rut}")
        elif parser.full:
            result = re.sub(r"(\d{1,2})(\d{3})(\d{3})", r"\1.\2.\3", rut)
            print(f"{result}-{digito}")

    if parser.random:
        if (int(parser.end) - int(parser.begin)) > parser.count:  rnd = random.sample(data, parser.count)
        else :  rnd = random.choices(data, k=parser.count)

        rnd.sort()
        rnd = list(set(rnd))

        for r in rnd:
            print(r)



if __name__ == '__main__':
    main()
    