import numpy as np

def clean_data(data):
     # Drop the 'Comments' column if it is entirely null
    if data['Comments'].isnull().all():
        data = data.drop(columns=['Comments'])
    
    # Handle missing values
    # For numeric columns, you can choose to fill missing values with the mean, median, or drop them
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    data[numeric_columns] = data[numeric_columns].apply(lambda x: x.fillna(x.median()))
    
    # Handle anomalies (e.g., negative values where only positive values should exist)
    # Replace negative values with NaN and then handle them
    columns_with_anomalies = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'Tamb', 'RH', 'WS', 'WSgust', 'BP']
    for col in columns_with_anomalies:
        data[col] = data[col].apply(lambda x: np.nan if x < 0 else x)
    
    # Reapply missing value handling after addressing anomalies
    data[numeric_columns] = data[numeric_columns].apply(lambda x: x.fillna(x.median()))
    
    # Drop any rows with remaining NaN values if necessary
    data = data.dropna()

    return data
