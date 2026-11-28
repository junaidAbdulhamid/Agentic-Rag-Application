from io import BytesIO

from pypdf import PdfReader

def load_pdf(file_content: bytes) -> list[dict]:

    reader = PdfReader(BytesIO(file_content))

    pages = []

    for page_number, page in enumerate(

        reader.pages,

        start=1

    ):

        text = page.extract_text() or ""

        if text.strip():

            pages.append({

                "page_number": page_number,

                "content": text

            })

    return pages