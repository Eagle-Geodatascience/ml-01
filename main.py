from typing import List
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def data_preparation(file_name: str, cols: List[str]) -> pd.DataFrame:
    """Data Preparation
    - Reads data from a CSV file.
    - Assigns column names to the DataFrame.
    - Maps class labels 'g' to 0 and 'h' to 1.
    
    Args:
        file_name (str): The path to the CSV file containing the data.
        cols (List[str]): List of column names.
    
    Returns:
        pd.DataFrame: A DataFrame containing the prepared data.
    """
    df = pd.read_csv(file_name, names=cols)
    df['class'] = df['class'].map({'g': 0, 'h': 1})
    return df


def explore_data(df: pd.DataFrame, label_column: str, numeric_columns: List[str]):
    """Explore data by plotting histograms for numeric columns by class label.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        label_column (str): The name of the class label column.
        numeric_columns (List[str]): List of numeric column names to plot.
    """
    for label in numeric_columns:
        plt.hist(df[df[label_column] == 1][label], color='blue', label='Hadron', alpha=0.7, density=True)
        plt.hist(df[df[label_column] == 0][label], color='red', label='Gamma', alpha=0.7, density=True)
        plt.xlabel(label)
        plt.ylabel('Probability')
        plt.legend()
        plt.show()


def main():
    # Specify the data file path & Define column names
    file_name = 'data/magic04.data'  # Adjust the file path as needed
    cols = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]

    # Call the data_preparation function
    df = data_preparation(file_name, cols)

    # List of numeric columns to explore
    numeric_columns = cols[:-1]  # All columns except the last one (class)

    # Explore data by plotting histograms for numeric columns
    explore_data(df, label_column='class', numeric_columns=numeric_columns)

    # Perform Tain, Validation, Test Datasets


if __name__ == "__main__":
    main()
