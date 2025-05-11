#   Geospatial Data Analysis Project

This project performs geospatial data analysis using Python and several libraries, including `gdal`, `rasterio`, and others.

## Description

This project processes Sentinel-2 and Landsat satellite imagery to perform several geospatial analysis tasks, including band merging, reprojection, clipping, pansharpening, and quality assessment.

**Sentinel-2 Processing:**

The script first processes Sentinel-2 imagery by:

1.  **Merging bands:** It merges specified bands (B02, B03, B04, B08) from Sentinel-2 tiles.
2.  **Reprojecting:** The merged image is reprojected to the EPSG:4326 coordinate system.
3.  **Clipping:** The reprojected image is then clipped to the extent of a specified shapefile.
4.  **Visualization:** It visualizes the resulting RGB image using normalized band values.

**Landsat Processing:**

The script also processes Landsat imagery, performing the following steps:

1.  **Unpacking Archive:** If necessary, it extracts a Landsat archive.
2.  **Renaming Bands:** It renames the extracted band files for easier handling.
3.  **Merging RGB Bands:** It merges the RGB bands (B2, B3, B4).
4.  **Pan-sharpening:** It performs pansharpening of the RGB image using the panchromatic band (B8) with different resampling methods (nearest, bilinear, cubic, cubicspline, lanczos, average).
5.  **Visualization:** It visualizes the original RGB image.
6.  **Quality Assessment:** It calculates and reports quality metrics (R², RMSE, MAE) to compare the pansharpened images with the original RGB image, providing a quantitative assessment of the pansharpening results. It then identifies the best performing method based on these metrics.

The script leverages libraries like `gdal`, `rasterio`, `numpy`, `matplotlib`, `tabulate`, and `sklearn` to achieve these tasks. It uses subprocess calls to execute GDAL commands and performs raster data manipulation and analysis within Python.

##   Requirements

To run this project, you need to install the following Python packages. You can install them using `pip`:

```bash
pip install -r requirements.txt
```

**Note on GDAL Installation:**

GDAL can be challenging to install. It is recommended to install it via OSGeo4W for Windows users. You can download it from the following link:

[https://trac.osgeo.org/osgeo4w/](https://trac.osgeo.org/osgeo4w/)

For other operating systems (Linux, macOS), you can usually install GDAL using your system's package manager (e.g., `apt-get`, `brew`, `conda`). Please refer to the official GDAL installation guide for your specific OS.

1.  **Install the Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Install GDAL:**

    * **Windows:** Download and install OSGeo4W from [https://trac.osgeo.org/osgeo4w/](https://trac.osgeo.org/osgeo4w/). Make sure to select the `gdal` package during installation. You might need to set environment variables (e.g., `GDAL_DATA`) after installation.

    * **Conda:**

        ```bash
        conda install -c conda-forge gdal
        ```

