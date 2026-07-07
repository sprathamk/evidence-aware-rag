import fitz
import os

def extract_pages(pdf_path: str) -> str:

    doc = fitz.open(pdf_path)

    pages = []

    for page_num, page in enumerate(doc, start=1):

        pages.append(
            {
                "text": page.get_text(),
                "page": page_num,
                "document": os.path.basename(pdf_path),
            }
        )

    doc.close()

    return pages


if __name__ == "__main__":
    pdf_path = "../../data/sample.pdf"

    text = extract_text(pdf_path)

    print(text[:2000])