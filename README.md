# 📘 Plate Parser: A Modular LLM-RAG System for Intelligent Menu Digitization and Food-Tech Q&A

**🔗 [Live Demo](https://plateparser.streamlit.app/)** 

---

## 📌 Abstract

This project presents **Plate Parser**, a scalable, research-inspired pipeline that transforms unstructured restaurant menu images into structured, queryable data using a combination of computer vision, retrieval-augmented generation (RAG), and large language model (LLM) techniques. 

Inspired by DoorDash’s [LLM Menu Intelligence system](https://careersatdoordash.com/blog/doordash-llm-transcribe-menu/), this implementation builds a fully operational version deployable in production, pushing the limits by integrating end-to-end OCR correction, token-aware preprocessing, document storage, and contextually grounded LLM inference.

---

## 🧠 System Overview

### Architecture Highlights

- **Frontend**: Streamlit UI for interactive image upload, OCR inspection, and LLM-based Q&A.

- **OCR Engine**: Built on `EasyOCR`, enhanced with OpenCV-driven image preprocessing:
  - Grayscale conversion
  - Binarization
  - Noise reduction
  - Morphological operations
  - Edge sharpening

- **Text Pipeline**:
  - Token normalization
  - Whitespace-sensitive segmentation
  - Regex-based line parsing
  - Text reflow logic to emulate human-readable menu structure

- **LLM Transcriber**:
  - Powered by `ChatGroq` + `llama-3.3-70b-versatile` via `LangChain`
  - Schema-constrained prompt engineering to extract structured JSON with `category`, `name`, `description`, and `price` fields

- **Storage Backend**:
  - Raw and processed menu documents stored in **MongoDB Atlas**
  - Enables schema-less retrieval and filtering for structured RAG

- **RAG-based Q&A Module**:
  - Retrieves documents from MongoDB
  - Builds semantic context prompts
  - Supports intelligent user queries about stored menus

---

## 🔬 Technical Innovations & ML Techniques

| Module             | Techniques Used                                                                 |
|--------------------|----------------------------------------------------------------------------------|
| Computer Vision     | OpenCV-based denoising, morphological closing, thresholding, edge sharpening    |
| OCR Postprocessing  | Context-aware whitespace segmentation, regex-based section detection            |
| NLP Preprocessing   | Tokenization, text normalization, few-shot formatting                           |
| LLM Extraction      | Prompt-based schema extraction via ChatGroq (`llama-3.3-70b-versatile`)          |
| Data Structuring    | JSON schema alignment, entity-label mapping, type inference                     |
| Q&A Engine          | MongoDB retrieval + prompt construction + RAG-style LLM inference                |
| Deployment          | Streamlit + `.streamlit/secrets.toml` for managed hosting                       |

---

## 🏭 Real-World Applications

### Food Delivery Platforms
- **DoorDash, Uber Eats, Zomato** can rapidly onboard restaurant partners
- Automatically extract structured schema from PDFs and photos
- Tag menu items, apply dietary filters, translate dishes

### Consumer-Facing Food Apps
- Nutrition assistants can answer queries like *"Which dishes are under 500 calories?"*
- Voice agents can support real-time ordering with rich metadata

### AI-Powered Restaurant Management
- Extend RAG pipeline to generate pricing suggestions, combo offers
- Use zero-shot models (e.g., BART) to classify cuisine types and dietary labels

---

## 🧰 Project Structure
```
Plate_Parser_Menu_AI/
├── app.py                   # Streamlit application logic
├── menu/
│   ├── ocr.py              # EasyOCR + OpenCV text extractor
│   ├── db.py               # MongoDB Atlas storage layer
│   ├── llm_transcriber.py  # LLM-based JSON extractor
│   ├── qa.py               # Mongo-aware context builder + RAG
│   └── groq_llm.py         # LangChain ChatGroq LLM setup
├── .streamlit/
│   └── secrets.toml        # API keys and secrets
├── requirements.txt        # Python dependencies
└── tests/                  # Unit test scaffolding
```

---

## 🚀 Deployment & Hosting

The app is **live** and publicly accessible at:

🔗 **[https://plateparser.streamlit.app/](https://plateparser.streamlit.app/)**

### To run locally:

```bash
git clone https://github.com/easycase00/Plate_Parser_Menu_AI.git
cd Plate_Parser_Menu_AI
pip install -r requirements.txt
streamlit run app.py
```
---

### 🔐 Environment Variables

Required via `.streamlit/secrets.toml`:

- `GROQ_API_KEY`
- `GROQ_MODEL=llama-3.3-70b-versatile`
- `MONGO_USERNAME`, `MONGO_PASSWORD`, `MONGO_CLUSTER`


---

## 🧪 Future Enhancements

- 🔤 **Multilingual OCR** with translation
- 🧠 **Neural entity linking** for nutrition tags (e.g., sodium, carbs)
- 📊 **Embedding-based search** using vector DBs like **Qdrant**, **Pinecone**, or **Chroma**
- 🖼️ **Layout-aware parsing** with models like **LayoutLM** or **Donut**

---

## 🧾 Citation & Credits

**Bharadwaj, Hrishikesh (2025)**  
*Plate Parser: An LLM-Driven Menu Intelligence Platform Using RAG and OCR*  
Indiana University, Data Science


### 🔍 Inspired by:

- [DoorDash’s LLM Menu Transcription Research](https://careersatdoordash.com/blog/doordash-llm-transcribe-menu/)

### 🛠️ Built using:

- **LangChain**
- **ChatGroq**
- **MongoDB Atlas**
- **Streamlit**
- **EasyOCR**
