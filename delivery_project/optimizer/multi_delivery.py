from itertools import permutations
from src.graph.models import Graph
from src.algorithms.dijkstra import Dijkstra


def _pairwise_costs(graph: Graph, points: list[str], mode: str = "time"):
    """Compute shortest path cost between every pair of delivery points."""
    dijkstra = Dijkstra()
    costs = {}
    paths = {}
    for a in points:
        for b in points:
            if a == b:
                continue
            path, cost, _ = dijkstra.find_path(graph, a, b, mode)
            costs[(a, b)] = cost
            paths[(a, b)] = path
    return costs, paths


def optimize_route_bruteforce(graph: Graph, start: str, stops: list[str], mode: str = "time"):
    """
    Exact solution via brute-force permutation (fine for <= ~8 stops).
    Returns best order, total cost, and full stitched path.
    """
    points = [start] + stops
    costs, paths = _pairwise_costs(graph, points, mode)

    best_order = None
    best_cost = float("inf")

    for perm in permutations(stops):
        order = [start] + list(perm)
        total = sum(costs[(order[i], order[i + 1])] for i in range(len(order) - 1))
        if total < best_cost:
            best_cost = total
            best_order = order

    full_path = _stitch_path(best_order, paths)
    return best_order, best_cost, full_path


def optimize_route_nearest_neighbor(graph: Graph, start: str, stops: list[str], mode: str = "time"):
    """
    Fast heuristic for larger stop counts. Not guaranteed optimal,
    but scales well beyond what brute-force can handle.
    """
    points = [start] + stops
    costs, paths = _pairwise_costs(graph, points, mode)

    remaining = set(stops)
    order = [start]
    current = start
    total_cost = 0

    while remaining:
        next_stop = min(remaining, key=lambda s: costs[(current, s)])
        total_cost += costs[(current, next_stop)]
        order.append(next_stop)
        remaining.remove(next_stop)
        current = next_stop

    full_path = _stitch_path(order, paths)
    return order, total_cost, full_path


def _stitch_path(order: list[str], paths: dict) -> list[str]:
    """Combine individual leg paths into one continuous path, avoiding duplicate junction nodes."""
    full_path = [order[0]]
    for i in range(len(order) - 1):
        leg = paths[(order[i], order[i + 1])]
        full_path.extend(leg[1:])  # skip first node, already in full_path
    return full_path


if __name__ == "__main__":
    from src.graph.builder import build_from_json
    g = build_from_json("data/sample_graph.json")

    stops = ["N5", "N10", "N15", "N20"]
    order, cost, path = optimize_route_nearest_neighbor(g, "N1", stops, mode="distance")
    print("Order:", order)
    print("Cost:", cost)
    print("Full path:", path)