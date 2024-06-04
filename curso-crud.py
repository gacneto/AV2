import json
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def lin(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)

def carregar_cursos():
    if not os.path.exists('cursos.json'):
        return []
    with open('cursos.json', 'r') as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []

def salvar_cursos(cursos):
    with open('cursos.json', 'w') as arquivo:
        json.dump(cursos, arquivo, indent=4)

def adicionar_curso():
    nome = input("Nome do curso: ")
    descricao = input("Descrição: ")
    duracao = input("Duração: ")
    if not nome or not descricao or not duracao:
        print("Todos os campos são obrigatórios!")
        return
    curso = {'nome': nome, 'descricao': descricao, 'duracao': duracao}
    cursos = carregar_cursos()
    cursos.append(curso)
    salvar_cursos(cursos)
    print("Curso adicionado com sucesso!")

def procurar_cursos():
    nome = input("Nome do curso: ")
    cursos = carregar_cursos()
    encontrados = [s for s in cursos if s['nome'].lower() == nome.lower()]
    if encontrados:
        for curso in encontrados:
            print(f"Nome: {curso['nome']}, Descrição: {curso['descricao']}, Duração: {curso['duracao']}")
    else:
        print(f"Nenhum curso encontrado com o nome {nome}")

def atualizar_curso():
    nome = input("Nome do curso a atualizar: ")
    cursos = carregar_cursos()
    encontrados = [s for s in cursos if s['nome'].lower() == nome.lower()]
    if encontrados:
        for i, curso in enumerate(encontrados, 1):
            print(f"{i}. Nome: {curso['nome']}, Descrição: {curso['descricao']}, Duração: {curso['duracao']}")
        try:
            indice = int(input("Escolha o número do curso a atualizar: ")) - 1
            if 0 <= indice < len(encontrados):
                novo_nome = input("Novo Nome (deixe vazio para não alterar): ")
                descricao = input("Nova Descrição (deixe vazio para não alterar): ")
                duracao = input("Nova Duração (deixe vazio para não alterar): ")
                if novo_nome:
                    encontrados[indice]['nome'] = novo_nome
                if descricao:
                    encontrados[indice]['descricao'] = descricao
                if duracao:
                    encontrados[indice]['duracao'] = duracao
                salvar_cursos(cursos)
                print("Curso atualizado com sucesso!")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    else:
        print(f"Nenhum curso encontrado com o nome {nome}")

def remover_curso():
    nome = input("Nome do curso a remover: ")
    cursos = carregar_cursos()
    encontrados = [c for c in cursos if c['nome'].lower() == nome.lower()]
    if encontrados:
        for i, curso in enumerate(encontrados, 1):
            print(f"{i}. Nome: {curso['nome']}, Descrição: {curso['descricao']}, Duração: {curso['duracao']}")
        try:
            indice = int(input("Escolha o número do curso a remover: ")) - 1
            if 0 <= indice < len(encontrados):
                cursos.remove(encontrados[indice])
                salvar_cursos(cursos)
                print("Curso removido com sucesso!")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    else:
        print(f"Nenhum curso encontrado com o nome {nome}")

def main():
    OPCOES_MENU = {
        "1": adicionar_curso,
        "2": procurar_cursos,
        "3": atualizar_curso,
        "4": remover_curso,
        "5": exit
    }

    while True:
        limpar()
        lin('   SISTEMA DE CURSOS')
        print('\n1. Adicionar curso')
        print('2. Procurar curso')
        print('3. Atualizar curso')
        print('4. Remover curso')
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
