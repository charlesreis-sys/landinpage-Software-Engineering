import sys

if not sys.stdin.isatty():
    print("Rodando no GitHub Actions - teste automático concluído")
    exit()

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

    if opcao == "1":
        titulo = input("Digite o título: ")
        descricao = input("Digite a descrição: ")
        prioridade = input("Prioridade (Baixa/Média/Alta): ")

        tarefa = {
            "id": id_tarefa,
            "titulo": titulo,
            "descricao": descricao,
            "prioridade": prioridade
        }

        tarefas.append(tarefa)
        id_tarefa += 1

        print("Tarefa adicionada!")

    elif opcao == "2":
        for tarefa in tarefas:
            print(
                tarefa["id"], "-",
                tarefa["titulo"], "-",
                tarefa["descricao"], "-",
                tarefa["prioridade"]
            )

    elif opcao == "3":
        editar_id = int(input("Digite o ID da tarefa: "))

        for tarefa in tarefas:
            if tarefa["id"] == editar_id:
                tarefa["titulo"] = input("Novo título: ")
                tarefa["descricao"] = input("Nova descrição: ")
                tarefa["prioridade"] = input("Nova prioridade: ")
                print("Tarefa atualizada!")

    elif opcao == "4":
        excluir_id = int(input("Digite o ID da tarefa: "))

        tarefas = [t for t in tarefas if t["id"] != excluir_id]

        print("Tarefa excluída!")

    elif opcao == "0":
        break

    else:
        print("Opção inválida")
