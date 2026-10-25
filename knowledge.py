from pathlib import Path
import re

DOCUMENTS_DIR = Path(__file__).parent / "documents"


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"\b[a-zA-Z0-9]+\b", text.lower()))


def load_documents() -> list[dict]:
    documents = []

    for path in DOCUMENTS_DIR.glob("*.txt"):
        documents.append({
            "title": path.stem,
            "content": path.read_text(encoding="utf-8"),
        })

    return documents


def search_documents(query: str, limit: int = 3) -> list[dict]:
    query_words = tokenize(query)
    results = []

    for document in load_documents():
        document_words = tokenize(
            document["title"] + " " + document["content"]
        )

        score = len(query_words & document_words)

        if score > 0:
            results.append({
                **document,
                "score": score,
            })

    results.sort(key=lambda item: item["score"], reverse=True)
    return results[:limit]