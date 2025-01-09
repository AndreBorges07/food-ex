import os
from modelos.restaurante import Restaurante

restaurantes = [{'nome':'Bom de boca', 'categoria': 'Rodizio', 'status': True},
                {'nome': 'Galioto', 'categoria': 'Pizzaria', 'status': False}, 
                {'nome': 'Oliva', 'categoria': 'Misto', 'status': True}]

def exibir_nome_programa():
    print("""
███╗░░██╗███████╗████████╗███████╗░█████╗░██████╗░
████╗░██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔══██╗
██╔██╗██║█████╗░░░░░██║░░░█████╗░░██║░░██║██║░░██║
██║╚████║██╔══╝░░░░░██║░░░██╔══╝░░██║░░██║██║░░██║
██║░╚███║███████╗░░░██║░░░██║░░░░░╚█████╔╝██████╔╝
╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝░░░░░░╚════╝░╚═════╝░\n""")
# Quando coloco 3x as aspas (""") é como se deixasse um espaço html, parecido com o `` que também usamos. 

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alterar status Restaurante')
    print('4. Sair \n')

def finalizar_app():
    os.system('cls') #É o famoso "clear Screan"
    print('Sistema encerrado')

def opcao_invalida():
    print('Opção Invalida')
    voltar_ao_menu()

def voltar_ao_menu(): #Só pra não repetir sempre esse trecho
    input('\nDigite "Enter" para voltar ao menu')
    main()
    
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '•' * (len(texto))

    print(linha)
    print(f'{texto}')    
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novo Restaurante')
    nome_restaurante = input('Digite o NOME do restaurante: ')
    categoria_restaurante = input(f'Digite a CATEGORIA do restaurante "{nome_restaurante}": ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'status':False}

    restaurantes.append(dados_restaurante) #Em outras linguagens, seria o "push", mas o Python gosta de assunto. 

    print(f'\nO restaurante "{nome_restaurante}" foi cadastrado com sucesso!\n')

    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes')

    print(f'{'RESTAURANTE'.ljust(22)} | {'CATEGORIA'.ljust(20)} | {'STATUS'.ljust(20)}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status_restaurante = 'Ativo' if restaurante['status'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {status_restaurante}')

    voltar_ao_menu()

def alternar_status_restaurante():
    exibir_subtitulo('Alternando status de Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status'] 
            mensagem_status = 'ATIVO' if restaurante['status'] else 'DESATIVADO'
            print(f'O restaurante "{nome_restaurante}" foi {mensagem_status} com sucesso!')

    if not restaurante_encontrado:
        print(f'O restaurante "{nome_restaurante}" não foi encontrado.')

    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: #Quando não tem mais opção, é nesse momento que entra o "else". 
            opcao_invalida()
    except:
        opcao_invalida() 


restaurante_nihao = Restaurante('Ni Hao', 'Chinesa')
restaurante_pomodoro = Restaurante('Pomodoro', 'Italiana')
restaurante_texas = Restaurante('Texas', 'Churrascaria')
restaurante_kian = Restaurante('Kian', 'Japonesa')

restaurante_texas.receber_avaliacao('João', 10)
restaurante_texas.receber_avaliacao('Maria', 8)
restaurante_texas.receber_avaliacao('José', 6)
restaurante_texas.receber_avaliacao('Ana', 7)
restaurante_texas.receber_avaliacao('Pedro', 5)


restaurante_pomodoro.alternar_status()

def main():
    os.system('cls')
    # exibir_nome_programa()
    # exibir_opcoes()
    # escolher_opcao()

    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
