import random

# ✅ Motimove – Seu motivador diário de atividade física!

# Lista para armazenar as pontuações do dia (não persiste)
atividades_do_dia = []

# Coleta os dados iniciais do usuário
def boas_vindas():
    print("🏃‍♂️ Bem-vindo ao MotiMove!")
    nome = input("Nome: ")
    input("Idade: ")
    input("Gênero: ")
    input("Estado: ")
    input("Bairro: ")
    print(f"\nOlá, {nome}! Pronto para se movimentar hoje?\n")
    return nome

# Sugestões simples de locais
def recomendar_locais():
    print("📍 Sugestões de locais para treinar:")
    print("- Praça pública")
    print("- Academia do bairro")
    print("- Centro de lutas")
    print("- Ciclovia ou parque")
    print("- 🏠 Treino em casa (com vídeos ou apps)\n")

# Registro de atividade do dia
def registrar_atividade():
    print("Tipos: corrida, academia, luta, caminhada, treino em casa, treino personalizado, outro")
    tipo = input("Atividade feita hoje: ").lower()
    tempo = int(input("Quantos minutos? "))
    distancia = 0

    if tipo == "corrida":
        distancia = float(input("Distância (km): "))

    pontos = calcular_pontos(tipo, tempo, distancia)
    atividades_do_dia.append(pontos)
    print(f"✅ Você ganhou {pontos} pontos nesta atividade!\n")
    return pontos

# Cálculo de pontos
def calcular_pontos(tipo, tempo, distancia=0):
    if tipo == "corrida":
        return tempo + int(distancia * 10)
    elif tipo == "academia":
        return tempo + 5
    elif tipo == "luta":
        return tempo + 8
    elif tipo == "caminhada":
        return int(tempo * 0.8)
    elif tipo == "treino em casa":
        return tempo + 4
    elif tipo == "treino personalizado":
        return tempo + 6
    else:
        return tempo

# Ranking do dia entre amigos (simulado)
def mostrar_ranking(nome):
    total = sum(atividades_do_dia)
    amigos = {
        "Ana": random.randint(50, 150),
        "Carlos": random.randint(50, 150),
        "Bruno": random.randint(50, 150),
        nome: total
    }
    ranking = sorted(amigos.items(), key=lambda x: x[1], reverse=True)
    posicao = [i for i, (n, _) in enumerate(ranking, 1) if n == nome][0]

    print(f"📊 Hoje você somou: {total} pontos")
    print(f"🏅 Posição no ranking diário: {posicao}º lugar\n")

# Execução principal
nome = boas_vindas()
recomendar_locais()

while input("Registrar uma atividade de hoje? (s/n): ").lower() == "s":
    registrar_atividade()
    mostrar_ranking(nome)

print("💪 Parabéns por se manter ativo hoje com o MotiMove!")
