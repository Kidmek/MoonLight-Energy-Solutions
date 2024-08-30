import matplotlib.pyplot as plt
import streamlit as st_plt
import pandas as pd
import seaborn as sns
from windrose import WindroseAxes

def plot_time_series(data, columns, timestamp_col='Timestamp',st=False):
    data[timestamp_col] = pd.to_datetime(data[timestamp_col])
    plt.figure(figsize=(14, 7))
    for column in columns:
        plt.plot(data[timestamp_col], data[column], label=column)
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.title('Time Series Analysis')
    plt.legend(loc='upper center')
    if(st):
        st_plt.pyplot(plt)
    else:
        plt.show()

def correlation_analysis(data,st=False):
    plt.figure(figsize=(10, 8))

    # Plot the heatmap
    solar_radiation = ['GHI', 'DNI', 'DHI']
    temperature_measures = ['TModA', 'TModB']

    # Create a DataFrame for the correlations between the solar radiation and temperature measures
    correlation_matrix = pd.DataFrame(index=solar_radiation, columns=temperature_measures)

    # Compute the correlation between each solar radiation component and each temperature measure
    for sr in solar_radiation:
        for tm in temperature_measures:
            correlation_matrix.loc[sr, tm] = data[sr].corr(data[tm])

    # Plot the heatmap
    sns.heatmap(correlation_matrix.astype(float), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap: Solar Radiation vs. Temperature Measures')
    if(st):
        st_plt.pyplot(plt)
    else:
        plt.show()


def wind_analysis(data, speed_col='WS', direction_col='WD',st=False):
    ax = WindroseAxes.from_ax()
    ax.bar(data[direction_col], data[speed_col], normed=True, opening=0.8, edgecolor='white')
    ax.set_legend()
    plt.title('Windrose: Wind Speed and Direction')
    if(st):
        st_plt.pyplot(plt)
    else:
        plt.show()

def temp_analysis(data,st=False):
    cols = ['RH', 'Tamb', 'GHI', 'DNI', 'DHI']
    correlation_matrix = data[cols].corr()
    
    # Plot heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap with RH')
    if(st):
        st_plt.pyplot(plt)
    else:
        plt.show()

def histogram(data,st=False):
     # Define the variables and their labels
    variables = {
        'GHI': 'Global Horizontal Irradiance (W/m²)',
        'DNI': 'Direct Normal Irradiance (W/m²)',
        'DHI': 'Diffuse Horizontal Irradiance (W/m²)',
        'WS': 'Wind Speed (m/s)',
        'Tamb': 'Ambient Temperature (°C)'
    }
    
    # Set up the figure and axes in a column
    num_vars = len(variables)
    fig, axes = plt.subplots(num_vars, 1, figsize=(10, 5 * num_vars), sharex=False, sharey=False)
    
    for i, (var, label) in enumerate(variables.items()):
        ax = axes[i]
        ax.hist(data[var].dropna(), bins=30, edgecolor='k', alpha=0.7)
        ax.set_ylabel('Frequency')
        ax.set_xlabel(label)
        ax.set_title(f'Histogram of {label}')
    
    plt.tight_layout()
    if(st):
        st_plt.pyplot(plt)
    else:
        plt.show()

def bubble_chart(data, x_var, y_var, size_var, color_var=None,st=False):
    plt.figure(figsize=(10, 6))
    
    # Create the bubble chart
    sns.scatterplot(
        x=data[x_var],
        y=data[y_var],
        size=data[size_var],
        hue=data[color_var] if color_var else data[size_var],
        sizes=(20, 500),
        alpha=0.6,
        palette='coolwarm',
        edgecolor='w',
        linewidth=0.5
    )
    
    plt.title(f'{y_var} vs {x_var} with bubble size representing {size_var}')
    plt.xlabel(x_var)
    plt.ylabel(y_var)
    plt.legend(title=size_var, bbox_to_anchor=(1.05, 1), loc='upper left')
    if(st):
        st_plt.pyplot(plt)
    else:
        plt.show()
