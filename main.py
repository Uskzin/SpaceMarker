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