secret_number = 20

while True:
    number = input('Adivinhe o numero: ')

    try:
        number = int(number)
    except:
        print('Numero errado')
        continue

    if number != secret_number:
        if number > secret_number:
            print(number, 'é maior que o esperado')

        elif number < secret_number:
            print(number, 'Menor do que o esperado')

    else:
        print('Você acertou o número')
        break
