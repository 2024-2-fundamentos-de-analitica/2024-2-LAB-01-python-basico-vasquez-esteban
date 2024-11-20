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
    """Mapear la secuencia a (Letra, 1)..."""

    return [(sequence[i][1][0], int(sequence[i][1][1])) for i in range(len(sequence))]


def shuffle_and_sort(sequence):
    """Sortear letras"""
    return sorted(sequence, key=lambda x: x[0])


def reducer(sequence):
    """Reduce to (Letter, Max, Min)"""

    seq = {}

    for k, v in sequence:
        if k not in seq:
            seq[k] = [v, v]
        else:
            if v >= seq[k][0]:
                seq[k][0] = max(seq[k][0], v)
            else:
                seq[k][1] = min(seq[k][1], v)

    return [(k, v[0], v[1]) for k, v in seq.items()]


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    seq = load_input("files/input")
    seq = line_preprocessing(seq)
    seq = mapper(seq)
    seq = shuffle_and_sort(seq)
    seq = reducer(seq)

    return seq
