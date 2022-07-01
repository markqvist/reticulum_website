import markdown
import os

SOURCES_PATH="./source"
BUILD_PATH="./build"
INPUT_ENCODING="utf-8"
OUTPUT_ENCODING="utf-8"

document_start = """
<!doctype html>
<html>
<head>
<link rel="stylesheet" href="css/water.css?v=1">
<meta charset="utf-8"/>
<title>Reticulum Network</title>
<![endif]-->
</head>
<body>
"""

document_end = """
</body>
</html>
"""

menu_md = """
<center>[Reticulum](index.html) | [Start](start.html) | [Hardware](hardware.html) | [Testnet](connect.html) | [Manual](docs.html) | [Crypto](crypto.html) | [Credits](credits.html) | [Source](https://github.com/markqvist/reticulum) | [Donate](donate.html)</center> 
"""

def scan_pages(base_path):
    files = [file for file in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, file)) and file[:1] != "."]
    directories = [file for file in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, file)) and file[:1] != "."]

    page_sources = []

    for file in files:
        if file.endswith(".md"):
            page_sources.append(base_path+"/"+file)

    for directory in directories:
        page_sources.append(scan_pages(base_path+"/"+directory))

    return page_sources

source_files = scan_pages(SOURCES_PATH)

for mdf in source_files:
    with open(mdf, "rb") as f:
        md = f.read().decode(INPUT_ENCODING)
        html = markdown.markdown(menu_md + md, extensions=["markdown.extensions.fenced_code"])
        html = document_start + html + document_end

        of = BUILD_PATH+mdf.replace(SOURCES_PATH, "").replace(".md", ".html")
        with open(of, "wb") as wf:
            wf.write(html.encode(OUTPUT_ENCODING))
