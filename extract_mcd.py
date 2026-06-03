import pymupdf
doc = pymupdf.open("mcdonalds_cprl.pdf")
# Extract all text with position info
for page in doc:
    blocks = page.get_text("dict")["blocks"]
    for b in blocks:
        if "lines" in b:
            for l in b["lines"]:
                text = " ".join([s["text"] for s in l["spans"]])
                y = round(l["bbox"][1], 0)
                print(f"{y:.0f}|{text}")
