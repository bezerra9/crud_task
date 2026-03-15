def criacao_task():
    id_task = input('Digite o identificador da task: ')
    titulo_task = input('Digite o título da task: ')
    status_task = input('Digite o status da task: ')

    nova_task = {
        'id': id_task,
        'titulo': titulo_task,
        'status': status_task
    }

    bd_improvisado.append(nova_task)

    print('Task criada com sucesso!')


def listando_task():
    if len(bd_improvisado) == 0:
        print('Nenhuma task encontrada por favor adicione uma nova')
    else:
        for task in bd_improvisado:
            print(task)


def buscando_task():
    id_busca = input('Digite o ID que você quer buscar: ')
    if len(bd_improvisado) == 0:
        print('Nenhuma task encontrada por favor adicione uma nova')

    else:
        resultado_busca = [
            task for task in bd_improvisado if task['id'] == id_busca]
        if len(resultado_busca) > 0:
            print('ID encontrado, mostrando task: ')
            print(resultado_busca[0])
        else:
            print('O ID não foi encontrado, por favor digite um ID válido!')


def atualizando_task():
    id_busca = input('Digite o ID que você quer atualizar: ')
    if len(bd_improvisado) == 0:
        print('Nenhuma task encontrada por favor adicione uma nova')
    else:
        resultado_busca = [
            task for task in bd_improvisado if task['id'] == id_busca]
        if len(resultado_busca) > 0:
            print('ID encontrado, atualizando task...\n')
            status_atualizado = input(
                'Digite o novo status dessa task: ')
            resultado_busca[0]['status'] = status_atualizado
            print('Task atualizada com sucesso')
        else:
            print('O ID não foi encontrado, por favor digite um ID válido!')


def deletando_task():
    id_busca = input('Digite o ID que você quer Deletar: ')
    if len(bd_improvisado) == 0:
        print('Nenhuma task encontrada por favor adicione uma nova')
    else:
        resultado_busca = [
            task for task in bd_improvisado if task['id'] == id_busca]
        if len(resultado_busca) > 0:
            print('ID encontrado, deletando task...\n')
            bd_improvisado.remove(resultado_busca[0])
            print('Task deletada com sucesso')
        else:
            print('O ID não foi encontrado, por favor digite um ID válido!')


bd_improvisado = []
sistema_rodando = True


print('CRUD Gerenciamento de Tasks: ')


while sistema_rodando:
    print('1 - Criar task')
    print('2 - Listar as tasks')
    print('3 - Buscar task especifica')
    print('4 - Atualizar task')
    print('5 - Deletar task')
    print('6 - Encerrar programa')
    opcao = input(
        'Para prosseguir digite um numero para entrar em uma operação: ')

    match opcao:
        case '1':
            print('Criando task...\n')
            criacao_task()

        case '2':
            print('\nListando task...\n')
            listando_task()

        case '3':
            print('\nBuscando task...')
            buscando_task()

        case '4':
            print('\nAtualizando task...')
            atualizando_task()

        case '5':
            print('\nDeletando task...')
            deletando_task()

        case '6':
            print('Encerrando programa!')
            sistema_rodando = False
            break
