import pandas as pd
import glob

def load_data():
    file_paths = glob.glob('../data/*.csv')
    if not file_paths:
        raise ValueError("No CSV files found in the 'data' directory.")
    pd.set_option('display.float_format', '{:.2f}'.format)
    df_list = [pd.read_csv(file) for file in file_paths]
    data = pd.concat(df_list, ignore_index=True)
    return data