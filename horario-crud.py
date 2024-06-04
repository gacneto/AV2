import json
import os
from datetime import datetime

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def lin(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)

def validar_data(data, formato="%d/%m"):
    try:
        datetime.strptime(data, formato)
        return True
    except ValueError:
        return False


def carregar_horarios():
    if not os.path.exists('horarios.json'):
        return []
    with open('horarios.json', 'r') as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []

def salvar_horarios(horarios):
    with open('horarios.json', 'w') as arquivo:
        json.dump(horarios, arquivo, indent=4)

def adicionar_horario():
    nome = input('Informe o seu nome completo: ').strip()
    while True:
            data = input('Informe o dia (DD/MM): ').strip()
            if validar_data(data):
                    break
            else:
                print("Data inválida. Tente novamente.")

    horario = input('Informe um horário: ').strip()
    if not nome or not data or not horario:
        print("Todos os campos são obrigatórios!")
        return
    horario_estudo = {'nome': nome, 'data': data, 'horario': horario}
    horarios = carregar_horarios()
    horarios.append(horario_estudo)
    salvar_horarios(horarios)
    print(f'Horário de {nome} adicionado com sucesso!')

def procurar_horarios():
    data = input('Informe o dia (DD/MM): ').strip()
    horarios = carregar_horarios()
    encontrados = [h for h in horarios if h['data'] == data]
    if encontrados:
        for horario in encontrados:
            print(f"Nome: {horario['nome']}, Data: {horario['data']}, Horário: {horario['horario']}")
    else:
        print(f"Nenhum horário encontrado para o dia {data}")

def atualizar_horario():
    data = input('Informe o dia (DD/MM) do horário a ser atualizado: ').strip()
    horarios = carregar_horarios()
    encontrados = [h for h in horarios if h['data'] == data]
    if encontrados:
        for i, horario in enumerate(encontrados, 1):
            print(f"{i}. Nome: {horario['nome']}, Data: {horario['data']}, Horário: {horario['horario']}")
        try:
            indice = int(input("Escolha o número do horário a atualizar: ")) - 1
            if 0 <= indice < len(encontrados):
                novo_nome = input("Novo Nome (deixe vazio para não alterar): ").strip()
                novo_horario = input("Novo Horário (deixe vazio para não alterar): ").strip()
                if novo_nome:
                    encontrados[indice]['nome'] = novo_nome
                if novo_horario:
                    encontrados[indice]['horario'] = novo_horario
                salvar_horarios(horarios)
                print("Horário atualizado com sucesso!")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    else:
        print(f"Nenhum horário encontrado para o dia {data}")

def remover_horario():
    data = input('Informe o dia (DD/MM) do horário a ser removido: ').strip()
    horarios = carregar_horarios()
    encontrados = [h for h in horarios if h['data'] == data]
    if encontrados:
        for i, horario in enumerate(encontrados, 1):
            print(f"{i}. Nome: {horario['nome']}, Data: {horario['data']}, Horário: {horario['horario']}")
        try:
            indice = int(input("Escolha o número do horário a remover: ")) - 1
            if 0 <= indice < len(encontrados):
                horarios.remove(encontrados[indice])
                salvar_horarios(horarios)
                print("Horário removido com sucesso!")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    else:
        print(f"Nenhum horário encontrado para o dia {data}")

def main():
    OPCOES_MENU = {
        "1": adicionar_horario,
        "2": procurar_horarios,
        "3": atualizar_horario,
        "4": remover_horario,
        "5": exit
    }

    while True:
        limpar()
        lin('   SISTEMA DE HORÁRIOS')
        print('\n1. Adicionar horário')
        print('2. Procurar horário salvo')
        print('3. Atualizar horário')
        print('4. Remover horário')
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
