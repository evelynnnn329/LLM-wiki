"""
Academic Paper Utility Script for LLM Wiki
Provides functions to:
1. Download papers from arXiv and save to raw/paper/
2. Extract text and metadata from PDFs in raw/paper/
"""

import sys
import os
import re
import json
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from pypdf import PdfReader

RAW_PAPER_DIR = Path("raw/paper")

def parse_arxiv_id(query: str) -> str:
    """Extract arXiv ID from url or raw ID string."""
    query = query.strip()
    match = re.search(r"(\d{4}\.\d{4,5}(?:v\d+)?)", query)
    if match:
        return match.group(1)
    match_old = re.search(r"([a-z\-]+/\d{7})", query)
    if match_old:
        return match_old.group(1)
    return query

def fetch_arxiv_metadata(arxiv_id: str) -> dict:
    """Fetch title, authors, summary, year, categories via arXiv API."""
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "LLM-Wiki-Agent/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        xml_data = resp.read()
    
    root = ET.fromstring(xml_data)
    entry = root.find("{http://www.w3.org/2005/Atom}entry")
    if entry is None:
        return {"error": f"No entry found for arXiv ID: {arxiv_id}"}
    
    title = entry.find("{http://www.w3.org/2005/Atom}title")
    title_text = re.sub(r"\s+", " ", title.text.strip()) if title is not None else ""
    
    summary = entry.find("{http://www.w3.org/2005/Atom}summary")
    summary_text = re.sub(r"\s+", " ", summary.text.strip()) if summary is not None else ""
    
    published = entry.find("{http://www.w3.org/2005/Atom}published")
    year = published.text[:4] if published is not None and published.text else ""
    
    authors = [
        author.find("{http://www.w3.org/2005/Atom}name").text
        for author in entry.findall("{http://www.w3.org/2005/Atom}author")
        if author.find("{http://www.w3.org/2005/Atom}name") is not None
    ]
    
    return {
        "arxiv_id": arxiv_id,
        "title": title_text,
        "authors": authors,
        "year": year,
        "abstract": summary_text,
        "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    }

def sanitize_filename(name: str) -> str:
    """Clean string to be safe for filenames."""
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    name = re.sub(r"\s+", " ", name)
    return name.strip()

def download_arxiv(query: str, target_dir: Path = RAW_PAPER_DIR) -> dict:
    """Download PDF from arXiv and return metadata and path."""
    target_dir.mkdir(parents=True, exist_ok=True)
    arxiv_id = parse_arxiv_id(query)
    meta = fetch_arxiv_metadata(arxiv_id)
    if "error" in meta:
        return meta

    # Format filename: [Year] FirstAuthor - Title or [ArXivID] Title
    first_author = meta["authors"][0].split()[-1] if meta["authors"] else "Unknown"
    short_title = meta["title"][:50].strip()
    filename = sanitize_filename(f"[{meta['year']}] {first_author} - {short_title} ({arxiv_id}).pdf")
    pdf_path = target_dir / filename

    pdf_url = meta["pdf_url"]
    req = urllib.request.Request(pdf_url, headers={"User-Agent": "LLM-Wiki-Agent/1.0"})
    print(f"Downloading from {pdf_url} to {pdf_path}...")
    with urllib.request.urlopen(req, timeout=30) as resp, open(pdf_path, "wb") as f:
        f.write(resp.read())

    meta["local_pdf_path"] = str(pdf_path)
    return meta

def extract_pdf_text(pdf_path: str, max_pages: int = 0) -> str:
    """Extract text from a PDF file."""
    reader = PdfReader(pdf_path)
    num_pages = len(reader.pages)
    limit = num_pages if max_pages <= 0 else min(num_pages, max_pages)
    
    extracted = []
    for i in range(limit):
        page_text = reader.pages[i].extract_text() or ""
        extracted.append(f"--- Page {i+1} ---\n{page_text}")
    
    return "\n\n".join(extracted)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python scripts/paper_utils.py download <arxiv_url_or_id>")
        print("  python scripts/paper_utils.py extract <pdf_path> [max_pages]")
        sys.exit(1)
    
    action = sys.argv[1].lower()
    arg = sys.argv[2]
    
    if action == "download":
        res = download_arxiv(arg)
        print(json.dumps(res, ensure_ascii=False, indent=2))
    elif action == "extract":
        pages = int(sys.argv[3]) if len(sys.argv) > 3 else 0
        text = extract_pdf_text(arg, pages)
        print(text[:4000] if len(text) > 4000 else text)
