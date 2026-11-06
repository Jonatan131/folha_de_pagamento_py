from funcionarios.funcionario_padrao import exibir_resumo_padrao
from funcionarios.funcionario_comissionado import exibir_resumo_comissionado
from funcionarios.funcionario_producao import exibir_resumo_producao


def gerar_folha(funcionarios):
    print("\n>>> FOLHA DE PAGAMENTO <<<")

    if not funcionarios:
        print("Nenhum funcionário cadastrado!")
        return

    print(f"Quantidade de funcionários: {len(funcionarios)}")

    total_folha = 0

    for funcionario in funcionarios:
        if funcionario["tipo"] == "padrao":
            exibir_resumo_padrao(funcionario)
        elif funcionario["tipo"] == "comissionado":
            exibir_resumo_comissionado(funcionario)
        elif funcionario["tipo"] == "producao":
            exibir_resumo_producao(funcionario)

        total_folha += funcionario["salario_final"]

    print(f"\nTotal da folha: R$ {total_folha:.2f}")