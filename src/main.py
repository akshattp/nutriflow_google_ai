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

@app.get("/")
def root():
    return {"status": "NutriFlow backend running 🚀"}
