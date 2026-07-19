import time
from src.graph.models import Graph
from src.algorithms.dijkstra import Dijkstra
from src.algorithms.astar import AStar


def compare(graph: Graph, start: str, end: str, mode: str = "time"):
    results = {}
    for name, algo in [("dijkstra", Dijkstra()), ("astar", AStar())]:
        t0 = time.perf_counter()
        path, cost, nodes_expanded = algo.find_path(graph, start, end, mode)
        elapsed = time.perf_counter() - t0
        results[name] = {
            "path": path,
            "cost": cost,
            "nodes_expanded": nodes_expanded,
            "time_seconds": elapsed,
        }
    return results


if __name__ == "__main__":
    from src.graph.builder import build_from_json
    g = build_from_json("data/sample_graph.json")
    print(compare(g, "A", "E", mode="distance"))