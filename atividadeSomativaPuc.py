import os

estudantes = []
professores = []
disciplinas = []
turmas = []
matriculas = []


def incluir_registro(modulo, registro):
    modulo.append(registro)


def listar_registros(modulo):
    for i, registro in enumerate(modulo, start=1):
        print(f"{i}. {registro}")


def atualizar_registro(modulo, indice, novo_registro):
    if 0 <= indice < len(modulo):
        modulo[indice] = novo_registro
        print("Registro atualizado com sucesso!")
    else:
        print("Índice inválido!")


def excluir_registro(modulo, indice):
    if 0 <= indice < len(modulo):
        modulo.pop(indice)
        print("Registro excluído com sucesso!")
    else:
        print("Índice inválido!")


def validar_codigo_unico(codigo, modulo):
    for registro in modulo:
        if registro[0] == codigo:
            return False
    return True


def menu_estudantes():
    while True:
        print("*** Menu de Estudantes ***")
        print("1- Inclusão de Estudante")
        print("2- Listagem de Estudantes")
        print("3- Atualização de Estudante")
        print("4- Exclusão de Estudante")
        print("5- Voltar ao Menu Principal")

        opcao = input("Selecione uma operação: ")

        if opcao == "1":
            nome = input("Digite o nome do estudante: ")
            estudantes.append((len(estudantes) + 1, nome))
            print("Estudante incluído com sucesso!")
        elif opcao == "2":
            print("*** Lista de Estudantes ***")
            listar_registros(estudantes)
        elif opcao == "3":
            print("*** Lista de Estudantes ***")
            listar_registros(estudantes)
            indice = int(input("Digite o número do estudante a ser editado: ")) - 1
            if 0 <= indice < len(estudantes):
                novo_nome = input("Digite o nome do novo estudante: ")
                estudantes[indice] = (estudantes[indice][0], novo_nome)
                print("Estudante editado com sucesso!")
            else:
                print("Índice inválido!")
        elif opcao == "4":
            print("*** Lista de Estudantes ***")
            listar_registros(estudantes)
            indice = int(input("Digite o número do estudante que será excluído: ")) - 1
            if 0 <= indice < len(estudantes):
                excluir_registro(estudantes, indice)
            else:
                print("Índice inválido!")
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")


def menu_principal():
    while True:
        print("*** Menu Principal ***")
        print("1- Menu de Estudantes")
        print("2- Menu de Professores")
        print("3- Menu de Disciplinas")
        print("4- Menu de Turmas")
        print("5- Menu de Matrículas")
        print("6- Sair")

        opcao_principal = input("Selecione uma opção: ")

        if opcao_principal == "1":
            menu_estudantes()

        elif opcao_principal == "6":
            print("Saindo do programa!")
            break
        else:
            print("Opção Inválida!")


def validar_codigo_unico(codigo, modulo):
    for registro in modulo:
        if registro[0] == codigo:
            return False
    return True


def salvar_dados_em_arquivo():
    with open("dados.txt", "w") as arquivo:
        arquivo.write("Estudantes:\n")
        for estudante in estudantes:
            arquivo.write(f"{estudante[0]},{estudante[1]}\n")


def carregar_dados_do_arquivo():
    if os.path.exists("dados.txt"):
        with open("dados.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            modulo_atual = None
            for linha in linhas:
                linha = linha.strip()
                if linha.startswith("Estudantes:"):
                    modulo_atual = estudantes
                elif linha:
                    partes = linha.split(",")
                    if modulo_atual is not None:
                        modulo_atual.append((int(partes[0]), partes[1]))


carregar_dados_do_arquivo()

menu_principal()

salvar_dados_em_arquivo()
