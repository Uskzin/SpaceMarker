import pygame
import sys
import math
import tkinter as tk
from tkinter import simpledialog

# Inicialização do Pygame
pygame.init()

sys = SystemExit
# Configuração da janela
largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("SPACE MARKER")
tamanho_tela = (largura, altura)

# Carregamento do som de fundo
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)  # Reproduzir em looping

# Carregamento do ícone
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)

# Definição das cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Carregamento dos recursos (sons, imagens, etc.)
fundo = pygame.image.load("imagem.fundo.jpg")
fundo = pygame.transform.scale(fundo, (largura, altura))

# Criação da janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("SPACE MARKER")

# Variáveis para armazenar os pontos clicados
pontos = []

# Variáveis para armazenar as marcações das estrelas
marcacoes = {}

# Variáveis para armazenar as linhas e as somas das distâncias
linhas = []
distancias = []
circulos = []
estrelas_encontradas = 0

def desenhar_linhas():
    for i in range(len(pontos) - 1):
        ponto1 = pontos[i]
        ponto2 = pontos[i + 1]
        pygame.draw.line(janela, branco, ponto1, ponto2, 2)


def obter_nome_estrela():
    root = tk.Tk()
    root.withdraw()
    nome = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    return nome if nome else "Desconhecido"

def salvar_marcacoes():
    with open("marcacoes.txt", "w") as arquivo:
        for posicao, nome in marcacoes.items():
            arquivo.write(f"{posicao[0]},{posicao[1]},{nome}\n")
        for linha in linhas:
            arquivo.write(f"linha,{linha[0][0]},{linha[0][1]},{linha[1][0]},{linha[1][1]}\n")

    print("Marcações e linhas salvas com sucesso!")


def carregar_marcacoes():
    try:
        with open("marcacoes.txt", "r") as arquivo:
            marcacoes.clear()
            linhas.clear()
            pontos.clear()  # Limpa a lista de pontos

            for linha in arquivo:
                dados = linha.strip().split(",")
                if dados[0] == "linha":
                    x1, y1, x2, y2 = map(int, dados[1:])
                    linhas.append([(x1, y1), (x2, y2)])
                else:
                    posicao_x, posicao_y, nome = dados
                    marcacoes[(int(posicao_x), int(posicao_y))] = nome
                    pontos.append((int(posicao_x), int(posicao_y)))  # Adiciona os pontos à lista

        # Desenha as linhas novamente após carregar as marcações
        for linha in linhas:
            pygame.draw.line(janela, branco, linha[0], linha[1], 2)

        print("Marcações e linhas carregadas")
    except FileNotFoundError:
        print("Arquivo de Marcações não encontrado.")

def excluir_marcacoes():
    marcacoes.clear()
    linhas.clear()
    circulos.clear()
    distancias.clear()
    pontos.clear()
    print("Todas as Marcações Foram Excluídas.")

# Fonte para exibir as opções
fonte_opcoes = pygame.font.Font(None, 20)


# Fonte para exibir a contagem de estrelas encontradas
fonte_estrelas = pygame.font.Font(None, 20)
for linha in linhas:
    pygame.draw.line(janela, branco, linha[0], linha[1], 2)

# Variáveis para controlar a exibição temporária das mensagens
mensagem_tempo = 0
mensagem_texto = ""
mensagem_posicao = (largura - 200, 10)

# Loop principal do jogo
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F10:
                    salvar_marcacoes()
                    mensagem_tempo = 7 * 60  # 7 segundos
                    mensagem_texto = "Marcações Salvas com Sucesso!"
                elif event.key == pygame.K_F11:
                    carregar_marcacoes()
                    mensagem_tempo = 7 * 60  # 7 segundos
                    mensagem_texto = "Marcações e Linhas Carregadas com Sucesso!"

                elif event.key == pygame.K_F12:
                    excluir_marcacoes()
                    mensagem_tempo = 7 * 60  # 7 segundos
                    mensagem_texto = "Todas as Marcações Foram Excluídas."

            elif event.type == pygame.QUIT:
                with open("marcacoes.txt", "w") as arquivo:
                    for posicao, nome in marcacoes.items():
                        arquivo.write(f"{posicao[0]},{posicao[1]},{nome}\n")
                pygame.quit()
                sys()

            if event.type == pygame.KEYDOWN and event.key== pygame.K_ESCAPE:
                with open("points.txt", "w") as arquivo:
                    for posicao, nome in circulos():
                        arquivo.write(f"{posicao[0]},{posicao[1]},{nome}\n")
                    pygame.quit()
                    sys()