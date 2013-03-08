while True:
    user = input('Informe o nome de usuario: ')
    password = input('Informe a senha (Diferente do usuario): ')
    if user != password:
        break
    else:
        print('Erro: Senha igual ao usuario!\n')
