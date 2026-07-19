from src.graph.builder import build_from_json


def test_build_from_json_loads_nodes():
    graph = build_from_json("data/sample_graph.json")
    assert "N1" in graph.nodes
    assert graph.nodes["N1"].name == "Warehouse Hub"


def test_build_from_json_loads_edges_bidirectionally():
    graph = build_from_json("data/sample_graph.json")
    # N1 -> N2 exists in file; N2 -> N1 should exist too since builder adds bidirectional
    n1_neighbors = [e.to_node for e in graph.neighbors("N1")]
    n2_neighbors = [e.to_node for e in graph.neighbors("N2")]
    assert "N2" in n1_neighbors
    assert "N1" in n2_neighbors


def test_all_nodes_have_adjacency_entry():
    graph = build_from_json("data/sample_graph.json")
    for node_id in graph.nodes:
        assert node_id in graph.adjacency