import exc1

while True:
    while True:
        menu()
        escolha = input('Digite a opção selecionada: ')
        if  escolha.isnumeric():
            if int(escolha) < 7 and int(escolha) > 0:
                break
            else:
                print('Você deve digitar um número entre 1 e 6')
        else:
            print('Você deve digitar um número')
        
    if int(escolha) == 1:
        cadastrarUsuario()
    elif int(escolha) == 2:
        excluirUsuario()
    elif int(escolha) == 3:
        buscaUsuario()
    elif int(escolha) == 4:
        contaUsuarios()
    elif int(escolha) == 5:
        mostraUsuarios()
    elif int(escolha) == 6:
        print('Saindo do programa...')
        time.sleep(2)
        break

