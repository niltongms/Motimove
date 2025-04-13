import random

# 🟢 Motimove – Seu motivador de movimento diário!

# Variável para armazenar os pontos do usuário ao longo da semana
pontos_semanais = []

# Função para coletar dados básicos do usuário
def boas_vindas():
    print("🟢 Bem-vindo ao Motimove – Seu motivador de movimento diário!")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    genero = input("Digite seu gênero: ")
    estado = input("Digite seu estado: ")
    bairro = input("Digite seu bairro: ")
    
    print(f"\nOlá, {nome}! Vamos te ajudar a se manter ativo!\n")
    return nome

# Sugestão de locais para atividade física
def recomendar_locais():
    print("📍 Sugestões de locais próximos para treinar:")
    print("- Praça pública (boa para caminhada ou corrida)")
    print("- Academia do bairro")
    print("- Centro de artes marciais")
    print("- Ciclovia ou parque para pedalar\n")

# Função que registra a atividade física feita
def registrar_atividade():
    tipo = input("Qual atividade você fez? (corrida, academia, luta, caminhada, outro): ").lower()
    tempo = int(input("Quantos minutos você praticou? "))

    distancia = 0
    if tipo == "corrida":
        distancia = float(input("Quantos quilômetros você correu? "))

    pontos = calcular_pontos(tipo, tempo, distancia)
    pontos_semanais.append(pontos)

    print(f"\n✅ Você ganhou {pontos} pontos hoje!")
    return pontos

# Função de pontuação por tipo de atividade
def calcular_pontos(tipo, tempo, distancia=0):
    if tipo == "corrida":
        return tempo + int(distancia * 10)
    elif tipo == "academia":
        return tempo + 5
    elif tipo == "luta":
        return tempo + 8
    elif tipo == "caminhada":
        return int(tempo * 0.8)
    else:
        return tempo

# Função que mostra pontuação total e ranking fictício com amigos
def mostrar_status(nome, pontos_hoje):
    total = sum(pontos_semanais)
    
    # Simulando pontuação de amigos
    amigos = {
        "Ana": random.randint(50, 150),
        "Carlos": random.randint(50, 150),
        "Bruno": random.randint(50, 150),
        nome: total
    }

    # Criar ranking ordenado
    ranking = sorted(amigos.items(), key=lambda x: x[1], reverse=True)
    posicao = [i for i, (n, _) in enumerate(ranking, 1) if n == nome][0]

    print(f"\n📊 {nome}, você tem {total} pontos acumulados essa semana.")
    print(f"🥇 Sua colocação entre os amigos hoje é: {posicao}º lugar\n")

# Função que mostra o relatório semanal de pontos
def gerar_relatorio_semanal(nome):
    print(f"\n📅 Relatório semanal de {nome}")
    dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
    for i, pontos in enumerate(pontos_semanais):
        dia = dias[i] if i < len(dias) else f"Dia {i+1}"
        print(f"- {dia}: {pontos} pontos")
    print(f"➡️ Total da semana: {sum(pontos_semanais)} pontos\n")

# Execução principal
nome_usuario = boas_vindas()
recomendar_locais()

continuar = "s"
while continuar.lower() == "s":
    pontos_hoje = registrar_atividade()
    mostrar_status(nome_usuario, pontos_hoje)
    continuar = input("Deseja registrar outra atividade? (s/n): ")

# Ao final, mostra o relatório completo
gerar_relatorio_semanal(nome_usuario)
print("Obrigado por usar o Motimove! Continue se movimentando com a gente! 💪")
