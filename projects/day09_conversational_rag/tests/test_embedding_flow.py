import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from document_loader import DocumentLoader


class EmbeddingFlowTests(unittest.TestCase):
    def test_document_loader_uses_generate_embeddings(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            data_path = Path(tmpdir) / "company_documents.json"
            data_path.write_text(
                json.dumps([
                    {
                        "id": "1",
                        "content": "hello world",
                        "title": "Doc 1",
                        "department": "Engineering",
                        "category": "General",
                        "author": "Alice",
                        "version": "1",
                    }
                ]),
                encoding="utf-8",
            )

            fake_settings = type("Settings", (), {"DATA_PATH": data_path})

            with patch("document_loader.settings", fake_settings), patch(
                "document_loader.vector_store"
            ) as fake_vector_store, patch("document_loader.embedding_service") as fake_embedding_service:
                fake_vector_store.count.return_value = 0
                fake_embedding_service.generate_embeddings.return_value = [0.1, 0.2, 0.3]

                loader = DocumentLoader()
                loader.load_documents()

                fake_embedding_service.generate_embeddings.assert_called_once_with("hello world")
                fake_vector_store.add_documents.assert_called_once()


if __name__ == "__main__":
    unittest.main()
