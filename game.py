#Importar librerias
import pygame
import time
import random

snake_speed = 15

#Tamaño ventana
window_x = 720
window_y = 480

#Definiendo colores
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
bkue = pygame.Color(0, 0, 255)

#Iniciar pygame
pygame.init()

#Iniciar ventana del juego
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))

#FPS
fps = pygame.time.Clock()

#posicion inicial snake
snake_position = [100, 50]

#Primeros 4 bloques de la snake
#body
snake_body = [ [100, 50],
               [90, 50],
               [80, 50],
               [70, 50] 
               ]

#Posicion de la fruta
fruit_position = [ random.randrange(1, (window_x//10)) * 10,
                   random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

#Direccion de la snake
#Derecha
direction = 'RIGHT'
change_to = direction

#Puntuacion inicial
score = 0

#Mostrar la puntuacion
def show_score(choice, color, font, size):

    #Font
    score_font = pygame.font.SysFont(font, size)

    #Superficie de visualizacion
    #Superficie de la puntuacion
    score_surface = score_font.render('Score: ' + str(score), True, color)

    #Objeto rectangular
    #Superficie de texto
    score_rect = score_surface.get_rect()

    #Mostrar el texto
    game_window.blit(score_surface, score_rect)

#Perdiste 
def game_over():

     #Creando my_font
     my_font = pygame.font.SysFont('times new roman', 50)

     #Creando una superficie de texto donde 
     #Dibujar texto
     game_over_surface = my_font.render('Your score is: ' + str(score), True, red)

     #Objeto rectangular 2
     game_over_rect = game_over_surface.get_rect()

     #Posicion del objeto
     game_over_rect.midtop = (window_x/2, window_y/4)

     #Blit que dibujara el score
     game_window.blit(game_over_surface, game_over_rect)
     pygame.display.flip()

     #despues de 2 segundos quitamos el juego
     time.sleep(2)

     #desactivando la libreria de pygame
     pygame.quit()

     #quitar el programa
     quit()

#Funcion principal
while True:

     #Eventos clave
     for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_UP:
                    change_to = 'UP'
               if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
               if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
               if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

    #Si no quiero que la snake se mueva en dos direccion a la hora de aplastar dos botones 
     if change_to == 'UP' and direction != 'DOWN':
          direction = 'UP'
     if change_to == 'DOWN' and direction != 'UP':
          direction = 'DOWN'
     if change_to == 'LEFT' and direction != 'RIGHT':
          direction = 'LEFT'
     if change_to == 'RIGHT' and direction != 'LEFT':
          direction = 'RIGHT'

    #Movimiento 
     if direction == 'UP':
          snake_position[1] -= 10
     if direction == 'DOWN':
          snake_position[1] += 10
     if direction == 'LEFT':
          snake_position[0] -= 10
     if direction == 'RIGHT':
          snake_position[0] += 10

    #Metodo de crecimiento de la serpiente
     snake_body.insert(0, list(snake_position))
     if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
          score += 10
          fruit_spawn = False
     else:
          snake_body.pop()

     if not fruit_spawn:
          fruit_position = [random.randrange(1, (window_x//10)) * 10,
                            random.randrange(1, (window_y//10)) * 10]

     fruit_spawn = True
     game_window.fill(black)

     for pos in snake_body:
          pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
          pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    #Condiciones para perder
     if snake_position[0] < 0 or snake_position[0] > window_x-10:
          game_over()
     if snake_position[1] < 0 or snake_position[1] > window_y-10:
          game_over()

    #Cuando toca el cuerpo de la snake
     for block in snake_body[1:]:
          if snake_position[0] == block[0] and snake_position[1] == block[1]:
               game_over()

    #Mostrando el score
     show_score(1, white, 'times new roman', 20)


    #Refrescar la pagina
     pygame.display.update()

    #Frame per second
     fps.tick(snake_speed)