import sys
import glob
import subprocess
from pathlib import Path
from html import escape


def find_cdxml_files(arguments):
    files = []

    for argument in arguments:
        matches = glob.glob(argument)

        for match in matches:
            path = Path(match)

            if path.is_file() and path.suffix.lower() == ".cdxml":
                files.append(path)

    return list(dict.fromkeys(files))


def get_formula(cdxml_file):
    result = subprocess.run(
        ["obabel", str(cdxml_file), "-oreport"],
        capture_output=True,
        text=True
    )

    for line in result.stdout.splitlines():
        if line.startswith("FORMULA:"):
            return line.split(":", 1)[1].strip()

    return "Unknown"


def create_png(cdxml_file):
    png_file = cdxml_file.with_suffix(".png")

    subprocess.run(
        ["obabel", str(cdxml_file), "-O", str(png_file)],
        check=True
    )

    return png_file


def create_html(molecules, output_file="index.html"):
    rows = []

    for molecule in molecules:
        row = f"""
        <tr>
            <td>{escape(molecule["filename"])}</td>
            <td>{escape(molecule["formula"])}</td>
            <td>
                <img src="{escape(molecule["png"])}"
                     alt="{escape(molecule["filename"])}">
            </td>
        </tr>
        """

        rows.append(row)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CDXML molecules</title>
</head>

<body>

<h1>Molecular structures</h1>

<table border="1">
    <tr>
        <th>filename</th>
        <th>formula</th>
        <th>2D structure</th>
    </tr>

    {''.join(rows)}

</table>

</body>
</html>
"""

    Path(output_file).write_text(
        html_content,
        encoding="utf-8"
    )


def main(arguments):
    cdxml_files = find_cdxml_files(arguments)

    if not cdxml_files:
        print("No CDXML files found.")
        return

    molecules = []

    for cdxml_file in cdxml_files:
        formula = get_formula(cdxml_file)
        png_file = create_png(cdxml_file)

        molecule_data = {
            "filename": cdxml_file.name,
            "formula": formula,
            "png": png_file.name
        }

        molecules.append(molecule_data)

        print(cdxml_file.name, formula, png_file.name)

    create_html(molecules)

    print("Created index.html")


if __name__ == "__main__":
    main(sys.argv[1:])