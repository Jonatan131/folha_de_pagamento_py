def funcionario_padrao():
    print("\n>>> Cadastro De Funcionário Padrão <<<")

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

    salario_base = 2000.0
    salario_final = salario_base

    funcionario = {
        "tipo": "padrao",
        "nome": nome,
        "matricula": matricula,
        "salario_final": salario_final,
    }

    return funcionario


def exibir_resumo_padrao(padrao):
    print("\nFUNCIONÁRIO PADRÃO")
    print(f"Nome: {padrao['nome']}")
    print(f"Matrícula: {padrao['matricula']}")
    print(f"Salário Final: R$ {padrao['salario_final']:.2f}")