import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the data
def load_data(file_path):
    data = pd.read_csv("/Users/praneethsattavaram/Downloads/Sales Data.csv")  # Load the sales data from CSV
    return data

# Step 2: Identify dimensions and measures automatically
def identify_dimensions_measures(data):
    dimensions = []
    measures = []
    
    for col in data.columns:
        if pd.api.types.is_numeric_dtype(data[col]):
            measures.append(col)  # Numerical columns are measures
        else:
            dimensions.append(col)  # Categorical columns are dimensions
    
    return dimensions, measures

# Step 3: Generate descriptive analysis and visualizations
def descriptive_analysis(data, dimensions, measures):
    # Basic summary statistics for measures
    summary = data[measures].describe()
    print("Summary statistics for measures:")
    print(summary)
    
    # Visualizations
    for dimension in dimensions:
        for measure in measures:
            if data[dimension].nunique() < 15:  # Limit to avoid overplotting with many categories
                plt.figure(figsize=(8, 6))
                sns.barplot(x=dimension, y=measure, data=data)
                plt.title(f"{measure} by {dimension}")
                plt.xticks(rotation=45)
                plt.show()
    
    # Correlation matrix for numerical measures
    correlation_matrix = data[measures].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix for Measures")
    plt.show()

# Step 4: Main function to run the entire process
def run_analysis(file_path):
    data = load_data(file_path)
    dimensions, measures = identify_dimensions_measures(data)
    descriptive_analysis(data, dimensions, measures)

# Usage:
file_path = "path_to_your_sales_data.csv"  # Replace with your sales dataset path
run_analysis(file_path)
