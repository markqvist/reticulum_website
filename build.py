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
<link rel="stylesheet" href="css/water.css?v=6">
<meta charset="utf-8"/>
<title>Reticulum Network</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
"""

document_end = """
</body>
</html>
"""

langs_md = """<div class="top_menu lang_menu">{LANGS}</div>"""
menu_md = """<div class="top_menu">[{RETICULUM}](index{LANG_EXT}.html) | [{START}](start{LANG_EXT}.html) | [{HARDWARE}](hardware{LANG_EXT}.html) | [{TESTNET}](connect{LANG_EXT}.html) | [{MANUAL}](docs{LANG_EXT}.html) | [{CRYPTO}](crypto{LANG_EXT}.html) | [{CREDITS}](credits{LANG_EXT}.html) | [{SOURCE}](https://github.com/markqvist/reticulum) | [{DONATE}](donate{LANG_EXT}.html)</div>"""

primary_lang = "en"
langs = [
    {"name": "Deutsch", "ext": "de"},
    {"name": "English", "ext": "en"},
    {"name": "Polski", "ext": "pl"},
    {"name": "Português", "ext": "pt-br"},
    {"name": "Türkçe", "ext": "tr"},
    {"name": "日本語", "ext": "jp"},
]

menu_translations = {
    "en": {
        "RETICULUM": "Reticulum",
        "START": "Start",
        "HARDWARE": "Hardware",
        "TESTNET": "Testnet",
        "MANUAL": "Manual",
        "CRYPTO": "Crypto",
        "CREDITS": "Credits",
        "SOURCE": "Source",
        "DONATE": "Donate",
    },
    "tr": {
        "RETICULUM": "Reticulum",
        "START": "Başlat",
        "HARDWARE": "Donanım",
        "TESTNET": "Test Ağı",
        "MANUAL": "Kılavuz",
        "CRYPTO": "Şifreleme",
        "CREDITS": "Hakkında",
        "SOURCE": "Kaynak",
        "DONATE": "Destekle",
    },
    "jp": {
        "RETICULUM": "レチキュラム",
        "START": "開始",
        "HARDWARE": "ハードウェア",
        "TESTNET": "テストネット",
        "MANUAL": "マニュアル",
        "CRYPTO": "暗号",
        "CREDITS": "クレジット",
        "SOURCE": "ソース",
        "DONATE": "寄付",
    },
    "de": {
        "RETICULUM": "Reticulum",
        "START": "Los Geht's",
        "HARDWARE": "Hardware",
        "TESTNET": "Testnetz",
        "MANUAL": "Handbuch",
        "CRYPTO": "Krypto",
        "CREDITS": "Credits",
        "SOURCE": "Quellcode",
        "DONATE": "Unterstützen",
    },"pl": {
        "RETICULUM": "Reticulum",
        "START": "Jak Zacząć",
        "HARDWARE": "Hardware",
        "TESTNET": "Testnet",
        "MANUAL": "Podręcznik",
        "CRYPTO": "Krypto",
        "CREDITS": "Zasługi",
        "SOURCE": "Kod Źródłowy",
        "DONATE": "Darowizna",
    },
    "pt-br": {
        "RETICULUM": "Reticulum",
        "START": "Começar",
        "HARDWARE": "Hardware",
        "TESTNET": "Rede de Teste",
        "MANUAL": "Manual",
        "CRYPTO": "Cripto",
        "CREDITS": "Créditos",
        "SOURCE": "Código",
        "DONATE": "Ajude",
    }
}

def get_page_lang(page):
    page_lang = primary_lang
    for lang in langs:
        base_name = mdf.replace(".md", "")
        if lang["ext"] != primary_lang:
            if base_name.endswith(lang["ext"]):
                page_lang = lang["ext"]
    return page_lang

def get_languages_md(page):
    page = page.replace(SOURCES_PATH, ".")
    current_page_lang = get_page_lang(page)
    if current_page_lang != primary_lang:
        page_base_name = page.replace("_"+current_page_lang+".md", "")
    else:
        page_base_name = page.replace(".md", "")

    lang_list = ""
    for lang_entry in langs:
        lang = lang_entry["name"]
        lang_ext = lang_entry["ext"]
        if lang_ext != primary_lang:
            lang_ext_str = "_"+lang_ext
        else:
            lang_ext_str = ""

        link_target = page_base_name+lang_ext_str+".html"
        link_md = "["+lang+"]("+link_target+") | "
        lang_list += link_md

    return langs_md.replace("{LANGS}", lang_list[:-3])


def get_menu_md(lang):
    local_menu_md = menu_md
    for entry in menu_translations[lang]:
        local_menu_md = local_menu_md.replace("{"+entry+"}", menu_translations[lang][entry])

    return local_menu_md

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
        page_lang = get_page_lang(mdf)

        if page_lang != primary_lang:
            page_lang_ext = "_"+page_lang
        else:
            page_lang_ext = ""

        md = f.read().decode(INPUT_ENCODING)
        page_md = "<center>"+get_languages_md(mdf)+""+get_menu_md(page_lang).replace("{LANG_EXT}", page_lang_ext) + "</center>\n\n" + md
        html = markdown.markdown(page_md, extensions=["markdown.extensions.fenced_code"])
        html = document_start + html + document_end

        of = BUILD_PATH+mdf.replace(SOURCES_PATH, "").replace(".md", ".html")
        with open(of, "wb") as wf:
            wf.write(html.encode(OUTPUT_ENCODING))
