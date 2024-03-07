import pandas as pd
import pytest
from sisyphus.agents.data_cleaning_agent import DataCleaningAgent

def generate_sample_data():
    """Generate a simple DataFrame with some duplicate rows, missing values, and a need for normalization."""
    data = {
        'Feature1': [1, 2, 2, 4, 5, pd.NA],
        'Feature2': [3, 4, 4, 2, 1, 8],
        'Feature3': [pd.NA, pd.NA, 2, 4, 5, 6]
    }
    return pd.DataFrame(data)

def test_data_cleaning():
    df = generate_sample_data()
    agent = DataCleaningAgent(name='TestCleaner')
    cleaned_df = agent.clean_data(df)

    # Test if duplicates were removed
    assert cleaned_df.duplicated().sum() == 0, "Duplicates were not removed"

    # Test if missing values were handled
    assert cleaned_df.isnull().sum().sum() == 0, "Missing values were not handled"

    # Test normalization (or other cleaning steps) as needed
    # For example, check if feature means are approximately 0 after normalization

@pytest.fixture
def agent():
    return DataCleaningAgent(name='TestAgent')

def test_evaluate_performance(agent):
    original_data = generate_sample_data()
    cleaned_data = agent.clean_data(original_data)
    result = agent.evaluate_performance(original_data, cleaned_data)
    assert "successful" in result, "Data cleaning was not successful according to evaluate_performance"