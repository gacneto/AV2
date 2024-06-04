import json
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def lin(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)

def carregar_simulados():
    if not os.path.exists('simulados.json'):
        return []
    with open('simulados.json', 'r') as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []

def salvar_simulados(simulados):
    with open('simulados.json', 'w') as arquivo:
        json.dump(simulados, arquivo, indent=4)

def adicionar_simulado():
    nome = input("Nome do simulado: ")
    disciplina = input("Disciplina: ")
    responsavel = input("Responsável: ")
    if not nome or not disciplina or not responsavel:
        print("Todos os campos são obrigatórios!")
        return
    simulado = {'nome': nome, 'disciplina': disciplina, 'responsavel': responsavel}
    simulados = carregar_simulados()
    simulados.append(simulado)
    salvar_simulados(simulados)
    print("Simulado adicionado com sucesso!")

def procurar_simulados_por_disciplina():
    disciplina = input("Disciplina: ")
    simulados = carregar_simulados()
    encontrados = [s for s in simulados if s['disciplina'].lower() == disciplina.lower()]
    if encontrados:
        for simulado in encontrados:
            print(f"Nome: {simulado['nome']}, Disciplina: {simulado['disciplina']}, Responsável: {simulado['responsavel']}")
    else:
        print(f"Nenhum simulado encontrado para a disciplina {disciplina}")

def atualizar_simulado():
    disciplina = input("Disciplina do simulado a atualizar: ")
    simulados = carregar_simulados()
    encontrados = [s for s in simulados if s['disciplina'].lower() == disciplina.lower()]
    if encontrados:
        for i, simulado in enumerate(encontrados, 1):
            print(f"{i}. Nome: {simulado['nome']}, Disciplina: {simulado['disciplina']}, Responsável: {simulado['responsavel']}")
        try:
            indice = int(input("Escolha o número do simulado a atualizar: ")) - 1
            if 0 <= indice < len(encontrados):
                nome = input("Novo Nome (deixe vazio para não alterar): ")
                responsavel = input("Novo Responsável (deixe vazio para não alterar): ")
                if nome:
                    encontrados[indice]['nome'] = nome
                if responsavel:
                    encontrados[indice]['responsavel'] = responsavel
                salvar_simulados(simulados)
                print("Simulado atualizado com sucesso!")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    else:
        print(f"Nenhum simulado encontrado para a disciplina {disciplina}")

def remover_simulado():
    disciplina = input("Disciplina do simulado a remover: ")
    simulados = carregar_simulados()
    encontrados = [s for s in simulados if s['disciplina'].lower() == disciplina.lower()]
    if encontrados:
        for i, simulado in enumerate(encontrados, 1):
            print(f"{i}. Nome: {simulado['nome']}, Disciplina: {simulado['disciplina']}, Responsável: {simulado['responsavel']}")
        try:
            indice = int(input("Escolha o número do simulado a remover: ")) - 1
            if 0 <= indice < len(encontrados):
                simulados.remove(encontrados[indice])
                salvar_simulados(simulados)
                print("Simulado removido com sucesso!")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    else:
        print(f"Nenhum simulado encontrado para a disciplina {disciplina}")

def main():
    OPCOES_MENU = {
        "1": adicionar_simulado,
        "2": procurar_simulados_por_disciplina,
        "3": atualizar_simulado,
        "4": remover_simulado,
        "5": exit
    }

    while True:
        limpar()
        lin('   SISTEMA DE SIMULADOS')
        print('\n1. Adicionar simulado')
        print('2. Procurar simulado por disciplina')
        print('3. Atualizar simulado')
        print('4. Remover simulado')
        print('5. Sair')

        opcao = input('Escolha uma opção: ')
        
        if opcao in OPCOES_MENU:
            limpar()
            try:
                OPCOES_MENU[opcao]()
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
            input("Pressione Enter para continuar...")
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
