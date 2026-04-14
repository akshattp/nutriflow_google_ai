import random

def generate_burnout_user() -> dict:
    return {
        "persona": "BURNOUT",
        "energy_score": random.randint(15, 40),
        "stress_level": random.randint(75, 95),
        "recent_meals": ["Donut", "Coffee", "Pizza"],
        "routine_variance": 0.8,
        "location": "Near Blue Bottle Coffee at 2:45 PM",
        "is_decision_moment": True
    }

class SyntheticDataAgent:
    @staticmethod
    def generate_persona_data(persona_type: str) -> dict:
        if persona_type == "BURNOUT":
            return generate_burnout_user()
        return {}
