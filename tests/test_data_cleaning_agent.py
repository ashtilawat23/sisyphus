import pandas as pd
import pytest
from sisyphus.agents.data_cleaning_agent import DataCleaningAgent

def generate_sample_data():
    """Generate a DataFrame with explicit duplicate rows, missing values, and values needing normalization."""
    data = {
        'Feature1': [1, 2, 2, 2, 4, 5, 5],  # Include an explicit duplicate (row 1 and 3, considering 0-based indexing)
        'Feature2': [3, 4, 4, 4, 2, 1, 1],  # Duplicate in 'Feature2' as well
        'Feature3': [1, 2, 2, 2, 4, 5, pd.NA]  # Include a missing value in the last row
    }
    return pd.DataFrame(data)

@pytest.fixture
def agent():
    # Assuming 'task_specific_parameter' is not required or has been handled in your implementation
    return DataCleaningAgent(name='TestAgent')

def test_data_cleaning(agent):
    df = generate_sample_data()
    cleaned_df = agent.clean_data(df)

    # Test if duplicates were removed
    assert cleaned_df.duplicated().sum() == 0, "Duplicates were not removed"

    # Test if missing values were handled
    assert cleaned_df.isnull().sum().sum() == 0, "Missing values were not handled"

    # Test normalization for numerical columns
    for col in cleaned_df.select_dtypes(include=['float64', 'int64']).columns:
        mean = cleaned_df[col].mean()
        std = cleaned_df[col].std()
        assert mean.round(decimals=6) == 0, f"{col} mean is not 0 after normalization"
        assert std.round(decimals=6) == 1, f"{col} std deviation is not 1 after normalization"

def test_evaluate_performance(agent):
    original_data = generate_sample_data()
    cleaned_data = agent.clean_data(original_data)
    result = agent.evaluate_performance(original_data, cleaned_data)
    assert "successful" in result, "Data cleaning was not successful according to evaluate_performance"
