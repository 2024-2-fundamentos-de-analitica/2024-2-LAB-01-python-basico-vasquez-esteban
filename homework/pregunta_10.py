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
        (elm[1][0], len(elm[1][3].split(",")), len(elm[1][4].split(",")))
        for elm in sequence
    ]


def shuffle_and_sort(sequence):
    """Sortear letras"""
    return sequence


def reducer(sequence):
    """Reduce to (Key, Max, Min)"""

    return sequence


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    seq = load_input("files/input")
    seq = line_preprocessing(seq)
    seq = mapper(seq)
    seq = shuffle_and_sort(seq)
    seq = reducer(seq)

    return seq
