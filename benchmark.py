import time
import tracemalloc
from backtracking import todas_solucoes as backtracking_92
from hill_climbing import hill_climbing
from simulated_annealing import simulated_annealing

# Avaliação individual (1 solução)
def avaliar_algoritmo(nome, funcao):
    tracemalloc.start()
    inicio = time.time()
    solucao, iteracoes = funcao()
    fim = time.time()
    memoria_usada, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        'algoritmo': nome,
        'tempo': fim - inicio,
        'memoria (KB)': memoria_usada / 1024,
        'iteracoes': iteracoes,
        'solucao': solucao
    }

# Busca todas as 92 soluções com backtracking
def buscar_todas_backtracking():
    from backtracking import todas_solucoes
    inicio = time.time()
    solucoes = todas_solucoes()
    fim = time.time()
    return len(solucoes), fim - inicio

# Executa benchmarks
resultados = [
    avaliar_algoritmo("Backtracking", lambda: (backtracking_92()[0], 1)),
    avaliar_algoritmo("Hill Climbing", hill_climbing),
    avaliar_algoritmo("Simulated Annealing", simulated_annealing),
]

# Imprime resultados (1 solução)
print("\n🧠 Tempo e memória para encontrar 1 solução:\n")
for r in resultados:
    print(f"Algoritmo: {r['algoritmo']}")
    print(f"  Tempo: {r['tempo']:.4f} segundos")
    print(f"  Memória: {r['memoria (KB)']:.2f} KB")
    print(f"  Iterações: {r['iteracoes']}")
    print(f"  Solução: {r['solucao']}")
    print()

# Busca todas as 92 soluções usando backtracking
print("🔍 Buscando as 92 soluções com Backtracking...")
total, tempo_total = buscar_todas_backtracking()
print(f"\n✅ Total de soluções encontradas: {total}")
print(f"⏱ Tempo: {tempo_total:.4f} segundos\n")

