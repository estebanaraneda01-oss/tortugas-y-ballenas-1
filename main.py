import pygame
import asyncio
pygame.init()
screen = pygame.display.set_mode((450, 600))
pygame.display.set_caption("Tic Tac Toe - Tortugas y Ballenas")

# Asegúrate de que estas imágenes existan en la carpeta 'static'
fondo = pygame.image.load('static/tablero.jpg')
ballena = pygame.image.load('static/x.png')
tortuga = pygame.image.load('static/o.png')

fondo = pygame.transform.scale(fondo, (450, 600))
ballena = pygame.transform.scale(ballena, (140, 140))
tortuga = pygame.transform.scale(tortuga, (140, 140))

ballena.set_colorkey((0, 0, 0))
tortuga.set_colorkey((0, 0, 0))

coordinate = [[(30, 50), (155, 50), (280, 50)],
              [(30, 195), (155, 195), (280, 195)],
              [(30, 335), (155, 335), (280, 335)]]

tablero = [['', '', ''],
           ['', '', ''],
           ['', '', '']]

turno = 'X'
game_over = False
ganador = None
tiempo_fin = None
fuente = pygame.font.SysFont(None, 60)
clock = pygame.time.Clock()

def graficar_tablero():
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == 'X':
                screen.blit(ballena, coordinate[i][j])
            elif tablero[i][j] == 'O':
                screen.blit(tortuga, coordinate[i][j])

def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != '':
            return tablero[i][0]
    for j in range(3):
        if tablero[0][j] == tablero[1][j] == tablero[2][j] != '':
            return tablero[0][j]
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
        return tablero[0][2]
    return None

def dibujar_texto_ganador(ganador):
    mensaje = "¡Ganaron las Ballenas!" if ganador == 'X' else "¡Ganaron las Tortugas!"
    texto = fuente.render(mensaje, True, (255, 255, 0))
    rect_texto = texto.get_rect(center=(225, 500))
    screen.blit(texto, rect_texto)

def reiniciar_juego():
    global tablero, turno, ganador, tiempo_fin
    tablero = [['', '', ''], ['', '', ''], ['', '', '']]
    turno = 'X'
    ganador = None
    tiempo_fin = None

async def main():
    global running, ganador, tiempo_fin, turno, tablero
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN and ganador is None:
                mousex, mousey = pygame.mouse.get_pos()
                fila = mousey // 150
                col = mousex // 150

                if 0 <= fila < 3 and 0 <= col < 3:
                    if tablero[fila][col] == '':
                        tablero[fila][col] = turno
                        ganador = verificar_ganador()
                        if ganador is None:
                            turno = 'O' if turno == 'X' else 'X'
                        else:
                            tiempo_fin = pygame.time.get_ticks()

        screen.blit(fondo, (0, 0))
        graficar_tablero()

        if ganador is not None:
            dibujar_texto_ganador(ganador)
            if pygame.time.get_ticks() - tiempo_fin > 3000:
                reiniciar_juego()

        pygame.display.update()
        await asyncio.sleep(0)

    pygame.quit()

running = True
asyncio.run(main())

           

