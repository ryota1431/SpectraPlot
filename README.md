# SpectraPlot

SpectraPlot is a simple tool for loading, visualising and analysing spectral data stored in CSV or TSV files.

## Features

- Load CSV and TSV files containing wavelength/frequency and intensity data
- Plot spectra using Matplotlib
- Save graphs to common image formats (PNG, JPEG)
- Basic peak finding and smoothing operations
- Command line interface for quick access

## Installation

```
pip install -r requirements.txt
```

## Usage

Load a data file and display a plot:

```
python -m spectraplot path/to/data.csv --show
```

Save a plot to an image:

```
python -m spectraplot path/to/data.csv --output graph.png
```

Run tests:

```
pytest
```
