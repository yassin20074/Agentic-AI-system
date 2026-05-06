# ​🤖 Agentic AI Research & Execution System
​A production-grade Agentic AI System designed for autonomous technical research and content synthesis. This system leverages a Multi-Agent Architecture to perform deep web searches and generate professional reports, all while maintaining a persistent long-term memory.

# ​🚀 Key Features
**​Multi-Agent Workflow:**  Orchestrates tasks between a Researcher Agent (data gathering) and a Technical Writer Agent (synthesis).
**​Long-term Memory:** Persistent user sessions using PostgreSQL via LangGraph Checkpointers.
**​Autonomous Decision Making:** Uses conditional logic to decide when to use tools (Tavily Search) vs. when to finalize a response.
**​State Persistence:** Capable of resuming complex tasks even after system restarts, thanks to its robust database backend.
​**Production-Ready:** Fully containerized with Docker and served via a high-performance FastAPI wrapper.

# ​🛠 Tech Stack
**​Orchestration:** LangGraph & LangChain.
**​Intelligence:** GPT-4o (OpenAI).
**​Backend:** FastAPI with Uvicorn.
**​Database:** PostgreSQL (using psycopg_pool and langgraph-checkpoint-postgres).
**​Deployment:** Docker & Docker Compose.
**​Data Source:** Tavily AI (Real-time Search).

# What happens behind the scenes?
​The Researcher identifies the need for fresh data and triggers the Search Tool.
​The results are passed to the Technical Writer.
​The final report is saved to Postgres under your session_id.
​Next time you ask a question, the agent remembers your previous context.

​**👨‍💻 Developed By**:eng.Yassin Sanad
