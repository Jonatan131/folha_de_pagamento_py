def funcionario_comissionado():
    print("\n>>> Cadastro De Funcionário Comissionado <<<")

    while True:
        nome = input("Digite o nome: ").strip()
        if nome:
            break
        print("O nome não pode ser vazio!")

    while True:
        try:
            matricula = int(input("Digite a matrícula: "))
            break
        except ValueError:
            print("A matrícula deve ser um número inteiro!")

    comissao = float(input("Digite a comissão: "))

    salario_base = 2000.0
    salario_final = salario_base + comissao

    funcionario = {
        "tipo": "comissionado",
        "nome": nome,
        "matricula": matricula,
        "salario_base": salario_base,
        "comissao": comissao,
        "salario_final": salario_final,
    }

    return funcionario


def exibir_resumo_comissionado(comissionado):
    print("\nFUNCIONÁRIO COMISSIONADO")
    print(f"Nome: {comissionado['nome']}")
    print(f"Matrícula: {comissionado['matricula']}")
    print(f"Salário base: R$ {comissionado['salario_base']:.2f}")
    print(f"Comissão: R$ {comissionado['comissao']:.2f}")
    print(f"Salário Final: R$ {comissionado['salario_final']:.2f}")