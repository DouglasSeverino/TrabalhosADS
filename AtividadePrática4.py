print('Bem-vindo(a) ao Controle de Colaboradores\n')
print('*****' * 14 + '\n' + '--' * 14 + 'MENU PRINCIPAL' + '--' * 14)

# ------------------------- Início das Variáveis Globais -----------------------------
lista_colaborador = []
id_colaborador = 0
# ------------------------- Fim das Variáveis Globais --------------------------------


# ------------------------- Início das Funções ---------------------------------------
def cadastrar_colaborador(id):
    while True:
        print('\nBem-vindo(a) ao Cadastro de Colaboradores')
        print(f'ID do Colaborador(a): {id}')
        nome = input('Nome do(a) colaborador(a): ')
        setor = input('Setor: ')
        salario = float(input('Salário: '))
        colaborador = {'id': id,
                       'nome': nome,
                       'setor': setor,
                       'salario': salario}
        id += 1
        lista_colaborador.append(colaborador.copy())
        finalizar = input('Deseja cadastrar mais um(a) colaborador(a) [ S | N ]: ')
        if finalizar.upper() in 'N':
            break
        elif finalizar.upper() not in 'S':
            print('Digite S para SIM ou N para NÃO.')
            continue
    return


def consultar_colaborador():
    global menu
    while True:
        print('\nBem-vindo(a) a Consulta de Colaboradores')
        menu = int(input(print('Selecione uma opção:'
                               '\n1 - Consultar Todos os Colaboradores'
                               '\n2 - Consultar Colaborador(a) por ID'
                               '\n3 - Consultar Colaborador(a) por Setor'
                               '\n4 - Retornar ao Menu Principal'
                               '\nOpção: ')))
        if menu == 1:
            print('\nVocê escolheu a opção consultar Todos os Colaboradores:\n')
            for colaborador in lista_colaborador:
                print('-------------------------')
                for k, v in colaborador.items():
                    print(f'{k} - {v}')
                print('-------------------------')
        if menu == 2:
            print('\nVocê escolheu a opção consultar Colaborador(a) por ID:\n')
            cod = int(input('Qual é a id do colaborador(a): '))
            for colaborador in lista_colaborador:
                if colaborador['id'] == cod:
                    print('-------------------------')
                    for k, v in colaborador.items():
                        print(f'{k} - {v}')
                    print('-------------------------')
        if menu == 3:
            print('\nVocê escolheu a opção consultar Colaborador(a) por Setor:\n')
            cod = input('Qual é o setor do colaborador(a): ')
            for colaborador in lista_colaborador:
                if colaborador['setor'] == cod:
                    print('-------------------------')
                    for k, v in colaborador.items():
                        print(f'{k} - {v}')
                    print('-------------------------')
        if menu == 4:
            break   # Retorna ao Main
        else:
            print('Opção inválida. Tente novamente...')
            continue  # Retorna ao menu de seleção


def remover_colaborador():
    print('Bem-vindo ao Desligamento de Colaborador(a)\n')
    cod = int(input('Digite a id do colaborador(a) a ser desligado: '))
    for colaborador in lista_colaborador:
        if colaborador['id'] == cod:
            lista_colaborador.remove(colaborador)
            print('Colaborador desligado com sucesso.')
# ------------------------- Fim das Funções ------------------------------------------


# ------------------------- Início do Main -------------------------------------------
while True:
    menu = int(input('\nEscolha a opção desejada:'
                     '\n1 - Cadastrar Colaborador(a)'
                     '\n2 - Consultar Colaborador(es)'
                     '\n3 - Remover Colaborador(a)'
                     '\n4 - Sair'
                     '\nOpção: '))
    if menu == 1:
        id_colaborador = id_colaborador + 1
        cadastrar_colaborador(id_colaborador)
    elif menu == 2:
        consultar_colaborador()
    elif menu == 3:
        remover_colaborador()
    elif menu == 4:
        print('--' * 13 + 'PROGRAMA ENCERRADO' + '--' * 13 + '\n' + '*****' * 14)
        break
    else:
        print('Opção inválida. Tente novamente...')
        continue    # Retorna ao menu
# ------------------------- Fim do Main ----------------------------------------------
