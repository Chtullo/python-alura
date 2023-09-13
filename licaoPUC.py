estudantes = []

while True:
    print("*** Menu Principal ***")
    print("1- Menu de Operações")
    print("2- Sair")

    opcao_principal = input("Selecione uma opção: ")

    if opcao_principal == "1":
        while True:
            print("*** Menu de Operações ***")
            print("1- Inclusão de estudante")
            print("2- Listagem de estudantes")
            print("3- Edição de estudante")
            print("4- Exclusão de estudante")
            print("5- Voltar ao Menu principal")

            opcao_operacoes = input("Selecione uma operação: ")

            if opcao_operacoes == "1":
                nome = input("Digite o nome do estudante: ")
                estudantes.append(nome)
                print("Estudante incluído com sucesso!")
            elif opcao_operacoes == "2":
                print("*** Lista de Estudantes ***")
                for i, estudante in enumerate(estudantes, start=1):
                    print(f"{i}. {estudante}")
            elif opcao_operacoes == "3":
                print("**** Lista de estudantes ***")
                for i, estudante in enumerate(estudantes, start=1):
                    print(f"{i}. {estudante}")
                indice = int(input("Digite o número do estudante a ser editado: ")) - 1
                if 0 <= indice < len(estudantes):
                    novo_estudante = input("Digite o nome do novo estudante: ")
                    estudantes[indice] = novo_estudante
                    print("Estudante editado com sucesso!")
                else:
                    print("Índice inválido!")
            elif opcao_operacoes == "4":
                print("**** Lista de Estudantes ***")
                for i, estudante in enumerate(estudantes, start=1):
                    print(f"{i}. {estudante}")
                indice = int(input("Digite o número do estudante que será excluído: ")) - 1
                if 0 <= indice < len(estudantes):
                    estudantes.pop(indice)
                    print("Estudante excluído com sucesso!")
                else:
                    print("Índice inválido!")
            elif opcao_operacoes == "5":
                break
            else:
                print("Opção inválida!")
    elif opcao_principal == "2":
        print("Saindo do programa!")
        break
    else:
        print("Opção Inválida!")
