import uuid
import datetime
import json

class TraceContext:
    def __init__(self, trace_id=None):
        self.trace_id = trace_id or str(uuid.uuid4())
        self.history = []

    def add_step(self, agent_name, step_type, details):
        step = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "agent": agent_name,
            "type": step_type,
            "details": details
        }
        self.history.append(step)

    def to_dict(self):
        return {
            "trace_id": self.trace_id,
            "history": self.history
        }

class SystemObserver:
    @staticmethod
    def log_input(trace_context: TraceContext, agent_name: str, payload: dict):
        print(f"[{agent_name}] [INPUT] Trace: {trace_context.trace_id} | Payload: {json.dumps(payload)}")
        trace_context.add_step(agent_name, "INPUT", payload)
        
    @staticmethod
    def log_decision(trace_context: TraceContext, agent_name: str, reason_code: str, rationale: str = ""):
        print(f"[{agent_name}] [DECISION] Trace: {trace_context.trace_id} | Reason: {reason_code} | Rationale: {rationale}")
        trace_context.add_step(agent_name, "DECISION", {"reason_code": reason_code, "rationale": rationale})

    @staticmethod
    def log_output(trace_context: TraceContext, agent_name: str, response: dict):
        print(f"[{agent_name}] [OUTPUT] Trace: {trace_context.trace_id} | Response: {json.dumps(response)}")
        trace_context.add_step(agent_name, "OUTPUT", response)

    @staticmethod
    def log_explainability(trace_context: TraceContext, agent_name: str, description: str):
        print(f"[{agent_name}] [EXPLAINABILITY] Trace: {trace_context.trace_id} | {description}")
        trace_context.add_step(agent_name, "EXPLAIN", {"description": description})
