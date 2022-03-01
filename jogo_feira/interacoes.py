import barr
import client


def criar_barraca():
    fruta = barr.barraca_fruta()
    legume = barr.barraca_legume()
    verdura = barr.barraca_verdura()
    escolha_cliente = input("Escolha qual barraca você quer:\n"
                            "Frutas: F/f\n"
                            "Legumes: L/l\n"
                            "Verduras: V/v").upper()
    print("\nLegal, vamos começar: ")

    if escolha_cliente == 'F':
        escolha = input("\nBem vind@! Escolha qual fruta você quer:\n"
                        "Abacate: A/a\n"
                        "Pera: P/p\n"
                        "Goiaba: G/g\n").upper()
        if escolha == 'A':
            escolha_quantidade = int(input("Temos 10 abacates na bacia. Quantos você precisa?\n"
                                           "0 a 10"))
            valor_total = escolha_quantidade * fruta.preco_abacate
            print(f"Você escolheu {escolha_quantidade}, e o valor fica {valor_total}")
            fruta.cobrar = fruta.cobrar + valor_total

            return valor_total
        elif escolha == 'P':
            escolha_quantidade = int(input("Temos 10 peras na bacia. Quantos você precisa?"
                                           "0 a 10"))
            valor_total = escolha_quantidade * fruta.preco_pera
            print(f"Você escolheu {escolha_quantidade}, e o valor fica {valor_total}")
            return valor_total
        elif escolha == 'G':
            escolha_quantidade = int(input("Temos 10 goiabas na bacia. Quantas você precisa?"
                                           "0 a 10"))
            valor_total = escolha_quantidade * fruta.preco_goiaba
            print(f"Você escolheu {escolha_quantidade}, e o valor fica {valor_total}")
            return valor_total

    elif escolha_cliente == 'L':
        escolha = input("Bem vind@! Escolha qual legume você quer:\n"
                        "Abobora: A/a\n"
                        "Milho: M/m\n"
                        "Pepino: P/p\n").upper()
        print(f"Ótimo! Você escolheu {escolha}.")
        if escolha == 'A':
            escolha_quantidade = int(input("Temos 10 abóboras na bacia. Quantos você precisa?\n"
                                           "0 a 10"))
            valor_total = escolha_quantidade * legume.preco_abobora
            print(f"Você escolheu {escolha_quantidade}, e o valor fica {valor_total}")
            return valor_total
        elif escolha == 'M':
            escolha_quantidade = int(input("Temos 10 milhos na bacia. Quantos você precisa?"
                                           "0 a 10"))
            valor_total = escolha_quantidade * legume.preco_milho
            print(f"Você escolheu {escolha_quantidade}, e o valor fica {valor_total}")
            return valor_total
        elif escolha == 'P':
            escolha_quantidade = int(input("Temos 10 pepinos na bacia. Quantas você precisa?"
                                           "0 a 10"))
            valor_total = escolha_quantidade * legume.preco_pepino
            print(f"Você escolheu {escolha_quantidade}, e o valor fica {valor_total}")
            return valor_total
    if escolha_cliente == 'V':
        escolha = input("Bem vind@! Escolha qual verdura você quer:\n"
                        "Escarola: E/e\n"
                        "Repolho: R/r\n"
                        "Hortela: H/h\n").upper()
        print(f"Ótimo! Você escolheu {escolha}.")
        if escolha == 'V':
            escolha_quantidade = int(input("Temos 10 escarolas na bacia. Quantas você precisa?\n"
                                           "0 a 10"))
            valor_total = escolha_quantidade * verdura.preco_escarola
            print(f"Você escolheu {escolha_quantidade}, e o valor fica {valor_total}")
        elif escolha == 'R':
            escolha_quantidade = int(input("Temos 10 repolhos na bacia. Quantos você precisa?"
                                           "0 a 10"))
            valor_total = escolha_quantidade * verdura.preco_repolho
            print(f"Você escolheu {escolha_quantidade}, e o valor fica {valor_total}")
        elif escolha == 'H':
            escolha_quantidade = int(input("Temos 10 hortelãs na bacia. Quantoss você precisa?"
                                           "0 a 10"))
            valor_total = escolha_quantidade * verdura.preco_hortela
            print(f"Você escolheu {escolha_quantidade}, e o valor fica {valor_total}")


def hora_de_pagar(cliente, valor):
    cliente.dinheiro -= valor
    print(f"O cliente pagou o valor {valor}")
    print(f"O cliente ficou com {cliente.dinheiro}")
    if cliente.dinheiro < 0:
        print('Ei, você ficou devendo!')





