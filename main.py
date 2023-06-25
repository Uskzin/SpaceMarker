import pygame
import pygame
import tkinter as tk
from tkinter import simpledialog
import winsound

pygame.init()

tamanho = (800,600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("SpaceMarker")
fundo = pygame.image.load("bg.jpg")
