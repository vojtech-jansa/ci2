# A05 – CDXML to HTML

This assignment contains a Python script `cdx2html.py` that processes ChemDraw `.cdxml` files.

For every `.cdxml` file given as a command-line argument, the script:

- converts the molecular structure to a `.png` image using Open Babel,
- obtains the molecular formula,
- creates an `index.html` file containing a table with the columns:
  - `filename`
  - `formula`
  - `2D structure`

The generated PNG files have the same base filename as the corresponding CDXML files.

## Requirements

- Python 3
- Open Babel command-line program (`obabel`)
- Git

The Open Babel installation must support the `cdxml` input format and the `png` output format.

The installation can be checked with:

```bash
obabel -V
obabel -L formats
```

On Windows, the following commands can be used to check the required formats:

```cmd
obabel -L formats | findstr /I cdxml
obabel -L formats | findstr /I png
```

## Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd ci2
```

Replace https://github.com/vojtech-jansa/ci2 with the URL of this GitHub repository.

## Create a virtual environment

### Windows

```cmd
py -m venv .venv
```

Activate it in Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install Python requirements

```bash
pip install -r A05/requirements.txt
```

No additional Python packages are required for this assignment. The script uses the separately installed Open Babel command-line program.

## Run the script

Move to the assignment folder:

```bash
cd A05
```

Run the script for all CDXML files:

```bash
python cdx2html.py "*.cdxml"
```

On Windows, if Python is available through the `py` launcher, the following command can also be used:

```cmd
py cdx2html.py "*.cdxml"
```

The script creates a PNG image for every CDXML file and generates:

```text
index.html
```

Open `index.html` in a web browser to view the table containing the filename, molecular formula, and 2D structure of each molecule.

## Files

The `A05` folder contains:

- `cdx2html.py` – Python script
- `requirements.txt` – Python dependency file
- `index.html` – generated HTML page
- `.cdxml` files – input ChemDraw structures
- `.png` files – generated 2D molecular structure images