from backtracking import BacktrackingSolver
from random_restart_hc import HillClimbingSolver, RandomRestartHillClimbingSolver
from utils import print_board, measure_memory_and_time, count_attacks
import statistics

N_QUEENS = 8

def run_backtracking_single_solution():
    print("\n--- Backtracking: Encontrando UMA Solução ---")
    solver = BacktrackingSolver(N_QUEENS)
    (solution, iterations), time_taken, memory_used = measure_memory_and_time(solver.solve, find_all=False)
    
    print(f"Tempo de execução: {time_taken:.6f} segundos")
    print(f"Uso de memória (pico estimado): {memory_used:.2f} MB")
    print(f"Custo computacional (iterações/estados visitados): {iterations}")
    if solution:
        print("Solução encontrada:")
        print_board(solver.get_board_from_solution(solution))
    else:
        print("Nenhuma solução encontrada.")
    return time_taken, memory_used, iterations, 1 if solution else 0

def run_backtracking_all_solutions():
    print("\n--- Backtracking: Encontrando TODAS as 92 Soluções ---")
    solver = BacktrackingSolver(N_QUEENS)
    (solutions, iterations), time_taken, memory_used = measure_memory_and_time(solver.solve, find_all=True)
    
    print(f"Tempo de execução: {time_taken:.6f} segundos")
    print(f"Uso de memória (pico estimado): {memory_used:.2f} MB")
    print(f"Custo computacional (iterações/estados visitados): {iterations}")
    if solutions:
        print(f"Total de soluções encontradas: {len(solutions)}")
        print("Primeira solução (exemplo):")
        print_board(solver.get_board_from_solution(solutions[0]))
    else:
        print("Nenhuma solução encontrada.")
    return time_taken, memory_used, iterations, len(solutions)

def run_hill_climbing_single_solution(num_trials=100):
    print(f"\n--- Hill Climbing: Encontrando UMA Solução (Média de {num_trials} tentativas) ---")
    hc_solver = HillClimbingSolver(N_QUEENS)
    
    total_time = []
    total_memory = []
    total_iterations = []
    solutions_found = 0
    
    for i in range(num_trials):
        (solution, cost, iterations_hc), time_taken, memory_used = measure_memory_and_time(hc_solver.hill_climbing)
        total_time.append(time_taken)
        total_memory.append(memory_used)
        total_iterations.append(iterations_hc)
        if cost == 0:
            solutions_found += 1
            # Para visualização, mostrar apenas a primeira solução ótima encontrada
            if solutions_found == 1:
                 print("\n--- Exemplo de solução ótima (HC): ---")
                 print_board(hc_solver.get_board_from_solution(solution))

    avg_time = statistics.mean(total_time)
    avg_memory = statistics.mean(total_memory)
    avg_iterations = statistics.mean(total_iterations)

    print(f"\nResultados médios em {num_trials} tentativas:")
    print(f"Tempo de execução (médio): {avg_time:.6f} segundos")
    print(f"Uso de memória (pico estimado médio): {avg_memory:.2f} MB")
    print(f"Custo computacional (iterações HC médio): {avg_iterations:.0f}")
    print(f"Soluções ótimas (custo 0) encontradas: {solutions_found} de {num_trials}")
    return avg_time, avg_memory, avg_iterations, solutions_found

def run_random_restart_hill_climbing_single_solution(num_trials=100, max_restarts=1000, max_hc_iterations=100):
    print(f"\n--- Random Restart Hill Climbing: Encontrando UMA Solução (Média de {num_trials} tentativas) ---")
    rrhc_solver = RandomRestartHillClimbingSolver(N_QUEENS)

    total_time = []
    total_memory = []
    total_restarts = []
    total_hc_iterations = []
    solutions_found = 0
    
    for i in range(num_trials):
        (solution, restarts, hc_iterations), time_taken, memory_used = measure_memory_and_time(
            rrhc_solver.solve, max_restarts=max_restarts, max_hc_iterations=max_hc_iterations
        )
        total_time.append(time_taken)
        total_memory.append(memory_used)
        total_restarts.append(restarts)
        total_hc_iterations.append(hc_iterations)
        if solution and count_attacks(solution) == 0:
            solutions_found += 1
            # Para visualização, mostrar apenas a primeira solução ótima encontrada
            if solutions_found == 1:
                print("\n--- Exemplo de solução ótima (RRHC): ---")
                print_board(rrhc_solver.get_board_from_solution(solution))


    avg_time = statistics.mean(total_time)
    avg_memory = statistics.mean(total_memory)
    avg_restarts = statistics.mean(total_restarts)
    avg_hc_iterations = statistics.mean(total_hc_iterations)

    print(f"\nResultados médios em {num_trials} tentativas:")
    print(f"Tempo de execução (médio): {avg_time:.6f} segundos")
    print(f"Uso de memória (pico estimado médio): {avg_memory:.2f} MB")
    print(f"Custo computacional (restarts médio): {avg_restarts:.0f}")
    print(f"Custo computacional (iterações HC total médio): {avg_hc_iterations:.0f}")
    print(f"Soluções ótimas (custo 0) encontradas: {solutions_found} de {num_trials}")
    return avg_time, avg_memory, avg_restarts, avg_hc_iterations, solutions_found

if __name__ == "__main__":
    print(f"Executando comparações para o Problema das {N_QUEENS} Rainhas...\n")

    # Backtracking - Uma Solução
    bt_single_time, bt_single_mem, bt_single_iter, _ = run_backtracking_single_solution()

    # Backtracking - Todas as Soluções
    bt_all_time, bt_all_mem, bt_all_iter, bt_all_count = run_backtracking_all_solutions()

    # Hill Climbing - Uma Solução (múltiplas tentativas para estatística)
    hc_single_time, hc_single_mem, hc_single_iter, hc_found_count = run_hill_climbing_single_solution(num_trials=50)

    # Random Restart Hill Climbing - Uma Solução (múltiplas tentativas para estatística)
    # Ajuste max_restarts e max_hc_iterations para o desempenho desejado
    rrhc_single_time, rrhc_single_mem, rrhc_restarts, rrhc_hc_iters, rrhc_found_count = \
        run_random_restart_hill_climbing_single_solution(num_trials=50, max_restarts=1000, max_hc_iterations=100)

    print("\n" + "="*50)
    print("RESUMO DA COMPARAÇÃO DE DESEMPENHO (Média de 50 Tentativas)")
    print("="*50)

    print("\n--- Backtracking ---")
    print(f"  Uma Solução:")
    print(f"    Tempo: {bt_single_time:.6f} s, Memória: {bt_single_mem:.2f} MB, Iterações: {bt_single_iter}")
    print(f"  Todas as 92 Soluções:")
    print(f"    Tempo: {bt_all_time:.6f} s, Memória: {bt_all_mem:.2f} MB, Iterações: {bt_all_iter}, Soluções Encontradas: {bt_all_count}")

    print("\n--- Hill Climbing ---")
    print(f"  Uma Solução (média):")
    print(f"    Tempo: {hc_single_time:.6f} s, Memória: {hc_single_mem:.2f} MB, Iterações HC: {hc_single_iter:.0f}, Sucesso: {hc_found_count}/50")

    print("\n--- Random Restart Hill Climbing ---")
    print(f"  Uma Solução (média):")
    print(f"    Tempo: {rrhc_single_time:.6f} s, Memória: {rrhc_single_mem:.2f} MB, Restarts: {rrhc_restarts:.0f}, Iterações HC Total: {rrhc_hc_iters:.0f}, Sucesso: {rrhc_found_count}/50")

    print("\n" + "="*50)
    print("FIM DA COMPARAÇÃO")
    print("="*50)
