# TYPES OF SAR DATA PRODUCTS

## Product Types

SAR data can be made into a multitude of different product types. Some are better suited for human exploitation whereas others are better exploited by algorithms and signal-processing tools.

On this page we describe the different SAR data products that ICEYE provides. Technical details about the format of these products, with some tips on how the use them are provided in the section on ['Techinal Information'](../technical/productFormats/introduction.md).

!!! info

    The section ["What is SAR?"](../technical/foundations/OverviewOfSAR/overviewOfSAR.md) provides a review of the technologies mentioned here. 

<!---
There are three different *levels* of SAR data product:

* RAW RADAR Data
* Single Look Complex imagery
* Multi-looked amplitude imagery
* Orthorectified imagery
-->

<!-- ## RAW RADAR Data -->
<!-- Each satellite transmits many pulses per second (between 2 and 7 thousand) and then listens to their reflections from the Earth's surface. The recorded reflected data forms the basic ingredients of every SAR image. This data is downloaded to the ground and passed through one of ICEYE's image formation processors where it is converted into a SAR image. -->
<!---->
<!-- The image formation processing performed on the raw data can be implemented in many different ways in the same way that a cake can be made from raw ingredients using many different recipes. We try to process the images in a way that is useful to the largest number of customers. If the standard processing is not quite what you want, you have two options: the first is to discuss your needs with our Cusomer Operations and Satellite Planning team who will get the SAR Engineers involved to see how we can help. The second option is to request the RAW SAR pulse data and pass this through your own SAR image formation processor. We provide this data in the US Government sponsored, sensor-agnostic format called 'Compensated Phase History Data' (CPHD).  -->
<!---->
<!-- !!! info -->
<!--     CPHD is particularly useful for governments - especially if they process SAR imagery from other vendors in addition to ICEYE. Controlling how the image is produced allows the images to be precisely compared and combined. It also allows a level of data assurance for the government as the integrity of the individual SAR pulses echoes can be validated. -->


## Complex Images

Unlike optical imagery, each pixel in a SAR image is represented as a *complex number*. The complex number represents two critical components of SAR imaging, *amplitude* and *phase*. The amplitude of a pixel is a measure of the amount of RADAR energy reflected back to the satellite and displayed as a grey-scale value when we look at a SAR image. The phase component is a measure of the position of the RADAR wave after it has interacted with all the scatterers within the pixel. After image formation, the phase information is usually discarded which reduces the size of the SAR image. Some advanced SAR capabilities such as interferometric SAR (INSAR) or coherent change detection (CCD) makes use of the phase information and therefore needs the complex image samples.

All ICEYE images are available as Complex Datasets (with the exception of SCAN mode collections). More details about complex image file formats can be found in the ['Technical Information'](../technical/productFormats/slc.md) section.

<!---
<span style="color:darkred">[TODO] make animation showing the nature of a complex image </span>.


### IQ Image Format
The conventional way of storing complex imagery is know as the *IQ Format*. In this format, each pixel is stored as two values, one called '*I*' (standing for 'In-phase') and one called '*Q*' (standing for 'Quadrature'). Because the format does not directly store the amplitude imformation, then a conversion must be made to view the image. Being a well understood standard however, there are many tools, often open-source, that can be used to help with IQ image operations. (eg SNAP[@snap]).

### CPX Image Format
In order to make the complex data more accessible to users, ICEYE has developed a new file format called '**CPX**'. Unlike the *IQ* format, which requires specialist tools to view the information, the CPX format uses a regular geoTiff container so the image can be viewed by normal (and geospatial) image viewers. The file contains two bands; the first contains the amplitude data of the scene (so that anyone openining the file will be able to recognise that it is a SAR image). The second band contains the phase information that can be exploited in the usual way.
-->

!!! Warning 
    Complex images, by their nature, are always *single-look*. This means that they contain the *native* resolution of the collection. ICEYE satellites always collect much finer resolution in the azimuth direction than the range direction. (eg a SPOT image has an azimuth resolution of 25cm whereas the slant range resolution is 50cm.) We also save our complex images in the slant-plane. This means that if you view the image in a picture viewing package (eg GIMP), the image will appear distorted as the square pixels on your screen are actually representing rectangular pixels on the ground. ICEYE CPX images also have a full geotif header and contain RPCs so any GIS viewer (eg QGIS) will render the image correctly on your screen. This is the best way to  view the finest resolution in ICEYE SAR images.

### Complex Image Parameters
<figure markdown>
| PARAMETER                                            | STRIP              | SPOT               | SPOT FINE | DWELL | COMMENTS                          |
|------------------------------------------------------|--------------------|--------------------|-----------|-------|-----------------------------------|
| Focusing plane                                       |  Slant Plane       | Slant Plane        | Slant Plane | Slant Plane |                           |
| Slant range resolution [m]                           | 0.5 to 2.5         | 0.5                | 0.25 | 0.5 | [Note 1](#notes-and-explanations) |
| Slant azimuth resolution [m]                         | 3                  | 0.25               | 0.1 | 0.05 |                           |
| Impulse response weighing function (peak side level) | Uniform (-13.3dB)  | Uniform (-13.3dB)  | Uniform (-13.3dB) | Uniform (-13.3dB) |                                  |
| Slant Range Sample Spacing [m]                       | 0.4 to 2.4         | < 0.4              | < 0.2 | < 0.4 | [Note 1](#notes-and-explanations) | 
| Slant Azimuth Sample Spacing [m]                     | 1.6                | < 0.2              | < 0.09 | < 0.05 |                             |
| Slant range product format                           | HDF5 + XML         | HDF5 + XML         | HDF5 + XML | HDF5 + XML |                                  |
| SLC Product Size [GB]                                | 3.4 to 2.9         | 0.6 to 7.2         |  < 15  | < 15 |                                |
| Dynamic Range (bits per pixel)                       | 16(uint) 32(Float) | 16(uint) 32(Float) | 16(uint) 32(Float)  | 16(uint) 32(Float) | [Note 3](#notes-and-explanations)| 
<figcaption align = "center"><em>Table 1 : Parameters for ICEYE Complex Images</em></figcaption>
</figure>

<!---
## Multi-looked Amplitude Images

Once the complex SAR image has been formed, additional processing is applied to make it as useful as possible for human exploitation. The image is first *mult

<span style="color:darkred">[TODO] make animation showing multi-looking. </span>.


## Orthorectified imagery

SAR complex images contain pixels that have both amplitude and phase values. They are produced at full resolution and are projected in the inclined direction of illumination, called the slant plane. Since complex images retain phase information, they can be used to produce numerous SAR products like coherent change images and precise surface motion measurements.
-->

!!! info
    Complex Images are used for 'interferometric SAR' such as the formation of digital elevation models (DEM), land subsidence monitoring or coherent change analysis.

## Amplitude Images

These are the familiar SAR gray-scale images with amplitude-only pixels. They are “multi-looked” to reduce the grainy effect of speckle, at the cost of slightly lower resolution. Amplitude images are projected to the ground surface and can be oriented with respect to the sensor or produced on an ellipsoid-based map projection. ICEYE produces amplitude images in the natural range-azimuth sensor orientation because they offer the most flexibility in exploitation. To be consistent with conventional terminology, these sensor-oriented images are called Ground Range Detected (GRD). This term may change in the future to be something more meaningful.

!!! info
    Amplitude images are most useful for rapid observation of a location regardless of lighting or weather conditions.



## Amplitude Image Parameters
<figure markdown>
| PARAMETER                                            | STRIP                    | SPOT/ SPOT EXTENDED AREA / DWELL                     | SPOT FINE               | SCAN                     | COMMENTS                           |
|------------------------------------------------------|--------------------------|--------------------------|-------------------------|--------------------------|------------------------------------|
| Nominal Ground Resolution [m]                          | 3                      | 1               | 0.5             | 15                     |  [Note 2](#notes-and-explanations) |
| Ground Range Resolution [m]                          | < 3                      | 1.5 to 0.9               | 0.73 to 0.43            | < 15                     |  [Note 1](#notes-and-explanations) |
| Ground Azimuth Resolution [m]                        | < 3                      | < 1                      | < 0.5                   | < 15                     |                                    |
| Impulse response weighing function (peak side level) | Taylor Weighting (-20dB) | Taylor Weighting (-20dB) | Taylor Weighting (-20dB)| Taylor Weighting (-20dB) |                                    |
| Ground Range Sample Spacing [m]                      | 2.5                      | 0.5                      | 0.25                    | 6                        |                                    |
| Ground Azimuth Sample Spacing [m]                    | 2.5                      | 0.5                      | 0.25                    | 6                        |                                    |
| Range Looks                                          | 1                        | 1                        | 1                       | 1                        |                                    |
| Azimuth Looks                                        | 1 to 2                   | 1 to 20                  | 5                       |  1                        |     [Note 3](#notes-and-explanations)                               |
| Product format                                       | Geotiff + XML            | Geotiff + XML            | Geotiff + XML           | Geotiff + XML            |                                    |
| GRD Product Size [MB]                                | 700                      | 250 to 1500                     | < 2500                  | 800                      |                                    |
| Dynamic Range (bits per pixel)                       | 16(uint) 32(Float)       | 16(uint) 32(Float)       | 16(uint) 32(Float)      | 16(uint) 32(Float)       | [Note 4](#notes-and-explanations) |
<figcaption align = "center"><em>Table 2 : Parameters for ICEYE Amplitude Images</em></figcaption>
</figure>

-----

## Notes and Explanations
1. **Slant Range Resolution:** For Strip mode the transmitted bandwidth is varied to make sure that the resolution on the ground remains the same. For Spot mode the maximum bandwidth is transmitted at all times. This means that the slant resolution for Spot images is constant and the ground resolution changes with incidence angle.
2. **Nominal Ground Resolution:**  Nominal ground resolution for all Spotlight modes (Spot, Spot Entended Area, Dwell and Spot fine) is the ground resolution at a 30° incidence angle. 
3. **Azimuth Looks:** Spot amplitude images are produced using 4 looks, Spot Extended Area 1 to 2 looks, and Dwell 20 looks.
4. **Complex Dynamic Range:** A complex number with 16bit I and 16bit Q values. 32 bit float values can be provided by request.


## References
\bibliography
