---
name: pandoc
description: Universal document converter using pandoc. Convert between any supported formats including markdown, docx, html, pdf, latex, epub, rst, and many more.
triggers:
  - convert to
  - convert this
  - pandoc
  - export as
---

# Pandoc Document Converter

Universal document converter supporting 50+ formats.

## Quick Reference

```bash
# Basic conversion (auto-detect from extensions)
pandoc input.docx -o output.md

# Specify formats explicitly
pandoc input.txt --from docx --to markdown -o output.md
pandoc input.md --to pdf -o output.pdf

# Extract media (images) from document
pandoc input.docx -o output.md --extract-media=./media

# List all supported formats
pandoc --list-input-formats
pandoc --list-output-formats
```

## Common Formats

**Documents:** markdown, docx, html, pdf, latex, epub, rst, odt, rtf, txt  
**Code/Data:** json, yaml, csv, tsv  
**Web:** html, xhtml  
**Markup:** asciidoc, org, textile, mediawiki  
**Books:** epub, fb2

## Key Options

| Option | Description |
|--------|-------------|
| `-f`, `--from` | Input format |
| `-t`, `--to` | Output format |
| `-o` | Output file |
| `--extract-media=DIR` | Extract images to directory |
| `--wrap=none` | Don't wrap lines |
| `--standalone` | Full document with headers |
| `--toc` | Add table of contents |
| `--pdf-engine=ENGINE` | xelatex, pdflatex, lualatex, wkhtmltopdf |
| `-V KEY=VAL` | Set template variable |
| `--resource-path=PATH` | Search path for images/resources |

## Usage Examples

### Document Conversions

```bash
# Word to Markdown with images
pandoc report.docx -o report.md --extract-media=./images

# Markdown to PDF (requires LaTeX)
pandoc README.md -o README.pdf --pdf-engine=xelatex

# Markdown to standalone HTML
pandoc doc.md -o doc.html --standalone --toc

# HTML to Word
pandoc page.html -o page.docx

# Multiple files to one PDF
pandoc chapter1.md chapter2.md chapter3.md -o book.pdf
```

### Working with Images

```bash
# Extract all images from Word document
pandoc input.docx -o output.md --extract-media=./extracted_images

# Convert with specific image handling
pandoc input.docx -o output.md \
  --extract-media=./media \
  --resource-path=./media
```

### Advanced Options

```bash
# Custom CSS for HTML output
pandoc input.md -o output.html --css=style.css

# Set metadata
pandoc input.md -o output.pdf -V geometry:margin=1in -V fontsize=12pt

# Filters (e.g., citeproc for citations)
pandoc input.md -o output.pdf --filter=pandoc-citeproc

# From stdin to stdout
cat file.md | pandoc -f markdown -t html > file.html
```

## Installation

```bash
# macOS
brew install pandoc

# Ubuntu/Debian
sudo apt-get install pandoc

# Windows
choco install pandoc
# or
winget install JohnMacFarlane.Pandoc

# For PDF output, also install LaTeX:
# macOS: brew install --cask mactex-no-gui
# Ubuntu: sudo apt-get install texlive-xetex
```

## Best Practices

1. **Use file extensions** - Pandoc auto-detects formats from extensions
2. **Extract media** - Always use `--extract-media` when images matter
3. **Specify formats** - Use `-f`/`-t` when auto-detection might fail
4. **PDF engines** - Use `xelatex` for better Unicode/font support
5. **No wrap** - Use `--wrap=none` for cleaner diffs in version control

## Common Issues

| Problem | Solution |
|---------|----------|
| "pdf-engine not found" | Install LaTeX (texlive/mactex) |
| Images not showing | Use `--extract-media` + `--resource-path` |
| Encoding issues | Use `--from` to specify input encoding |
| Missing fonts | Install fonts or use `--pdf-engine=xelatex` |

## See Also

- Full manual: https://pandoc.org/MANUAL.html
- Try online: https://pandoc.org/try/
