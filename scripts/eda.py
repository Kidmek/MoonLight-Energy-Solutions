from data_loading import load_data
from analysis import summary_statistics, data_quality_check, z_score_analysis
from visualization import plot_time_series, correlation_analysis, wind_analysis,temp_analysis,histogram
from data_cleaning import clean_data

def main():
    # Load the data
    data = load_data()

    # Perform summary statistics
    # print("##############################################################")
    # summary_stats = summary_statistics(data)
    # print("Summary Statistics:\n", summary_stats)
    # print("##############################################################")

    # Data quality check
    # print("##############################################################")
    # missing_values, outliers = data_quality_check(data)
    # print("Missing Values:\n", missing_values)
    # print("Outliers:\n", outliers)
    # print("##############################################################")

    # Plot time series
    # print("Time series visualization")
    # plot_time_series(data, ['GHI', 'DNI', 'DHI', 'Tamb'])
    # print("##############################################################")


    # Correlation analysis
    # print("Correlation analysis visualization")
    # correlation_analysis(data)
    # print("##############################################################")

    # Wind analysis
    # print("Wind analysis visualization")
    # wind_analysis(data)
    # print("##############################################################")

    # Temperature analysis
    # print("Temperature analysis visualization")
    # temp_analysis(data)
    # print("##############################################################")

    # Histogram
    # print("Histogram")
    # histogram(data)
    # print("##############################################################")

    # Z-score analysis
    print("##############################################################")
    anomalies = z_score_analysis(data)
    print("Anomalies detected:\n", anomalies)
    print("##############################################################")

    # Clean data
    # data_cleaned = clean_data(data)
    # print("Data cleaned. Rows remaining:", len(data_cleaned))

if __name__ == "__main__":
    main()
