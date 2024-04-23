import os

restaurantes = [
    {'Nome' : 'ValhallaBurguer', 'Categoria':'Hamburgueria', 'Ativo':True }, 
    {'Nome' : 'All Capone', 'Categoria':'Italiano', 'Ativo':False }, 
    {'Nome' : 'BonJour', 'Categoria':'Francêes', 'Ativo':True } 
                ]

def ExibirNomeDoPrograma():
    print("""          
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░     
      """)

def ExibirOpcoes():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurantes')
    print('3 - Alterar status do restaurante')
    print('4 - Sair')

def ExibirSubtitulo(titulo):
    os.system('cls')
    linha = '=' * (len(titulo))
    print(linha)
    print(titulo)
    print(linha)
    print()

def VoltarAoMenuPrincipal():
    input('Aperte enter para voltar ao menu principal')
    main()

def FinalizarApp():
    ExibirSubtitulo('Tchau tchau!!')

def OpcaoInvalida():
    print('Opção Invalida\n')
    VoltarAoMenuPrincipal()

def CadastrarNovoRestaurante():
    ExibirSubtitulo('Cadastrar novo restaurante')
    NomeDoRestaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    CategoriaRestaurante = input(f'Digite o nome da categoria do restaurante {NomeDoRestaurante}: ')
    DadosDoRestaurante = {'Nome':NomeDoRestaurante, 'Categoria':CategoriaRestaurante, 'Ativo': False}
    restaurantes.append(DadosDoRestaurante)
    print(f'Restaurante {NomeDoRestaurante} da Categoria {CategoriaRestaurante} foi cadastrado com sucesso!')
    VoltarAoMenuPrincipal()

def ListarRestaurantes():
    ExibirSubtitulo('Lista de todos os restaurantes cadastrados!')
    print(f'{'Nome do Restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status\n')
    for restaurante in restaurantes:
        NomeRestaurante = restaurante['Nome']
        CategoriaRestaurante = restaurante['Categoria']
        AtivoRestaurante = 'Ativado' if restaurante['Ativo'] else 'Desativado'
        print(f' - {NomeRestaurante.ljust(20)} | {CategoriaRestaurante.ljust(20)} | {AtivoRestaurante}')
    VoltarAoMenuPrincipal()

def StatusRestaurante():
    ExibirSubtitulo('Alterando o status do restauramte')
    NomeRestaurante = input('Digite o nome do restaurante que deseje alterar o status: ')
    RestauranteEncontrado = False
    for restaurante in restaurantes:
        if NomeRestaurante == restaurante['Nome']:
            RestauranteEncontrado = True 
            restaurante['Ativo'] = not restaurante['Ativo']
            mensagem = f'O restaurante {NomeRestaurante} foi ativado com sucesso!' if restaurante['Ativo'] else f'O restaurante {NomeRestaurante} foi desativado com sucesso!'
            print(mensagem)
    if not RestauranteEncontrado:
        print('O restaurante não foi encontrado') 
    VoltarAoMenuPrincipal()

def EscolherOpcao():
    try: 
        OpcaoEscolhida = int(input('\nDigite uma opção: '))
        # OpcaoEscolhida = int(OpcaoEscolhida)
        if OpcaoEscolhida == 1:
            CadastrarNovoRestaurante()
        elif OpcaoEscolhida == 2:
            ListarRestaurantes()
        elif OpcaoEscolhida == 3:
            StatusRestaurante()
        elif OpcaoEscolhida == 4:
            FinalizarApp()
        else:
            OpcaoInvalida()
    except: 
        OpcaoInvalida()

def main():
    os.system('cls')
    ExibirNomeDoPrograma()
    ExibirOpcoes()
    EscolherOpcao()

if __name__ == '__main__':
    main()