from src.graph.builder import build_from_json
from src.algorithms.dijkstra import Dijkstra


def test_shortest_path_distance():
    graph = build_from_json("data/sample_graph.json")
    path, cost, _ = Dijkstra().find_path(graph, "A", "E", mode="distance")
    assert path[0] == "A"
    assert path[-1] == "E"
    assert cost > 0