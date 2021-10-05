import numpy as np


def check_double_letters(text):
    output = ''
    for index in range(0, len(text), 2):
        pair = text[index:index + 2]
        if len(pair) > 1 and pair[0] == pair[1]:
            output += pair[0] + 'X' + pair[1]
        else:
            output += pair
    if len(output) % 2:
        output += 'X'
    return output


def read_message(file):
    with open(file, "r") as input_file:
        text = input_file.readlines()
        text_str = text[0]
        text_str = text_str.upper().replace('Z', 'Y').replace(' ', '')
        text_str = check_double_letters(text_str)

        return text_str


def matrix_gen(key='', alphabet_user='YQDLGMJXFUVWCPBOSKRETHNAI'):
    table = []
    # default_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXY'
    for char in key.upper():
        if char not in table and char in alphabet_user:
            table.append(char)

    for char in alphabet_user:
        if char not in table:
            table.append(char)
    return table


def separate_pairs(message):
    separated_pairs = list((message[index:index + 2]) for index in range(0, len(message), 2))
    return separated_pairs


def find_position(find, matriz):
    coords = [np.where(matriz == find)]

    row = int(coords[0][0])
    column = int(coords[0][1])

    position = [row, column]

    return position


def format_matrix(matrix):
    matrix = np.array(matrix).reshape(5, 5)
    return matrix
