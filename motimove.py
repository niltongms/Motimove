# Versao 1: App de Terminal com CRUD e Persistencia em Arquivos

import json
import os# Versao 1: App de Terminal com CRUD e Persistencia em Arquivos

import json
import os
import random

ARQUIVO_DADOS = 'usuarios.json'

# ----------------- Utilitários -----------------
def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r') as f:
            return json.load(f)
    return {}

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, 'w') as f:
        json.dump(dados, f, indent=4)

# ----------------- CRUD -----------------
def criar_usuario(dados):
    nome = input("Nome: ")
    idade = input("Idade: ")
    genero = input("Gênero: ")
    estado = input("Estado: ")
    bairro = input("Bairro: ")
    dados[nome] = {
        'idade': idade,
        'genero': genero,
        'estado': estado,
        'bairro': bairro,
        'atividades': []
    }
    salvar_dados(dados)
    print(f"Usuário {nome} criado com sucesso!\n")

def listar_usuarios(dados):
    if not dados:
        print("Nenhum usuário encontrado.")
        return
    for i, nome in enumerate(dados):
        print(f"{i+1}. {nome} - {dados[nome]['estado']}/{dados[nome]['bairro']}")

def atualizar_usuario(dados):
    nome = input("Nome do usuário a atualizar: ")
    if nome in dados:
        dados[nome]['idade'] = input("Nova idade: ")
        dados[nome]['genero'] = input("Novo gênero: ")
        dados[nome]['estado'] = input("Novo estado: ")
        dados[nome]['bairro'] = input("Novo bairro: ")
        salvar_dados(dados)
        print("Usuário atualizado com sucesso!\n")
    else:
        print("Usuário não encontrado.\n")

def deletar_usuario(dados):
    nome = input("Nome do usuário a deletar: ")
    if nome in dados:
        del dados[nome]
        salvar_dados(dados)
        print("Usuário deletado.\n")
    else:
        print("Usuário não encontrado.\n")

# ----------------- Atividades -----------------
def registrar_atividade(dados):
    nome = input("Nome do usuário: ")
    if nome not in dados:
        print("Usuário não encontrado.\n")
        return

    tipo = input("Atividade (corrida, academia, luta, caminhada, casa, personalizado, outro): ").lower()
    tempo = int(input("Tempo (min): "))
    distancia = 0
    if tipo == "corrida":
        distancia = float(input("Distância (km): "))

    pontos = calcular_pontos(tipo, tempo, distancia)
    dados[nome]['atividades'].append({'tipo': tipo, 'tempo': tempo, 'distancia': distancia, 'pontos': pontos})
    salvar_dados(dados)
    print(f"Atividade registrada! Pontos ganhos: {pontos}\n")

def calcular_pontos(tipo, tempo, distancia):
    if tipo == "corrida":
        return tempo + int(distancia * 10)
    elif tipo == "academia":
        return tempo + 5
    elif tipo == "luta":
        return tempo + 8
    elif tipo == "caminhada":
        return int(tempo * 0.8)
    elif tipo == "casa":
        return tempo + 4
    elif tipo == "personalizado":
        return tempo + 6
    else:
        return tempo

def mostrar_ranking(dados):
    print("\n🏆 Ranking Diário")
    placar = {}
    for nome, info in dados.items():
        total = sum([a['pontos'] for a in info['atividades']])
        placar[nome] = total
    placar = dict(sorted(placar.items(), key=lambda x: x[1], reverse=True))
    for i, (nome, pontos) in enumerate(placar.items(), 1):
        print(f"{i}. {nome} - {pontos} pontos")

# ----------------- Menu Principal -----------------
def menu():
    dados = carregar_dados()
    opcoes = {
        '1': criar_usuario,
        '2': listar_usuarios,
        '3': atualizar_usuario,
        '4': deletar_usuario,
        '5': registrar_atividade,
        '6': mostrar_ranking
    }
    while True:
        print("""
MotiMove - Menu Principal
1. Criar usuário
2. Listar usuários
3. Atualizar usuário
4. Deletar usuário
5. Registrar atividade
6. Ver ranking
0. Sair
""")
        escolha = input("Escolha uma opção: ")
        if escolha == '0':
            break
        elif escolha in opcoes:
            try:
                opcoes[escolha](dados)
            except Exception as e:
                print(f"Erro: {e}\n")
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()

import random

ARQUIVO_DADOS = 'usuarios.json'

# ----------------- Utilitários -----------------
def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r') as f:
            return json.load(f)
    return {}

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, 'w') as f:
        json.dump(dados, f, indent=4)

# ----------------- CRUD -----------------
def criar_usuario(dados):
    nome = input("Nome: ")
    idade = input("Idade: ")
    genero = input("Gênero: ")
    estado = input("Estado: ")
    bairro = input("Bairro: ")
    dados[nome] = {
        'idade': idade,
        'genero': genero,
        'estado': estado,
        'bairro': bairro,
        'atividades': []
    }
    salvar_dados(dados)
    print(f"Usuário {nome} criado com sucesso!\n")

def listar_usuarios(dados):
    if not dados:
        print("Nenhum usuário encontrado.")
        return
    for i, nome in enumerate(dados):
        print(f"{i+1}. {nome} - {dados[nome]['estado']}/{dados[nome]['bairro']}")

def atualizar_usuario(dados):
    nome = input("Nome do usuário a atualizar: ")
    if nome in dados:
        dados[nome]['idade'] = input("Nova idade: ")
        dados[nome]['genero'] = input("Novo gênero: ")
        dados[nome]['estado'] = input("Novo estado: ")
        dados[nome]['bairro'] = input("Novo bairro: ")
        salvar_dados(dados)
        print("Usuário atualizado com sucesso!\n")
    else:
        print("Usuário não encontrado.\n")

def deletar_usuario(dados):
    nome = input("Nome do usuário a deletar: ")
    if nome in dados:
        del dados[nome]
        salvar_dados(dados)
        print("Usuário deletado.\n")
    else:
        print("Usuário não encontrado.\n")

# ----------------- Atividades -----------------
def registrar_atividade(dados):
    nome = input("Nome do usuário: ")
    if nome not in dados:
        print("Usuário não encontrado.\n")
        return

    tipo = input("Atividade (corrida, academia, luta, caminhada, casa, personalizado, outro): ").lower()
    tempo = int(input("Tempo (min): "))
    distancia = 0
    if tipo == "corrida":
        distancia = float(input("Distância (km): "))

    pontos = calcular_pontos(tipo, tempo, distancia)
    dados[nome]['atividades'].append({'tipo': tipo, 'tempo': tempo, 'distancia': distancia, 'pontos': pontos})
    salvar_dados(dados)
    print(f"Atividade registrada! Pontos ganhos: {pontos}\n")

def calcular_pontos(tipo, tempo, distancia):
    if tipo == "corrida":
        return tempo + int(distancia * 10)
    elif tipo == "academia":
        return tempo + 5
    elif tipo == "luta":
        return tempo + 8
    elif tipo == "caminhada":
        return int(tempo * 0.8)
    elif tipo == "casa":
        return tempo + 4
    elif tipo == "personalizado":
        return tempo + 6
    else:
        return tempo

def mostrar_ranking(dados):
    print("\n🏆 Ranking Diário")
    placar = {}
    for nome, info in dados.items():
        total = sum([a['pontos'] for a in info['atividades']])
        placar[nome] = total
    placar = dict(sorted(placar.items(), key=lambda x: x[1], reverse=True))
    for i, (nome, pontos) in enumerate(placar.items(), 1):
        print(f"{i}. {nome} - {pontos} pontos")

# ----------------- Menu Principal -----------------
def menu():
    dados = carregar_dados()
    opcoes = {
        '1': criar_usuario,
        '2': listar_usuarios,
        '3': atualizar_usuario,
        '4': deletar_usuario,
        '5': registrar_atividade,
        '6': mostrar_ranking
    }
    while True:
        print("""
MotiMove - Menu Principal
1. Criar usuário
2. Listar usuários
3. Atualizar usuário
4. Deletar usuário
5. Registrar atividade
6. Ver ranking
0. Sair
""")
        escolha = input("Escolha uma opção: ")
        if escolha == '0':
            break
        elif escolha in opcoes:
            try:
                opcoes[escolha](dados)
            except Exception as e:
                print(f"Erro: {e}\n")
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()
