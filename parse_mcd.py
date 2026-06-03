import pymupdf, re, json

doc = pymupdf.open("mcdonalds_cprl.pdf")
# Each item has a block starting with the item name, followed by serve size, energy, etc.
# Pattern: item name line, then "Serve Size (g)" line, then "Energy (kCal)" line with the value
items = []
current_item = {}
page_text = ""

for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    page_text += text + "\n---PAGE BREAK---\n"

# Now parse the text to extract items
# Each item in the PDF has a specific structure
lines = page_text.split('\n')
items_data = []
item_block = []
in_item = False

for line in lines:
    line = line.strip()
    if not line:
        if item_block:
            items_data.append('\n'.join(item_block))
            item_block = []
        in_item = False
        continue
    
    # Look for item name + "Serve Size"
    if 'Serve Size (g)' in line:
        in_item = True
        item_block = [line]
    elif in_item:
        item_block.append(line)

if item_block:
    items_data.append('\n'.join(item_block))

# Print first 30 blocks to understand structure
for i, block in enumerate(items_data[:30]):
    print(f"=== ITEM {i} ===")
    print(block[:500])
    print()
