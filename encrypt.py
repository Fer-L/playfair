import cipher


def encrypt(message, matrix):
    message = cipher.separate_pairs(message)
    ciphertext = []

    for pair in message:
        # Atribui o primeiro par de letras em variáveis
        first_pair = cipher.find_position(pair[0], matrix)
        second_pair = cipher.find_position(pair[1], matrix)

        # Faz as trocas para a primeira regra
        first_pair, second_pair = changes_rule_one(first_pair, second_pair)
        second_pair, first_pair = changes_rule_one(second_pair, first_pair)

        # Faz as trocas para a segunda regra
        first_pair, second_pair = changes_rule_two(first_pair, second_pair)
        second_pair, first_pair = changes_rule_two(second_pair, first_pair)

        # Faz as trocas para a terceira regra
        first_pair, second_pair = changes_rule_three(first_pair, second_pair)

        # Adiciona os valores alterados na cifra final
        ciphertext.append(matrix[first_pair[0], first_pair[1]])
        ciphertext.append(matrix[second_pair[0], second_pair[1]])

    ciphertext_text = [''.join(char) for char in ciphertext]
    ciphertext_text = ''.join(ciphertext_text)

    return ciphertext_text


def decrypt(message, matrix):
    message = cipher.check_double_letters(message)
    message = cipher.separate_pairs(message)

    decrypted_message = []

    for pair in message:
        # Atribui o primeiro par de letras em variáveis
        first_pair = cipher.find_position(pair[0], matrix)
        second_pair = cipher.find_position(pair[1], matrix)

        # Faz as trocas para a primeira regra
        first_pair, second_pair = changes_rule_one(first_pair, second_pair, False)
        second_pair, first_pair = changes_rule_one(second_pair, first_pair, False)

        # Faz as trocas para a segunda regra
        first_pair, second_pair = changes_rule_two(first_pair, second_pair, False)
        second_pair, first_pair = changes_rule_two(second_pair, first_pair, False)

        # Faz as trocas para a terceira regra
        first_pair, second_pair = changes_rule_three(first_pair, second_pair)

        # Adiciona os valores alterados na cifra final
        decrypted_message.append(matrix[first_pair[0], first_pair[1]])
        decrypted_message.append(matrix[second_pair[0], second_pair[1]])

    decrypted_message_text = [''.join(char) for char in decrypted_message]
    decrypted_message_text = ''.join(decrypted_message_text)

    return decrypted_message_text


def changes_rule_one(pair1, pair2, encryption=True):
    if pair1[0] == pair2[0]:
        if encryption:
            if pair1[1] == 4:
                pair1[1] = 0
            else:
                pair1[1] += 1
        else:
            if pair1[1] == 0:
                pair1[1] = 4
            else:
                pair1[1] -= 1
    return pair1, pair2


def changes_rule_two(pair1, pair2, encryption=True):
    if pair1[1] == pair2[1]:
        if encryption:
            if pair1[0] == 4:
                pair1[0] = 0
            else:
                pair1[0] += 1
        else:
            if pair1[0] == 0:
                pair1[0] = 4
            else:
                pair1[0] -= 1
    return pair1, pair2


def changes_rule_three(pair1, pair2):
    pair1_copy = pair1.copy()
    pair2_copy = pair2.copy()

    if pair1[0] != pair2[0] and pair1[1] != pair2[1]:
        # Altera a posição da primeira letra
        pair1[1] = pair2_copy[1]

        # Altera a posição da segunda letra
        pair2[1] = pair1_copy[1]
    return pair1, pair2
