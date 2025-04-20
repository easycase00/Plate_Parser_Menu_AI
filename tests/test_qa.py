from menu.qa import answer_question

def test_answer_question(monkeypatch):
    class DummyQA:
        def run(self, query):
            return f"Mocked answer to: {query}"

    monkeypatch.setattr("menu.qa.get_qa_chain", lambda: DummyQA())
    result = answer_question("What are vegetarian options?")
    assert "vegetarian" in result
