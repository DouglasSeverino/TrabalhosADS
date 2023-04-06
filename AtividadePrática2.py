# Bloco de Identificação:
print('\nBem-vindo a Sorveteria.\n')

# Bloco de cardápio:
print('|' + '-' * 43 + 'CARDÁPIO' + '-' * 43 + '|')
print('| CÓDIGO | DESCRIÇÃO            | TAMANHO P (500ml) | TAMANHO M (750ml) | TAMANHO G (1000ml)   |')
print('|   TR   | SABORES TRADICIONAIS |      R$ 6,00      |      R$ 10,00     |     R$ 18,00         |')
print('|   ES   | SABORES ESPECIAIS    |      R$ 7,00      |      R$ 12,00     |     R$ 21,00         |')
print('|   PR   | SABORES PREMIUM      |      R$ 8,00      |      R$ 14,00     |     R$ 24,00         |')
print('|' + '--' * 47 + '|')

preco = 0
while True:  # Bloco de validação de dados digitados pelo usuário:
    c = input('\nQual o código do tipo de sorvete?[ TR | ES | PR ]: ')
    cod = c.upper()
    t = input('\nQual o tamanho do pote de sorvete?[ P | M | G ]: ')
    tam = t.upper()

    if cod == 'TR':     # Bloco do Sabor Tradicional e os seus valores
        if tam == 'P':
            preco += 6
            print('Você escolheu sabor TRADICIONAL no tamanho P de R$ 6,00.')
        elif tam == 'M':
            preco += 10
            print('Você escolheu sabor TRADICIONAL no tamanho M de R$ 10,00.')
        elif tam == 'G':
            preco += 18
            print('Você escolheu sabor TRADICIONAL no tamanho G de R$ 18,00.')
        else:
            print('Tamanho incorreto. Por favor, tente novamente...')
            continue
    elif cod == 'ES':     # Bloco do Sabor Especial e os seus valores
        if tam == 'P':
            preco += 7
            print('Você escolheu sabor ESPECIAL no tamanho P de R$ 7,00.')
        elif tam == 'M':
            preco += 12
            print('Você escolheu sabor ESPECIAL no tamanho M de R$ 12,00.')
        elif tam == 'G':
            preco += 21
            print('Você escolheu sabor ESPECIAL no tamanho G de R$ 21,00.')
        else:
            print('Tamanho incorreto. Por favor, tente novamente...')
            continue
    elif cod == 'PR':     # Bloco do Sabor Premium e os seus valores
        if tam == 'P':
            preco += 8
            print('Você escolheu sabor PREMIUM no tamanho P de R$ 8,00.')
        elif tam == 'M':
            preco += 14
            print('Você escolheu sabor PREMIUM no tamanho M de R$ 14,00.')
        elif tam == 'G':
            preco += 24
            print('Você escolheu sabor PREMIUM no tamanho G de R$ 24,00.')
        else:
            print('Tamanho incorreto. Por favor, tente novamente...')
            continue
    else:
        print('Código inválido. Tente novamente...')    # Retorna ao início do laço caso um dos valores for incorreto
        continue

    try:    # Bloco do pedido adicional
        a = input('\nDeseja adicionar mais?\n[ Pressione Enter para continuar | Pressione N para finalizar ]: ')
        adc = a.upper()
        if adc == 'S':
            preco += 0
            continue
        elif adc == 'N':
            print('O preco total é de R$ {} reais.'.format(preco))
            print('Obrigado por comprar em nossa loja! Volte sempre!')
            break
    except TypeError:
        print('Apenas S para Sim ou N para Não. Tente novamente...')
