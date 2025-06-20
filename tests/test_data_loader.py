import pandas as pd
from spectraplot.data_loader import load_spectrum


def test_load_csv(tmp_path):
    p = tmp_path / "data.csv"
    p.write_text("1,2\n3,4\n")
    df = load_spectrum(p)
    assert list(df.columns) == ["x", "y"]
    assert df.shape == (2, 2)
    assert df["x"].iloc[0] == 1
    assert df["y"].iloc[1] == 4
