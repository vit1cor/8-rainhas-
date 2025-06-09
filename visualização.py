import pygame
import sys
import time

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (100, 149, 237)
VERMELHO = (255, 0, 0)

TAMANHO_CASA = 60
MARGEM = 20
TAMANHO_TABULEIRO = 8
LARGURA_TELA = ALTURA_TELA = TAMANHO_CASA * TAMANHO_TABULEIRO + 2 * MARGEM

def desenhar_tabuleiro(solucao, titulo=""):
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(titulo)
    fonte = pygame.font.SysFont(None, 36)

    tela.fill(BRANCO)

    for linha in range(TAMANHO_TABULEIRO):
        for col in range(TAMANHO_TABULEIRO):
            cor = BRANCO if (linha + col) % 2 == 0 else AZUL
            pygame.draw.rect(
                tela,
                cor,
                pygame.Rect(MARGEM + col * TAMANHO_CASA,
                            MARGEM + linha * TAMANHO_CASA,
                            TAMANHO_CASA,
                            TAMANHO_CASA)
            )

    # Desenha rainhas
    for linha, col in enumerate(solucao):
        centro_x = MARGEM + col * TAMANHO_CASA + TAMANHO_CASA // 2
        centro_y = MARGEM + linha * TAMANHO_CASA + TAMANHO_CASA // 2
        pygame.draw.circle(tela, VERMELHO, (centro_x, centro_y), TAMANHO_CASA // 3)

    pygame.display.flip()

    # Aguarda 5 segundos ou evento de fechar a janela
    esperar = True
    tempo_inicio = time.time()
    while esperar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                esperar = False
        if time.time() - tempo_inicio > 5:
            esperar = False

    pygame.quit()

