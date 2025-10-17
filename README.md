Personal Investment Advisor Agent

A conversational, agentic AI system that provides personalized investment advice, risk analysis, and actionable insights based on your portfolio, real-time market data, and the latest financial news. Built with Azure OpenAI, Azure AI Search, and cloud-native services.

Table of Contents

Project Overview

Features

Architecture

Tech Stack

Getting Started

Usage

Contributing

License

Contact

Project Overview
Personal Investment Advisor Agent is an AI-powered assistant that helps you make smarter investment decisions. It securely stores your portfolio, analyzes your assets, fetches real-time news and market data, and provides explainable recommendations and risk assessments—all through a conversational interface.

Features
Securely store and manage your personal investment portfolio (stocks, crypto, etc.)

Ask questions like “Should I buy bitcoin?” and receive explainable, data-driven advice

Real-time integration with financial news, analyst reports, and market data

Forecasting and pattern recognition using ML models

Risk analysis and personalized alerts

User-friendly web interface and REST API

Tech Stack
Backend: Python (FastAPI/Flask)

Frontend: Streamlit or React (optional: Electron for desktop)

Cloud: Azure OpenAI, Azure AI Search, Azure Cosmos DB, Azure Functions

Data: External APIs for real-time stock/crypto/news

DevOps: Docker, GitHub Actions, Azure App Service

Prerequisites
Python 3.10+

Azure account with OpenAI, AI Search, and Cosmos DB enabled

Docker (optional, for containerized deployment)

Installation
1.Clone the repository:

git clone https://github.com/yourusername/personal-investment-advisor-agent.git
cd personal-investment-advisor-agent

2.Install dependencies:
pip install -r requirements.txt

3.Set up environment variables API keys 

4.Run The API locally:
uvicorn app.main:app --reload

Usage:
Access the web UI at http://localhost:8501 (if using Streamlit).

Use the REST API endpoints to interact programmatically.
POST /api/ask
{
  "question": "Should I buy bitcoin?",
  "portfolio": ["AAPL", "TSLA", "BTC"]
}
Contributing
Contributions are welcome! Please open an issue or submit a pull request.

Contact
Created by Shiva Heydari — feel free to reach out!