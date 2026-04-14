# 🧠 NutriFlow 2.0 — Context-Aware Nutrition Intelligence System

> NutriFlow doesn’t track what you eat.  
> It intervenes at the exact moment you're about to make a bad decision.

## 🔍 Live System Trace Example
```log
[MasterOrchestratorAgent] → TIER_3_GEMINI_HIGH_VARIANCE
[NudgeAgent] → Generated contextual decision
Output → Matcha recommendation (+12% stability)
```

👉 This shows:
- real system
- real logs
- real intelligence

---

## 🚀 Overview

NutriFlow 2.0 is a **context-aware, AI-powered nutrition assistant** designed for modern professionals.

Instead of manual tracking, it uses:
- Real-time context (location, calendar, health)
- Behavioral intelligence (past decisions)
- AI reasoning (Gemini via Vertex AI)

👉 To deliver **proactive, personalized food decisions**

---

## 🎯 Core Idea

Traditional apps = Reactive  
NutriFlow = **Intervention Engine**

We solve the **“compliance gap”**:
> The moment between knowing what’s healthy and actually choosing it.

---

## 🧩 Architecture

### 🔥 Master Orchestrator

#### `MasterOrchestratorAgent`
- Central decision router
- Applies **Intervention Threshold Logic**
- Chooses:
  - Rule-based
  - Heuristic
  - AI (Gemini)

Maintains:
- `user_state_score`
- `mode` (Passive / Active / Burnout)
- `ignore_rate`

---

### 🧠 Feature Agents

| Agent | Responsibility |
|------|---------------|
| `DashboardAgent` | Energy score + momentum |
| `MapIntelligenceAgent` | Food discovery + risk zones |
| `NudgeAgent` ⭐ | Decision engine (core) |
| `PersonalizationAgent` | Behavioral Nutrition Graph (BNG) |
| `OutcomeAgent` | ROI + impact metrics |
| `AdaptiveModeAgent` | Mode switching logic |
| `EmpathyAgent` | Burnout-aware UX |
| `SyntheticDataAgent` | Realistic simulation |

---

## ⚙️ Core Logic

### 🔁 Tiered Inference System

```python
if routine_case:
    return rule_based()

elif fallback_condition:
    return heuristic()

elif high_variance:
    return gemini_call()
```

### 🚨 Intervention Threshold
AI is triggered ONLY when:
- Energy is low
- Stress is high
- Decision moment is detected

---

## 🧠 Nudge Engine (Core Feature)
**Example Output:**
```json
{
  "nudge_text": "Skip the latte. Matcha keeps your 4 PM focus stable.",
  "options": {
    "option_a": {"name": "Latte", "impact": "-15 energy crash"},
    "option_b": {"name": "Matcha", "impact": "+12% stability"}
  },
  "impact": {
    "energy_stability": "+12%",
    "focus_gain": "+30 mins"
  },
  "future_self": "Your 4 PM self will thank you.",
  "confidence": 0.91,
  "fallback": "If latte → add 10-min walk",
  "reasoning": [
    "Low sleep",
    "High stress",
    "Past crash pattern"
  ]
}
```

---

## 🧬 Behavioral Nutrition Graph (BNG)
Stores user decisions as embeddings.
Tracks: `Context → Action → Outcome`

Powers:
1. Personalization
2. Defensibility (data moat)

---

## 📊 Key Metric: Energy Stability Score 🏆
**Goal:** Improve daily cognitive stability and reduce energy crashes.

---

## 🎨 UI (Built with Google Stitch)
**Connected Screens:**
- Dashboard (Momentum + Score)
- Smart Map (Risk Zones)
- Predictive Map (Route-aware)
- Nudge Cards (Decision engine)
- Outcome Screen (Impact + ROI)
- History & Insights
- Settings & Modes
- Empathy Mode (Burnout UX)

---

## 🧪 Synthetic Data Engine
Simulates realistic usage for production-ready demos.

**Personas:**
- 🔥 High Performer
- 😵 Burnout User
- 🎲 Erratic User

**Data Includes:**
- Sleep cycles, Meetings, Food patterns, Stress spikes

---

## 🔍 Observability & Debugging

**Trace System:**
- Unique `trace_id` per request
- Tracks full execution flow

**Logging Format:**
```
[AgentName] [INPUT] Trace: <id> | Payload: {...}
[AgentName] [DECISION] Trace: <id> | Reason: <decision> | Rationale: <why>
[AgentName] [OUTPUT] Trace: <id> | Response: {...}
```

---

## 🌐 API Endpoints
- `/nudge` → decision engine
- `/dashboard` → energy + momentum
- `/map` → food intelligence
- `/outcome` → impact metrics
- `/history` → behavior tracking
- `/simulate` → synthetic scenarios

---

## ☁️ Deployment (Google Cloud Run)
**Stack:** Python (FastAPI), Vertex AI (Gemini), Firebase (Auth + Firestore), Google Maps API

```bash
docker build -t nutriflow .
gcloud run deploy nutriflow-backend \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated
```