from random import randint
import time 

arrayPessoas = []


def menu():
    print('\n 1 - Cadastre um usuário \n 2 - Remova um usuário \n 3 - Busque um usuário \n 4 - Ver quantidade de registros \n 5 - Ver todos os usuários \n 6 - sair ')


def cadastrarUsuario():
    nome = input('Insira o primeiro nome: ')
    sobrenome = input('Insira o sobrenome: ')
    cod = randint(1000, 9999)
    if (len(nome) < 4 and len(sobrenome) < 4):
        print('O nome e o sobrenome devem ter pelo menos 3 caracteres')
    else:
        objPessoa = {}
        objPessoa['Cod'] = cod
        objPessoa['Nome'] = nome + ' ' + sobrenome
        arrayPessoas.append(objPessoa)
        print(objPessoa)


def excluirUsuario():
    cod = int(input('Insira o código de usuário: '))
    for person in arrayPessoas: 
        if person['Cod'] == cod:
            name = person['Nome']
            indice = arrayPessoas.index(person)
            print(f'Usuário {name} encontrado!')
            confirmar = input(f'Deseja mesmo que o usuário: {name} seja deletado (s/sim - n/não)')
            if confirmar in ('s', 'sim'): 
                del arrayPessoas[indice]
        elif (arrayPessoas.index(person) == len(arrayPessoas) -1 and person['Cod'] != cod):
            print('Nenhum usuário encontrado')

def buscaUsuario():
    cod = int(input('Insira o código de usuário: '))
    for person in arrayPessoas: 
        if person['Cod'] == cod:
            name = person['Nome']
            print(f'Usuário encontrado: {name}')
            escolha = input(f'Deseja procurar outro usuário? (s/sim - n/não)')
            if escolha in ('s', 'sim'):
                buscaUsuario()
            else:
                break
                time.sleep(1)

def contaUsuarios():
    print("A quantidade de usuários é: ",len(arrayPessoas))

def mostraUsuarios():
    while True:
        while True:
            print('\n 1 - Mostrar os usuários por ordem de cadastro \n 2 - Mostrar os usuários por ordem alfábetica \n 3 - Mostrar os usuários por ordem de código \n 4 - voltar ao menu inicial')
            escolha = input('Digite a opção selecionada: ')
            if  escolha.isnumeric():
                if int(escolha) < 5 and int(escolha) > 0:
                    break
                else:
                    print('Você deve digitar um número entre 1 e 4')
            else:
                print('Você deve digitar um número')
        
        if int(escolha) == 1:
            for pessoa in arrayPessoas:
                print('Código: ', pessoa['Cod'], ' - ', 'Nome: ', pessoa['Nome'] )
            
        elif int(escolha) == 2:
            lista_oredenada = sorted(arrayPessoas, key=lambda dicionario: dicionario['Nome'])
            for pessoa in lista_oredenada:
                print('Código: ', pessoa['Cod'],' ', 'Nome: ', pessoa['Nome'])
        elif int(escolha) == 3:
            lista_oredenada = sorted(arrayPessoas, key=lambda dicionario: dicionario['Cod'])
            for pessoa in lista_oredenada:
                print('Código: ', pessoa['Cod'],' ', 'Nome: ', pessoa['Nome'])
        elif int(escolha) == 4:
            time.sleep(1)
            break


    

