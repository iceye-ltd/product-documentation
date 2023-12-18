!!! info 
    The data formats described in this page are available as a preview and can be provided to ICEYE customers upon request. More information in the FAQ. 

We are excited to provide a preview of upcoming new formats for our complex and amplitude data products as well as their corresponding metadata format. These new formats attempt to lower the barriers for getting the maximum value out of ICEYE SAR data: They are more user friendly, and compatible with more GIS and image viewing software and web applications. They also offer easier access to  all the information they contain without the need for specialized scientific tools or advanced SAR knowledge.

## CPX: Complex Image (Preview)

### The challenge with complex data

SAR complex data has traditionally been packaged in scientific or military-intel formats like [SLC](../slc) ([HDF container](../slc#hdf5-container)) or ([SICD](../slc#sensor-independent-complex-data-sicd)) ([NITF container](../slc#sensor-independent-complex-data-sicd)) where each image pixel is stored with in-phase I and quadrature Q components and therefore, contains both amplitude and phase information. These formats require compliant tools and software that is currently difficult to use without specialized skill and experience. For this reason, the user of complex images has been limited to automated processing and advanced exploitation such as interferometric applications, or by users who prefer lower-level processing in order to implement their own processing chains. 

### CPX is complex data in a GeoTiff

CPX images are packaged in the open, international [GeoTiff](https://en.wikipedia.org/wiki/GeoTIFF) format. This enables their easy ingestion and manipulation in most image readers, GIS tools and libraries. The amplitude and phase data is formatted in two GeoTiff bands, similar to how bands are used for multispectral images. Image readers and GIS tools are able to ingest this complex image just like they do any other GeoTiff file. The amplitude band can be immediately presented for viewing, while the phase band is available for further exploitation by more specialized tools. **The key advantage is that the CPX image is at full resolution, so users have access to the full resolution as well as to reduced-speckle, pixel-ageraged views (equivalent to different levels of multi-looking) that are produced instantly when zooming in and out.** 

While the SAR data inside the CPX format is stored in the slant plane (the satellite image acquisition geometry), the metadata in the CPX format contains [RPC values](../../foundations/geospatialAccuracy/#fast-and-simple-geolocation-rapid-positioning-capability) that allows GIS tools to perform automatic ground projection, so they  are ready to be used as part of analysis and exploitation workflows. Please note that Orthorectification using a Digital Elevation Model is still recommended for accurate geospatial comparison and analysis.

THe CPX format uses the [Cloud-Optimized GeoTIFF](https://docs.ogc.org/is/21-026/21-026.html) standard that allows fast data visualization and geospatial processing workflows. GIS applications can efficiently stream or download only the parts of the information they need to visualize or process web-based data. Tiles and overviews are included to enable fast image rendering. CPX files accessed by web applications or stored online can be efficiently streamed and partially downloaded with the use of HTTP range queries. 

<figure markdown>
![placeholder](img/grd_preview.png){width="800"}
<figcaption align = "center"><em>Figure 1: Detail of a Dwell GRD viewed in QGIS. Squared pixels are limited by range resolution </em></figcaption>
![placeholder](img/cpx_preview.png){width="800"}
<figcaption align = "center"><em>Figure 2: Detail of a Dwell CPX viewed in QGIS. Full azimuth resolution visible without the need for scientific viewing software. </em></figcaption>
</figure> 

### Recommended QGIS settings

The following settings are recommended when using [QGIS](https://qgis.org/) to visualize CPX images. They ensure that the correct render type and optimal resampling method is used to display the amplitude band. 

<figure markdown>
![placeholder](img/QGIS-CPX.png){width="800"}
<figcaption align = "center"><em>Figure 3: Recommended QGIS settings for exploiting the CPX format.</em></figcaption>
</figure> 

1. Select <code>Layer Properties -> Symbology</code>
1. Under <code>Band Rendering</code>
    * Render type: <code>Singleband gray</code>
    * Gray band: <code>Band 1 (Gray)</code>
1. Under Contrast enhancement, start with <code>Cumulative count cut 2 - 98%</code>, and adjust if necessary
1. Under Resampling
    * Early resampling: <code>On</code>
    * Zoomed in: <code>Lanczos</code>
    * Zoomed out: <code>Lanczos</code>

**Explanation:** Although CPX image has a single look, QGIS performs [Lanczos averaging](https://en.wikipedia.org/wiki/Lanczos_resampling) when rendering to make the projection correct. This is equivalent to multilooking, but the software is doing it in real time. The user gets the benefit of reduced speckle when zoomed out and the benefit of the finest resolution when zoomed in.

<figure markdown>
![placeholder](img/cpx_dwell_zoomed_out.png){width="800"}
<figcaption align = "center"><em>Figure 4: Zoomed out image showing reduced speckle because of Lanczos averaging (multi-looking) </em></figcaption>
![placeholder](img/cpx_dwell_zoomed_in.png){width="800"}
<figcaption align = "center"><em>Figure 5: Zoomed in image showing speckle but also higher azimuth resolution  </em></figcaption>
</figure> 


## AML: Amplitude Multi-looked Image (Preview)

AML images contain the amplitude part of the backscattering signal. They are a more user friendly implementation of the current [GRD](../grd) format.
The AML format uses the [Cloud-Optimized GeoTIFF standard](https://docs.ogc.org/is/21-026/21-026.html) and offers the following advantages:

* Supported by most image viewing software, GIS applications, data exploitation tools and libraries.
* Allows for faster data visualization and geospatial processing workflows.  Applications can efficiently stream/download only the parts of the information they need to visualize data. Tiles and overviews are included to enable fast image rendering. AML files accessed by web applications or stored online can be efficiently streamed and partially downloaded with the use of HTTP range queries.
* The AML format allows for increased data precision (u32/f32) to support the very high dynamic range of the latest ICEYE data product.
* Defaults to shadows-down data orientation to facilitate interpretation of topography and elevated features


## Metadata 3.0 (Preview)

The metadata of the new CPX and AML image formats is stored in [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) format which is more modern than the XML used to store metadata by the current [SLC](../slc) and [GRD](../grd) formats. GeoJSON is a geocoded metadata format supported by many GIS tools.  

The included satellite orbit metadata can be used to visualize the exact position of the satellite when the SAR data was collected as well as the imaging geometry. 

A JSON schema that can be used for validation purposes is available at the following location:

[https://sar.iceye.com/schema/product-spec/0.0.1/image.json](https://sar.iceye.com/schema/product-spec/0.0.1/image.json) 

<figure markdown>
![placeholder](img/imaging_geometry.png){width="800"}
<figcaption align = "center"><em>Figure 6: Imaging geometry and satellite orbit track can be visualized by opening the AML/CPX metadata files Google Earth Pro</em></figcaption>
</figure> 


## Frequently asked questions

### Are CPX and AML available to ICEYE customers?
Yes, both formats are available as a preview and can be provided to customers upon request. ICEYE encourages customers to try these new product formats and provide us with feedback. We look forward to continuing to develop and improve all our data products.

### Will CPX or AML eventually replace any of the existing formats currently offered by ICEYE?
Based on customer feedback, ICEYE may decide to adjust its product format offering in the future. There is currently no planned timeline for this. 

