import barr
import client
import interacoes


def main():
    cliente_nome = client.cliente()
    x = interacoes.criar_barraca()
    interacoes.hora_de_pagar(cliente_nome, x)


if __name__ == '__main__':
    main()

