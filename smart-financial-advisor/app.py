import sys
import os

# ✅ Fix root path (VERY IMPORTANT)
BASE_DIR = os.path.dirname(os.path.abspath(r"C:\Users\mohammad.qureshi\Documents\smart-financial-advisor"))
sys.path.append(BASE_DIR)

# ------------------ IMPORTS ------------------
import streamlit as st
import pandas as pd

from modules.expense import load_data, category_summary, monthly_summary
from modules.budget import train_model, predict_next
from modules.recommender import recommend
from chatbot.rag import load_rag, ask_query

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Smart Financial Advisor", layout="wide")

st.title("💰 Smart Financial Advisor")
st.markdown("### 🚀 AI + ML Powered Personal Finance Assistant")
st.markdown("---")

# ------------------ SIDEBAR ------------------
st.sidebar.header("📂 Upload Your Data")
file = st.sidebar.file_uploader("Upload Expenses CSV", type=["csv"])

# ------------------ LOAD CHATBOT ------------------
@st.cache_resource
def init_rag():
    try:
        return load_rag()
    except Exception as e:
        return None

db = init_rag()

# ------------------ TABS ------------------
tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "💹 Investment", "🤖 AI Chatbot"])

# ================== TAB 1: DASHBOARD ==================
with tab1:
    st.header("📊 Expense Dashboard")

    if file is not None:
        try:
            df = load_data(file)

            st.subheader("📋 Raw Data")
            st.dataframe(df, use_container_width=True)

            st.subheader("📂 Category-wise Spending")
            st.dataframe(category_summary(df))

            st.subheader("📅 Monthly Spending Trend")
            st.bar_chart(monthly_summary(df))

            st.subheader("💡 AI Prediction (Next Month Spend)")
            model = train_model(df)
            prediction = predict_next(model, len(df))

            st.success(f"Estimated Next Month Expense: ₹{prediction}")

        except Exception as e:
            st.error(f"Error processing file: {e}")
    else:
        st.info("📌 Please upload a CSV file to view analysis.")

# ================== TAB 2: INVESTMENT ==================
with tab2:
    st.header("💹 Investment Advisor")

    risk = st.selectbox("Select Your Risk Level", ["Low", "Medium", "High"])

    recommendations = recommend(risk)

    st.subheader("📌 Recommended Options:")
    for rec in recommendations:
        st.success(rec)

# ================== TAB 3: CHATBOT ==================
with tab3:
    st.header("🤖 AI Financial Chatbot")
    st.markdown("Ask anything about finance 💬")

    # ✅ Check API Key
    if not os.getenv("OPENAI_API_KEY"):
        st.error("⚠️ OpenAI API key not found. Please set it in environment variables.")
    elif db is None:
        st.error("⚠️ Chatbot failed to load. Check your RAG setup.")
    else:
        query = st.text_input("Enter your question:")

        if query:
            with st.spinner("Thinking... 🤖"):
                try:
                    response = ask_query(db, query)
                    st.success(response)
                except Exception as e:
                    st.error(f"❌ Error: {e}")

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown("👨‍💻 Built with ❤️ using Streamlit | AI | ML | RAG")