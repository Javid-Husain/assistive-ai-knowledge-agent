
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOCUMENTS_DIR = PROJECT_ROOT / "data" / "documents"


def load_document(file_path: Path) -> str:
    """Read a UTF-8 text document and return its contents."""
    return file_path.read_text(encoding="utf-8")


def main() -> None:
    document_path = DOCUMENTS_DIR / "spectov_intro.txt"

    if not document_path.exists():
        print(f"Document not found: {document_path}")
        return

    text = load_document(document_path)

    print("=" * 50)
    print("DOCUMENT INGESTION")
    print("=" * 50)
    print(f"Filename: {document_path.name}")
    print(f"Characters extracted: {len(text)}")
    print("\nExtracted text:\n")
    print(text)


if __name__ == "__main__":
    main()
