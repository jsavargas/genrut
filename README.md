

# Descripción

**genRutChile.py** es una herramienta que permite generar diccionarios con **ruts chilenos válidos** en distintos formatos para nuestros ejercicios de Ethical Hacking.


| Opción                                      | Descripción                                                         |
|---------------------------------------------|---------------------------------------------------------------------|
| `--inicio`, `-i`                            | Número de inicio del rango. (Requerido)                             |
| `--fin`, `-f`                               | Número de fin del rango. (Requerido)                                |
| `--cantidad`, `-c`                          | Cantidad de RUTs a generar.                                         |
| `--incluir_puntos_miles`, `-p`              | Incluir puntos de miles en los RUTs generados.                      |
| `--incluir_digito_verificador`, `-d`        | Incluir el dígito verificador en los RUTs generados.                |
| `--incluir_guion_digito_verificador`, `-gd` | Incluir guión con el dígito verificador en los RUTs generados.      |


## Uso

### Rango sin incluir puntos ni dígito verificador:

| Opción             | Descripción                                      |
|--------------------|--------------------------------------------------|
| `--inicio`, `-i`   | Número de inicio del rango. (Requerido)          |
| `--fin`, `-f`      | Número de fin del rango. (Requerido)             |

**Ejemplo:**
```bash
python3 genRutChile.py --inicio 10000000 --fin 10000010 > 10.txt

10000000
10000001
10000002
...
10000010
```

### Rango con puntos de miles:

| Opción             | Descripción                                      |
|--------------------|--------------------------------------------------|
| `--inicio`, `-i`   | Número de inicio del rango. (Requerido)          |
| `--fin`, `-f`      | Número de fin del rango. (Requerido)             |
| `--incluir_puntos_miles`, `-p`| Incluir puntos de miles en los RUTs generados.|

**Ejemplo:**
```bash
python3 genRutChile.py --inicio 10000000 --fin 10000010 --incluir_puntos_miles > rut.txt

10.000.000
10.000.001
10.000.002
...
10.000.010
```

### Rango sin guión y con dígito verificador:

| Opción                                | Descripción                                      |
|---------------------------------------|--------------------------------------------------|
| `--inicio`, `-i`                      | Número de inicio del rango. (Requerido)          |
| `--fin`, `-f`                         | Número de fin del rango. (Requerido)             |
| `--incluir_digito_verificador`, `-d`  | Incluir el dígito verificador en los RUTs generados.|

**Ejemplo:**
```bash
python3 genRutChile.py --inicio 10000000 --fin 10000010 --incluir_digito_verificador > rut.txt

100000008
100000016
100000024
...
100000105
```

### Rango con puntos de miles y dígito verificador:

| Opción                                | Descripción                                      |
|---------------------------------------|--------------------------------------------------|
| `--inicio`, `-i`                      | Número de inicio del rango. (Requerido)          |
| `--fin`, `-f`                         | Número de fin del rango. (Requerido)             |
| `--incluir_puntos_miles`, `-p`        | Incluir puntos de miles en los RUTs generados.   |
| `--incluir_digito_verificador`, `-d`  | Incluir el dígito verificador en los RUTs generados.|

**Ejemplo:**
```bash
python3 genRutChile.py --inicio 10000000 --fin 10000010 --incluir_puntos_miles --incluir_digito_verificador > rut.txt

10.000.0008
10.000.0016
10.000.0024
...
10.000.0105
```

### Rango con guión y dígito verificador:

| Opción                                  | Descripción                                      |
|-----------------------------------------|--------------------------------------------------|
| `--inicio`, `-i`                        | Número de inicio del rango. (Requerido)          |
| `--fin`, `-f`                           | Número de fin del rango. (Requerido)             |
| `--incluir_guion_digito_verificador`, `-gd` | Incluir guión con el dígito verificador en los RUTs generados.|

**Ejemplo:**
```bash
python3 genRutChile.py --inicio 10000000 --fin 10000010 --incluir_guion_digito_verificador > rut.txt

10000000-8
10000001-6
10000002-4
...
10000010-5
```

### Rango con todas las opciones:

| Opción                                  | Descripción                                      |
|-----------------------------------------|--------------------------------------------------|
| `--inicio`, `-i`                        | Número de inicio del rango. (Requerido)          |
| `--fin`, `-f`                           | Número de fin del rango. (Requerido)             |
| `--cantidad`, `-c`                      | Cantidad de RUTs a generar.                      |
| `--incluir_puntos_miles`, `-p`          | Incluir puntos de miles en los RUTs generados.   |
| `--incluir_digito_verificador`, `-d`    | Incluir el dígito verificador en los RUTs generados.|
| `--incluir_guion_digito_verificador`, `-gd` | Incluir guión con el dígito verificador en los RUTs generados.|

**Ejemplo:**
```bash
python3 genRutChile.py --inicio 10000000 --fin 10000010 --cantidad 5 --incluir_puntos_miles --incluir_digito_verificador --incluir_guion_digito_verificador > rut.txt

10.000.001-6
10.000.002-4
10.000.005-9
10.000.009-1
10.000.010-5
```




