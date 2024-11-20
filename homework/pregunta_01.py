"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import fileinput
import string
from glob import glob


def load_input(input_directory):
    """Funcion load_input"""
    sequence = []

    files = glob(f"{input_directory}/*")

    with fileinput.input(files=files) as f:
        for line in f:
            sequence.append((fileinput.filename(), line))

    return sequence


def line_preprocessing(sequence):
    """Line Preprocessing"""
    sequence = [
        (
            k,
            v.translate(str.maketrans("", "", string.punctuation))
            .lower()
            .strip()
            .split("\t"),
        )
        for k, v in sequence
    ]

    return sequence


def reducer(sequence):
    """Column sum"""

    return sum(int(row[1][1]) for row in sequence)


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    seq = load_input("files/input")
    seq = line_preprocessing(seq)
    return reducer(seq)
