lista_de_compras = []

opcao = 1000

while opcao != 0:
    print('\n =============================')
    print('1 - Adicionar novo item')
    print('2 - Remover item')
    print('3 - Exibir lista completa')
    print('0 - Sair')

    opcao = int(input('Digite a opção desejada: '))

    # Criar opção adicionar novo item à lista
    if opcao == 1:
        print('\n======> ADICIONAR ITEM <=======\n')
        novo_item = input('Digite o novo item a ser adicionado: ')
        if novo_item:  # Verifica se o item não está vazio
            lista_de_compras.append(novo_item)  # Corrigido para usar append
            print(f'Item "{novo_item}" adicionado com sucesso!')  # Mensagem de confirmação
        else:
            print("O item não pode estar vazio.")

    # Remover item
    elif opcao == 2:
        print('\n =====> REMOVER ITEM DA LISTA <=====\n')
        if lista_de_compras:  # Verifica se a lista não está vazia
            for i in range(len(lista_de_compras)):
                print(f'{i + 1} - {lista_de_compras[i]}')

            print('\n===')
            item_remover = int(input('Digite o código do item: ')) - 1

            if 0 <= item_remover < len(lista_de_compras):  # Verifica se o índice é válido
                del lista_de_compras[item_remover]
                print("Item removido com sucesso!")
            else:
                print("Código inválido.")
        else:
            print("A lista está vazia.")

    # Exibir a lista completa
    elif opcao == 3:
        print('\n======> LISTA DE COMPRAS <=======\n')
        if lista_de_compras:  # Verifica se a lista não está vazia
            for i in range(len(lista_de_compras)):
                print(f'{i + 1} - {lista_de_compras[i]}')
        else:
            print("A lista está vazia.")

    elif opcao == 0:
        print("Saindo...")

    else:
        print("Opção inválida. Tente novamente.")