from fastapi import FastAPI
from src.graph.builder import build_from_json
from src.api.routes import router

app = FastAPI(title="Delivery Route Optimizer")

# Load graph once at startup
app.state.graph = build_from_json("data/sample_graph.json")

app.include_router(router)