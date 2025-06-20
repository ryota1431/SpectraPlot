"""Data loading utilities for SpectraPlot."""

from __future__ import annotations

import pandas as pd
from pathlib import Path


def load_spectrum(path: str | Path) -> pd.DataFrame:
    """Load a spectrum from a CSV or TSV file.

    Parameters
    ----------
    path:
        Path to the data file. The first column should contain the x-axis
        values (wavelength or frequency) and the second column the intensity.

    Returns
    -------
    pandas.DataFrame
        DataFrame with columns ``x`` and ``y``.
    """
    file_path = Path(path)
    if file_path.suffix.lower() in {".tsv", ".txt"}:
        df = pd.read_csv(file_path, sep="\t", header=None, names=["x", "y"])
    else:
        df = pd.read_csv(file_path, header=None, names=["x", "y"])
    return df
