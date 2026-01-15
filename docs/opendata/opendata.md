# ICEYE Open Data Program on AWS

Welcome to the ICEYE Open Data Program. As part of our commitment to scientific collaboration and advancement, we are making a growing selection of our **Synthetic Aperture Radar (SAR)** datasets available for free under a **Creative Commons Attribution (CC-BY 4.0)** license.

This documentation explains how the data is organized, how to access it via AWS, and provides a tutorial to help users get started with analysis and exploitation!

## 📁 Dataset Overview

All products are delivered as **Cloud-Optimized GeoTIFFs (COGs)** and, where applicable, adhere to the specifications defined in the ICEYE product documentation. Please note, however, that this open catalog contains example datasets and imaging products that may be experimental and/or may not fully comply with the latest data product specifications. For the most up-to-date documentation on commercially available products, please refer to the latest data product specifications available at [static STAC catalog](sar.iceye.com)

Each SAR scene typically includes:

- **SLC COG**: Single Look Complex image
- **GRD COG**: Ground Range Detected image
- **QLK COG**: Quicklook preview image
- **Metadata JSON**: STAC compliant image product metadata

Additionally, collections acquired in Dwell imaging modes, the catalog includes:

- **CSI COG**: Colorized Subaperture image
- **VID COG**: SAR Video in COG, GIF, and MP4 formats
  
## 📚 Data Organization

The ICEYE Open Data catalog is a [static STAC catalog](https://stacspec.org) hosted as publicly accessible files on Amazon S3. The data can be accessed directly from a public S3 bucket without requiring an AWS account or credentials.

### Resource Details

| **Resource Type**           | **Details**                                                  |
|----------------------------|--------------------------------------------------------------|
| **S3 Bucket**              | `iceye-open-data-catalog`                                            |
| **Amazon Resource Name (ARN)** | `arn:aws:s3:::iceye-open-data-catalog`                      |
| **AWS Region**             | `us-west-2`                                                  |
| **AWS CLI Access**         | `aws s3 ls --no-sign-request s3://iceye-open-data-catalog/data/`     |

> **Note**: The `--no-sign-request` flag allows public access without requiring an AWS account.

---

### 🌐 Browse the ICEYE Open Data Catalog

You can explore the contents of the ICEYE Open Data S3 bucket through a web-based file browser:

🔗 [Open the Catalog](http://iceye-open-data-catalog.s3-website-us-west-2.amazonaws.com/?prefix=)

This static website interface allows you to:

- View the available datasets and all the `.tif`, `.json`, and `.png` files included in them
- Access the image and metadata files directly from your browser

### Browse Data with STAC Browser

You can also explore the dataset using the STAC Browser via the link below:

🔗 [STAC Browser - ICEYE Open Data Catalog](https://radiantearth.github.io/stac-browser/#/external/iceye-open-data-catalog.s3-us-west-2.amazonaws.com/catalog.json?.language=en)

The STAC Browser provides an interactive interface to navigate and preview metadata and available assets.

## 🧪 Tutorial: Access and Analyze ICEYE SAR Data on AWS

To get started with the ICEYE open SAR data, you can simply:

1. Discover a scene using STAC tools or by browsing the bucket
2. Load a COG (Cloud Optimized GeoTIFF) directly from S3
3. Visualize and analyze the image using GIS software or Python

### 🔍 Viewing in GIS Tools

All `.tif` files in this dataset are **Cloud-Optimized GeoTIFFs (COGs)**, which can be opened directly over the network in common GIS tools like:

- **QGIS**: Use the “Raster > Add Layer > Add Raster Layer” menu and select the tif file.
- **ArcGIS Pro**: Use “Add Data from Path” and specify the file path or public COG URL.
- **GDAL-based tools**: COGs can be read directly in GDAL-based applications and libraries that support raster access.

---

## 🎓 Licensing and Use

All data is made available under the **CC-BY 4.0 license**. Users are free to use, modify, and redistribute the data for academic, research, and commercial purposes (with attribution to ICEYE).

We actively encourage academic users, Earth observation researchers, and the broader remote sensing community to explore these high-resolution SAR datasets and incorporate them into their work.
