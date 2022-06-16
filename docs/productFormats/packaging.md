# SAR Data Package

## File Naming
Product file naming convention describes the product processing level so that a user does not have to analyze product metadata to understand key properties. The product filename components are shown in Figure 1. The Product ID is a unique identifier of the acquired scene and is assigned during scene ordering and acquisition. 

<figure markdown>
![placeholder](img/FileNamingConvention.png){width="600"}
<figcaption align = "center"><em>Figure 1: Data product filename components</em></figcaption>
</figure> 
The constituent elements are explained in more detail in  Table 1

<figure markdown>
| CONSTITUENT |	NAME	|VALUE	|NOTES|
|-------------|---------|-------|-----|
|ICEYE_	      | constellation |	ICEYE_	|fixed|
|XN_	|sensor	|X2/X4/X5	|specific sensor that has acquired the scene|
|PPL_	|product processing level	|SLC/GRD	|variant of processing level|
|IM_	|imaging mode	|SM/SMH/SL/SLH	|stripmap, stripmap-high, spotlight, spotlight-high|
|PRID_	|product id	|eg. 6403	|data take ID|
|YYYYMMDD	|UTC start date	|eg. 20190211	|YYYYMMDD format|
|Thhmmss	|UTC start time	|eg. T131415	|Thhmmss format|

<figcaption align = "center"><em>Table 1: Product filename components. Example : ICEYE_X6_GRD_SM_153426_20211026T060946</em></figcaption>
</figure>

## Package Overview
<!-- Earth Observation Products are available in varying processing levels. The levels are defined by the Committee for Earth Observation Satellites[@ceoslevels] as :

* RAW Data - Data in their original packets, as received from a satellite. 
* Level 0 - Reconstructed unprocessed instrument data at full space time resolution with all available supplemental information to be used in subsequent processing (e.g., ephemeris, health and safety) appended. 
* Level 1 - Unpacked, reformatted level 0 data, with all supplemental information to be used in subsequent processing appended. Optional radiometric and geometric correction applied to produce parameters in physical units. Data generally presented as full time/space resolution. A wide variety of sub level products are possible. 
* Level 2 - Retrieved environmental variables (e.g., ocean wave height, soil moisture, ice concentration) at the same resolution and location as the level 1 source data. 
* Level 3 - Data or retrieved environmental variables which have been spatially and/or temporally re-sampled (i.e., derived from level 1 or 2 products). Such re-sampling may include averaging and compositing. 
* Level 4 - Model output or results from analyses of lower level data (i.e., variables that are not directly measured by the instruments, but are derived from these measurements).  -->

<!-- At the moment ICEYE provides its imagery products as CEOS Level 1.  -->

SAR images can be ordered either from archive (previously collected imagery) or as a planned future acquisition. Products are geo-coded and radiometrically corrected.

ICEYE’s focus is currently on the integrity of complex and amplitude images. This will expand over the next year as we introduce a phase history data product and other products derived from complex and amplitude images.
 
A basic ICEYE product is represented by a set of SAR image binary data, corresponding image metadata and it is delivered as a singular product package. Products are characterized by the payload configuration (such as imaging mode and look direction) used by the respective satellite, as well as the level of processing that has been applied to the SAR scene. With respect to the data geometric projection and representation, products are differentiated into two primary types: geo-referenced Single Look Complex (SLC) and Amplitude Images (Also known as Ground Range Detected (GRD) and terrain projected (ORTHO) scenes). SAR image binary data, delivered as digital numbers or quadrature components, can be converted to radar brightness $\beta_0$ and mean radar cross section $\sigma_0$ using the annotated calibration factor in the image metadata.

