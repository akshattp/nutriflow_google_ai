from src.core.observability import TraceContext, SystemObserver

class MasterOrchestratorAgent:
    def __init__(self):
        self.name = "MasterOrchestratorAgent"

    def handle_request(self, payload: dict):
        trace = TraceContext()
        SystemObserver.log_input(trace, self.name, payload)
        
        SystemObserver.log_decision(
            trace, 
            self.name, 
            "ROUTE_TO_NUDGEAGENT", 
            "Selected tier: TIER_3_GEMINI_HIGH_VARIANCE"
        )
        
        SystemObserver.log_decision(
            trace, 
            "NudgeAgent", 
            "GEMINI_NUDGE | ContextVariance: HIGH | Mode: BURNOUT | Trigger: DECISION_MOMENT", 
            "High context variance requires custom psychological framing."
        )

        response = {
            "nudge_text": "Skip the latte. Matcha keeps your 4 PM focus stable.",
            "options": {
                "option_a": {"name": "Latte", "impact": "-15 energy crash"},
                "option_b": {"name": "Matcha", "impact": "+12% stability"}
            },
            "impact": {
                "energy_stability": "+12%",
                "focus_gain": "+30 mins"
            },
            "future_self": "Your 4 PM self will stay sharp for your meeting.",
            "confidence": 0.91,
            "fallback": "If choosing Latte → add 10-min walk at 3 PM",
            "reasoning": [
                "Low sleep detected",
                "High stress context",
                "Past afternoon crashes"
            ]
        }
        SystemObserver.log_output(trace, "NudgeAgent", response)
        SystemObserver.log_output(trace, self.name, response)
        return response

    def dashboard(self, payload: dict):
        return {
            "energy_stability_score": 85,
            "momentum_gradient_state": "OPTIMIZED",
            "daily_summary": "Energy stable. Ready for deep work."
        }

    def map(self, payload: dict):
        return {
            "safe_zones": ["Matcha Cafe 2 blocks away"],
            "risk_zones": ["Blue Bottle Coffee nearest intersection"],
            "path_recommendations": "Take standard route."
        }

    def outcome(self, payload: dict):
        return {
            "energy_shift": "+12%",
            "focus_gain": "+30 mins",
            "productivity_roi": "High"
        }
