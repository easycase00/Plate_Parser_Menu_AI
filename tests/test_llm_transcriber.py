from menu.llm_transcriber import ocr_to_menu

def test_ocr_to_menu(monkeypatch):
    class DummyLLM:
        def invoke(self, prompt):
            return type("Response", (), {"content": '{"items": [{"Name": "Test"}]}'})
    monkeypatch.setattr("menu.groq_llm.get_groq_llm", lambda: DummyLLM())
    result = ocr_to_menu("Test OCR")
    assert "Test" in result
