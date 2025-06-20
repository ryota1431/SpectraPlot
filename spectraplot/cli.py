"""Command line interface for SpectraPlot."""

from __future__ import annotations

import argparse
from pathlib import Path

from .data_loader import load_spectrum
from .plotting import plot_spectrum, save_plot
from .analysis import smooth, find_peaks


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="SpectraPlot CLI")
    parser.add_argument("input", help="Input CSV or TSV file")
    parser.add_argument("--output", help="Path to save the plot")
    parser.add_argument("--show", action="store_true", help="Display the plot")
    parser.add_argument("--smooth", type=int, default=0, help="Apply moving average window")
    parser.add_argument("--find-peaks", action="store_true", help="Print peak indices")

    args = parser.parse_args(argv)

    df = load_spectrum(args.input)
    if args.smooth > 0:
        df["y"] = smooth(df["y"], window=args.smooth)

    fig = plot_spectrum(df, show=args.show)
    if args.output:
        save_plot(fig, args.output)

    if args.find_peaks:
        indices = find_peaks(df["y"])
        print("Peaks at indices:", indices)


if __name__ == "__main__":  # pragma: no cover
    main()
