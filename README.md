

# Descripción

**rutchile.py** es una herramienta que permite generar diccionarios con **ruts chilenos válidos** en distintos formator para nuestros ejercicios de Ethical Hacking.

```
usage: rutchile.py [-h] [-f] [-d] [-l] [-m] [-r] [-c COUNT] -b BEGIN -e END

Generador de RUTs Chilenos válidos

optional arguments:
  -h, --help                show this help message and exit
  -f, --full                Generar RUTs con puntos, guión y dígito verificador Ej: 12.345.678-9
  -d, --digit               Generar RUTs solo con dígito verificador Ej: 12345678-9
  -l, --list                Generar RUTs sin puntos ni guión con dígito verificador Ej: 123456789
  -m, --miss                Generar solo RUTs sin dígito verificador Ej: 12345678
  -r, --random              Generar solo RUTs sin dígito verificador Ej: 12345678
  -c COUNT, --count COUNT   Opcional. Especifica la cantidad de RUTs a generar (10 por default).
  -b BEGIN, --begin BEGIN   Indique el RUT inicial Ej: 12345678
  -e END, --end END         Indique el RUT inicial Ej: 12345678

```



## Instalación

```
pip install -r requirements.txt
```

## Uso

```
+-----------+--------------------------------------------------------------------------------------+--------------------------------------------------------+
| Argumento |                                     Descripción                                      |                 Ejemplo                                |
+-----------+--------------------------------------------------------------------------------------+--------------------------------------------------------+
|     -b    | Indique el RUT inicial. Ej: 12345678                                                 | python3 rutchile.py -b 12000000 -e 13123123 -f         |
|     -e    | Indique el RUT final.   Ej: 12345678                                                 | python3 rutchile.py -b 12000000 -e 13123123 -f         |
|     -f    | Generar diccionario de RUTs con puntos, guión y dígito verificador Ej: 12.345.678-9  | python3 rutchile.py -b 12000000 -e 13123123 -f         |
|     -d    | Generar diccionario de RUTs solo con dígito verificador Ej: 12345678-9               | python3 rutchile.py -b 12000000 -e 13123123 -d         |
|     -l    | Generar diccionario de RUTs sin puntos ni guión con dígito verificador Ej: 123456789 | python3 rutchile.py -b 12000000 -e 13123123 -l         |
|     -m    | Generar diccionario de RUTs sin dígito verificador Ej: 12345678                      | python3 rutchile.py -b 12000000 -e 13123123 -m         |
|     -r    | Generar diccionario de RUTs randoms, 10 por default                                  | python3 rutchile.py -b 12000000 -e 13123123 -m -r      |
|     -c    | Especifica la cantidad de RUTs a generar (10 por default). Requiere -r               | python3 rutchile.py -b 12000000 -e 13123123 -m -r -c 50|
+-----------+--------------------------------------------------------------------------------------+--------------------------------------------------------+
```

## EJEMPLOS

```

python3 rutchile.py  -b 7000000 -e 8000000 -f
python3 rutchile.py  -b 7000000 -e 8000000 -f > ruts_chilenos.txt
python3 rutchile.py  -b 7000000 -e 8000000 -f > ruts_chilenos.txt | tee

python3 rutchile.py  -b 10000000 -e 12123123 -f
python3 rutchile.py  -b 10000000 -e 12123123 -f > ruts_chilenos.txt
python3 rutchile.py  -b 10000000 -e 12123123 -f > ruts_chilenos.txt | tee

python3 rutchile.py  -b 16000000 -e 17000000 -f
python3 rutchile.py  -b 16000000 -e 17000000 -f > ruts_chilenos.txt
python3 rutchile.py  -b 16000000 -e 17000000 -f > ruts_chilenos.txt | tee

python3 rutchile.py  -b 7000000 -e 8000000 -d -r -c100 
python3 rutchile.py  -b 7000000 -e 8000000 -d -r -c100 > ruts_chilenos.txt
python3 rutchile.py  -b 7000000 -e 8000000 -d -r -c100 > ruts_chilenos.txt | tee




$ python3 rutchile.py  -b 16000000 -e 17000000 -r -d
16003781-4
16028930-9
16139328-2
16174943-5
16220776-8
16325952-4
16498210-6
16587115-4
16782798-5
16805911-6

```
