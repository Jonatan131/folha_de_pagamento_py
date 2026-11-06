from folha_de_pagamento.utils import ler_inteiro
from funcionarios.funcionario_padrao import funcionario_padrao
from funcionarios.funcionario_comissionado import funcionario_comissionado
from funcionarios.funcionario_producao import funcionario_producao
from folha_de_pagamento.folha import gerar_folha


def mostrar_menu():
    print("\n   GESTÃO DE COLABORADORES   ")
    print("——————————————————————————————")
    print(" 1 - Funcionário Padrão      ")
    print(" 2 - Funcionário Comissionado")
    print(" 3 - Funcionário Produção    ")
    print(" 4 - Gerar Folha             ")
    print(" 0 - Sair                    ")


funcionarios = []
opcao = -1

while opcao != 0:
    mostrar_menu()
    opcao = ler_inteiro("\nSelecione uma opção: ")

    match opcao:
        case 1:
            funcionarios.append(funcionario_padrao())
        case 2:
            funcionarios.append(funcionario_comissionado())
        case 3:
            funcionarios.append(funcionario_producao())
        case 4:
            gerar_folha(funcionarios)
        case 0:
            print("\n>>> Encerrando Programa <<<")
        case _:
            print("Opção Invalida!")