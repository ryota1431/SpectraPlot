"""Analysis utilities."""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.signal import find_peaks as _find_peaks


def smooth(y: pd.Series, window: int = 5) -> pd.Series:
    """Return a moving average of the data."""
    if window < 1:
        raise ValueError("window must be >= 1")
    return y.rolling(window=window, center=True, min_periods=1).mean()


def find_peaks(y: pd.Series, height: float | None = None) -> np.ndarray:
    """Find peaks in ``y`` using scipy.signal.find_peaks."""
    peaks, _ = _find_peaks(y.values, height=height)
    return peaks
