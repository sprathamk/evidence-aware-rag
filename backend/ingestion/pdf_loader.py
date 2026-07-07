import fitz

def extract_text(pdf_path: str) -> str:

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    return text


if __name__ == "__main__":
    pdf_path = "../../data/sample.pdf"

    text = extract_text(pdf_path)

    print(text[:2000])