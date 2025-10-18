import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# ✅ Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("⚠️ GOOGLE_API_KEY not found. Please set it in your .env file.")
    st.stop()

# ✅ Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=api_key
)

# ✅ Load support_info.txt (automatically finds it in the same folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "support_info.txt")

# Debug print (appears in terminal, not Streamlit UI)
print("📂 Looking for file at:", file_path)

if not os.path.exists(file_path):
    raise FileNotFoundError(f"❌ File not found at: {file_path}")

with open(file_path, "r", encoding="utf-8") as f:
    support_data = f.read()

# ✅ Define prompt template
template = """
You are an AI assistant helping parents understand university student well-being support.
Use the following info to answer clearly and supportively:

{support_info}

Parent Question: {question}

Answer:
"""

prompt = PromptTemplate(
    input_variables=["support_info", "question"],
    template=template
)

# ✅ Create LLM chain
chain = LLMChain(llm=llm, prompt=prompt)

# ✅ Streamlit UI with mobile-responsive design
st.set_page_config(
    page_title="Student Wellbeing Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🎓 Parent Wellbeing Assistant")
st.markdown("*Powered by Gemini AI*")

# Mobile-friendly container
with st.container():
    st.write("Ask questions about student support and wellbeing.")
    st.info("💡 Example: *'How can a student access counselling services?'*")
    
    # Use text_area for better mobile experience
    user_q = st.text_area(
        "Enter your question:",
        height=100,
        placeholder="Type your question here..."
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        get_answer = st.button("Get Answer", use_container_width=True)
    
    if get_answer:
        if user_q.strip():
            with st.spinner("🤔 Thinking..."):
                try:
                    response = chain.run(support_info=support_data, question=user_q)
                    st.success("✅ Answer:")
                    st.write(response)
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter a question before clicking the button.")
