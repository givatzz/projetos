from datetime import datetime
import re  # Para validações com expressões regulares
from tabulate import tabulate  # Para formatação de tabelas
from termcolor import colored  # Para colorir o texto na tabela

# Número de vagas (alterado para 10)
NUMERO_VAGAS = 10

# Lista para armazenar os dados
veiculos = []

# Função para verificar se a placa já existe
def verificar_placa(placa):
    for index, veiculo in enumerate(veiculos):
        if veiculo['placa'] == placa:
            return index  # Retorna o índice se encontrar
    return -1  # Retorna -1 se não encontrar

# Função para validar texto
def validar_texto(entrada, campo_nome):
    if not entrada.replace(" ", "").isalpha():
        print(f"O campo '{campo_nome}' deve conter apenas letras.")
        return False
    return True

# Função para validar placa
def validar_placa(placa):
    padrao = r"^[A-Z]{3}\d{4}$"  # Padrão: 3 letras seguidas de 4 números (ex: ABC1234)
    if not re.match(padrao, placa.upper()):
        print("Placa inválida! Deve estar no formato 'AAA1234'.")
        return False
    return True

# Função para validar número da vaga
def validar_numero_vaga(numero_vaga):
    try:
        numero = int(numero_vaga)
        if 1 <= numero <= NUMERO_VAGAS:
            return True
        print(f"O número da vaga deve estar entre 1 e {NUMERO_VAGAS}.")
    except ValueError:
        print("O número da vaga deve ser um valor numérico válido.")
    return False

# Função para verificar se a vaga está ocupada
def verificar_vaga_ocupada(numero_vaga):
    return any(int(veiculo['numero_vaga']) == int(numero_vaga) for veiculo in veiculos)

# Função para solicitar e validar um campo de texto
def solicitar_campo_texto(campo_nome):
    while True:
        entrada = input(f"Digite o {campo_nome}: ")
        if validar_texto(entrada, campo_nome):
            return entrada

# Função para pausar antes de retornar ao menu
def pausar():
    input("\nPressione Enter para voltar ao menu principal...")

# Função para adicionar veículo
def adicionar_veiculo():
    placa = input("Digite a placa do veículo (formato 'AAA1234'): ")
    if not validar_placa(placa):
        return

    if verificar_placa(placa.upper()) != -1:
        print("Placa já cadastrada.")
        return

    modelo = solicitar_campo_texto("marca do veículo")
    cor = solicitar_campo_texto("cor do veículo")
    nome_dono = solicitar_campo_texto("nome do dono")

    numero_vaga = input("Digite o número da vaga (1-10): ")
    if not validar_numero_vaga(numero_vaga) or verificar_vaga_ocupada(numero_vaga):
        print("Número de vaga inválido ou já ocupado.")
        return

    # Utilizar o horário atual do sistema
    horario = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Horário gerado: {horario}")

    veiculos.append({
        'placa': placa.upper(),
        'modelo': modelo,
        'cor': cor,
        'nome_dono': nome_dono,
        'numero_vaga': numero_vaga,
        'horario': horario
    })
    print("Veículo adicionado com sucesso!")
    pausar()

# Função para excluir veículo
def excluir_veiculo():
    placa = input("Digite a placa do veículo a ser excluído: ")
    if not validar_placa(placa):
        return

    index = verificar_placa(placa.upper())
    if index == -1:
        print("Placa não encontrada.")
    else:
        confirmacao = input(f"Tem certeza que deseja excluir o veículo com a placa {placa.upper()}? (S/N): ").strip().lower()
        if confirmacao == 's':
            veiculos.pop(index)
            print("Veículo excluído com sucesso!")
        else:
            print("Operação cancelada.")
    pausar()

# Função para alterar veículo
def alterar_veiculo():
    placa = input("Digite a placa do veículo a ser alterado: ")
    if not validar_placa(placa):
        return

    index = verificar_placa(placa.upper())
    if index == -1:
        print("Placa não encontrada.")
        return

    modelo = solicitar_campo_texto("marca do veículo")
    cor = solicitar_campo_texto("cor do veículo")
    nome_dono = solicitar_campo_texto("nome do dono")

    numero_vaga = input("Digite o novo número da vaga (1-10): ")
    if not validar_numero_vaga(numero_vaga) or verificar_vaga_ocupada(numero_vaga):
        print("Número de vaga inválido ou já ocupado.")
        return

    # Utilizar o horário atual do sistema para a alteração
    horario = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Novo horário gerado: {horario}")

    veiculos[index] = {
        'placa': placa.upper(),
        'modelo': modelo,
        'cor': cor,
        'nome_dono': nome_dono,
        'numero_vaga': numero_vaga,
        'horario': horario
    }
    print("Veículo alterado com sucesso!")
    pausar()

# Função para mostrar relatório geral com tabulate e termcolor
def relatorio_geral():
    if not veiculos:
        print("Nenhum veículo cadastrado.")
    else:
        print("\nRelatório Geral:")
        
        # Tabela com os dados dos veículos
        tabela = [
            [
                veiculo['placa'],
                veiculo['modelo'],
                veiculo['cor'],
                veiculo['nome_dono'],
                veiculo['numero_vaga'],
                veiculo['horario']
            ]
            for veiculo in veiculos
        ]
        
        # Definindo as cores dos cabeçalhos e das células
        cabecalho = ["Placa", "Modelo", "Cor", "Dono", "Vaga", "Horário"]
        
        # Cor do cabeçalho (exemplo: rosa)
        cabecalho_colorido = [colored(coluna, 'magenta') for coluna in cabecalho]  # Alterado para 'magenta' (rosa)

        # Exibindo a tabela com as cores
        print(tabulate(tabela, headers=cabecalho_colorido, tablefmt="fancy_grid"))
    
    pausar()

def visualizar_vagas():
    ocupadas = {int(veiculo['numero_vaga']) for veiculo in veiculos}
    todas_as_vagas = set(range(1, NUMERO_VAGAS + 1))
    vagas_disponiveis = todas_as_vagas - ocupadas

    print("\nStatus das Vagas:")

    # Criar a tabela com células coloridas diretamente com 'colored'
    tabela = [
        [colored("Ocupadas", 'magenta'), colored(", ".join(map(str, sorted(ocupadas))), 'magenta')],
        [colored("Disponíveis", 'magenta'), colored(", ".join(map(str, sorted(vagas_disponiveis))), 'magenta')],
    ]
    
    # Definindo os cabeçalhos com a cor 'magenta' para rosa
    cabecalho_colorido = [colored(coluna, 'magenta') for coluna in ["Status", "Vagas"]]
    
    # Exibindo a tabela com as cores
    print(tabulate(tabela, headers=cabecalho_colorido, tablefmt="fancy_grid", numalign="center", stralign="center"))
    pausar()



def pesquisar_por_nome():
    modelo = input("Digite o modelo do veículo para pesquisa: ")
    resultados = [v for v in veiculos if v['modelo'].lower() == modelo.lower()]

    if resultados:
        # Criar tabela com células coloridas diretamente com 'colored'
        tabela = [
            [
                colored(veiculo['placa'], 'magenta'), 
                colored(veiculo['modelo'], 'magenta'), 
                colored(veiculo['cor'], 'magenta'),
                colored(veiculo['nome_dono'], 'magenta'),
                colored(veiculo['numero_vaga'], 'magenta'),
                colored(veiculo['horario'], 'magenta')
            ]
            for veiculo in resultados
        ]
        
        # Definindo o cabeçalho com a cor 'magenta' para deixar em rosa
        cabecalho_colorido = [colored(coluna, 'magenta') for coluna in ["Placa", "Modelo", "Cor", "Dono", "Vaga", "Horário"]]
        
        # Agora só usamos o tabulate para o layout, com os cabeçalhos coloridos
        print(tabulate(tabela, headers=cabecalho_colorido, tablefmt="fancy_grid"))
    else:
        print("Veículo não encontrado.")
    pausar()


# Função principal do menu
def menu():
    while True:
        # Definindo o cabeçalho e as opções do menu
        cabecalho = ["Opção", "Descrição"]
        opcoes = [
            ['1', 'Adicionar Veículo'],
            ['2', 'Excluir Veículo'],
            ['3', 'Alterar Veículo'],
            ['4', 'Relatório Geral'],
            ['5', 'Visualizar Vagas'],
            ['6', 'Pesquisar por modelo'],
            ['7', 'Sair']
        ]
        
        # Exibindo a tabela do menu principal na cor rosa
        opcoes_coloridas = [
            [colored(opcao[0], 'magenta'), colored(opcao[1], 'magenta')] 
            for opcao in opcoes
        ]
        
        print(tabulate(opcoes_coloridas, headers=cabecalho, tablefmt="fancy_grid"))
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_veiculo()
        elif escolha == '2':
            excluir_veiculo()
        elif escolha == '3':
            alterar_veiculo()
        elif escolha == '4':
            relatorio_geral()
        elif escolha == '5':
            visualizar_vagas()
        elif escolha == '6':
            pesquisar_por_nome()
        elif escolha == '7':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Chama o menu
menu()
