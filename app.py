import heapq
from collections import defaultdict


def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist


def bellman_ford(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

    for u in graph:
        for v, weight in graph[u].items():
            if dist[u] + weight < dist[v]:
                raise ValueError("O gráfico contém um ciclo de peso negativo")

    return dist


def floyd_warshall(graph):
    nodes = list(graph.keys())
    dist = {u: {v: float('inf') for v in nodes} for u in nodes}

    for node in nodes:
        dist[node][node] = 0

    for u in graph:
        for v, weight in graph[u].items():
            dist[u][v] = weight

    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


graph = {
    0: {1: 2, 2: 7},
    1: {2: 3, 3: 8, 4: 5},
    2: {3: 1},
    3: {4: 4},
    4: {3: 5}
}

print("Dijkstra (partindo de 0):", dijkstra(graph, 0))
print("Bellman-Ford (partindo de 0):", bellman_ford(graph, 0))

distances = floyd_warshall(graph)
print("Floyd-Warshall:")
for u in distances:
    for v in distances[u]:
        print(f"Distância de {u} para {v}: {distances[u][v]}")

# Código feito com ajuda do Gemini, ChatGPT e alguns canais do YouTube para entendimento do funcionamento dos algoritmos
