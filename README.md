# 💼 Personal Investment Advisor Agent

> **An AI-powered financial assistant** that provides personalized investment advice, risk analysis, and actionable insights — powered by **Azure OpenAI**, **Azure AI Search**, and cloud-native services.

---

## 🧭 Table of Contents
- [📘 Overview](#-project-overview)
- [✨ Features](#-features)
- [🏗️ Architecture](#-architecture)
- [🧰 Tech Stack](#-tech-stack)
- [🚀 Getting Started](#-getting-started)
- [🧪 Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [📬 Contact](#-contact)

---

## 📘 Project Overview

**Personal Investment Advisor Agent** is a conversational, agentic AI system that helps you make **smarter investment decisions**.  
It securely stores your portfolio, analyzes your assets, fetches **real-time financial data**, and provides **explainable recommendations** and **risk assessments** — all through a **chat-based interface**.

> 💡 *Think of it as your personal financial analyst — available 24/7.*

---

## ✨ Features

✅ Securely store and manage your personal investment portfolio (stocks, crypto, etc.)  
✅ Ask natural-language questions like *“Should I buy Bitcoin?”* and get **explainable**, **data-driven** insights  
✅ Fetch **real-time news**, analyst reports, and market trends  
✅ Perform **forecasting** and **pattern recognition** using ML models  
✅ **Risk analysis** and personalized alerts  
✅ Modern, **user-friendly web interface** and **REST API** support  

---

## 🏗️ Architecture


---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | Python (FastAPI / Flask) |
| **Frontend** | Streamlit / React *(optional: Electron for desktop)* |
| **Cloud** | Azure OpenAI, Azure AI Search, Azure Cosmos DB, Azure Functions |
| **Data** | External APIs for Stocks, Crypto, Financial News |
| **DevOps** | Docker, GitHub Actions, Azure App Service |

---

## ⚙️ Prerequisites

- 🐍 Python **3.10+**
- ☁️ Azure account with **OpenAI**, **AI Search**, and **Cosmos DB**
- 🐳 Docker *(optional for container deployment)*

Local dev note
----------------
If you don't have Cosmos DB credentials while developing locally you can enable a small in-memory fallback by setting an environment variable:

```bash
export PFA_DEV_FALLBACK=1
# or on Windows PowerShell:
$Env:PFA_DEV_FALLBACK = '1'
```

When enabled the portfolio service uses an in-memory store so the Streamlit UI and API work without Azure.

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/personal-investment-advisor-agent.git
cd personal-investment-advisor-agent
```

### 2️⃣ Install dependencies
pip install -r requirements.txt

### 3️⃣ Set up environment variables
Configure your API keys and Azure credentials in a .env file.

### 4️⃣ Run the API locally
uvicorn app.main:app --reload

Alternatively, run the module or the built-in dev runner:

```bash
# Run with python -m uvicorn
python -m uvicorn app.main:app --reload

# Or use the built-in runner in app/main.py
python -m app.main
```

🧪 Usage
💻 Web Interface

Access the Streamlit UI at:
👉 http://localhost:8501

🔗 REST API Example

Endpoint: POST /api/ask

{
  "question": "Should I buy bitcoin?",
  "portfolio": ["AAPL", "TSLA", "BTC"]
}

🤝 Contributing

Contributions are welcome! 🙌
If you have ideas or improvements:

Fork the repo 🍴

Create your feature branch 🌿

Commit your changes 💬

Open a Pull Request 🚀