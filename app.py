import os
#lista para armazenar os jogos cadastrados
jogos = []
def exibir_nome_do_programa():
    print("""
    ░█████╗░░█████╗░██╗░░░░░███████╗░█████╗░░█████╗░░█████╗░  ██████╗░███████╗
    ██╔══██╗██╔══██╗██║░░░░░██╔════╝██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝
    ██║░░╚═╝██║░░██║██║░░░░░█████╗░░██║░░╚═╝███████║██║░░██║  ██║░░██║█████╗░░
    ██║░░██╗██║░░██║██║░░░░░██╔══╝░░██║░░██╗██╔══██║██║░░██║  ██║░░██║██╔══╝░░
    ╚█████╔╝╚█████╔╝███████╗███████╗╚█████╔╝██║░░██║╚█████╔╝  ██████╔╝███████╗
    ░╚════╝░░╚════╝░╚══════╝╚══════╝░╚════╝░╚═╝░░╚═╝░╚════╝░  ╚═════╝░╚══════╝

    ░░░░░██╗░█████╗░░██████╗░░█████╗░░██████╗
    ░░░░░██║██╔══██╗██╔════╝░██╔══██╗██╔════╝
    ░░░░░██║██║░░██║██║░░██╗░██║░░██║╚█████╗░
    ██╗░░██║██║░░██║██║░░╚██╗██║░░██║░╚═══██╗
    ╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝██████╔╝
    ░╚════╝░░╚════╝░░╚═════╝░░╚════╝░╚═════╝░
    ███████████████████████████
    ███████▀▀▀░░░░░░░▀▀▀███████
    ████▀░░░░░░░░░░░░░░░░░▀████
    ███│░░░░░░░░░░░░░░░░░░░│███
    ██▌│░░░░░░░░░░░░░░░░░░░│▐██
    ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
    ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
    ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
    ██▌░│██████▌░░░▐██████│░▐██
    ███░│▐███▀▀░░▄░░▀▀███▌│░███
    ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
    ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
    ████▄─┘██▌░░░░░░░▐██└─▄████
    █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
    ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
    █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
    ███████▄░░░░░░░░░░░▄███████
    ██████████▄▄▄▄▄▄▄██████████
    ███████████████████████████""")


def exibir_opcoes():
    print('1. Cadastrar jogos')
    print('2. Listar Jogos')
    print('3. Ativar Jogo')
    print('4. sair\n')
    

def finalizar_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Sua Locadora de jogos foi finalizada, Obrigado pela visita')

def opcao_invalida():
    print('Opção Invalida!\n')
    input('digite uma tecla para reiniciar o programa:')

def cadastrar_jogo():
    nome = input('digite o nome do jogo: ')
    genero = input('digite o gênero do jogo ')
    ano = input('Digite o ano de lançamento do jogo ')
    jogo = {
        'nome': nome,
        'genêro': genero,
        'ano':ano,
    }
    jogos.append(jogos)
    print(f'jogo "{nome}" cadastro com sucesso!\n')

def listar_jogo():
    if not jogos:
        print('Nenhum jogo cadastrado.\n')
    else:
        for i, jogos in enumerate(jogos, 1):
            print(f'{i}. nome:{jogo["nome"]}, Gênero: {jogos["gênero"]}, Ano:{jogos["ano"]}')
            print('')

def ativar_jogo():
    listar_jogo()
    if jogos:
        try:
            escolha = int(input('Escolha o número do jogo para ativar: '))
            jogo = jogos 

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print( f'Você escolheu a opção:{opcao_escolhida}')

        if opcao_escolhida == 1:
            print('Cadastro de jogo')
        elif opcao_escolhida == 1:
            print('Cadastro de Jogos')
        elif opcao_escolhida == 2:
            print('Listar e Organizar seus jogos')
        elif opcao_escolhida == 3:
            print('Ativar seu jogo')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
            opcao_invalida()

def main():
    exibir_nome_do_programa()
    continuar = True
    while continuar:
        exibir_opcoes()
        continuar = escolher_opcoes()


if __name__ == '__main__':
    main()
    