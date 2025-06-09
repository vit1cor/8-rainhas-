import time
import tracemalloc
from backtracking import resolver_8_rainhas as backtracking
from hill_climbing import hill_climbing
from simulated_annealing import simulated_annealing

# Medidor de tempo e memória
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

# Executa as avaliações
resultados = [
    avaliar_algoritmo("Backtracking", lambda: (backtracking(), 1)),  # apenas 1 iteração
    avaliar_algoritmo("Hill Climbing", hill_climbing),
    avaliar_algoritmo("Simulated Annealing", simulated_annealing),
]

# Exibe os resultados
for r in resultados:
    print(f"\nAlgoritmo: {r['algoritmo']}")
    print(f"Tempo: {r['tempo']:.4f} segundos")
    print(f"Memória: {r['memoria (KB)']:.2f} KB")
    print(f"Iterações: {r['iteracoes']}")
    print(f"Solução: {r['solucao']}")
