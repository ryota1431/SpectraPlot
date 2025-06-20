import pandas as pd
from spectraplot.analysis import smooth, find_peaks


def test_smooth():
    s = pd.Series([0, 2, 4, 2, 0])
    result = smooth(s, window=3)
    assert len(result) == 5
    assert abs(result.iloc[2] - 8/3) < 1e-6


def test_find_peaks():
    s = pd.Series([0, 1, 0, 2, 0])
    peaks = find_peaks(s)
    assert list(peaks) == [1, 3]
