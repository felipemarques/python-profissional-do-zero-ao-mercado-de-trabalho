from random import randint

def interface_usuario(opcoes):
    '''
    Função que apresenta as opções e pergunta para o jogador a opção pretendida
    Retorna um inteiro.
    '''

def escolha_computador(conteudo):
    '''
    Função que gera a escolha aleatória de uma opção dentre as disponíveis.
    retorna um inteiro aleatório
    '''

def verifica_resultado(escolhas, jogador, computador):
    '''
    Função que verifica quem ganhou.
    retorna uma string
    '''

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