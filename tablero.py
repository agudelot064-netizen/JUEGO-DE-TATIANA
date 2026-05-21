import pygame 

def tablero(pantalla, tamaño_celda):
   
    BLANCO = (255,255,255)
    NEGRO = (0,0,0)
   
    filas = 8
    columnas = 8

    for fila in range(filas):
        for col in range(columnas):
            if(fila + col) % 2 == 0:
                color = BLANCO
            else:
                color = NEGRO

            rect = (col * tamaño_celda, fila * tamaño_celda,tamaño_celda,tamaño_celda)
            pygame.draw.rect(pantalla,color,rect)
