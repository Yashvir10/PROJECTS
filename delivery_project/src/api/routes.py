from fastapi import APIRouter, Request, HTTPException
from src.api.schemas import RouteRequest, RouteResponse
from src.algorithms.dijkstra import Dijkstra
from src.algorithms.astar import AStar

router = APIRouter()

ALGORITHMS = {"dijkstra": Dijkstra(), "astar": AStar()}


@router.post("/route", response_model=RouteResponse)
def get_route(req: RouteRequest, request: Request):
    graph = request.app.state.graph
    algo = ALGORITHMS.get(req.algorithm)
    if not algo:
        raise HTTPException(400, f"Unknown algorithm: {req.algorithm}")

    path, cost, nodes_expanded = algo.find_path(graph, req.start, req.end, req.mode)
    if not path:
        raise HTTPException(404, "No path found")

    return RouteResponse(path=path, cost=cost, nodes_expanded=nodes_expanded, algorithm=req.algorithm)