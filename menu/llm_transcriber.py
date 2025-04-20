import json
from menu.groq_llm import get_groq_llm

def ocr_to_menu(ocr_text: str) -> dict:
    llm = get_groq_llm()

    prompt = f"""You are a helpful assistant. Extract the restaurant menu from the following OCR text and format it as a JSON object.

OCR Text:
{ocr_text}

The JSON should have this structure:
{{
  "menu": [
    {{
      "category": "CATEGORY NAME",
      "items": [
        {{
          "name": "ITEM NAME",
          "description": "ITEM DESCRIPTION (if available)",
          "price": ITEM PRICE (as a float)
        }},
        ...
      ]
    }},
    ...
  ]
}}
Only output the JSON.
"""

    response = llm.invoke(prompt)
    
    raw_output = response.content.strip()
    print("🔍 Raw LLM Output:\n", raw_output)

    try:
        cleaned = (
            raw_output
            .removeprefix("```json")
            .removeprefix("```")
            .removesuffix("```")
            .strip()
        )
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        print("❌ JSON parsing failed:", e)
        return {"error": "LLM response could not be parsed into JSON."}
