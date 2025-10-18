from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv


# Build an absolute path dynamically (works anywhere)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "support_info.txt")

# Debug print (optional)
print("📁 Looking for support_info.txt at:", file_path)

if not os.path.exists(file_path):
    raise FileNotFoundError(f"❌ File not found at: {file_path}")

with open(file_path, "r", encoding="utf-8") as f:
    support_data = f.read()

# ✅ Load environment
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("⚠️ GOOGLE_API_KEY not found. Please set it in your .env file.")
    exit()

# ✅ Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=api_key
)

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

# ✅ Load support info
with open("support_info.txt", "r", encoding="utf-8") as f:
    support_data = f.read()

# ✅ CLI interaction loop
while True:
    user_q = input("Ask a question about student well-being (or 'quit'): ")
    if user_q.lower() == "quit":
        break
    response = chain.run(support_info=support_data, question=user_q)
    print("\nAI Response:", response, "\n")
