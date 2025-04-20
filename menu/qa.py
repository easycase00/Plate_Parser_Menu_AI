# menu/qa.py

from menu.db import get_all_menus
from menu.groq_llm import get_groq_llm

def get_qa_chain():
    llm = get_groq_llm()
    return llm

def answer_question(query: str):
    llm = get_qa_chain()
    menus = get_all_menus()

    if not menus:
        return "❌ No menus available in the database."

    # Create a single unified context from all menus
    context_parts = []
    for menu in menus:
        structured = menu.get("structured", {})
        context_parts.append(str(structured))

    context = "\n".join(context_parts)

    # Prompt for LLM
    prompt = f"""You are a helpful assistant that answers questions about restaurant menus.

Context:
{context}

Question:
{query}

Answer:"""

    response = llm.invoke(prompt)
    return response.content.strip()
