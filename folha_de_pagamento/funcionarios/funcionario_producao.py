def funcionario_producao():
    print("\n>>> Cadastro De Funcionário Producao <<<")

    while True:
        nome = input("Digite o nome: ").strip()
        if nome:
            break
        print("O nome não pode ser vazio!")

    while True:
        try:
            matricula = int(input("Digite a matricula: "))
            break
        except ValueError:
            print("A matrícula deve ser um número inteiro!")

    quantidade_peca = int(input("Informe a quantidade de peças: "))
    valor_peca = float(input("Informe o valor da peça: "))

    salario_base = 2000.0
    produtividade = quantidade_peca * valor_peca
    salario_final = salario_base + produtividade

    funcionario = {
        "nome": nome,
        "matricula": matricula,
        "quantidade_peca": quantidade_peca,
        "valor_peca": valor_peca,
        "salario_base": salario_base,
        "salario_final": salario_final,
    }
    return funcionario

def exibir_resumo_producao(producao):
    print("\nFUNCIONÁRIO PRODUÇÃO")
    print(f"Nome: {producao['nome']}")
    print(f"Matrícula: {producao['matricula']}")
    print(f"Salário base: R$ {producao['salario_base']:.2f}")
    print(f"Produtividade: R$ {producao['produtividade']:.2f}")
    print(f"Salário Final: R$ {producao['salario_final']:.2f}")
