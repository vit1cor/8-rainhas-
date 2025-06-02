import random
from utils import count_attacks, initialize_board

class HillClimbingSolver:
    def __init__(self, n):
        self.n = n

    def _generate_random_state(self):
        """
        Gera um estado inicial aleatório para o tabuleiro,
        onde cada rainha está em uma coluna aleatória em sua respectiva linha.
        Ex: [0, 5, 7, 2, 6, 3, 1, 4] significa Q na (0,0), (1,5), etc.
        """
        return [random.randrange(self.n) for _ in range(self.n)]

    def _get_neighbors(self, state):
        """
        Gera todos os estados vizinhos movendo uma rainha para uma nova coluna na mesma linha.
        """
        neighbors = []
        for row in range(self.n):
            original_col = state[row]
            for col in range(self.n):
                if col != original_col:
                    new_state = list(state)
                    new_state[row] = col
                    neighbors.append(new_state)
        return neighbors

    def hill_climbing(self, initial_state=None, max_iterations=1000):
        """
        Implementa o algoritmo Hill Climbing.
        Retorna (solução_encontrada, custo_final, num_iterações).
        """
        current_state = initial_state if initial_state is not None else self._generate_random_state()
        current_cost = count_attacks(current_state)
        iterations = 0

        while iterations < max_iterations:
            iterations += 1
            neighbors = self._get_neighbors(current_state)
            best_neighbor = current_state
            best_neighbor_cost = current_cost

            found_better = False
            for neighbor in neighbors:
                neighbor_cost = count_attacks(neighbor)
                if neighbor_cost < best_neighbor_cost:
                    best_neighbor = neighbor
                    best_neighbor_cost = neighbor_cost
                    found_better = True

            if not found_better:
                # Chegou a um mínimo local (ou global)
                break
            
            current_state = best_neighbor
            current_cost = best_neighbor_cost

            if current_cost == 0:
                # Solução encontrada
                break
        
        return current_state, current_cost, iterations

class RandomRestartHillClimbingSolver:
    def __init__(self, n):
        self.n = n
        self.hc_solver = HillClimbingSolver(n)

    def solve(self, max_restarts=10000, max_hc_iterations=1000):
        """
        Implementa o Random Restart Hill Climbing.
        Tenta encontrar uma solução (custo 0).
        Retorna (solução_encontrada, total_restarts, total_hc_iterations).
        """
        total_restarts = 0
        total_hc_iterations = 0
        best_solution = None
        best_cost = float('inf')

        for restart_num in range(max_restarts):
            total_restarts += 1
            initial_state = self.hc_solver._generate_random_state()
            current_solution, current_cost, hc_iterations = self.hc_solver.hill_climbing(initial_state, max_hc_iterations)
            total_hc_iterations += hc_iterations

            if current_cost < best_cost:
                best_cost = current_cost
                best_solution = current_solution
            
            if current_cost == 0:
                # Solução encontrada
                break
        
        return best_solution, total_restarts, total_hc_iterations

    def get_board_from_solution(self, solution):
        """
        Converte uma solução (lista de colunas) para a representação do tabuleiro.
        """
        board = initialize_board(self.n)
        for r, c in enumerate(solution):
            board[r][c] = 'Q'
        return board

# Exemplo de uso (para teste individual)
if __name__ == "__main__':
    n = 8
    
    print(f"\n--- Hill Climbing (uma tentativa) para {n} Rainhas ---")
    hc_solver = HillClimbingSolver(n)
    solution_hc, cost_hc, iterations_hc = hc_solver.hill_climbing()
    print(f"HC - Solução encontrada: {solution_hc}, Custo: {cost_hc}, Iterações: {iterations_hc}")
    if cost_hc == 0:
        print_board(hc_solver.get_board_from_solution(solution_hc))
    else:
        print("HC pode ter parado em um mínimo local.")
        board_hc = hc_solver.get_board_from_solution(solution_hc)
        print_board(board_hc)

    print(f"\n--- Random Restart Hill Climbing para {n} Rainhas ---")
    rrhc_solver = RandomRestartHillClimbingSolver(n)
    solution_rrhc, restarts_rrhc, hc_iters_rrhc = rrhc_solver.solve(max_restarts=10000, max_hc_iterations=100)
    print(f"RRHC - Solução encontrada: {solution_rrhc}, Restarts: {restarts_rrhc}, Iterações HC: {hc_iters_rrhc}")
    if solution_rrhc and count_attacks(solution_rrhc) == 0:
        print_board(rrhc_solver.get_board_from_solution(solution_rrhc))
    else:
        print("RRHC não encontrou uma solução ótima dentro dos limites ou pode estar em um mínimo local.")
        if solution_rrhc:
            print_board(rrhc_solver.get_board_from_solution(solution_rrhc))
