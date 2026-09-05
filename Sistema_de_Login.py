while True:
    print("1 - Cadastrar usuário")
    print("2 - Login")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        usuario = input("Cadastrar nome de usuário: ")

        senha = input(
            "Cadastre uma senha. Ela deve conter no mínimo 5 caracteres e 1 número: "
        )

        tem_numero = False

        for caractere in senha:
            if caractere.isdigit():
                tem_numero = True

        if len(senha) >= 5 and tem_numero:
            print("Senha cadastrada com sucesso!")
        else:
            print("A senha deve conter no mínimo 5 caracteres e 1 número.")

    elif opcao == "2":
        usuario_login = input("Digite o nome do seu usário: ")
        senha_login = input("Digite sua senha: ")
        if usuario_login == usuario and senha_login == senha:
            print("Login realizado com sucesso!")

        else:
            print("Usuários ou senha incorretos.")


    elif opcao == "3":
        sair=input("Deseja sair so sistema? S/N")
        if sair == "N":
            print("Voltando ao menu...")


        else:
            print("Encerrando sistema...")
        break