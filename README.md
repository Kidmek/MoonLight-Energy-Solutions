# Exploratory Data Analysis (EDA) Notebook

This Jupyter Notebook is designed to perform an in-depth Exploratory Data Analysis (EDA) on a dataset containing various environmental measurements, including solar irradiance, temperature, humidity, wind speed, and more. The notebook is structured into several code blocks, each serving a specific purpose in the analysis process.

## Project Structure

### 1. Import Scripts

The first block of the notebook imports all necessary scripts and libraries required for the analysis. This includes libraries for data manipulation, visualization, and custom scripts for specific tasks.

### 2. Load Data

The second block loads the dataset into the notebook. The data includes columns such as Timestamp, GHI, DNI, DHI, ModA, ModB, Tamb, RH, WS, WSgust, WD, BP, and others. This data is then prepared for analysis in the subsequent blocks.

### 3. Summary Statistics

This block calculates key statistical measures for each numeric column, including:

- Mean
- Median
- Standard Deviation
- Other relevant statistics

These measures help in understanding the data distribution and provide insights into the central tendency and variability of the data.

### 4. Data Quality Check

This block checks for data quality issues, including:

- Missing values
- Outliers
- Incorrect entries (e.g., negative values in columns where only positive values should exist)

The focus is particularly on columns like GHI, DNI, DHI, ModA, ModB, WS, and WSgust.

### 5. Time Series Analysis

In this block, time series analysis is performed by plotting line graphs or area plots for key variables over time. This includes:

- Observing patterns by month
- Trends throughout the day
- Anomalies such as peaks in solar irradiance or temperature fluctuations

Additionally, the impact of cleaning activities on sensor readings (ModA, ModB) is evaluated over time.

### 6. Correlation Analysis

This block uses heatmaps and pair plots to visualize correlations between different variables. The analysis focuses on:

- Solar radiation components (GHI, DNI, DHI) and temperature measures (TModA, TModB)
- Relationship between wind conditions (WS, WSgust, WD) and solar irradiance

### 7. Wind Analysis

In this block, polar plots are used to analyze wind data. The plots show:

- Distribution of wind speed and direction
- Variability in wind direction
- Identification of trends and significant wind events

### 8. Temperature Analysis

This block examines how relative humidity (RH) influences temperature readings and solar radiation, providing insights into the relationship between these variables.

### 9. Histograms

Histograms are created in this block for variables like GHI, DNI, DHI, WS, and temperature. These plots help visualize the frequency distribution of these variables.

### 10. Z-Score Analysis

This block calculates Z-scores to identify data points that deviate significantly from the mean. Z-score analysis is useful for flagging potential outliers.

### 11. Bubble Charts

In this block, bubble charts are created to explore complex relationships between variables, such as:

- GHI vs. Tamb vs. WS
- Bubble size representing an additional variable like RH or BP (Barometric Pressure)

### 12. Data Cleaning

The final block focuses on data cleaning. Based on the initial analysis, this block handles anomalies and missing values, especially in columns like `Comments` that may be entirely null. The cleaning process ensures the dataset is ready for further analysis or modeling.

## How to Use

1. **Clone the repository**: Clone the repository to your local machine to access the notebook and data files.
2. **Run the Notebook**: Open the notebook in Jupyter and execute each block sequentially to perform the analysis.
3. **Customize the Analysis**: Modify the code blocks as needed to adapt the analysis to your specific dataset or research questions.

## Requirements

- Python 3.x
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Windrose (for wind analysis)

Ensure all dependencies are installed before running the notebook.
