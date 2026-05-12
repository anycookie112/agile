import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path.cwd()))

from src.remove_duplicates import remove_duplicates


def test_remove_duplicates(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    df = pd.DataFrame({
        "Name": ["Ali", "Siti", "Ali"],
        "Age": [20, 21, 20],
        "City": ["KL", "Penang", "KL"]
    })

    df.to_csv(input_file, index=False)

    cleaned_df = remove_duplicates(input_file, output_file)

    assert len(cleaned_df) == 2
    assert cleaned_df.duplicated().sum() == 0
    assert output_file.exists()
