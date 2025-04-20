from langchain_groq import ChatGroq

def get_groq_llm():
    return ChatGroq(
        model_name="llama3-70b-8192",
        temperature=0.3
    )
