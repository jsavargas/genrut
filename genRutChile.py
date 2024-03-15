#!/usr/bin/python3
# _*_ coding: utf8 _*_


import sys
import random
import argparse


def generar_rut_secuencial(
    inicio,
    fin,
    incluir_puntos_miles=True,
    incluir_digito_verificador=True,
    incluir_guion_digito_verificador=True,
):
    for numero in range(inicio, fin + 1):
        if incluir_digito_verificador:
            digito_verificador = calcular_digito_verificador(numero)
        else:
            digito_verificador = ""

        separador_digito_verificador = (
            "-"
            if incluir_guion_digito_verificador and incluir_digito_verificador
            else ""
        )
        rut_numero = (
            f"{numero:,}".replace(",", ".") if incluir_puntos_miles else f"{numero}"
        )

        rut = f"{rut_numero}{separador_digito_verificador}{digito_verificador}"
        print(rut)


def generar_rut_aleatorio(
    inicio,
    fin,
    incluir_puntos_miles=True,
    incluir_digito_verificador=True,
    incluir_guion_digito_verificador=True,
):
    numero = random.randrange(inicio, fin + 1)

    if incluir_digito_verificador:
        digito_verificador = calcular_digito_verificador(numero)
    else:
        digito_verificador = ""

    separador_digito_verificador = (
        "-" if incluir_guion_digito_verificador and incluir_digito_verificador else ""
    )
    rut_numero = (
        f"{numero:,}".replace(",", ".") if incluir_puntos_miles else f"{numero}"
    )

    rut = f"{rut_numero}{separador_digito_verificador}{digito_verificador}"
    return rut


def calcular_digito_verificador(numero):
    numero_str = str(numero)
    factor = 2
    suma = 0

    for digito in reversed(numero_str):
        resultado = int(digito) * factor
        suma += resultado
        factor = 2 if factor == 7 else factor + 1

    digito_verificador = (11 - suma % 11) % 11

    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador

    return str(digito_verificador) if digito_verificador < 10 else "0"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generador de RUTs aleatorios sin repetición"
    )
    parser.add_argument(
        "--inicio", "-i", type=int, help="Número de inicio del rango", required=True
    )
    parser.add_argument(
        "--fin", "-f", type=int, help="Número de fin del rango", required=True
    )
    parser.add_argument("--cantidad", "-c", type=int, help="Cantidad de RUTs a generar")
    parser.add_argument(
        "--incluir_puntos_miles",
        "-p",
        action="store_true",
        help="Incluir puntos de miles en los RUTs generados",
    )
    parser.add_argument(
        "--incluir_digito_verificador",
        "-d",
        action="store_true",
        help="Incluir el dígito verificador en los RUTs generados",
    )
    parser.add_argument(
        "--incluir_guion_digito_verificador",
        "-gd",
        action="store_true",
        help="Incluir guión con el dígito verificador en los RUTs generados",
    )

    args = parser.parse_args()

    # Validar que la diferencia entre fin e inicio sea igual o mayor a la cantidad
    if args.cantidad and not (
        args.inicio
        and args.fin
        and args.cantidad
        and args.fin - args.inicio >= args.cantidad
    ):
        print(
            "Error: La diferencia entre fin e inicio debe ser igual o mayor a la cantidad."
        )
        sys.exit(1)

    if not args.inicio or not args.fin:
        print(
            "Uso: python script.py --inicio/-i <inicio> --fin/-f <fin> --cantidad/-c <cantidad> [--incluir_puntos_miles/-p] [--incluir_digito_verificador/-d] [--incluir_guion_digito_verificador/-gd]"
        )
        sys.exit(1)

    if args.incluir_guion_digito_verificador:
        args.incluir_digito_verificador = True

    inicio = args.inicio
    fin = args.fin
    cantidad_ruts = args.cantidad
    incluir_puntos_miles = args.incluir_puntos_miles
    incluir_digito_verificador = args.incluir_digito_verificador
    incluir_guion_digito_verificador = args.incluir_guion_digito_verificador

    if inicio >= fin:
        print("El inicio debe ser menor que el fin.")
    elif not args.cantidad:
        ruts_generados = generar_rut_secuencial(
            inicio,
            fin,
            incluir_puntos_miles=incluir_puntos_miles,
            incluir_digito_verificador=incluir_digito_verificador,
            incluir_guion_digito_verificador=incluir_guion_digito_verificador,
        )
    else:
        ruts_generados = set()

        while len(ruts_generados) < cantidad_ruts:
            nuevo_rut = generar_rut_aleatorio(
                inicio,
                fin,
                incluir_puntos_miles=incluir_puntos_miles,
                incluir_digito_verificador=incluir_digito_verificador,
                incluir_guion_digito_verificador=incluir_guion_digito_verificador,
            )
            ruts_generados.add(nuevo_rut)

        ruts_ordenados = sorted(ruts_generados)

        for rut in ruts_ordenados:
            print(rut)
