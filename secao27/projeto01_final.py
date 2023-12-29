from random import randint


def interface_usuario(opcoes):
    '''
    Função que apresenta as opções e pergunta para o jogador a opção pretendida
    Retorna um inteiro.
    '''
    for indice, opcao in enumerate(opcoes):
        print(f'{indice} = {opcao}')

    entrada_usuario = int(input('Qual sua opção? '))
    return entrada_usuario


def escolha_computador(conteudo):
    '''
    Função que gera a escolha aleatória de uma opção dentre as disponíveis.
    retorna um inteiro aleatório
    '''
    entrada_computador = randint(0, len(conteudo) - 1)
    return entrada_computador


def verifica_resultado(escolhas, jogador, computador):
    '''
    Função que verifica quem ganhou.
    retorna uma string
    '''
    if jogador == computador:
        return 'Empatou!!'
    elif (jogador == 0 and computador == len(escolhas) - 1) or (
            jogador > computador and not (jogador == len(escolhas) - 1 and computador == 0)):
        return 'Você Ganhou!!'
    return 'Você Perdeu!!'


def jogar():
    print('''
    ---------------------------------
    Bem vindo ao Pedra, Papel e Tesoura.
    Prepare-se!
    ''')

    # Define as opções e pergunta a cada um a sua escolha
    lista_opcoes = ['Pedra', 'Papel', 'Tesoura']
    resultado_jogador = interface_usuario(lista_opcoes)
    resultado_computador = escolha_computador(lista_opcoes)

    # Representação visual no terminal qual foi a opção escolhida por cada um
    print(f'          sua escolha: {lista_opcoes[resultado_jogador]}')
    print(f'escolha do computador: {lista_opcoes[resultado_computador]}')

    # checa o resultado entre as duas opções e mostra o ganhador
    resultado = verifica_resultado(lista_opcoes, resultado_jogador, resultado_computador)
    print(f'\n{resultado}')


def main():
    # Força um loop de jogos, até o jogador decidir parar.
    jogar_novamente = ''
    while jogar_novamente.lower() != 'n':
        jogar()
        print(f'Você gostaria de jogar novamente? ')
        jogar_novamente = input('Digite \'s\' para sim ou \'n\' para não: ')


# Aqui inicia a execução do programa!
main()