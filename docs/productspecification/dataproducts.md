# 5. Data Products

## 5.1 Introduction

A multitude of different products can be generated from SAR data. Some product types are well suited for human exploitation whereas others are designed with algorithmic and signal processing systems in mind. ICEYE’s data product offering can be used to fulfill a variety of use cases. The following distinctions are useful in order to understand ICEYE’s data product offering:

**Complex vs Amplitude Data Products**: SAR imaging datasets initially contain samples of in-phase and quadrature value pairs representing the measured radio wave backscatter. These value pairs can be converted computationally to amplitude and phase values. The data products that contain both amplitude and phase data are called **Complex Data Products**. However, for use cases where phase data is redundant the data can be stripped to reduce file size and increase convenience. Products with only amplitude data are called **Amplitude Data Products**. However, because of the lack of phase values, amplitude data products cannot be used for certain use cases such as interferometric SAR (InSAR) or coherent change detection (CCD).

**Standard vs Custom Data Products**: The below subsections define all the **Standard Data Products** in ICEYE’s offering. However, it may be possible to generate **Custom Data Products** to fulfill special customer requirements. Such custom products are available on demand as custom orders. These non-standard products **are not** guaranteed to adhere to the delivery timelines described in Section [3.7.3](tasking.md#373-delivery-time-service-level).

**Availability and Service Level**: Most standard products are available on **Standard Service Levels** but some are only available **On** (special) **Demand** via **Custom Orders** at separately agreed (and thus custom) service levels despite being standard products. Refer to Sections [3.7.3](tasking.md#373-delivery-time-service-level) and [5.5](#55-on-demand-only-data-products) for more information. Additionally, customers with specific timeline requirements should consult ICEYE to discuss special needs. New customers are advised to reach out via [the ICEYE website](https://www.iceye.com/contact/).

**Imaging Mode Support**: Many data products can be generated from SAR collections acquired with any **Imaging Mode** (see Section [2](imagingmodes.md#2-iamaspaceimaging-modes)). However, some imaging modes can be used to generate only a limited set of different data products and vice versa.

While all of these distinctions could be used to group and present the data product offering, this Section [5.1](#51-introduction) prioritizes the complex vs amplitude data products grouping in structuring an overview onto ICEYE’s data product offering in Sections [5.1.1](#511-amplitude-data-product-offering) and [5.1.2](#512-complex-data-product-offering) but the availability and service level as well as imaging mode support differences are also clearly highlighted.


### 5.1.1 Amplitude Data Product Offering

The following four products make up ICEYE’s Amplitude Data Product offering:

The primary product within ICEYE's **Amplitude Data Products** offering is the **Ground Range Detected (GRD)** amplitude image data product. During the production process, the image data is oriented in the natural range-azimuth sensor orientation, projected to the ground surface using an Earth ellipsoid model, and may be multi-looked to reduce speckle. The products are packaged into the Cloud Optimized GeoTIFF file format with metadata included. Overall, GRD is excellent for most common SAR image analysis use cases. The Cloud Optimized GeoTIFF GRD format is described in detail in section [5.2.2](#522-ground-range-detected-grd-image-3). A legacy GRD format described in Section [5.2.3](#523-legacy-grd-format) will continue to be offered for compatibility reasons until 31 December, 2026. 

ICEYE also offers the **Quicklook** product which is a raster graphic preview of a GRD image. Quicklook images are encoded in the PNG file format with metadata included. They are compatible with most common documentation, presentation and publishing software. As such they are easily exploitable by non-technical staff without specialized GIS software or uncommon expertise. More information on the Quicklook product is available in Section [5.2.1](#521-quicklook).

Two amplitude data products are only offered with the Dwell, Dwell Fine and Dwell Precise imaging modes. The first of these is the **Colorized Sub-aperture Image (CSI)** product which is a composite SAR image resulting from the coadding of 13 distinctively colored sub-aperture images. These are packaged into the Cloud Optimized GeoTIFF format with all metadata included. They are excellent for detecting human-made structures and moving objects. More information on the CSI product is available in Section [5.4.1](#541-colorized-sub-aperture-image-csi). A legacy CSI format described in Section [5.4.2](#542-legacy-colorized-sub-aperture-image-csi) will continue to be offered for compatibility reasons until 31 December, 2026. 

The second Dwell, Dwell Fine and Dwell Precise specific product is the **SAR Video (VID)** product which is a short video with 25 individual frames each representing a discrete sub-aperture SAR image taken during the same collection. VID products are delivered in both MPEG4 and GIF formats; a Cloud Optimized GeoTIFF file is also provided with each video frame as a separate band. The metadata is also stored in the GeoTIFF file. Like the CSI, the VID product is excellent for detecting human-made structures and moving objects. More information on the VID product is available in Section [5.4.3](#543-sar-video-vid). A legacy SAR Video format described in Section [5.4.4](#544-legacy-sar-video-vid) will continue to be offered for compatibility reasons until 31 December, 2026. 

Table [5-1](#table-5-1-amplitude-data-products-available-for-each-iceye-imaging-mode) provides a summary of the different amplitude data products in terms of their availability and the imaging modes through which they can be obtained. Further descriptions of the different data products are given in the following subsections as referenced above.


##### _Table 5-1: Amplitude Data Products available for each ICEYE Imaging Mode_

| Service level    |  Product  | Scan /<br>Scan Wide | Strip | Spot /<br>Spot Fine /<br>Spot Extended Area | Dwell /<br>Dwell Fine /<br>Dwell Precise |
| -------------------------- | :-------: | :--: | :---: | :-----------------------------: | :--------------------------: |
| **Standard** <br>_Delivery SLAs in Section_ [_3.7.3_](tasking.md#373-delivery-time-service-level) _apply_ | Quicklook |  ✅︎  |   ✅︎  |                ✅︎               |              ✅︎              |
| **Standard** <br>_Delivery SLAs in Section_ [_3.7.3_](tasking.md#373-delivery-time-service-level) _apply_      |    GRD    |  ✅︎  |   ✅︎  |                ✅︎               |              ✅︎              |
| **Standard** <br>_Delivery SLAs in Section_ [_3.7.3_](tasking.md#373-delivery-time-service-level) _apply_      |    CSI    |   ❌  |   ❌   |                ❌                |              ✅︎              |
| **Standard** <br>_Delivery SLAs in Section_ [_3.7.3_](tasking.md#373-delivery-time-service-level) _apply_      |    VID    |   ❌  |   ❌   |                ❌                |              ✅︎              |



### 5.1.2 Complex Data Product Offering

The following three products constitute ICEYE’s Complex Data Product offering:

The primary product within ICEYE's **Complex Data Products** offering is the **Single Look Complex (SLC)** which is a SAR image with all the original sensor data retained. It offers the highest fidelity and the full resolution in azimuth and range. It is also free from interpolation artifacts or projection issues. SLC products are packaged into the Cloud Optimized GeoTIFF file format with metadata included. They are excellent as input for automated algorithmic processing workflows and advanced exploitation use cases where phase data is leveraged, such as coherent change detection (CCD). The Cloud Optimized GeoTIFF SLC format is described in detail in section [5.3.1](#531-single-look-complex-slc-image). A legacy SLC format described in Section[ 5.3.2](#532-legacy-slc-image-format) will continue to be offered for compatibility reasons until 31 December 2026. 

The ICEYE complex product offering also includes the **Sensor Independent Complex Data (SICD)** and **Sensor Independent Derived Data (SIDD)** which are industry standard SAR image data products designed to be used in conjunction with each other, and thus come as a bundle. This product is sensor, collection strategy and processing algorithm agnostic and is stored in the NITF file format with metadata in XML. The SICD + SIDD product design and packaging has been optimized to facilitate SAR data exploitation together with other products in the same format from other vendors. It is thus excellent for vendor-agnostic automated data processing. More information about the SICD and SIDD products is available in Section [5.5.1](#551-sensor-independent-complex-data-sicd-and-sensor-independent-derived-data-sidd-1).

The third ICEYE complex data product is **Compensated Phase History Data (CPHD)** which is an industry standard product for SAR phase history data. CPHD is compensated for hardware timing and platform motion and accommodates the Phase History Data (PHD) signal arrays from a variety of SAR sensors in a sensor-independent fashion. It is stored in a purpose-built binary CPHD file format and includes a complete set of metadata describing collection geometry and the included PHD arrays. More information on the CPHD product is available in Section [5.5.2](#552-compensated-phase-history-data-cphd-1).

Table [5-2](#table-5-2-complex-data-products-available-for-each-iceye-imaging-mode) provides a summary of the different complex data products in terms of their availability and the imaging modes through which they can be obtained. Further descriptions of the different data products are given in the following subsections as referenced above. As is shown in the table, the Scan and Scan Wide imaging modes cannot be used to generate complex data products but any other imaging mode can be used for any of the complex data products.


##### _Table 5-2: Complex Data Products available for each ICEYE Imaging Mode_

| Service level                                                                                                                                                         |  Product  | Scan /<br>Scan Wide | Strip | Spot /<br>Spot Fine /<br>Spot Extended Area | Dwell /<br>Dwell Fine /<br>Dwell Precise |
| -------------------------------------------------------------------------------------------- | :-------: | :--: | :---: | :-----------------------------: | :--------------------------: |
| **Standard** <br> _Delivery SLAs in Section_ [_3.7.3_](tasking.md#373-delivery-time-service-level) _apply_ |    SLC    |   ❌  |   ✅︎  |                ✅︎               |              ✅︎              |
| **Custom**     | SICD+SIDD |   ❌  |   ✅︎  |                ✅︎               |              ✅︎              |
| **Custom**        |    CPHD   |   ❌  |   ✅︎  |                ✅︎               |              ✅︎              |


## 5.2 Amplitude Data Products

### 5.2.1 Quicklook

The **Quicklook** product is an image preview of a higher resolution GRD image ([5.2.2](#522-ground-range-detected-grd-image)). It is available for all imaging modes and is provided in PNG format. These are very easily leveraged by non-technical users, as they can be opened by basic image viewing software, document editing tools and raster graphics editing software. Quicklook can also be used to perform basic rapid image analysis and/or to determine if the more detailed data products below should be further exploited and analyzed. 


### 5.2.2 Ground Range Detected (GRD) Image

As outlined in Section [5.1.1](#511-amplitude-data-product-offering), the primary product within ICEYE Amplitude Data Products offering is the **Ground Range Detected (GRD)** amplitude image data product.  Amplitude images represent focused SAR data that has been detected and projected to the ground plane using an Earth ellipsoid model. The pixels of SAR amplitude images only contain amplitude values. With many imaging modes, **Ground Range Detected (GRD)** data products are also multi-looked to reduce the effect of speckle. Ground range coordinates are the slant range coordinates projected onto the ellipsoid of the Earth. For this projection the WGS84 reference ellipsoid (see Table [5-3](#table-5-3-parameters-of-the-earth-ellipsoid-model-used-in-ground-surface-projection)) is used and an averaged fixed value of terrain height is used. This makes the ellipsoid surface closer to the true ground surface. The mean ellipsoid height used is annotated in the avg\_scene\_height metadata element.


##### _Table 5-3: Parameters of the Earth ellipsoid model used in ground surface projection_

| Ellipsoid Reference | Semi Major Axis | Semi Minor Axis | Inverse Flattening |
| ------------------- | --------------- | --------------- | ------------------ |
| WGS84               | 6378137.0 m     | 356752.314245 m | 298.257 223 563    |

ICEYE packages GRD amplitude images onto the [Cloud Optimized GeoTIFF (COG)](https://docs.ogc.org/is/21-026/21-026.html) format which is supported by most image viewing software, GIS applications, and data exploitation tools and libraries. The format also allows for faster data visualization and geospatial processing workflows especially when the image data itself is  stored in the cloud. This format allows for increased data precision (up to u32/f32) to support the very high dynamic range of the latest ICEYE data products.

Pixel values represent a scaled amplitude. The resulting product has approximately circular spatial resolution and square pixel spacing. Additionally, an incidence angle dependence in range, calculated using the ellipsoidal Earth model has been applied to enable the conversion of radar brightness to backscatter intensity. 

The core advantages of GRD images is that they are laid out in the natural SAR orientation, which is required for rigorous geolocation, and their pixels are free of the interpolation artifacts of map projection images. This product is the form of a SAR amplitude image that retains its SAR heritage. Pixels are presented in the natural range-azimuth form best suited for shadows-down interpretation, that is free of map-projection-induced artifact and facilitates interpretation of topography and elevated features.

To assist users that require geocoded imagery with minimal interpolation artifacts, ICEYE amplitude image products are tagged with ground control points (GCP) and rapid positioning capability polynomial coefficients (RPC’s). These allow precise geospatial exploitation using freely available tools such as QGIS or GDAL.

Associated image metadata is stored in the GeoJSON format. 


### 5.2.3 Legacy GRD Format

A legacy GRD format can be provided for backward compatibility until **31 December 2026**. This legacy format differs from the current GRD product primarily as summarized in Table [5-4](#table-5-4-simplified-comparison-of-the-new-grd-and-the-old-legacy-grd-version). Customers are strongly encouraged to migrate to the new Cloud Optimized GeoTIFF GRD product to benefit from its enhanced features and performance. ICEYE is available to support customers during this transition. Capacity to deliver images within specific delivery timelines may be reduced when legacy data formats are requested.


##### _Table 5-4: Simplified comparison of the new GRD and the old Legacy GRD version_

|                                              | GRD                                            | Legacy GRD                                           |
| -------------------------------------------- | ---------------------------------------------- | ---------------------------------------------------- |
| File format                                  | Cloud Optimized GeoTIFF                        | GeoTIFF                                              |
| Support for very high dynamic range products | Yes                                            | No                                                   |
| Metadata format                              | GeoJSON                                        | XML                                                  |
| File naming convention                       | Regular ([5.6.1](#561-file-naming-convention)) | Legacy ([5.6.2](#562-legacy-file-naming-convention)) |
| Availability                      | Now | Now; to be deprecated in 2026 with final availability on December 31, 2026. |

The format of the legacy GRD is the non-cloud optimized GeoTIFF. It is compatible with many GIS software and tools. Software tools might not be able to optimally utilize  legacy GRD products stored in the cloud, or use will require a full download of the files before any part of the images can be utilized.

The legacy GRD format supports lower data precision and is thus less suitable for data products with high dynamic range. The metadata is stored in the XML format rather than GeoJSON, and the file names follow the legacy naming convention described in Section [5.6.2](#562-legacy-file-naming-convention). 


## 5.3 Complex Data Products

### 5.3.1 Single Look Complex (SLC) Image

**Single Look Complex (SLC)** images have the highest fidelity of all SAR image products because they are only one step removed from the original RADAR collected data. They retain all the original sensor measurements and are free from interpolation artifacts or projection issues. As the name suggests, SLC images have only a single look. This means they retain full resolution in azimuth and range. In most cases the impulse response function (the shape of a single, isolated radar-bright object in the radar image) is asymmetrical with azimuth resolution being smaller (finer) than range resolution.

Scenes are stored in the satellite image acquisition geometry (also known as the slant plane). The image coordinate system is centered on the zero-Doppler (time of closest approach) SAR coordinates and data is  arranged in the slant-range-by-azimuth imaging plane. The pixels are spaced equidistant in azimuth (according to the inverse of the pulse repetition frequency) and in slant range (according to the range sampling frequency). 

SLC products are the best source for SAR image analysis, but complex data has traditionally been packaged in scientific or military-intel formats that were difficult to use without specialized software or experience. To address this, ICEYE images are packaged in the open, international **[Cloud Optimized GeoTIFF (COG)](https://docs.ogc.org/is/21-026/21-026.html)** format. This enables easy ingestion and manipulation in most image readers, GIS tools and libraries. The amplitude and phase data is formatted in two separate GeoTIFF bands, similar to how bands are used for multispectral images. Image readers and GIS tools are able to ingest this complex image just like they do any other GeoTIFF file. The amplitude band can be immediately presented for viewing, while the phase band is available for further exploitation by more specialized tools. 

The Cloud Optimized GeoTIFF format also enables  faster data visualization and geospatial processing workflows especially when the image data itself is being stored in the cloud.

The SLC images are at full resolution, so users have access to the full resolution as well as to reduced-speckle, pixel-aggregated views (equivalent to different levels of multi-looking) that are produced instantly when zooming in and out (e.g. [QGIS](https://qgis.org/) can perform this via [Lanczos averaging](https://en.wikipedia.org/wiki/Lanczos_resampling) with appropriate settings enabled).  While the SAR data inside the format is stored in the slant plane (the satellite image acquisition geometry), the metadata contains [RPC values](https://sar.iceye.com/5.2.2/foundations/geospatialAccuracy/#fast-and-simple-geolocation-rapid-positioning-capability) that allows GIS tools to perform automatic ground projection, so they are ready to be used as part of analysis and exploitation workflows. Please note that Orthorectification using a Digital Elevation Model is still recommended for accurate geospatial comparison and analysis.

The complex data is stored as a matrix in a separate band in the GeoTIFF container. Each row of the matrix is a single range line (often called a range profile by RADAR engineers) of the image with increasing range preceding from lower indices to higher indices. Early row indices in the matrix correspond to early pulses and later rows correspond to later pulses. 

Metadata is stored with the GeoJSON format. GeoJSON is a geocoded metadata format supported by many GIS tools.

### 5.3.2 Legacy SLC Image Format

A legacy legacy format can be provided for backward compatibility until **31 December 2026**. This legacy format differs from the current SLC product primarily as summarized in Table [5-5](#table-5-5-simplified-comparison-of-the-new-slc-and-the-old-legacy-slc-version). Customers are strongly encouraged to migrate to the new Cloud Optimized GeoTIFF SLC product to benefit from its enhanced features and performance. ICEYE is available to support customers during this transition. Capacity to deliver images within specific delivery timelines may be reduced when legacy data formats are requested.


##### _Table 5-5: Simplified comparison of the new SLC and the old Legacy SLC version_

|                                                     | SLC                                              | Legacy SLC                                             |
| --------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------ |
| Container                                           | Cloud Optimized GeoTIFF                          | HDF5                                                   |
| Can be opened in any GIS and image viewing software | Yes                                              | No                                                     |
| Full resolution in range and azimuth                | Yes                                              | Yes                                                    |
| Metadata format                                     | GeoJSON                                          | XML                                                    |
| File naming convention                              | Regular ([5.6.1](#561-file-naming-convention-1)) | Legacy ([5.6.2](#562-legacy-file-naming-convention-2)) |
| Availability                      | Now | Now; to be deprecated in 2026 with final availability on December 31, 2026. |

Images in the legacy SLC format are stored as binary matrices in an [HDF5](https://www.hdfgroup.org/solutions/hdf5/) file container. Each image pixel is stored with in-phase (I) and quadrature (Q) components and therefore, contains both amplitude and phase information. The legacy SLC metadata is stored in XML format. The file names follow a legacy naming convention .


## 5.4 Dwell, Dwell Fine and Dwell Precise Exclusive Data Products

### 5.4.1 Colorized Sub-Aperture Image (CSI)

ICEYE will release a new Cloud Optimized GeoTIFF CSI format that is described in this section, within the first quarter of 2026. A legacy CSI format described in [Section 5.4.2](#542-legacy-colorized-sub-aperture-image-csi) will continue to be offered for compatibility reasons until December 31, 2026.

**Colorized Sub-aperture Images (CSI)** are made by assigning distinct colors to backscatter signals received from various sub-apertures, which are then integrated into a composite color image. Human-made objects with flat surfaces or sharp angles typically produce preferential scattering orientations (anisotropic scatterers) that appear highlighted as a dominant color in the CSI image.  In contrast, natural objects that scatter uniformly in all directions (isotropic scatterers) do not show preferential scattering geometries and tend to appear as gray tones in the CSI image. Additionally, objects partially obscured by vegetation or tree canopies may also be highlighted in dominant colors, as only a subset of sub-apertures captures strong backscatter returns. This feature enhances the CSI image’s effectiveness in identifying objects that might otherwise be concealed. This distinctive capability is particularly valuable in search, monitoring and surveillance operations.  Figure [5-1](#) shows an example of a CSI image, demonstrating how the CSI image can preferentially reveal human-made objects relative to a background of natural foliage.


##### __![](https://github.com/iceye-ltd/product-documentation/releases/download/additional-assets/csi.png)__

##### _Figure 5-1: An example of a CSI image, demonstrating how the CSI image can preferentially reveal human-made objects relative to a background of natural foliage._

The colors denote the geometry that a point in the image predominantly scatters in. The collection time is split into 13 individual sub-apertures. Each sub-aperture is individually colored from red at the start of the collection to blue at the end of the collection. A composite image is made by coadding all the sub-apertures.
<img src="https://github.com/iceye-ltd/product-documentation/releases/download/additional-assets/csisubapertures_2.png" alt="subapertures" width="500"/>

##### _Figure 5-2: An illustration of the 13 different sub-apertures and their individual coloring.._

CSI products are generated exclusively for the Dwell, Dwell Fine, and Dwell Precise imaging modes, as these modes provide an extended total illumination time and thus a sufficiently long synthetic aperture. The aperture is partitioned into 13 sub-apertures, each acquired under slightly different illumination geometry, with each sub-aperture contributing distinct radar backscatter information to the final composite color image.  

The CSI product is provided in a Cloud Optimized GeoTIFF container, enabling direct visualization with standard image viewers as well as geospatial software. For each sub-aperture, the CSI includes metadata describing the acquisition time, integration duration, color encoding, and satellite position. The ground resolution of the CSI product in Cloud Optimized GeoTIFF format is identical to the ground resolution of the amplitude GRD product.

### 5.4.2 Legacy Colorized Sub-Aperture Image (CSI)

A legacy CSI format can be provided for backward compatibility until *31 December 2026*. This legacy format differs from the current CSI product primarily as summarized in Table [5-6](#table-5-6-simplified-comparison-of-the-new-csi-and-the-old-legacy-csi-formats). Note that in this legacy format the CSI product has a lower ground resolution than the new Cloud Optimized GeoTIFF CSI. Customers are strongly encouraged to migrate to the new Cloud Optimized GeoTIFF CSI product to benefit from its enhanced features and performance. ICEYE is available to support customers during this transition. Capacity to deliver images within specific delivery timelines may be reduced when legacy data formats are requested.

##### Table 5-6: Simplified comparison of the new CSI and the old Legacy CSI formats

|                                                     | CSI                                              | Legacy CSI                                             |
| --------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------ |
| Container                                           | Cloud Optimized GeoTIFF                          | GeoTIFF                                                |
| Full ground resolution (same as GRD)                | Yes                                              | Yes                                                    |
| Metadata format                                     | GeoJSON                                          | XML                                                    |
| File naming convention                              | Regular ([5.6.1](#561-file-naming-convention-1)) | Legacy ([5.6.2](#562-legacy-file-naming-convention-2)) |
| Availability                      | 1Q 2026 | Now; to be deprecated in 2026 with final availability on December 31, 2026. |



### 5.4.3 SAR Video (VID)

ICEYE will release a new Cloud Optimized GeoTIFF SAR Video (VID) format that is described in this section, within the first quarter of 2026. A legacy SAR Video (VID) format described in [Section 5.4.4](#544-legacy-sar-video-vid) will continue to be offered for compatibility reasons until December 31, 2026.

**SAR Video (VID)** is similar to the CSI product described in Section [5.4.1](#541-colorized-sub-aperture-image-csi) in which the acquired SAR data is first divided into multiple sub-apertures. However, in the case of SAR Video each discrete sub-aperture image is used as a frame to compile a short video clip. The Dwell, Dwell Fine and Dwell Precise imaging modes generate videos consisting of 25 individual frames.

The VID product is useful in applications for which the motion of moving objects, such as vessels and land vehicles, is to be analyzed. By simple inspection and analysis of a video, it is possible to infer the general direction and speed of the moving object. SAR Video is also effective for detecting objects hidden in forested areas as well as human-made objects as these tend to give bright reflections revealed as glints when playing a video.

The formats for the VID data products are MPEG4 and GIF. Additionally, a file in Cloud Optimized GeoTIFF format is produced where each of the video frames is available as a separate band to facilitate frame by frame analysis in a GIS image exploitation tool. The user can measure and track changes and moving objects between frames by stepping through the different bands of the image. Metadata for each of the video frames, including exact time, duration, and satellite location, is available in the Cloud Optimized GeoTIFF.

### 5.4.4 Legacy SAR Video (VID)

A legacy SAR Video (VID) format can be provided for backward compatibility until *31 December 2026*. This legacy format differs from the current VID product primarily as summarized in Table [5-7](#table-5-7-simplified-comparison-of-the-new-sar-video-vid-and-the-old-legacy-sar-video-vid-formats). Customers are strongly encouraged to migrate to the new Cloud Optimized GeoTIFF VID product to benefit from its enhanced features and performance. ICEYE is available to support customers during this transition. Capacity to deliver images within specific delivery timelines may be reduced when legacy data formats are requested.

##### Table 5-7: Simplified comparison of the new SAR Video (VID) and the old Legacy SAR Video (VID) formats

|                                                     | SAR Video (VID)                                  | Legacy SAR Video (VID)                                 |
| --------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------ |
| Container                                           | Cloud Optimized GeoTIFF, MPEG4, GIF              | GeoTIFF,MPEG4, GIF                                     |
| Metadata format                                     | GeoJSON                                          | XML                                                    |
| File naming convention                              | Regular ([5.6.1](#561-file-naming-convention-1)) | Legacy ([5.6.2](#562-legacy-file-naming-convention-2)) |
| Availability                      | 1Q 2026 | Now; to be deprecated in 2026 with final availability on December 31, 2026. |


## 5.5 On Demand Only Data Products

ICEYE is also able to provide a range of complementary data products that are generated only when specifically requested by a customer. Delivery times for these data products fall outside of the Standard Delivery Time Service Level described in Section [3.7.3](tasking.md#373-delivery-time-service-level). Contact ICEYE via [the ICEYE website](https://www.iceye.com/contact) (or via email if you are already a customer of ICEYE) for more information regarding on demand only Data Products.


### 5.5.1 Sensor Independent Complex Data (SICD) and Sensor Independent Derived Data (SIDD)

The **Sensor Independent Complex Data (SICD)** format is a form of complex data that removes any sensor-specific parameters. SICD image data is in the same format regardless of processing algorithm or collection strategy. In theory, any algorithm that uses SICD will work on SAR imagery from any SAR vendor. The [SICD specification](https://github.com/ngageoint/six-library/wiki/Sensor-Independent-Complex-Data-\(SICD\)-Standard) was developed by the US National Geospatial Intelligence Agency (NGA) and it is stored in the National Imagery Transmission Format (NITF) container.

The **Sensor Independent Derived Data (SIDD)** format is designed to store Synthetic Aperture Radar (SAR) derived image products and associated metadata that is grouped around common tasks for downstream users. It is meant to be used in conjunction with the Sensor Independent Complex Data (SICD) standard to define format standards for SAR image processing. The [SIDD specification](https://github.com/ngageoint/six-library/wiki/Sensor-Independent-Derived-Data-\(SIDD\)-Standard) work is sponsored by NGA.

NGA has released a range of libraries in common environments (e.g. [MATLAB SAR](https://github.com/ngageoint/MATLAB_SAR) for MATLAB and [SarPy](https://github.com/ngageoint/sarpy) for Python; see also the sensor independent XML library [SIX](https://github.com/ngageoint/six-library)) so that tools and algorithms can convert a wide range of SLC formats into SICD and can use SICD files for SAR sensor-independent analysis and visualization.

The SICD and SIDD products are currently only available from ICEYE by request as a custom order. Interested customers are advised to reach out via [the ICEYE website](https://www.iceye.com/contact) (or via email if you are already an ICEYE customer).


### 5.5.2 Compensated Phase History Data (CPHD)

The **Compensated Phase History Data (CPHD)** product provides a sensor-independent [data structure and file format](https://nsgreg.nga.mil/doc/view?i=4638\&month=3\&day=8\&year=2022) for the transmission and storage of SAR Phase History Data (PHD). The [data structure](https://ieeexplore.ieee.org/document/8898868) is designed to accommodate PHD signal arrays from a variety of SAR sensors and supports both monostatic and bistatic SAR imaging data sets. The data is compensated for hardware timing and platform motion. The product includes metadata to describe the collection geometry and the PHD signal arrays contained in the product. The CPHD product is only available from ICEYE by request as a custom order.  Customers interested in purchasing CPHD products should reach out to ICEYE via [the ICEYE website](https://www.iceye.com/contact) (or via email if you are already an ICEYE customer).


### 5.5.3 Orthorectified Imagery

ICEYE does not provide **orthorectified imagery** as part of its standard deliverables, but it can be requested as a custom product. Contact ICEYE Customer Service via [the Contact page at ICEYE website](https://www.iceye.com/contact) (or via email if you are already an ICEYE customer) for more information.


## 5.6 File Naming and Metadata

All ICEYE data products are delivered packaged into one or more files each with informative file names and metadata.

**Metadata** is the term used to describe all the ancillary information about an image that might be important to the user. All the metadata items that are present in ICEYE imagery are described at <https://sar.iceye.com/latest/productFormats/metadata/>

The ICEYE data product **file naming** convention describes the product processing level so that a user does not have to analyze product metadata to understand key properties of the enclosed product. This is intended to facilitate file management. The current file naming convention is described in Section [5.6.1](#561-file-naming-convention-2). A legacy file naming convention continues to be supported in some data products for compatibility, and this is described in Section [5.6.2](#562-legacy-file-naming-convention-3).


### 5.6.1 File Naming Convention

The file naming convention can be described with the following pattern:

    ICEYE_<geohash>_<iso-datetime>_<image-id>_<satellite-id>_<imaging-mode>_<product>.<extension>

Example of data product that follows the file naming convention:

    ICEYE_75CMBF_20240612T174339Z_4119892_X11_SLF_GRD.tif

The components of the file name are described below:

- **geohash:** A hash identifier which helps users to immediately identify the location of the image (please see [GeoHash in wikipedia](https://en.wikipedia.org/wiki/Geohash), as these  [examples](http://geohash.co/) of [conversion tools](https://www.movable-type.co.uk/scripts/geohash.html) ) .

- **iso-datetime**: A string that communicates the date, time and timezone of when the image was collected, formatted according to the ISO 8601 standard.

- **image\_id:** unique identifier for the acquired SAR data  

- **satellite-id**: An identifier of which satellite has performed the collection.

- **imaging-mode**: A string that describes which imaging mode was used for the SAR data collection. The string - imaging mode mapping is as follows:

  - SLH: Spot

  - SLF: Spot Fine

  - SLEA: Spot Extended Area

  - SM: Strip

  - SC: Scan

  - SCW: Scan Wide

  - SLED: Dwell

  - SLEDF: Dwell Fine
  
  - SLEDP: Dwell Precise

- **product**: A string that describes which data product is packaged in the file. The string - data product mapping is as follows:

  - QL: Quicklook

  - GRD: Ground Range Detected

  - SLC: Single Look Complex

  - CSI: Colorized Sub-aperture Image

  - VID: SAR Video

- **extension**: A string that describes the file format. Examples include json and  tif.

The geohash in the file names offers the benefit of automatic sorting of data on file storage directories, with collections of the same or nearby locations automatically grouped next to each other.


### 5.6.2 Legacy File Naming Convention

ICEYE delivers some of its data products utilizing a legacy file naming convention. This naming convention is used by legacy products described in sections 5.2.3 and 5.3.2. The file naming convention can be described with the following pattern:

    ICEYE_<satellite-id>_<product>_<imaging-mode>_<image_id>_<iso-datetime>.<extension>

Example of data product that follows the file naming convention:

    ICEYE_X6_GRD_SM_453426_20231026T060946.tif

The components of the legacy file names are described below:

- **satellite-id**: An identifier of which satellite has performed the collection.

- **imaging-mode**: A string that describes which imaging mode was used for the SAR data collection. See section 5.6.1 for a listing of possible values. 

- **product**: A string that describes which data product is packaged in the file. See section 5.6.1 for a listing of possible values. 

- **image\_id:** unique identifier for the acquired SAR data  

- **iso-datetime**: A string that communicates the date, time and timezone of when the image was collected, formatted according to the ISO 8601 standard.

- **extension**: A string that describes the file format. Examples include json and  tif.

