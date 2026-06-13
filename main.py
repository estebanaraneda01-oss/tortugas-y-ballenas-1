import pygame
import asyncio

# Inicializar pygame fuera para que esté listo
pygame.init()

async def main():
    screen = pygame.display.set_mode((450, 600))
    pygame.display.set_caption("Tic Tac Toe - Tortugas y Ballenas")

    # CARGA DE IMÁGENES - Ajusta los nombres EXACTOS (minusculas/mayusculas)
    try:
        # Usamos nombres relativos. Asegúrate de que existan en la carpeta static-1
        fondo = pygame.image.load('static-1/tablero.jpg')
        ballena = pygame.image.load('static-1/x.png')
        tortuga = pygame.image.load('static-1/o.png')
    except Exception as e:
        print(f"ERROR CARGANDO IMAGENES: {e}")
        return # Si falla, se detiene aquí y verás el error en la consola F12

    fondo = pygame.transform.scale(fondo, (450, 600))
    ballena = pygame.transform.scale(ballena, (140, 140))
    tortuga = pygame.transform.scale(tortuga, (140, 140))
    ballena.set_colorkey((0, 0, 0))
    tortuga.set_colorkey((0, 0, 0))

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
                    # Verificar ganador simple (puedes meter tu función aquí o simplificar)
                    # ... (lógica de victoria) ...
                    turno = 'O' if turno == 'X' else 'X'

        pygame.display.update()
        
        # VITAL PARA LA WEB:
        await asyncio.sleep(0) 
        clock.tick(30)

# Iniciar el bucle de asyncio
asyncio.run(main())



           

