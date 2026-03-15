from pydantic import BaseModel, ValidationError, field_validator

class Task(BaseModel):
    id: int
    titulo: str
    status: str

    @field_validator('titulo')
    @classmethod
    def ensure_title_n_empty(cls, value:str) -> str:
        if value.strip() == '':
            raise ValueError('Title cannot be empty!')
        return value
 
def criacao_task():
    id_task = input('Digite o identificador da task: ')
    

# abc
    try:
        id_temp = int(id_task)
        for task in bd_improvisado:
            if task['id'] == id_temp:
                print('ERROR: THIS ID ALREADY EXISTS')
                return
    except ValueError:
        pass 

    titulo_task = input('Digite o título da task: ')
    status_task = input('Digite o status da task: ')

    try:
        nova_task = Task(
            id=id_task,
            titulo= titulo_task,
            status= status_task
        )
            
        bd_improvisado.append(nova_task.model_dump())
        print('Task was created succesfuly and validated by Pydantic')
    except ValidationError as e:
        print('\n')
        print('Validation error! check the data')
        print(e)


def listando_task():
    if len(bd_improvisado) == 0:
        print('Nenhuma task encontrada por favor adicione uma nova')
    else:
        for task in bd_improvisado:
            print(task)


def buscando_task():
    if len(bd_improvisado) == 0:
        print('Nenhuma task encontrada por favor adicione uma nova')
        return

    try: 
        id_busca = int(input('Digite o ID que você quer buscar: '))
    except ValueError:
        print('ERROR! the ID needs to be a integer value')
        return
    
    resultado_busca = [task for task in bd_improvisado if task['id'] == id_busca]
    if len(resultado_busca) > 0:
        print('ID encontrado, mostrando task: ')
        print(resultado_busca[0])
    else:
        print('O ID não foi encontrado, por favor digite um ID válido!')    


def atualizando_task():
    if len(bd_improvisado) == 0:
        print('Nenhuma task encontrada por favor adicione uma nova')
        return
    try:
        id_busca = int(input('Digite o ID que você quer atualizar: '))
    except ValueError:
        print('ERROR! the ID needs to be a integer value')
        return

    resultado_busca = [task for task in bd_improvisado if task['id'] == id_busca] 

    if len(resultado_busca) > 0:
        print('ID encontrado, atualizando task...\n')
        status_atualizado = input('Digite o novo status dessa task: ')
        resultado_busca[0]['status'] = status_atualizado
        print('Task atualizada com sucesso')
    else:
        print('O ID não foi encontrado, por favor digite um ID válido!')


def deletando_task():
    if len(bd_improvisado) == 0:
        print('Nenhuma task encontrada por favor adicione uma nova')
        return
    try:
        id_busca = int(input('Digite o ID que você quer Deletar: '))
    except ValueError:
        print('ERROR! the ID needs to be a integer value')
        return
    resultado_busca = [task for task in bd_improvisado if task['id'] == id_busca]


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
