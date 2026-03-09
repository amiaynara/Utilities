#!/Users/amiaynarayan/Projects/utilities/.util-env/bin/python

import sys
from pypdf import PdfReader, PdfWriter

def parse_pages(spec):
    pages = set()

    parts = spec.split(",")

    for part in parts:
        if "-" in part:
            start, end = part.split("-")
            pages.update(range(int(start)-1, int(end)))
        else:
            pages.add(int(part)-1)

    return pages


if len(sys.argv) < 3:
    print("Usage: pdfcut input.pdf 2-5 or 2,4,7")
    sys.exit(1)

input_file = sys.argv[1]
delete_spec = sys.argv[2]

pages_to_delete = parse_pages(delete_spec)

reader = PdfReader(input_file)
writer = PdfWriter()

for i, page in enumerate(reader.pages):
    if i not in pages_to_delete:
        writer.add_page(page)

output = input_file.replace(".pdf", "_cut.pdf")

with open(output, "wb") as f:
    writer.write(f)

print(f"Saved: {output}")

