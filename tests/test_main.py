import pytest
import pandas as pd

def test_dataframe_creation():
    # Expected DataFrame
    expected_df = pd.DataFrame({"column_a": [1, 2, 3]})

    # Actual DataFrame
    actual_df = pd.DataFrame({"column_a": [1, 2, 3]})

    # Check if the actual DataFrame matches the expected DataFrame
    pd.testing.assert_frame_equal(actual_df, expected_df)
