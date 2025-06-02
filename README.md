# Problema das 8 Rainhas: Comparação de Abordagens Algorítmicas

Este repositório contém implementações e uma análise comparativa de diferentes abordagens algorítmicas para resolver o clássico Problema das 8 Rainhas. O objetivo é posicionar 8 rainhas em um tabuleiro de xadrez 8x8 de forma que nenhuma rainha ataque outra.

As abordagens implementadas e comparadas são:

1.  **Backtracking:** Uma abordagem exaustiva que explora todas as possíveis configurações, recuando quando uma solução inválida é encontrada.
2.  **Busca Local (Hill Climbing):** Um algoritmo de otimização local que tenta melhorar uma solução candidata através de pequenas modificações.
3.  **Busca Aleatória com Repetições (Random Restart Hill Climbing):** Uma variação do Hill Climbing que reinicia o processo de busca de uma nova configuração inicial aleatória quando um mínimo local é atingido, na esperança de encontrar uma solução global.

## Requisitos

* Python 3.x

## Instalação

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/SEU_USUARIO/8-Queens-Problem-Comparison.git](https://github.com/SEU_USUARIO/8-Queens-Problem-Comparison.git)
    cd 8-Queens-Problem-Comparison
    ```
2.  Crie e ative um ambiente virtual (recomendado):
    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Como Executar

Para executar o comparativo das abordagens e visualizar os resultados:

```bash
python main.py
