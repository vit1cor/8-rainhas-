import random
import math
from utils.visualizacao import desenhar_tabuleiro



# Gera um estado inicial aleatório (uma rainha por coluna, linha aleatória)
def gerar_estado_inicial():
    return [random.randint(0, 7) for _ in range(8)]

# Conta quantos pares de rainhas estão em conflito
def conflitos(estado):
    confl = 0
    for i in range(len(estado)):
        for j in range(i + 1, len(estado)):
            if estado[i] == estado[j] or abs(estado[i] - estado[j]) == abs(i - j):
                confl += 1
    return confl

# Gera um vizinho alterando a linha de uma rainha aleatoriamente
def gerar_estado_vizinho(estado):
    novo = estado[:]
    col = random.randint(0, 7)
    nova_linha = random.choice([i for i in range(8) if i != estado[col]])
    novo[col] = nova_linha
    return novo

# Algoritmo Simulated Annealing
def simulated_annealing():
    estado = gerar_estado_inicial()
    temperatura = 100
    resfriamento = 0.99
    iteracoes = 0

    while temperatura > 0.1:
        novo_estado = gerar_estado_vizinho(estado)
        delta = conflitos(estado) - conflitos(novo_estado)

        if delta > 0 or random.random() < math.exp(delta / temperatura):
            estado = novo_estado

        temperatura *= resfriamento
        iteracoes += 1

        if conflitos(estado) == 0:
            break

    return estado, iteracoes
def simulated_annealing():
    ...
    if conflitos(estado) == 0:
        desenhar_tabuleiro(estado, "Simulated Annealing - Solução")
        break
    ...
