"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import fileinput
from glob import glob


def load_input(input_directory):
    """Cargar input"""

    sequence = []

    files = glob(f"{input_directory}/*")

    with fileinput.input(files=files) as f:
        for line in f:
            sequence.append((fileinput.filename(), line))

    return sequence


def line_preprocessing(sequence):
    """Preprocesar líneas"""
    sequence = [
        (k, v.translate(str.maketrans("", "", "")).strip().split("\t"))
        for k, v in sequence
    ]

    return sequence


def mapper(sequence):
    """Mapear la secuencia a (dict_key, dict_val)..."""

    return [
        (elm[1][0], int(v))
        for elm in sequence
        for _, v in (item.split(":") for item in elm[1][4].split(","))
    ]


def shuffle_and_sort(sequence):
    """Sortear letras"""
    return sorted(sequence, key=lambda x: x[0])


def reducer(sequence):
    """Reduce to (Key, Max, Min)"""

    seq = {}

    for k, v in sequence:
        if k not in seq:
            seq[k] = 0
        seq[k] += v

    return seq


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    seq = load_input("files/input")
    seq = line_preprocessing(seq)
    seq = mapper(seq)
    seq = shuffle_and_sort(seq)
    seq = reducer(seq)

    return seq
