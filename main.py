import pygame
import asyncio

async def main():
    pygame.init()
    screen = pygame.display.set_mode((450, 600))
    pygame.display.set_caption("Tic Tac Toe - Tortugas y Ballenas")

    try:
        fondo = pygame.image.load('static-1/tablero.jpg').convert()
        ballena = pygame.image.load('static-1/x.png').convert_alpha()
        tortuga = pygame.image.load('static-1/o.png').convert_alpha()
        print("Imágenes cargadas correctamente")
    except Exception as e:
        print(f"ERROR CARGANDO IMÁGENES: {e}")
        return

    fondo = pygame.transform.scale(fondo, (450, 600))
    ballena = pygame.transform.scale(ballena, (140, 140))
    tortuga = pygame.transform.scale(tortuga, (140, 140))

    coordinate = [[(30, 50), (155, 50), (280, 50)],
                  [(30, 195), (155, 195), (280, 195)],
                  [(30, 335), (155, 335), (280, 335)]]

    def verificar_ganador(tablero):
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

    def reiniciar():
        return [['', '', ''], ['', '', ''], ['', '', '']], 'X', None, None

    tablero, turno, ganador, tiempo_fin = reiniciar()
    fuente = pygame.font.SysFont(None, 50)
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.blit(fondo, (0, 0))

        for i in range(3):
            for j in range(3):
                if tablero[i][j] == 'X':
                    screen.blit(ballena, coordinate[i][j])
                elif tablero[i][j] == 'O':
                    screen.blit(tortuga, coordinate[i][j])

        if ganador:
            if ganador == 'X':
                mensaje = "Ganaron las Ballenas!"
            else:
                mensaje = "Ganaron las Tortugas!"
            texto = fuente.render(mensaje, True, (255, 255, 0))
            rect = texto.get_rect(center=(225, 500))
            screen.blit(texto, rect)

            if pygame.time.get_ticks() - tiempo_fin > 3000:
                tablero, turno, ganador, tiempo_fin = reiniciar()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and ganador is None:
                mousex, mousey = pygame.mouse.get_pos()
                fila, col = mousey // 150, mousex // 150
                if 0 <= fila < 3 and 0 <= col < 3 and tablero[fila][col] == '':
                    tablero[fila][col] = turno
                    ganador = verificar_ganador(tablero)
                    if ganador:
                        tiempo_fin = pygame.time.get_ticks()
                    else:
                        turno = 'O' if turno == 'X' else 'X'

        pygame.display.update()
        await asyncio.sleep(0)
        clock.tick(30)

asyncio.run(main())