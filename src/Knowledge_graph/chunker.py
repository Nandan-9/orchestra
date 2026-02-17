import re
import pypdf





reader = pypdf.PdfReader("/home/das/pro/orchestra/src/Knowledge_graph/matrices")


# Function to clean common NCERT headers/footers
def clean_page_text(text):
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        # Remove page numbers and headers like "34 MATHEMATICS" or "MATRICES 35"
        if re.search(r'^\s*\d+\s+MATHEMATICS', line) or re.search(r'MATRICES\s+\d+\s*$', line):
            continue
        # Remove reprint info
        if "Reprint" in line:
            continue
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)

# Process the file
full_text = ""
for page in reader.pages:
    full_text += clean_page_text(page.extract_text()) + "\n"
    

# Simple chunking by Section Headers (e.g., 3.1, 3.2)
# Pattern: Look for "3.<digit> <Title>" at start of line
sections = re.split(r'\n(3\.\d+\.?\s+[A-Za-z ]+)', full_text)
chunked_data = {}
headings = []
if len(sections) > 1:
    print('fdf')
    # sections[0] is intro text before first header
    chunked_data["Intro"] = sections[0].strip()
    # sections[1] is header, sections[2] is content, sections[3] is header...
    for i in range(1, len(sections), 2):
        header = sections[i].strip()
        print(header)
        headings.append(header)
        content = sections[i+1].strip() if i+1 < len(sections) else ""
        chunked_data[header] = content

# Print found sections to confirm
# print(f"Total Sections Found: {len(chunked_data)}")
# print("Sections:", list(chunked_data.keys()))
# print("-" * 20)
# # Show a snippet of one section to verify
# # if "3.2  Matrix" in chunked_data:
# #     print("Snippet from '3.2 Matrix':")
# #     print(chunked_data["3.2  Matrix"][:300] + "...") # First 300 chars

for i in headings:
    print("contents of:"+i)
    print(chunked_data[i])
    print("-" * 20)