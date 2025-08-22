import pytest
import pandas as pd
from covid19br.download import download_covid19

# Real-data test (integration style; may fail if network is down or URL changes)
def test_download_covid19_real_brazil():
    df = download_covid19(level="brazil")
    assert df is not None
    assert isinstance(df, pd.DataFrame)
    assert "date" in df.columns

def test_download_covid19_invalid_level():
    with pytest.raises(ValueError):
        download_covid19(level="invalid_level")

# Mock-based test (unit style, avoids network)
def test_download_covid19_mock(monkeypatch):
    # Prepare fake DataFrame
    fake_df = pd.DataFrame({"date": ["2021-01-01"], "accumCases": [100]})

    def fake_read_parquet(url):
        return fake_df

    monkeypatch.setattr(pd, "read_parquet", fake_read_parquet)

    df = download_covid19(level="brazil")
    assert df.equals(fake_df)
    assert "date" in df.columns

def test_download_covid19_import_error(monkeypatch):
    def fake_read_parquet(url):
        raise ImportError("pyarrow not installed")
    monkeypatch.setattr(pd, "read_parquet", fake_read_parquet)
    df = download_covid19(level="brazil")
    assert df is None

def test_download_covid19_oserror(monkeypatch):
    def fake_read_parquet(url):
        raise OSError("File not found")
    monkeypatch.setattr(pd, "read_parquet", fake_read_parquet)
    df = download_covid19(level="brazil")
    assert df is None

def test_download_covid19_valueerror(monkeypatch):
    def fake_read_parquet(url):
        raise ValueError("Invalid parquet file")
    monkeypatch.setattr(pd, "read_parquet", fake_read_parquet)
    df = download_covid19(level="brazil")
    assert df is None
