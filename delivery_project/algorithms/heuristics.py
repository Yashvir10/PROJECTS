from math import radians, sin, cos, sqrt, atan2
from src.graph.models import Graph


def haversine(lat1, lng1, lat2, lng2) -> float:
    """Great-circle distance in km."""
    R = 6371.0
    d_lat = radians(lat2 - lat1)
    d_lng = radians(lng2 - lng1)
    a = sin(d_lat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(d_lng / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


def heuristic(graph: Graph, node_id: str, goal_id: str) -> float:
    n1 = graph.get_node(node_id)
    n2 = graph.get_node(goal_id)
    return haversine(n1.lat, n1.lng, n2.lat, n2.lng)