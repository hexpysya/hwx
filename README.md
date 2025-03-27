# NOAA VHI Data Analysis Project

This project automates the download and analysis of Vegetation Health Index (VHI) data from NOAA's STAR service for Ukrainian regions.

## Project Description

The script performs the following operations:
1. Automatically downloads VHI data for all 27 Ukrainian regions
2. Cleans and processes the raw CSV files
3. Combines data into a unified DataFrame
4. Provides analytical functions for VHI data exploration

## Features

- **Automatic Download**: Fetches the latest VHI data from NOAA servers
- **Collision Handling**: Ensures no duplicate files by removing old versions before download
- **Data Cleaning**: Processes raw CSV files to remove formatting artifacts
- **Region Mapping**: Corrects region indexes to match standard Ukrainian administrative divisions
- **Analytical Functions**:
  - Get VHI time series for specific regions and years
  - Calculate VHI extremes (min/max), averages and medians
  - Analyze VHI across year ranges
  - Identify years with extreme drought conditions

## Usage

### Data Download
```python
data_update()  # Downloads data for all 27 regions
