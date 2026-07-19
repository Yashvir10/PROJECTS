import heapq
from src.algorithms.base import PathFinder
from src.graph.models import Graph


class Dijkstra(PathFinder):
    def find_path(self, graph: Graph, start: str, end: str, mode: str = "time"):
        pq = [(0, start)]
        costs = {start: 0}
        came_from = {start: None}
        nodes_expanded = 0

        while pq:
            current_cost, current = heapq.heappop(pq)
            nodes_expanded += 1

            if current == end:
                break

            for edge in graph.neighbors(current):
                new_cost = current_cost + edge.weight(mode)
                if edge.to_node not in costs or new_cost < costs[edge.to_node]:
                    costs[edge.to_node] = new_cost
                    came_from[edge.to_node] = current
                    heapq.heappush(pq, (new_cost, edge.to_node))

        if end not in costs:
            return [], float("inf"), nodes_expanded

        path = self._reconstruct(came_from, start, end)
        return path, costs[end], nodes_expanded

    def _reconstruct(self, came_from, start, end):
        path = [end]
        while path[-1] != start:
            path.append(came_from[path[-1]])
        return list(reversed(path))