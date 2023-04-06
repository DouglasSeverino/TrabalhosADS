
cliente = []

def cliente_novo():
    print("\nSeja bem-vindo! Estamos muito felizes em ser escolhido por você!"
          + "\nPrecisamos pegar algumas informações para poder entrar em contato."
          + "\nApenas duas coisas e ligaremos o mais rápido possível!")
    nome = str(input("Digite seu nome: "))
    telefone = str(input("Digite o número do teu telefone com DDD: "))
    cliente.append({nome, telefone})

def cliente_empotencial():
    print("\nDeseja fechar o orçamento conosco? \nSomos a melhor empresa de limpeza da região,"
          + "\nbuscamos eficácia e excelência em nosso trabalho.")
    decisao = int(input("Digite '1' para SIM para fechar o contrato \nou '0' para NÃO para encerrar o programa. "))
    if  decisao == 1:
        cliente_novo()
        print("\nObrigado! Fique de olho no celular, pois ligaremos nos próximos minutos.")
    elif decisao == 0:
                print("Obrigado pela sua visita. Volte sempre!")
                return
    else:
       print("Não entendi! Tente novamente.")

def orcamento():    # Função de Orçamento de Valores
    avalor = 0
    mvalor = 0      # Variáveis Globais
    lvalor = 0
    lpz = ''
    while True:
        try:    # Bloco de verificação de metragem
            metragem = float(input('\n>> Qual é a metragem em m² da casa? '))
            if (metragem >= 30) and (metragem <= 299):
                mvalor = mvalor + (0.3 * metragem) + 60
                print('É necessário contratar 1 pessoa.')
                break
            if (metragem >= 300) and (metragem <= 699):
                mvalor += (0.5 * metragem) + 120
                print('É necessário contratar 2 pessoa.')
                break
            else:
                print('\nNão trabalhamos com limpezas em casas com metragem abaixo de 30m² ou acima de 700m².\n')
                continue
        except:
            print('Opção inválida. Somente números.')
            return

    while True:
        try:       # Bloco de verificação de tipo de limpeza
            lpz = input('\n>> Temos o tipo de limpeza Básica (B), que é indicada \npara sujeiras semanais'
                        ' ou quinzenais, ou Completa (C), \nque é indicada para sujeiras antigas e/ou não rotineiras.'
                        '\n\nQual é o tipo de limpeza? [ B | C ]: ')
            limpeza = lpz.upper()
            if limpeza == 'B':
                lvalor += 1
                print('Você selecionou a Limpeza Básica.')
                break
            if limpeza == 'C':
                lvalor += 1.30
                print('Você selecionou a Limpeza Completa.')
                break
            else:
                print('Opção inválida. Apenas B para Básica \nou C para Completa. Tente novamente...\n')
                continue
        except ValueError:
            print('Opção inválida. Tente novamente...')

    while True:
        try:    # Bloco de adicionais e os seus valores
            adc = int(input('\n>> Você deseja um adicional?\n'
                            '0 - Não desejo mais nada. (Encerrar)\n'
                            '1 - Passar 10 peças de roupas: R$ 10,00\n'
                            '2 - Limpeza de 1 Forno/Microondas: R$ 12,00\n'
                            '3 - Limpeza de 1 Geladeira/Freezer: R$ 20,00\n'))
            if adc == 1:
                avalor += 10
                print('Você escolheu o adicional de "Passar 10 peças de roupas".')
                continue
            elif adc == 2:
                avalor += 12
                print('Você escolheu o adicional de "Limpeza de 1 Forno/Microondas".')
                continue
            elif adc == 3:
                avalor += 20
                print('Você escolheu o adicional de "Limpeza de 1 Geladeira/Freezer".')
                continue
            elif adc == 0:
                print('Finalizando o pedido...')
                break
            else:
                print('Número inválido. Tente novamente...')
                continue
        except ValueError:
            print('Apenas número entre 0 e 3. Tente novamente...')

    # Bloco de valor total do orçamento
    total = (mvalor * lvalor) + avalor
    print('\nO valor total deste orçamento é de R$ {:.2f}.\n'
          '\nMetragem: {:.2f} * Tipo de Limpeza: {} + Adicional: {:.2f}'.format(total, lvalor, mvalor, avalor))
    cliente_empotencial()

print("*--------------- Boas vindas a DS Serviços de Limpeza LTDA ---------------*")
orcamento()  # Início do programa
print("*-------------------------------------------------------------------------*")
