import pandas as pd
from sisyphus.agents.base import NarrowTaskAgent

class DataCleaningAgent(NarrowTaskAgent):
    """
    A Narrow Task AI Agent dedicated to cleaning data within a DataFrame.
    """

    def __init__(self, name):
        super().__init__(name, task="Data Cleaning")

    def clean_data(self, df):
        """
        Perform a series of data cleaning operations on the provided DataFrame.

        :param df: A Pandas DataFrame containing the data to be cleaned.
        :return: A cleaned Pandas DataFrame.
        """
        cleaned_df = df.copy()

        # Remove duplicate rows
        cleaned_df.drop_duplicates(inplace=True)

        # Handle missing values (example: fill with median for numerical columns)
        for col in cleaned_df.select_dtypes(include=['float64', 'int64']).columns:
            cleaned_df[col].fillna(cleaned_df[col].median(), inplace=True)

        # Example normalization (adjust based on your needs)
        for col in cleaned_df.select_dtypes(include=['float64', 'int64']).columns:
            cleaned_df[col] = (cleaned_df[col] - cleaned_df[col].mean()) / cleaned_df[col].std()

        return cleaned_df

    def evaluate_performance(self, original_data, cleaned_data):
        """
        Evaluate the cleaning performance. This can be subjective based on the task's requirements.

        :param original_data: The original DataFrame before cleaning.
        :param cleaned_data: The cleaned DataFrame to evaluate.
        :return: A performance metric or message.
        """
        # Placeholder for actual evaluation logic
        # In a real scenario, this could involve checking for data consistency, 
        # the absence of outliers, correct data types, etc.
        if not cleaned_data.isnull().values.any():
            return "Cleaning successful: No missing values."
        else:
            return "Cleaning unsuccessful: Missing values detected."