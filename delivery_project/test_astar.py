from src.graph.builder import build_from_json
from src.algorithms.astar import AStar
from src.algorithms.dijkstra import Dijkstra


def test_astar_finds_path():
    graph = build_from_json("data/sample_graph.json")
    path, cost, _ = AStar().find_path(graph, "N1", "N20", mode="distance")
    assert path[0] == "N1"
    assert path[-1] == "N20"
    assert cost > 0


def test_astar_matches_dijkstra_cost():
    """A* and Dijkstra should agree on the optimal cost, even if they expand different nodes."""
    graph = build_from_json("data/sample_graph.json")

    astar_path, astar_cost, _ = AStar().find_path(graph, "N1", "N20", mode="distance")
    dijkstra_path, dijkstra_cost, _ = Dijkstra().find_path(graph, "N1", "N20", mode="distance")

    assert abs(astar_cost - dijkstra_cost) < 1e-6


def test_astar_no_path_exists():
    graph = build_from_json("data/sample_graph.json")
    path, cost, _ = AStar().find_path(graph, "N1", "NONEXISTENT", mode="distance")
    assert path == []
    assert cost == float("inf")