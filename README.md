# Smart-Finance-Advisor

📌 Overview

Smart Financial Advisor is an AI-powered personal finance assistant that helps users analyze their spending habits, predict future expenses, and receive intelligent financial advice through a conversational chatbot powered by Retrieval-Augmented Generation (RAG).

🚀 Features
📊 Expense Analysis Dashboard
Upload your expense data and visualize category-wise and monthly spending trends.
🧠 AI-Based Budget Prediction
Uses Machine Learning (Linear Regression) to predict future expenses.
💹 Investment Recommendation System
Suggests financial instruments based on user risk profile (Low, Medium, High).
🤖 RAG-Based Chatbot
Answers finance-related queries using contextual knowledge from a custom dataset.
📂 CSV Upload Support
Easily upload and analyze your financial data.
🧠 Tech Stack
Frontend: Streamlit
Backend: Python
Machine Learning: Scikit-learn
AI/LLM: LangChain + OpenAI / Ollama / HuggingFace
Vector Database: FAISS
Data Processing: Pandas, NumPy
🏗️ Architecture
User Input
   ↓
Streamlit UI
   ↓
Backend Processing
   ├── Expense Analysis (Pandas)
   ├── ML Prediction (Scikit-learn)
   ├── Recommendation Engine
   └── RAG Chatbot (FAISS + LLM)
   ↓
Output (Insights + AI Response)
📁 Project Structure
smart-financial-advisor/
│
├── app.py
├── data/
├── modules/
├── chatbot/
└── requirements.txt
⚙️ Installation
git clone <your-repo-link>
cd smart-financial-advisor
pip install -r requirements.txt
python -m streamlit run app.py
🔑 Environment Setup

If using OpenAI:

setx OPENAI_API_KEY "your_api_key"
📊 Sample Use Case
Upload your monthly expenses
View insights and trends
Get predicted next month spending
Ask questions like:
“How can I save money?”
“Best investment for beginners?”
