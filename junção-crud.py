import json
import os
import re
from time import sleep

info = os.path.join(os.path.dirname(__file__), 'usuarios.json')

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def texto_legal():
    print("\nBem vindo a ENEMAPROVADO, aqui seu sucesso no ENEM é nossa prioridade.") 
    print("Oferecemos materiais atualizados, videoaulas com os melhores professores, simulados realistas e planos de estudo personalizados.")
    print("Nossos mentores estão prontos para ajudar com orientação personalizada e dicas valiosas.")
    print("\nJunte-se à nossa comunidade acolhedora e transforme sua preparação para o ENEM em uma jornada eficaz e motivadora. Vamos juntos conquistar a sua vitória!")

def lin(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)

def inicio1():
    print('-'* 34)
    print("BEM VINDO A SUA PLATAFORMA DE ENEM")
    print('-'* 34)

def carregar_usuarios():
    if not os.path.exists('usuarios.json'):
        return []
    with open('usuarios.json', 'r') as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []

def salvar_usuarios(usuarios):
    with open('usuarios.json', 'w') as arquivo:
        json.dump(usuarios, arquivo, indent=4)

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(padrao, email):
        return True
    return False

def cadastro():
    nome = input('Informe seu nome completo: ')
    while True:
        cpf = input('Informe seu CPF (11 dígitos): ')
        if validar_cpf(cpf):
            break
        else:
            print('CPF inválido. Deve conter exatamente 11 dígitos numéricos.')
    email = input('Informe seu e-mail: ')
    while True:
        email = input("Digite seu email: ")
        if validar_email(email):
            break
        else:
            print("Email inválido! Tente novamente.")
    senha = input('Informe sua senha: ')
    if not nome or not cpf or not email or not senha:
        print("Todos os campos são obrigatórios!")
        return
    usuario = {'nome': nome, 'cpf': cpf, 'email': email, 'senha': senha}
    usuarios = carregar_usuarios()
    usuarios.append(usuario)
    salvar_usuarios(usuarios)
    print(f'Cadastro de {nome} concluído com sucesso!')

def login():
    while True:
        cpf = input('Informe seu CPF (11 dígitos): ')
        if validar_cpf(cpf):
            break
        else:
            print('CPF inválido. Deve conter exatamente 11 dígitos numéricos.')
    senha = input('Informe sua senha: ')
    usuarios = carregar_usuarios()
    encontrados = [s for s in usuarios if s['cpf'] == cpf and s['senha'] == senha]
    if encontrados:
        usuario = encontrados[0]  
        while True:
            limpar()
            lin('   CONTA PESSOAL')
            print('\n1. Meus dados')
            print('2. Atualizar dados')
            print('3. Remover dados')
            print('4. Mais informações')
            print('5. Sair')

            opcao2 = input('Escolha uma opção: ')

            if opcao2 == '1':
                limpar()
                print(f'Dados encontrados para o usuário {usuario["nome"]}:')
                print(f'CPF: {usuario["cpf"]}')
                print(f'E-mail: {usuario["email"]}')
                print(f'Senha: {usuario["senha"]}')
                input("Pressione Enter para continuar...")

            elif opcao2 == '2':
                limpar()
                atualizar_dados(usuarios, cpf, senha)
                input("Pressione Enter para continuar...")

            elif opcao2 == '3':
                limpar()
                remover_dados(usuarios, cpf)
                print("Cadastro removido com sucesso!")
                break
            
            elif opcao2 == '4':
                while True:
                    limpar()
                    lin('   SISTEMAS DE APRENDIZADO')
                    print('\n1. Simulado')
                    print('2. Cursos')
                    print('3. Horários')
                    print('4. Voltar')

                    opcao3 = input('Escolha uma opção: ')

                    if opcao3 == '1':
                        opcoes_simulado = {
                        "1": adicionar_simulado,
                        "2": procurar_simulados_por_disciplina,
                        "3": atualizar_simulado,
                        "4": remover_simulado,
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
                            
                            if opcao in opcoes_simulado:
                                limpar()
                                try:
                                    opcoes_simulado[opcao]()
                                except Exception as e:
                                    print(f"Ocorreu um erro: {e}")
                                input("Pressione Enter para continuar...")
                            elif opcao == '5':
                                break
                            else:
                                print("Opção inválida. Tente novamente.")
                                input("Pressione Enter para continuar...")  

                    elif opcao3 == '2':
                        opcoes_curso = {
                        "1": adicionar_curso,
                        "2": procurar_cursos,
                        "3": atualizar_curso,
                        "4": remover_curso,
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
                            
                            if opcao in opcoes_curso:
                                limpar()
                                try:
                                    opcoes_curso[opcao]()
                                except Exception as e:
                                    print(f"Ocorreu um erro: {e}")
                                input("Pressione Enter para continuar...")
                            elif opcao == '5':
                                break
                            else:
                                print("Opção inválida. Tente novamente.")
                                input("Pressione Enter para continuar...")

                    elif opcao3 == '3':
                        opcoes_horario = {
                        "1": adicionar_horario,
                        "2": procurar_horarios,
                        "3": atualizar_horario,
                        "4": remover_horario,
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
                            
                            if opcao in opcoes_horario:
                                limpar()
                                try:
                                    opcoes_horario[opcao]()
                                except Exception as e:
                                    print(f"Ocorreu um erro: {e}")
                                input("Pressione Enter para continuar...")
                            elif opcao == '5':
                                break
                            else:
                                print("Opção inválida. Tente novamente.")
                                input("Pressione Enter para continuar...")
                        
                    elif opcao3 == '4':
                        print("Saindo...")
                        break

                    else:
                        print("Opção inválida. Tente novamente.")
                        input("Pressione Enter para continuar...")
                        
            elif opcao2 == '4':
                print("Saindo...")
                break

            else:
                print("Opção inválida. Tente novamente.")
                input("Pressione Enter para continuar...")

    else:
        print('Nenhum cadastro encontrado!')

def atualizar_dados(usuarios, cpf, senha):
    for usuario in usuarios:
        if usuario['cpf'] == cpf and usuario['senha'] == senha:
            usuario['nome'] = input('Informe o novo nome: ')
            usuario['email'] = input('Informe o novo e-mail: ')
            usuario['senha'] = input('Informe a nova senha: ')
            break
    salvar_usuarios(usuarios)

def remover_dados(usuarios, cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuarios.remove(usuario)
            break
    salvar_usuarios(usuarios)

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
    data = input('Informe o dia (DD/MM): ').strip()
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
    opcoes_menu = {
        '1': login,
        '2': cadastro,
        '3': exit
    }

    while True:
        limpar()
        inicio1()
        texto_legal()
        lin('   SISTEMA DE LOGIN')
        print('\n1. Login')
        print('2. Cadastrar-se')
        print('3. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao in opcoes_menu:
            limpar()
            try:
                opcoes_menu[opcao]()
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
                input("Pressione Enter para continuar...")
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()