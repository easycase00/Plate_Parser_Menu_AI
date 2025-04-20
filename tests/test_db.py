from menu import db

def test_store_and_retrieve(monkeypatch):
    fake_storage = []

    # Mock insert_one to append to in-memory list
    class MockCollection:
        def insert_one(self, data):
            fake_storage.append(data)

        def find(self, *args, **kwargs):
            return fake_storage

    # Patch the actual `collection` object used in db.py
    monkeypatch.setattr(db, "collection", MockCollection())

    # Now run test logic
    sample_data = {"raw": "mock ocr", "structured": "mock menu"}
    db.store_menu(sample_data)
    all_data = db.get_all_menus()

    assert any(item["structured"] == "mock menu" for item in all_data)
