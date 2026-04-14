from src.data.synthetic import generate_burnout_user
from src.agents.orchestrator import MasterOrchestratorAgent

agent = MasterOrchestratorAgent()

user = generate_burnout_user()

response = agent.handle_request(user)

print("\n🔥 SIMULATION RESULT:\n")
print(response)
