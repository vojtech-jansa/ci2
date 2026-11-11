"""Plot the x and y columns of a CSV file."""

import argparse
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np


def plot_graph(csv_path, output_path):
    """Read the CSV and save its plot as a PNG."""
    data = np.genfromtxt(csv_path, delimiter=",", names=True)
    fig, ax = plt.subplots(figsize=(8, 5), layout="constrained")
    try:
        ax.plot(data["x"], data["y"], marker="o", markersize=4)
        ax.set(xlabel="x", ylabel="y", title="Reciprocal function  y = 1/x")
        ax.set_xticks([1, 5, 10, 15, 20])
        ax.grid(alpha=0.3)
        fig.savefig(output_path, dpi=150)
    finally:
        plt.close(fig)


def main(argv):
    """Parse the input and output paths and generate the plot."""
    assignment_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="?", type=Path, default=assignment_dir / "graph.csv")
    parser.add_argument("output", nargs="?", type=Path, default=assignment_dir / "graph.png")
    args = parser.parse_args(argv)
    plot_graph(args.csv, args.output)


if __name__ == "__main__":
    main(sys.argv[1:])
