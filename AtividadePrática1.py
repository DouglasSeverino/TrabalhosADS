# Bloco de Identificação:
print('|' + '--' * 10 + '|' + '\n|     ATACADO DS     |\n' + '|' + '--' * 10 + '|')
print('Seja bem-vindo à loja')

while True:  # Criei uma condição que repete enquanto o valor não for o verdadeiro
    try:
        prod = float(input(print('\nDigite o valor do produto R$ ')))
        qtd = int(input(print('\nDigite a quantidade do produto: ')))
    except ValueError:
        print('Dado incorreto. Tente novamente...')
        continue  # Usei o continue para dar continuidade na condição abaixo após a verificação acima
    if qtd <= 11:
        soma1 = qtd * prod + 30
        soma2 = qtd * prod
        print('Valor sem frete: R$ R$ {:.2f}'.format(soma2))
        print('Valor com frete: R$ {:.2f} (Frete R$ 30.00)'.format(soma1))
        break  # Usei o break para finalizar o programa após os cálculos
    elif qtd <= 101:
        soma1 = qtd * prod + 60
        soma2 = qtd * prod
        print('Valor sem frete: R$ {:.2f}'.format(soma2))
        print('Valor com frete: R$ {:.2f} (Frete R$ 60.00)'.format(soma1))
        break
    elif qtd <= 1000:
        soma1 = qtd * prod + 120
        soma2 = qtd * prod
        print('Valor sem frete: R$ {:.2f}'.format(soma2))
        print('Valor com frete: R$ {:.2f} (Frete R$ 120.00)'.format(soma1))
        break
    elif qtd >= 1001:
        soma1 = qtd * prod + 240
        soma2 = qtd * prod
        print('Valor sem frete: R$ {:.2f}'.format(soma2))
        print('Valor com frete: R$ {:.2f} (Frete R$ 240.00)'.format(soma1))
        break
