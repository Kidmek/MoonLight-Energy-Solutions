import numpy as np
import pandas as pd
from scipy.stats import zscore

def summary_statistics(data):
    return data.describe().T

def data_quality_check(data):
    missing_values = data.isnull().sum()
    z_scores = np.abs(zscore(data.select_dtypes(include=[np.number])))
    outliers = (z_scores > 3).sum()

    # Check for negative values where only positive values should exist
    # Define columns that should only have positive values
    positive_columns = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']
    
    # Initialize a dictionary to store negative value counts
    negative_values = {}
    
    for column in positive_columns:
        if column in data.columns:
            negative_count = (data[column] < 0).sum()
            negative_values[column] = negative_count
    
    # Create a DataFrame to display all metrics
    quality_summary = pd.DataFrame({
        'Missing Values': missing_values,
        'Outliers': outliers,
        'Negative Values': pd.Series(negative_values)
    }).fillna(0)  # Fill NaN values with 0 for columns that might not be in `negative_values`
    
    return quality_summary.astype(int)

def z_score_analysis(data, threshold=3):
    # Select numeric columns for Z-score analysis
    numeric_data = data.select_dtypes(include=[np.number])
    
    # Calculate Z-scores
    z_scores = zscore(numeric_data)
    z_scores_df = pd.DataFrame(z_scores, columns=numeric_data.columns,index=data.index)
    outliers = (np.abs(z_scores_df) > threshold)
    outlier_rows = data[outliers.any(axis=1)]
    return outlier_rows

