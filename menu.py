import pygame
from astar import *

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))


def run_menu(win, width):
    pygame.init()
    font = pygame.font.Font(None, 36)
    options = [
        ("A* Algorithm", astar_algorithm),
        ("BFS Algorithm", bfs_algorithm),
        ("DFS Algorithm", dfs_algorithm),
        ("Dijkstra Algorithm", dijkstra_algorithm),
    ]

    selected = 0
    running = True
    while running:
        win.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    return options[selected][1]

        for i, (text, _) in enumerate(options):
            color = (0, 0, 0)
            if i == selected:
                color = (255, 0, 0)
            text_surface = font.render(text, True, color)
            win.blit(
                text_surface, (width // 2 - text_surface.get_width() // 2, 100 + i * 50)
            )

        pygame.display.flip()

    return None


def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


# main(WIN, WIDTH)
