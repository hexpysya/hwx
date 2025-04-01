# Automatic Download and Processing of VHI Data

## Project Description
This project automatically downloads CSV files containing Vegetation Health Index (VHI) data for Ukraine, processes them, and analyzes extreme weather conditions such as droughts. The data is sourced from NOAA (National Oceanic and Atmospheric Administration) for all Ukrainian regions from 1981 to 2024.

## Features
- **Automatic data download** for all Ukrainian regions.
- **Data cleaning and processing** to ensure correct formatting.
- **VHI analysis**: retrieving minimum, maximum, average, and median values, as well as detecting extreme droughts.

## Requirements
- Python 3.x
- Pandas
- urllib
- os

## Installation
1. Clone the repository or copy the project files:
   ```sh
   git clone <URL>
   ```
2. Install the required libraries:
   ```sh
   pip install pandas
   ```

## Usage
### Downloading Data
The script automatically creates a `vhi` folder and downloads CSV files for each region, deleting previous versions:
```python
data_update()
```

### Data Processing
The `load_data(directory)` function loads and cleans the data, returning a DataFrame:
```python
vhi = load_data("vhi")
vhi.head()
```

### Updating Region Indices
```python
vhi = update_indx(vhi)
```

### Saving Processed Data to CSV
```python
vhi.to_csv("vhi_dataset.csv", index=False, encoding='utf-8')
```

## Data Analysis
### Retrieving VHI for a Region by Year
```python
vhi_reg_year(vhi, "Kiev", 2017)
```

### Finding Extremes (Min, Max, Mean, Median) for Selected Regions and Years
```python
extr(vhi, ["Kiev", "Poltava"], [2017, 2024])
```

### Retrieving VHI for a Year Range
```python
vhi_range_year(vhi, ["Poltava", "Kiev"], 2023, 2024, 5)
```

### Detecting Years with Widespread Droughts
```python
vhi_dryness(vhi, 10)
```
