# Levels of SAR Data
## UNDER CONSTRUCTION

<figure>
<img src="../img/underconstruction.png" style="width:100%">
<figcaption align = "center"><em>Its on the backlog.....</em></figcaption>
</figure>
Earth Observation Products are available in varying processing levels. The levels are defined by the Committee for Earth Observation Satellites[@ceoslevels] as :

* RAW Data - Data in their original packets, as received from a satellite. 
* Level 0 - Reconstructed unprocessed instrument data at full space time resolution with all available supplemental information to be used in subsequent processing (e.g., ephemeris, health and safety) appended. 
* Level 1 - Unpacked, reformatted level 0 data, with all supplemental information to be used in subsequent processing appended. Optional radiometric and geometric correction applied to produce parameters in physical units. Data generally presented as full time/space resolution. A wide variety of sub level products are possible. 
* Level 2 - Retrieved environmental variables (e.g., ocean wave height, soil moisture, ice concentration) at the same resolution and location as the level 1 source data. 
* Level 3 - Data or retrieved environmental variables which have been spatially and/or temporally re-sampled (i.e., derived from level 1 or 2 products). Such re-sampling may include averaging and compositing. 
* Level 4 - Model output or results from analyses of lower level data (i.e., variables that are not directly measured by the instruments, but are derived from these measurements). 

At the moment ICEYE provides its imagery products as CEOS Level 1. These can be ordered either from archive (previously collected imagery) or as future acquisitions by contacting ICEYE’s [Customer Operations and Satellite Planning team](mailto:customer@iceye.com). Products are geo-coded and radiometrically corrected.
 
ICEYE’s main focus is currently on the development of high integrity level 1 products with some level 2 products being obtained through second party applications. This will gradually evolve over the next year as processing modes and calibration metrics evolve with new level 0 and level 2 products being provided by the ICEYE processing architecture. 

A basic ICEYE product is represented by a set of SAR image binary data, corresponding image metadata and delivered as a singular product package. Products are characterized by the payload configuration (such as imaging mode and look direction) used by the respective satellite, as well as the level of processing that has been applied to the SAR scene. With respect to the data geometric projection and representation, Level 1 products are differentiated into two primary product types: geo-referenced Single Look Complex (SLC) and Amplitude Images (Also known as Ground Range Detected (GRD) scenes). SAR image binary data, delivered as digital numbers or quadrature components, can be converted to radar brightness $\beta_0$ and mean radar cross section $\sigma_0$ using the annotated calibration factor in the image metadata (further instruction can be found here).  


## References
\bibliography