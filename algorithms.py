# algorithms.py
from queue import PriorityQueue
from collections import deque

#heuristic used in A*
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# A* Algorithm
def astar_algorithm(draw, grid, start, end, reconstruct_path):
    #needs to understand astar here 
    return 
	

# Dijkstra's Algorithm
def dijkstra_algorithm(draw, grid, start, end, reconstruct_path):
    dist = {spot: float("inf") for row in grid for spot in row}
    dist[start] = 0
    unvisited = {spot for row in grid for spot in row}

    while unvisited:
        min_spot = min(unvisited, key=lambda spot: dist[spot])

        if dist[min_spot] == float("inf"):
            break

        if min_spot == end:
            reconstruct_path(min_spot.came_from, end, draw)
            end.make_end()
            return True

        unvisited.remove(min_spot)

        for neighbor in min_spot.neighbors:
            alt = dist[min_spot] + 1
            if alt < dist[neighbor]:
                neighbor.came_from = min_spot
                dist[neighbor] = alt
                if neighbor != end:
                    neighbor.make_open()

        draw()

        if min_spot != start:
            min_spot.make_closed()

    return False


# BFS Algorithm
def bfs_algorithm(draw, grid, start, end, reconstruct_path):
    queue = deque([start])
    visited = set([start])

    while queue:
        current = queue.popleft()

        if current == end:
            reconstruct_path(current.came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                neighbor.came_from = current
                queue.append(neighbor)
                if neighbor != end:
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

# DFS Algorithm
def dfs_algorithm(draw, grid, start, end):
    stack = [start]
    visited = set([start])

    while stack:
        current = stack.pop()

        if current == end:
            reconstruct_path(current.came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                neighbor.came_from = current
                stack.append(neighbor)
                if neighbor != end:
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False
