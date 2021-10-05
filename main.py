from time import sleep
import cipher as cp
import encrypt as en

counter = res = 0

choice = {
    1: 'Escolher uma tabela de cifra nova',
    2: 'Introduzir uma mensagem para cifrar (de um arquivo ou do stdin)',
    3: 'Ver a mensagem cifrada',
    4: 'Decifrar a mensagem',
    5: 'Ver o alfabeto',
    6: 'Terminar'
}
# Gera uma matriz inicial
base_matrix_array = cp.matrix_gen()
base_matrix = cp.format_matrix(base_matrix_array)

user_choices = {
    'key': '',
    'alphabet': 'YQDLGMJXFUVWCPBOSKRETHNAI',
    'message': '',
    'encrypted': '',
    'decrypted': '',
    'matriz': base_matrix
}

if __name__ == '__main__':
    while True:
        print()
        print("=" * 30)
        print()

        print('Faça uma escolha:')
        for key, value in choice.items():
            print(key, value)
        print()
        res = int(input("Por favor, digite a sua resposta: "))
        if res >= 7:
            print('Número incorreto.')
            sleep(2.5)
            print('Tente novamente.')
            sleep(2.5)
            continue

        if res == 1:
            choose_key = input('Deseja adicionar uma chave? [S/N] ').upper().strip()
            if choose_key in 'S':
                key = input('Insira a chave: ').upper().strip()
                user_choices['key'] = key
                print('Chave adicionada com sucesso!')
            choose_alphabet = input('Deseja adicionar um alfabeto? [S/N] ').upper().strip()
            if choose_alphabet in 'S':
                alphabet = input('Insira o alfabeto: ').upper().strip()
                user_choices['alphabet'] = alphabet
                print('Alfabeto adicionado com sucesso!')
            print('Gerando a matriz...')
            sleep(0.5)

            if user_choices['alphabet'] == '':
                matriz_array = cp.matrix_gen(user_choices['key'])
            else:
                matriz_array = cp.matrix_gen(user_choices['key'], user_choices['alphabet'])
            matriz = cp.format_matrix(matriz_array)

            print('Matriz gerada com sucesso!')
            print('A matriz foi escrita no arquivo "matriz.txt"')
            print('Para visualizar o novo arquivo, é necessário parar a atual execução do programa.')
            sleep(2.0)

            user_choices['matriz'] = matriz

            with open("matriz.txt", "w+") as file:
                file.write(f'{user_choices["matriz"]}')
        if res == 2:
            print("Insira a mensagem em um arquivo .txt com o nome 'mensagem.txt', e salve.")
            sleep(1.0)
            message = cp.read_message("mensagem.txt")
            user_choices['message'] = message
            print('Mensagem adicionada com sucesso!')
            sleep(2.5)
        if res == 3:
            if len(user_choices['message']) > 0:
                user_choices['encrypted'] = en.encrypt(user_choices['message'], user_choices['matriz'])
                print('Encriptando...')
                sleep(1.5)
                with open("encrypted.txt", "w+") as file:
                    file.write(f'{user_choices["encrypted"]}')
                print('Mensagem encriptada com sucesso!')
                print('A mensagem foi guardada no arquivo "encrypted.txt"')
                print('Para visualizar o novo arquivo, é necessário parar a atual execução do programa.')
                sleep(2.5)
            else:
                print('É necessário definir uma mensagem antes de criptografar!')
                sleep(1.5)
                continue
        if res == 4:
            if len(user_choices['encrypted']) > 0:
                print('Decifrando a mensagem...')
                sleep(1.5)
                user_choices['decrypted'] = en.decrypt(user_choices['encrypted'], user_choices['matriz'])
                print('Mensagem decifrada com sucesso!')
                print(f'A mensagem decifrada é {user_choices["decrypted"]}.')
                sleep(2.5)
            else:
                print('Não há nenhuma mensagem criptografada..')
                sleep(1.5)
                continue
        if res == 5:
            print(f'O atual alfabeto é {user_choices["alphabet"]}.')
            sleep(2.5)
        if res == 6:
            break
