import sys
from bs4 import BeautifulSoup


def parse_molbase(filename):
    with open(filename, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    compounds = soup.find_all("h3", title=True)

    for compound in compounds:
        print(compound["title"].strip())


def main(args):
    if len(args) != 2:
        print(f"Usage: python {args[0]} <html_file>", file=sys.stderr)
        return 1

    parse_molbase(args[1])
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))