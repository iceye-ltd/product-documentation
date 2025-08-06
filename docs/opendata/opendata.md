# Launcing Soon: ICEYE Open Data Program on AWS 🚀

Welcome to the ICEYE Open Data Program. As part of our commitment to scientific collaboration and advancement, we are making a growing selection of our **Synthetic Aperture Radar (SAR)** datasets available for free under a **Creative Commons Attribution (CC-BY 4.0)** license.

This documentation explains how the data is organized, how to access it via AWS, and provides a tutorial to help users get started with analysis and exploitation!

## 📁 Dataset Overview

The ICEYE open data catalog contains high-resolution SAR scenes acquired in different imaging modes.

All products are delivered as **Cloud-Optimized GeoTIFFs (COGs)** and are aligned with the specifications documented in ICEYE’s product documentation.

Each SAR scene typically includes:

- **GRD COG**: Ground Range Detected image
- **SLC COG**: Single Look Complex image
- **QLK PNG**: Compressed preview image, including a .kml file for visualization in Google Earth
- **Metadata JSON**: Original metadata used to generate STAC
  
## 📚 Data Organization

The ICEYE Open Data catalog is structured as a [static STAC catalog](https://stacspec.org), hosted as publicly accessible files on Amazon S3. The s3 bucket is organized as follows:

```text
s3://iceye-open-data/
├── catalog.json
├── collections/
│ └── iceye-sar.json
├── stac-items/
│ └── YYYY/MM/scene_timestamp_product.json
├── data/
│ └── <ICEYE_scene_id_timestamp_satellite_mode>/
│ ├── *.tif # GRD / SLC COGs
│ ├── *.png # Quicklook
│ └── *.json # Metadata
```

### 🔍 Finding Data

- **Catalog browsing**: You can use STAC Browser or command-line tools like [`pystac-client`](https://github.com/stac-utils/pystac-client) to crawl and filter the catalog.
- **Scene organization**: STAC items are grouped by **acquisition date (YYYY/MM)**.
- **Assets** are linked inside each STAC item, referencing public URLs to their respective COGs and metadata.

For a direct listing of files, visit the [ICEYE Open Data S3 Website](TBD).

## 🧪 Tutorial: Access and Analyze ICEYE SAR Data on AWS

This tutorial walks through how to:

1. Discover a scene using STAC tools or by browsing the bucket
2. Load a COG (Cloud Optimized GeoTIFF) directly from S3
3. Visualize and analyze the image using GIS software or Python

### 🔍 Viewing in GIS Tools

All `.tif` files in this dataset are **Cloud-Optimized GeoTIFFs (COGs)**, which can be opened directly over the network in common GIS tools like:

- **QGIS**: Use the “Raster > Add Layer > Add Raster Layer” menu and paste in the HTTPS S3 URL.
- **ArcGIS Pro**: Use “Add Data from Path” and specify the public COG URL.
- **GDAL-based tools**: COGs can be read directly with `gdal_translate`, `gdalinfo`, or used in server workflows like GeoServer or MapServer.

---

## 🎓 Licensing and Use

All data is made available under the **CC-BY 4.0 license**. Users are free to use, modify, and redistribute the data for academic, research, and commercial purposes (with attribution to ICEYE).

We actively encourage academic users, Earth observation researchers, and the broader remote sensing community to explore these high-resolution SAR datasets and incorporate them into their work.
