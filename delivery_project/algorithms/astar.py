import heapq
from src.algorithms.base import PathFinder
from src.algorithms.heuristics import heuristic
from src.graph.models import Graph


class AStar(PathFinder):
    def find_path(self, graph: Graph, start: str, end: str, mode: str = "time"):
        pq = [(0, start)]
        g_cost = {start: 0}
        came_from = {start: None}
        nodes_expanded = 0

        while pq:
            _, current = heapq.heappop(pq)
            nodes_expanded += 1

            if current == end:
                break

            for edge in graph.neighbors(current):
                tentative_g = g_cost[current] + edge.weight(mode)
                if edge.to_node not in g_cost or tentative_g < g_cost[edge.to_node]:
                    g_cost[edge.to_node] = tentative_g
                    f_cost = tentative_g + heuristic(graph, edge.to_node, end)
                    came_from[edge.to_node] = current
                    heapq.heappush(pq, (f_cost, edge.to_node))

        if end not in g_cost:
            return [], float("inf"), nodes_expanded

        path = self._reconstruct(came_from, start, end)
        return path, g_cost[end], nodes_expanded

    def _reconstruct(self, came_from, start, end):
        path = [end]
        while path[-1] != start:
            path.append(came_from[path[-1]])
        return list(reversed(path))