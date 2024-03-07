import pandas as pd
from sisyphus.agents.base import NarrowTaskAgent

class DataCleaningAgent(NarrowTaskAgent):
    """
    A Narrow Task AI Agent dedicated to cleaning data within a DataFrame.
    """

    def __init__(self, name, task_specific_parameter=None):
        super().__init__(name, task="Data Cleaning", task_specific_parameter=task_specific_parameter)

    
    def clean_data(self, df):
        """
        Perform a series of data cleaning operations on the provided DataFrame.

        :param df: A Pandas DataFrame containing the data to be cleaned.
        :return: A cleaned Pandas DataFrame.
        """
        cleaned_df = df.copy()

        # Remove duplicate rows
        cleaned_df.drop_duplicates(inplace=True)

        # Handle missing values
        for col in cleaned_df.columns:
            if cleaned_df[col].dtype in ['float64', 'int64']:
                cleaned_df[col].fillna(cleaned_df[col].median(), inplace=True)
            else:
                cleaned_df[col].fillna(cleaned_df[col].mode()[0], inplace=True)

        # Normalize numerical columns
        for col in cleaned_df.select_dtypes(include=['float64', 'int64']).columns:
            column_mean = cleaned_df[col].mean()
            column_std = cleaned_df[col].std()
            if column_std > 0:
                cleaned_df[col] = (cleaned_df[col] - column_mean) / column_std
            else:
                # Set normalized values to 0 (or another value) if std is 0
                cleaned_df[col] = 0

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