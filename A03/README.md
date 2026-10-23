# A03 – Molbase parser

This assignment parses the first page of Molbase search results for `benzidine` using Python and BeautifulSoup.

The script reads the HTML filename from the first command-line argument and prints the values of the `title` attributes of all `h3` elements, one compound name per line.

## Files

- `molbase_benzidine.html` – saved HTML source of the Molbase search results
- `molbase_parser.py` – parser script
- `requirements.txt` – required Python packages

## Installation and usage

Clone the repository:

```bash
git clone https://github.com/vojtech-jansa/ci2.git
cd ci2/A03
```

Create a virtual environment:

```bash
py -m venv .venv
```

Activate the virtual environment in Windows PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

Run the script:

```bash
python molbase_parser.py molbase_benzidine.html
```
