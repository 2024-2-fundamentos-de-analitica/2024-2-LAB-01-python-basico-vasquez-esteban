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
    """Cargar input"""

    sequence = []

    files = glob(f"{input_directory}/*")

    with fileinput.input(files=files) as f:
        for line in f:
            sequence.append((fileinput.filename(), line))

    return sequence


def line_preprocessing(sequence):
    """Preprocess lines"""
    sequence = [
        (
            k,
            v.translate(str.maketrans("", "", string.punctuation)).strip().split("\t"),
        )
        for k, v in sequence
    ]

    return sequence


def mapper(sequence):
    """Mapear la secuencia a (Letra, 1)..."""

    return [(sequence[i][1][0], 1) for i in range(len(sequence))]


def shuffle_and_sort(sequence):
    """Sortear letras"""
    return sorted(sequence, key=lambda x: x[0])


def reducer(sequence):
    """Reduce to (Letter, Num of occur )"""

    seq = {}

    for k, _ in sequence:
        if k not in seq:
            seq[k] = 0
        seq[k] += 1

    return list(seq.items())


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    seq = load_input("files/input")
    seq = line_preprocessing(seq)
    seq = mapper(seq)
    seq = shuffle_and_sort(seq)
    seq = reducer(seq)

    return seq
