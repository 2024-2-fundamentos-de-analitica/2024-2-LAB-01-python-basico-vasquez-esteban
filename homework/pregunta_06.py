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
        (k, int(v))
        for elm in sequence
        for k, v in (item.split(":") for item in elm[1][4].split(","))
    ]


def shuffle_and_sort(sequence):
    """Sortear letras"""
    return sorted(sequence, key=lambda x: x[0])


def reducer(sequence):
    """Reduce to (Key, Max, Min)"""

    seq = {}

    for k, v in sequence:
        if k not in seq:
            seq[k] = [v, v]
        else:
            if v >= seq[k][0]:
                seq[k][0] = max(seq[k][0], v)
            else:
                seq[k][1] = min(seq[k][1], v)

    return [(k, v[1], v[0]) for k, v in seq.items()]


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    seq = load_input("files/input")
    seq = line_preprocessing(seq)
    seq = mapper(seq)
    seq = shuffle_and_sort(seq)
    seq = reducer(seq)

    return seq


pregunta_06()
