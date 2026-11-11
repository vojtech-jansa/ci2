# A06 – Reciprocal function

Variant 4 plots `y = 1/x`. The file `graph.csv` contains the columns `x` and `y` and 20 data rows for integer values of `x` from 1 through 20. The script reads the CSV with NumPy and saves the plot with Matplotlib.

## Clone the repository

```bash
git clone https://github.com/vojtech-jansa/ci2.git
cd ci2/A06
```

## Create and activate a virtual environment

On Windows (Command Prompt):

```cmd
py -m venv .venv
.venv\Scripts\activate.bat
```

On Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install the dependencies and generate the graph

```bash
python -m pip install -r requirements.txt
python graph.py
```

Open `graph.png` to verify that the curve decreases from `y = 1` at `x = 1` to `y = 0.05` at `x = 20`.
