# Levantamento de Requisitos (Perguntas e Respostas)

Qual é o principal objetivo do sistema?
Permitir o gerenciamento de tarefas da equipe, facilitando o acompanhamento do fluxo de trabalho.

Quem utilizará o sistema?
Membros da equipe da startup de logística e gestores de projeto.

Quais funcionalidades básicas são esperadas?
Cadastro, visualização, edição e exclusão de tarefas (CRUD).

O sistema deve permitir priorização?
Sim. Cada tarefa pode ter prioridade Baixa, Média ou Alta.

É necessário acompanhar o status das tarefas?
Sim. As tarefas podem ser marcadas como pendentes ou concluídas.

O sistema precisa de testes automatizados?
Sim. Pelo menos testes unitários básicos devem ser implementados.

Como será feito o controle de versões?
Utilizando GitHub, com commits semânticos e frequentes.

Haverá integração contínua?
Sim. O projeto utiliza GitHub Actions para executar testes automaticamente.

## Requisitos Funcionais

RF01 – O sistema deve permitir criar tarefas.
RF02 – O sistema deve listar todas as tarefas cadastradas.
RF03 – O sistema deve permitir editar tarefas existentes.
RF04 – O sistema deve permitir excluir tarefas.
RF05 – O sistema deve permitir definir prioridade da tarefa (Baixa, Média, Alta).

## Requisitos Não Funcionais

RNF01 – O código deve ser organizado em diretórios (src, tests, docs).
RNF02 – O projeto deve possuir no mínimo 10 commits bem descritos.
RNF03 – Deve existir pipeline CI com GitHub Actions executando testes.