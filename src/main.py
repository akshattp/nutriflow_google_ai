from fastapi import FastAPI
from src.agents.orchestrator import MasterOrchestratorAgent

app = FastAPI()
orchestrator = MasterOrchestratorAgent()

@app.post("/nudge")
def get_nudge(payload: dict):
    return orchestrator.handle_request(payload)

@app.post("/dashboard")
def dashboard(payload: dict):
    return orchestrator.dashboard(payload)

@app.post("/map")
def map_data(payload: dict):
    return orchestrator.map(payload)

@app.post("/outcome")
def outcome(payload: dict):
    return orchestrator.outcome(payload)

from fastapi.responses import HTMLResponse
import os

@app.get("/", response_class=HTMLResponse)
def root():
    ui_path = os.path.join(os.path.dirname(__file__), "..", "ui", "index.html")
    if os.path.exists(ui_path):
        with open(ui_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>NutriFlow UI Starting...</h1>"
