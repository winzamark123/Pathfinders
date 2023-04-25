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
    count = 0
    open_set = PriorityQueue()

    # tuple, or contains three items: f_score, count, node
    # f_score: used for priority, lower score means lower priority (less weight)
    # count: to keep count for stable (if they have the same f_score then go for lowest count)
    # node: the node object being stored
    open_set.put((0, count, start))

    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():

        # take the current node from the priority queue
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()  # change color of ending node
            return True

        # ALGO STARTS HERE
        # iterate through neigbors of current node
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            # if the temp_g_score (g_score of curr + 1) is bigger than g_score of neighbor
            if temp_g_score < g_score[neighbor]:
                # current -> neighbor
                # neighbor camefrom current
                came_from[neighbor] = current

                # updating the scores of 2 nodes, replacing it with less
                # Example:
                # if A -> B: 4 g_score
                # but A -> C -> B: 2 g_score
                # then A -> B = 2 g_score
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()  # change color indicating its open to explore

        draw()

        if current != start:
            current.make_closed()  # change color indicating its closed (explorED)

    return False
	

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
