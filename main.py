import pygame
import asyncio

async def main():
    pygame.init()
    # Tamaño fijo para la web
    screen = pygame.display.set_mode((450, 600))
    pygame.display.set_caption("Tic Tac Toe - Tortugas y Ballenas")

    # Intentar cargar imágenes con manejo de errores para verlos en consola
    try:
        fondo = pygame.image.load('static-1/tablero.jpg').convert()
        ballena = pygame.image.load('static-1/x.png').convert_alpha()
        tortuga = pygame.image.load('static-1/o.png').convert_alpha()
        print("Imágenes cargadas correctamente")
    except Exception as e:
        print(f"ERROR CARGANDO IMÁGENES: {e}")
        # Si fallan las imágenes, el juego se detendrá aquí y verás el porqué en la consola F12
        return

    fondo = pygame.transform.scale(fondo, (450, 600))
    ballena = pygame.transform.scale(ballena, (140, 140))
    tortuga = pygame.transform.scale(tortuga, (140, 140))

    coordinate = [[(30, 50), (155, 50), (280, 50)],
                  [(30, 195), (155, 195), (280, 195)],
                  [(30, 335), (155, 335), (280, 335)]]

    tablero = [['', '', ''], ['', '', ''], ['', '', '']]
    turno, ganador, tiempo_fin = 'X', None, None
    fuente = pygame.font.SysFont(None, 50)
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.blit(fondo, (0, 0))
        
        # Dibujar tablero
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == 'X': screen.blit(ballena, coordinate[i][j])
                elif tablero[i][j] == 'O': screen.blit(tortuga, coordinate[i][j])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and ganador is None:
                mousex, mousey = pygame.mouse.get_pos()
                fila, col = mousey // 150, mousex // 150
                if 0 <= fila < 3 and 0 <= col < 3 and tablero[fila][col] == '':
                    tablero[fila][col] = turno
                    # Lógica de ganador (puedes añadirla aquí)
                    turno = 'O' if turno == 'X' else 'X'

        pygame.display.update()
        
        # ESTO ES LO MÁS IMPORTANTE PARA QUE NO SE QUEDE NEGRO
        await asyncio.sleep(0) 
        clock.tick(30)

# Iniciar el bucle
asyncio.run(main())


           

