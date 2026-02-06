tarefas = []
id_tarefa = 1

while True:

    print("\nGERENCIADOR DE TAREFAS")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Editar tarefa")
    print("4 - Excluir tarefa")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # CRIAR
    if opcao == "1":
        titulo = input("Digite o título: ")
        descricao = input("Digite a descrição: ")

        tarefa = {
            "id": id_tarefa,
            "titulo": titulo,
            "descricao": descricao
        }

        tarefas.append(tarefa)
        id_tarefa += 1

        print("Tarefa adicionada!")

    # LISTAR
    elif opcao == "2":
        for tarefa in tarefas:
            print(tarefa["id"], "-", tarefa["titulo"], "-", tarefa["descricao"])

    # EDITAR
    elif opcao == "3":
        editar_id = int(input("Digite o ID da tarefa: "))

        for tarefa in tarefas:
            if tarefa["id"] == editar_id:
                tarefa["titulo"] = input("Novo título: ")
                tarefa["descricao"] = input("Nova descrição: ")
                print("Tarefa atualizada!")

    # EXCLUIR
    elif opcao == "4":
        excluir_id = int(input("Digite o ID da tarefa: "))

        tarefas = [t for t in tarefas if t["id"] != excluir_id]

        print("Tarefa excluída!")

    # SAIR
    elif opcao == "0":
        break

    else:
        print("Opção inválida")
