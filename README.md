# 🔎 TruthLens


AI-powered fact verification agent built with **Python + Groq**.


TruthLens takes a factual claim, analyzes it using an LLM, and returns a structured verdict with confidence, reasoning, and evidence.


## 🧠 Architecture


```text
User Claim
    ↓
Python Agent
    ↓
Groq LLM
    ↓
Evidence Analysis
    ↓
Verdict + Confidence
🛠️ Tech Stack
Python — Agent/controller
Groq — AI reasoning
Pydantic — Structured data validation
python-dotenv — API key management
📁 Structure
truthlens/
├── app.py
├── agent.py
├── verifier.py
├── models.py
├── prompts.py
├── config.py
├── requirements.txt
└── tests/
    └── test_claims.py
⚙️ Setup
git clone https://github.com/YOUR_USERNAME/truthlens.git
cd truthlens


python -m venv .venv

Windows:

.\.venv\Scripts\Activate.ps1

Install dependencies:

python -m pip install -r requirements.txt

Create .env:

GROQ_API_KEY=your_api_key

Run:

python app.py
📊 Verdicts

TRUE · MOSTLY_TRUE · MISLEADING · MOSTLY_FALSE · FALSE · UNVERIFIABLE · OPINION

🔬 Evaluation

Planned metrics:

Accuracy
Precision
Recall
F1 Score
Confusion Matrix
Hallucination Rate
Confidence Calibration
🚧 Roadmap
 Groq-powered verification
 Structured outputs
 Confidence scoring
 Evidence handling
 Real-time web search
 Source reliability scoring
 Contradiction detection
 FastAPI backend
 Web UI

V1 is a prototype focused on understanding and building the core AI-agent architecture.
