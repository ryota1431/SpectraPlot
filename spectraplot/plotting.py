"""Plotting utilities."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


def plot_spectrum(df: pd.DataFrame, show: bool = True, **kwargs) -> plt.Figure:
    """Plot the spectrum contained in ``df``."""
    fig, ax = plt.subplots()
    ax.plot(df["x"], df["y"], **kwargs)
    ax.set_xlabel("X")
    ax.set_ylabel("Intensity")
    ax.grid(True)
    if show:
        plt.show()
    return fig


def save_plot(fig: plt.Figure, path: str | Path) -> None:
    """Save ``fig`` to ``path``."""
    fig.savefig(Path(path))
