"""
Generals methods to works with DataFrames (so far).
"""

from math import prod
import pandas as pd


def df_initial_analysis(df, name_df):
    """
    Initial analysis on the DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame to analyze.
        name_df (str): DataFrame name.

    Returns:
        None.
        Print the initial analysis on the DataFrame. 
    """
    if df.empty:
        print("The", name_df, "dataset is empty. Please verify the file.")
    else:
        empty_cols = [col for col in df.columns if df[col].isna().all()]
        df_rows_duplicates = df[df.duplicated()]
        
        print("The", name_df, "dataset shape is:", df.shape[0], "rows &", df.shape[1], "columns")
        print("Total of NaN values in the", name_df, "dataset is:", df.isna().sum().sum())
        print("Percentage of NaN values in the", name_df, "dataset is:", 
                round((df.isna().sum().sum() / prod(df.shape)) * 100, 2), "%")
        print("There are", df_rows_duplicates.shape[0], "full duplicates rows")
        print("There are", len(empty_cols), "empty columns")
        if len(empty_cols) != 0:
            print("   The empty columns are:", empty_cols)
        print("------------------------------------------------------------------------\n")
        print("Number of values/records per columns in", name_df, "dataset")
        print(df.count().sort_values(ascending=False))



def remove_empty_columns(df):
    """
    Remove empty columns in DataFramte.

    Args:
        df (pandas.DataFrame): DataFrame to remove empty columns.

    Returns:
        df (pandas.DataFrame): DataFrame withou empty columns.
    """
    empty_cols = [col for col in df.columns if df[col].isna().all()]
    for col in df.columns:
        for empty_col in empty_cols:
            if col == empty_col:
                df = df.drop([col], axis=1)
    return df

        