"""SpectraPlot package."""

from .data_loader import load_spectrum
from .plotting import plot_spectrum, save_plot
from .analysis import smooth, find_peaks

__all__ = [
    "load_spectrum",
    "plot_spectrum",
    "save_plot",
    "smooth",
    "find_peaks",
]


def main(argv=None):
    from .cli import main as cli_main
    cli_main(argv)

if __name__ == "__main__":  # pragma: no cover
    main()
