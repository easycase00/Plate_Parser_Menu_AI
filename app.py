import streamlit as st
from PIL import Image
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# === Clean up `.DS_Store` and `._*` files ===
def cleanup_mac_junk_files():
    dirs_to_clean = [
        os.getcwd(),  # current working directory
        os.path.join(os.getcwd(), "data/vectorstore")
    ]
    for dir_path in dirs_to_clean:
        if not os.path.exists(dir_path):
            continue
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.startswith("._") or file == ".DS_Store":
                    try:
                        os.remove(os.path.join(root, file))
                        print(f"✅ Deleted: {os.path.join(root, file)}")
                    except Exception as e:
                        print(f"⚠️ Could not delete {file}: {e}")

# Run cleanup on app launch
cleanup_mac_junk_files()

# === App imports ===
from menu.db import store_menu, get_all_menus
from menu.ocr import extract_text_from_image
from menu.llm_transcriber import ocr_to_menu
from menu.qa import answer_question

# === Streamlit UI ===
st.set_page_config(page_title="📸 Menu Intelligence App")
st.title("📸 Menu Intelligence App")

# === Upload Section ===
uploaded_file = st.file_uploader("Upload a menu photo", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Menu")

    if st.button("🔍 Extract & Transcribe"):
        with st.spinner("Running OCR..."):
            ocr_text = extract_text_from_image(image)
            st.text_area("OCR Result", ocr_text, height=200)

        with st.spinner("Transcribing into structured menu..."):
            structured = ocr_to_menu(ocr_text)

            if "error" in structured:
                st.error("❌ Failed to parse structured menu from LLM.")
            else:
                st.code(json.dumps(structured, indent=2), language="json")

                store_menu({
                    "raw": ocr_text,
                    "structured": structured
                })

                st.success("✅ Menu stored in MongoDB!")

# === Q&A Section ===
st.divider()
st.subheader("🔎 Ask questions about stored menus")

query = st.text_input("e.g. 'What are the vegetarian options?'")
if st.button("Answer"):
    if query:
        with st.spinner("Thinking..."):
            answer = answer_question(query)
            st.success(answer)

# === View All Stored Menus ===
st.divider()
st.subheader("📂 Stored Menus in MongoDB")

menus = get_all_menus()
if menus:
    for i, menu in enumerate(menus, 1):
        st.json(menu.get("structured", {}), expanded=False)
else:
    st.info("No menus stored yet. Upload one to get started!")
