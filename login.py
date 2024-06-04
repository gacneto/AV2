import json
import os
import re
from time import sleep


info = os.path.join(os.path.dirname(__file__), 'usuarios.json')

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def texto_legal():
    print("\nBem vindo a ENEMAPROVADO, aqui seu sucesso no ENEM é nossa prioridade.") 
    print("Oferecemos materiais atualizados, videoaulas com os melhores professores, simulados realistas e planos de estudo personalizados.")
    print("Nossos mentores estão prontos para ajudar com orientação personalizada e dicas valiosas.")
    print("\nJunte-se à nossa comunidade acolhedora e transforme sua preparação para o ENEM em uma jornada eficaz e motivadora. Vamos juntos conquistar a sua vitória!")


def inicio1():
    print('-'* 34)
    print("BEM VINDO A SUA PLATAFORMA DE ENEM")
    print('-'* 34)

def inicio():
    texto_legal()
    print("\n")
    print("1 - Login")
    print("2 - Cadastro")
    print("3 - Sair")
    while True:
        opcao1 = input("\nEscolha uma opção: ")
        if opcao1 == '1':
            login()
        elif opcao1 == '2':
                cadastro()
        elif opcao1 == '3':
            limpar()
            print("Saindo...")
            sleep(1)
            limpar()
            break
        
def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(padrao, email):
        return True
    return False

def cadastro():
    limpar()
    inicio1()
    nome = input("Digite seu nome completo: ")
    while True:
        email = input("Digite seu email: ")
        if validar_email(email):
            break
        else:
            print("Email inválido! Tente novamente.")

    while True:
        cpf = input("Digite seu cpf: ")
        if validar_cpf(cpf):
            break
        else:
            print("CPF inválido. Tente novamente")

    senha = input("Digite uma senha: ")

    with open(info, 'r') as infs:
        usuarios = json.load(infs)

    usuarios.append({'nome': nome, 'email': email, 'cpf': cpf, 'senha': senha})

    with open(info, 'w') as infs:
        json.dump(usuarios, infs, indent=4)
    print("\nBem vindo " + nome + " a sua plataforma de ENEM favorita")
    print()
    menu_plataforma()

def menu_plataforma():
    while True:
        limpar()
        print("-------------")
        print("ENEM APROVADO")
        print("-------------")
        print("1- Atualizar dados")
        print("2- Remover dados")
        print("3- Buscar usuário")
        print("4- Voltar ao menu")
        opcao2 = input("\nEscolha uma opção: ")

        if opcao2 == '1':
            limpar()
            atualizar()
            break
        elif opcao2 == '2':
            limpar()
            remover()
        elif opcao2 == '3':
            limpar()
            buscar()
        elif opcao2 == '4':
            limpar()
            inicio1()
            inicio()
            break

def remover():
    with open(info, 'r') as infs:
        usuarios = json.load(infs)
        
    print("-------------")
    print("ENEM APROVADO")
    print("-------------")
    print("\nQual o usuário que deseja remover? ")
    cpf = input("CPF---->")
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuarios.remove(usuario)
            print("\nUsuário removido com sucesso!")
        else:
            print("\nUsuario não encontrado, tente novamente.")
            break
        with open(info, 'w') as infs:
            json.dump(usuarios, infs, indent=4)
            
        while True:
            voltar = input("\nAperte Enter para voltar ao menu")
            match voltar:
                case __:
                    menu_plataforma()
                

def atualizar():
    limpar()
    with open(info, 'r') as infs:
        usuarios = json.load(infs)

    print("\n====================")
    print("Atualização de Dados")
    print("====================")

    while True:
        cpf = input("\nDigite seu CPF: ")
        if validar_cpf(cpf):
            break
        else:
            print("CPF inválido. Tente novamente.")

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("Nenhum usuário com esse CPF encontrado.")
        return

    while True:
        print("\n1- CPF")
        print("2- Email")
        print("3- Nome")
        print("4- Senha")
        escolha = input("Deseja atualizar qual dado? ")

        if escolha == '1':
            cpf_att = input("Qual o novo CPF desejado? ")
            if validar_cpf(cpf_att):
                usuario_encontrado['cpf'] = cpf_att
                print("CPF atualizado com sucesso!")
            else:
                print("CPF inválido. Tente novamente.")
                continue
        elif escolha == '2':
            email_att = input("Qual o novo email desejado? ")
            usuario_encontrado['email'] = email_att
            print("Email atualizado com sucesso!")
        elif escolha == '3':
            nome_att = input("Qual o novo nome desejado? ")
            usuario_encontrado['nome'] = nome_att
            print("Nome atualizado com sucesso!")
        elif escolha == '4':
            senha_att = input("Qual a nova senha desejada? ")
            usuario_encontrado['senha'] = senha_att
            print("Senha atualizada com sucesso!")
        else:
            print("Opção inválida.")
            continue

        desejo = input("Deseja mudar mais algum dado? S/N\n")
        if desejo.lower() == 'n':
            break

    with open(info, 'w') as outfs:
        json.dump(usuarios, outfs, indent=4)

    menu_plataforma()

    
    


def login():
    limpar()
    inicio1()
    cpf = input("Digite seu cpf: ")
    senha = input("Digite sua senha: ")

    with open(info, 'r') as infs:
        usuarios = json.load(infs)

    for usuario in usuarios:
        if usuario['cpf'] == cpf and usuario['senha'] == senha:
            print(f"Bem vindo, {usuario['nome']}!")
            menu_plataforma()
            return
    limpar()
    print("CPF ou senha incorretos.")
    inicio1()
    inicio()

def buscar():
    limpar()
    
    with open(info, 'r') as infs:
        usuarios = json.load(infs)

    if usuarios:
        print("==================")
        print("Busca de usuários:")
        print("==================")
        while True:
            cpf = input("\nDigite o CPF desejado: ")
            if validar_cpf(cpf):
                break
            else:
                print("CPF inválido. Tente novamente.")

        usuario_encontrado = None
        for usuario in usuarios:
            if usuario['cpf'] == cpf:
                usuario_encontrado = usuario
                break

        if usuario_encontrado:
            print("\nAqui estão as informações do usuário:")
            print(f"Nome: {usuario_encontrado['nome']}, Email: {usuario_encontrado['email']}, CPF: {usuario_encontrado['cpf']}, senha: {usuario_encontrado['senha']}")
        else:
            print("Nenhum usuário com esse CPF encontrado.")

    desejo = input("\nDeseja fazer mais uma busca? S/N\n").strip().lower()
    if desejo == 's':
        buscar()
    else:
        menu_plataforma()

def main():
    while True:
        inicio1()
        if not inicio():
            break

if __name__=='__main__':
    main()
