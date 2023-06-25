import pygame
import pygame
import tkinter as tk
from tkinter import simpledialog
import winsound

pygame.init()
tamanho = (800, 600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Marker")
icon=pygame.image.load("space.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
fundo = pygame.image.load("imagem.fundo.jpg")
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(0,0,5)
branco=(255,255,255)
circulos=[]
estrelas = []
sys = SystemExit

#DEFS

def carregar_pontos(filename):
    global estrelas, circulos
    estrelas = []
    circulos = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip()
            name_start = data.index(' ') + 1
            name_end = data.index('(')
            name = data[name_start:name_end].strip()
            coords_start = data.index('(') + 1
            coords_end = data.index(')')
            coords = data[coords_start:coords_end].strip().split(',')
            pos = (int(coords[0]), int(coords[1]))
            estrelas.append((pos, name))
            circulos.append(pos)

def calcular_distancia(p1, p2):
    distancia_x = abs(p2[0] - p1[0])
    distancia_y = abs(p2[1] - p1[1])
    return distancia_x + distancia_y

def salvamento_de_pontos(filename):
    with open(filename, 'w') as file:
        for pos, name in estrelas:
            file.write(f"{name} ({pos[0]}, {pos[1]})\n")

def reset_de_marcações():
    global estrelas,circulos
    estrelas=[]
    circulos=[]   

#GAME

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salvamento_de_pontos("points.txt") 
                pygame.quit()  

            if event.type == pygame.KEYDOWN and event.key== pygame.K_ESCAPE:
                with open("points.txt", "w") as arquivo:
                    for posicao, nome in estrelas():
                        arquivo.write(f"{posicao[0]},{posicao[1]},{nome}\n")
                    pygame.quit()
                    sys()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F10:
                    salvamento_de_pontos("points.txt")    
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] < tamanho[0] and pos[1] < tamanho[1]:
                    
                    circulos.append(pos)
                    
                item=simpledialog.askstring("Space ", "Nome da Estrela")
                print (item)
                if item == None:
                    item = "desconhecido "+str(pos)
                estrelas.append((pos, item))
                tela.blit(fundo, (0, 0))

        for pos,nome  in estrelas:
            pygame.draw.circle(tela, (branco), pos, 3)
            fonte = pygame.font.Font(None, 18)
            texto = fonte.render(f"{nome} ({pos[0]}, {pos[1]})", True, branco)
            pos_texto=(pos[0]+10,pos[1]-10)
            tela.blit(texto,pos_texto)
        if len(circulos)>1:
            for i in range (1, len(circulos)):
                p1 = circulos[i - 1]
                p2 = circulos[i]
                pygame.draw.line(tela, branco, p1, p2, 3)
                distance = calcular_distancia(p1, p2)
                fonte_distancia = pygame.font.Font(None, 18)
                texto_distancia = fonte_distancia.render(f"Distância: {distance:.2f}", True, branco)
                pos_distancia = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
                tela.blit(texto_distancia, pos_distancia)