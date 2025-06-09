from utils import print_board, initialize_board
from backtracking import todas_solucoes as backtracking_92
from utils.visualizacao import desenhar_tabuleiro

if __name__ == "__main__":
    ...
    if first_solution:
        desenhar_tabuleiro(first_solution, "Backtracking - Solução Única")

solucoes = backtracking_92()

class BacktrackingSolver:
    def __init__(self, n):
        self.n = n
        self.solutions = []
        self.board = initialize_board(n)
        self.iterations = 0 # Para custo computacional: número de estados visitados

    def _is_safe(self, row, col):
        """
        Verifica se é seguro colocar uma rainha em (row, col).
        """
        # Checar a linha (não é necessário, pois colocamos uma rainha por linha)
        # Checar a coluna acima
        for i in range(row):
            if self.board[i][col] == 'Q':
                return False

        # Checar diagonal superior esquerda
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if self.board[i][j] == 'Q':
                return False

        # Checar diagonal superior direita
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, self.n)):
            if self.board[i][j] == 'Q':
                return False
        return True

    def _solve_recursive(self, row):
        """
        Função recursiva do backtracking para encontrar soluções.
        """
        self.iterations += 1
        if row == self.n:
            # Todas as rainhas foram colocadas, adicionar a solução
            current_solution = []
            for r in range(self.n):
                for c in range(self.n):
                    if self.board[r][c] == 'Q':
                        current_solution.append(c) # Armazena a coluna da rainha na linha r
                        break
            self.solutions.append(current_solution)
            return

        for col in range(self.n):
            if self._is_safe(row, col):
                self.board[row][col] = 'Q'
                self._solve_recursive(row + 1)
                self.board[row][col] = '.' # Backtrack: remove a rainha

    def solve(self, find_all=True):
        """
        Inicia a busca por soluções.
        Se find_all for True, encontra todas as soluções.
        Se find_all for False, encontra a primeira solução e para.
        """
        self.solutions = []
        self.iterations = 0
        self._solve_recursive(0)

        if not find_all and self.solutions:
            # Retorna apenas a primeira solução se find_all for False
            return self.solutions[0], self.iterations
        elif find_all:
            # Retorna todas as soluções
            return self.solutions, self.iterations
        else:
            # Nenhuma solução encontrada (geralmente não ocorre para N=8)
            return [], self.iterations

    def get_board_from_solution(self, solution):
        """
        Converte uma solução (lista de colunas) para a representação do tabuleiro.
        """
        board = initialize_board(self.n)
        for r, c in enumerate(solution):
            board[r][c] = 'Q'
        return board

# Exemplo de uso (para teste individual)
if __name__ == "__main__":
    n = 8
    solver = BacktrackingSolver(n)

    print(f"\n--- Backtracking: Encontrando UMA solução para {n} Rainhas ---")
    first_solution, iterations_one = solver.solve(find_all=False)
    if first_solution:
        print(f"Solução encontrada em {iterations_one} iterações:")
        print_board(solver.get_board_from_solution(first_solution))
    else:
        print("Nenhuma solução encontrada.")

    print(f"\n--- Backtracking: Encontrando TODAS as soluções para {n} Rainhas ---")
    all_solutions, iterations_all = solver.solve(find_all=True)
    if all_solutions:
        print(f"Total de {len(all_solutions)} soluções encontradas em {iterations_all} iterações.")
        print("Primeira solução de todas:")
        print_board(solver.get_board_from_solution(all_solutions[0]))
    else:
        print("Nenhuma solução encontrada.")
