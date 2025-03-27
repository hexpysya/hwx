# VHI Data Analysis Web App

## Project Description
This project is a web-based data visualization tool for analyzing Vegetation Health Index (VHI) data using Streamlit. It allows users to explore VHI trends across different regions of Ukraine, filter data based on weeks and years, and generate visual comparisons.

## Features
- **Interactive UI** built with Streamlit.
- **Dynamic data filtering** by region, week, and year range.
- **Visualization tools**: time series plots, bar charts, and comparison plots.
- **Sorting options** to analyze trends.
- **Reset filters** to quickly start a new analysis.

## Requirements
- Python 3.x
- Streamlit
- Pandas
- Matplotlib
- Seaborn

## Installation
1. Clone the repository:
   ```sh
   git clone <URL>
   ```
2. Install the required dependencies:
   ```sh
   pip install streamlit pandas matplotlib seaborn
   ```
3. Place the `vhi_dataset.csv` file in the project directory.

## Usage
### Running the Streamlit App
Run the following command in the terminal:
```sh
streamlit run app.py
```

### Interacting with the App
- **Select Index**: Choose between VHI, VCI, and TCI.
- **Select Region**: Pick a specific region to analyze.
- **Filter by Week and Year Range**: Adjust sliders to refine the dataset.
- **Sorting**: Choose ascending or descending order.
- **Visualizations**:
  - **Table View**: Display filtered data.
  - **Time Series Plot**: View VHI trends over time.
  - **Comparison Plot**: Compare average VHI values across regions.
