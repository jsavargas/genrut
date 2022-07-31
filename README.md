

# Descripción

**rutchile.py** es una herramienta que permite generar diccionarios con **ruts chilenos válidos** en distintos formator para nuestros ejercicios de Ethical Hacking.



## Instalación

```
pip install -r requirements.txt
```

## Uso

```
+-----------+--------------------------------------------------------------------------------------+------------------------------------------------+
| Argumento |                                     Descripción                                      |                 Ejemplo                        |
+-----------+--------------------------------------------------------------------------------------+------------------------------------------------+
|     -b    | Indique el RUT inicial. Ej: 12345678                                                 | python3 rutchile.py -b 12000000 -e 13123123 -f |
|     -e    | Indique el RUT final.   Ej: 12345678                                                 | python3 rutchile.py -b 12000000 -e 13123123 -f |
|     -f    | Generar diccionario de RUTs con puntos, guión y dígito verificador Ej: 12.345.678-9  | python3 rutchile.py -b 12000000 -e 13123123 -f |
|     -d    | Generar diccionario de RUTs solo con dígito verificador Ej: 12345678-9               | python3 rutchile.py -b 12000000 -e 13123123 -d |
|     -l    | Generar diccionario de RUTs sin puntos ni guión con dígito verificador Ej: 123456789 | python3 rutchile.py -b 12000000 -e 13123123 -l |
|     -m    | Generar diccionario de RUTs sin dígito verificador Ej: 12345678                      | python3 rutchile.py -b 12000000 -e 13123123 -m |
+-----------+--------------------------------------------------------------------------------------+------------------------------------------------+
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

```
