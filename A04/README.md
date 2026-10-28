# A04 – SQLite World Database

This program creates an SQLite database from CSV files from the World dataset and answers the assigned database question.

## Requirements

- Python 3
- No external Python packages are required.

The program uses only modules from the Python standard library:

- `csv`
- `os`
- `sqlite3`
- `sys`

## Clone the repository

Clone the repository using Git:

```bash
git clone https://github.com/vojtech-jansa/ci2
```

Enter the repository directory:

```bash
cd ci2
```

Then enter the A04 directory:

```bash
cd A04
```

## Running the program

On the first run, provide the CSV files as command-line arguments:

```bash
py db.py city.csv country.csv countrylanguage.csv
```

The program creates a database file named `db.sqlite`.

Each CSV file is imported into a table whose name corresponds to the CSV filename without the `.csv` extension.

For example:

- `city.csv` creates the table `city`
- `country.csv` creates the table `country`
- `countrylanguage.csv` creates the table `countrylanguage`

If a table already exists, it is not recreated.

After the database has been created, the program can also be executed without arguments:

```bash
py db.py
```

## Assigned question

Question 4:

**In what countries is used the Spanish language? Provide their full names, sorted alphabetically.**

The program joins the `country` and `countrylanguage` tables and prints the matching country names sorted alphabetically.