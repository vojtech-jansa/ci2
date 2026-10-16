import sys


class Texter:
    def __init__(self, filename):
        self.filename = filename

    def run(self):
        with open(self.filename, encoding="utf-8") as file:
            text = file.read()
          
# Count blocks of text separated by empty lines.
        paragraph_count = 0
        in_paragraph = False

        for line in text.splitlines():
            if line.strip():
                if not in_paragraph:
                    paragraph_count += 1
                in_paragraph = True
            else:
                in_paragraph = False

        # Count spaces immediately following a dot.
        spaces_after_dot = text.count(". ")

        print("Number of paragraphs:", paragraph_count)
        print("Spaces after a dot:", spaces_after_dot)


if len(sys.argv) < 2:
    print("Usage: python texter.py <file_name>")
else:
    Texter(sys.argv[1]).run()
