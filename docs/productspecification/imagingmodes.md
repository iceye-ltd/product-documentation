# 2.  Imaging Modes

## 2.1 Introduction

ICEYE offers several **Imaging Modes** to suit a wide range of applications. Refer to Table [2-1](#table-2-1-summary-of-iceye-imaging-modes) for a high-level summary of these imaging modes.  Table [2-1](#table-2-1-summary-of-iceye-imaging-modes-1) tabulates the ground resolution, geospatial accuracy, scene size, information density, and number of azimuth looks for each imaging mode.


##### _Table 2-1: Summary of ICEYE imaging modes_

| Service level                        |               Spot              |            Spot Fine            |        Spot Extended Area       |               Dwell               |             Dwell Fine            |                 Strip                |                   Scan                  |
| ------------------------------------ | :-----------------------------: | :-----------------------------: | :-----------------------------: | :-------------------------------: | :-------------------------------: | :----------------------------------: | :-------------------------------------: |
| Ground Resolution \[m]               |                1                |               0.5               |                1                |                 1                 |                0.5                |                   3                  |                    15                   |
| Geospatial Accuracy \[m RMSE]        |                6                |                6                |                6                |                 6                 |                 6                 |                   6                  |                    15                   |
| Scene Size \[range x azimuth, in km] |              5 x 5              |              5 x 5              |             15 x 15             |               5 x 5               |               5 x 5               | 30 x 50Up to30 x 840 (custom option) | 100 x 100Up to100 x 840 (custom option) |
| Information Density \[bits/m2]       |                22               |                83               |               8.4               |                125                |                185                |                  0.8                 |                   0.1                   |
| Number of  Azimuth Looks             |                4                |                5                |                2                |                 20                |                 10                |                   1                  |                    1                    |
| Section Reference                    | [2.2](#22-spot-and-spot-fine-1) | [2.2](#22-spot-and-spot-fine-2) | [2.3](#23-spot-extended-area-1) | [2.4](#24-dwell-and-dwell-fine-1) | [2.4](#24-dwell-and-dwell-fine-2) |          [2.5](#25-strip-1)          |            [2.6](#26-scan-1)            |

**Geospatial Accuracy** refers to the accuracy with which a point in an ICEYE satellite image agrees with a true reference on the ground. Geospatial Accuracy here is evaluated as a statistical value: Each satellite in the ICEYE fleet is periodically evaluated against ground based calibration targets to obtain the geospatial accuracy of the system. This process involves measuring the location of each target in the SAR imagery after the image has been terrain corrected, and comparing each location to their known ground truth. Each calibration target will have its own slightly different error. The numeric value indicating Geospatial Accuracy in Table [2-1](#table-2-1-summary-of-iceye-imaging-modes-2) above is the Root Mean Square Error (RMSE) of all the measured calibration points from all the satellites, as meters. Note that the geospatial accuracy of a SAR image is a function of the accuracy of the terrain model used. Especially in high elevation terrains significant distortion can impact the accuracy. This means the values in this table cannot be guaranteed for every Digital Elevation Model (DEM) available. Moreover, irrespective of the DEM used, accuracy is decreased in high elevation areas due to geometric distortion.

The **Information Density** figures tabulated in Table [2-1](#table-2-1-summary-of-iceye-imaging-modes-3) describe the number of bits of imaging data per scene square meter. In principle, higher information densities offer potential for superior interpretability of an image. Larger scene sizes tend to have lower resolution and therefore lower information density. Also, for fixed scene size, e.g., 5 km x 5 km, higher information density products tend to have larger file sizes (see e.g. SLC Product Size rows in e.g. Table [2-5](#table-2-5-product-attributes-for-spot-and-spot-fine-complex-data-products)).

For more information about each mode presented in Table [2-1](#table-2-1-summary-of-iceye-imaging-modes-4), please follow the subsection references tabulated onto the last row.

Each imaging mode subsection has one of each of the following tables:

- **Tasking parameter** tables provide the standard collection parameters applied to create the desired mode. These parameters are an _input_ governing how the collection is performed (see Table [2-2](#table-2-2-tasking-parameters-for-standard-iceye-imaging-modes-for-spot-and-spot-fine) for an example). These tables describe parameters relating to the number of radar beams used, scene sizes, collection durations, and incidence angle ranges. Collections satisfying these criteria should result in products that satisfy the product specification.

- **Collection performance attribute** tables describe the expected features of the resulting imagery when the performant tasking parameters for the imaging mode in question are utilized (see Table [2-3](#table-2-3-collection-performance-attributes-for-spot-and-spot-fine-imaging-modes) for an example). These tables describe technical parameters related mostly to image quality and accuracy. Collection performance attributes will not be achieved for images that are tasked outside of the performant tasking parameters for each imaging mode, for example when images are tasked outside of their performant incidence angle range.

- **Data product attribute** tables describe attributes that are specific to the amplitude and complex data products that are generated with the collected SAR data. The ICEYE imaging modes can be used to generate both amplitude and complex data products and therefore these are described in **product attributes for amplitude data products**, and **product attributes for complex data products** tables, respectively (see Tables [2-4](#table-2-4-product-attributes-for-spot-and-spot-fine-amplitude-data-products) and [2-5](#table-2-5-product-attributes-for-spot-and-spot-fine-complex-data-products-1) for examples). No complex data product attribute tables are provided for the Scan imaging mode, which is only offered as an amplitude data product.

ICEYE endeavors to continuously improve the performance of its SAR products. The values for attributes and parameters in this specification communicate the minimum performance values of our standard products across the current fleet at the time of publication. Note that values are approximate and may vary with image imaging mode, incidence angle, and contents of scene.

Finally, many parameters, and performance and product attributes in this section deserve a detailed explanation in order to ensure they are properly understood. The [Glossary](#glossary) at the end of this document provides many of the most important definitions. More information is available in [ICEYE SAR 101 pages](https://sar.iceye.com/latest/foundations/OverviewOfSAR/overviewOfSAR/).


##

## 2.2 Spot and Spot Fine

In the Spotlight collection strategy, the radar beam is steered to illuminate a fixed point for an extended period of time. This increases the illumination time and also increases the effective length of the synthetic aperture and therefore improves azimuth resolution.

![](https://github.com/iceye-ltd/product-documentation/releases/download/additional-assets/spot.png)

ICEYE **Spot** and **Spot Fine** imaging modes employ the Spotlight collection strategy. Spot collections are performed with a 300 MHz pulse bandwidth to achieve a 0.5 m slant range resolution. ICEYE Gen2 and Gen3 satellites are both capable of Spot collections. Spot Fine collections are performed with a 600 MHz (see Section [1.4](introduction.md#14-satellites-and-sensors)) pulse bandwidth to achieve a 0.25m slant range resolution. Currently, only Gen3 satellites are capable of Spot Fine collections. In both cases, the “ground range detected” resolution degrades the resolution by a geometric factor as explained in Section [1.4](introduction.md#14-satellites-and-sensors) and thus the ground range detected resolutions of Spot and Spot Fine are 1 m and 50 cm, respectively (see “Ground Range Resolution” in Table [2-4](#table-2-4-product-attributes-for-spot-and-spot-fine-amplitude-data-products)).

ICEYE Spot and Spot Fine imaging modes cover an area of 5 km x 5 km for multi-looked amplitude images. These are formed from multiple independent looks to suppress speckle noise and to increase image quality and interpretability (4 looks  in case of Spot, and 5 in case of Spot Fine).

Having very high resolution, Spot and Spot Fine  images are useful for detailed investigation of an area. They are used primarily to discriminate between different types of objects such as vessels, aircraft, buildings and infrastructure.

ICEYE aims to ensure that the the resulting imagery for tasks collected with the Spot and Spot Fine imaging modes within the tasking parameters listed in Table [2-2](#table-2-2-tasking-parameters-for-standard-iceye-imaging-modes-for-spot-and-spot-fine) (excluding Time Dominant Incidence Range) will have the collection performance tabulated in Table [2-3](#table-2-3-collection-performance-attributes-for-spot-and-spot-fine-imaging-modes) and product attributes listed in Tables [2-4](#table-2-4-product-attributes-for-spot-and-spot-fine-amplitude-data-products) and [2-5](#table-2-5-product-attributes-for-spot-and-spot-fine-complex-data-products), for amplitude and complex data products respectively.


##### _Table 2-2: Tasking parameters for standard ICEYE imaging modes for Spot and Spot Fine_

|             Parameter \ Imaging Mode |    Spot    |  Spot Fine |
| -----------------------------------: | :--------: | :--------: |
|                Radar Beams Used \[#] |      1     |      1     |
|            Nominal Scene Width \[km] |      5     |      5     |
|           Nominal Scene Length \[km] |      5     |      5     |
|           Maximum Scene Length \[km] |      5     |      5     |
|   Nominal Collection Duration \[sec] |     10     |     15     |
|   Maximum Collection Duration \[sec] |     10     |     15     |
|                         Polarization |     VV     |     VV     |
|    Performant Incidence Range \[deg] |    20-40   |    20-40   |
| Time Dominant Incidence Range \[deg] |    5-45    |    5-45    |
|            Squint Angle Range \[deg] | -45 to +45 | -45 to +45 |


##### _Table 2-3: Collection performance attributes for Spot and Spot Fine imaging modes_

|                  Attribute \ Imaging Mode |    Spot    |  Spot Fine |
| ----------------------------------------: | :--------: | :--------: |
|    Noise Equivalent Sigma-Zero \[dBm2/m2] | -18 to -15 | -18 to -11 |
|             Azimuth Ambiguity Ratio \[dB] |     -17    |     -17    |
|               Range Ambiguity Ratio \[dB] |     -20    |     -20    |
|             Geospatial Accuracy \[m RMSE] |      6     |      6     |
| ESA Copernicus Contributing Mission Class |    VHR1    |    VHR1    |
|                                    RNIIRS |     5.5    |     6.3    |
|                          RGIQE \[bits/m²] |     22     |     83     |


#####

##### _Table 2-4: Product attributes for Spot and Spot Fine amplitude data products_

|                                                 Product Attribute |                          Spot                         |                       Spot Fine                       |
| ----------------------------------------------------------------: | :---------------------------------------------------: | :---------------------------------------------------: |
|                                    Nominal Ground Resolution \[m] |                           1                           |                          0.5                          |
|                                      Ground Range Resolution \[m] |                      1.46 - 0.78                      |                      0.73 - 0.39                      |
|                                    Ground Azimuth Resolution \[m] |                           <1                          |                          <0.5                         |
|                                                  Range Looks \[#] |                           1                           |                           1                           |
|                                                Azimuth Looks \[#] |                           4                           |                           5                           |
|              Impulse Response Weighing Function (peak side level) |                Taylor Weighting (-20dB)               |                Taylor Weighting (-20dB)               |
|                                  Ground Range Sample Spacing \[m] |                          0.5                          |                          0.25                         |
|                                Ground Azimuth Sample Spacing \[m] |                          0.5                          |                          0.25                         |
| Product Format(see section [5](#5-data-products-4) for more info) | Cloud Optimized GeoTIFF + JSON(legacy: GeoTIFF + XML) | Cloud Optimized GeoTIFF + JSON(legacy: GeoTIFF + XML) |
|                                            GRD Product Size \[MB] |                      250 to 1500                      |                      2000 to 3500                     |
|                                   Dynamic Range \[bits per pixel] |                  16 (uint) 32 (float)                 |                  16 (uint) 32 (float)                 |
|                                        Radiometrically Calibrated |                          Yes                          |                          Yes                          |


#####

##### _Table 2-5: Product attributes for Spot and Spot Fine complex data products_

|                                                             Product Attribute |                        Spot                        |                      Spot Fine                     |
| ----------------------------------------------------------------------------: | :------------------------------------------------: | :------------------------------------------------: |
|                                                                Focusing Plane |                     Slant Plane                    |                     Slant Plane                    |
|                                                  Slant Range Resolution \[m]  |                         0.5                        |                        0.25                        |
|                                                 Slant Azimuth Resolution \[m] |                        0.25                        |                         0.1                        |
|                          Impulse Response Weighing Function (peak side level) |                 Uniform (-13.3 dB)                 |                  Uniform (-13.3dB)                 |
|                                               Slant Range Sample Spacing \[m] |                        < 0.4                       |                        < 0.2                       |
|                                             Slant Azimuth Sample Spacing \[m] |                        < 0.2                       |                       < 0.09                       |
| Slant Range Product Format(see section [5](#5-data-products-5) for more info) | Cloud Optimized GeoTIFF + JSON(legacy: HDF5 + XML) | Cloud Optimized GeoTIFF + JSON(legacy: HDF5 + XML) |
|                                                    Complex Product Size \[GB] |                      0.6 to 4                      |                       5 to 15                      |
|                                                Dynamic Range (bits per pixel) |                16 (uint) 32 (float)                |                16 (uint) 32 (float)                |


## 2.3 Spot Extended Area

In **Spot Extended Area** (**SLEA**) mode a Spotlight image is taken by pointing the satellite at a location farther away, instead of at a point on the ground. The radar beam 'slides' over the ground to cover a larger area; which is why SLEA is also known as Sliding Spot mode. This means that more area is imaged than in Spot mode.However, the trade-off is that each pixel in the image is illuminated from varying angles as the beam moves, leading to a reduction in image resolution compared to the standard Spot mode. To mitigate this resolution loss, the spotlight operation is extended by utilizing a slightly longer illumination time. This way, the imaging process captures information over the extended area, helping to preserve the resolution.

As described in Table [2-6](#table-2-6-tasking-parameters-for-the-slea-imaging-mode), the maximum scene size for SLEA is 15 km x 15 km and within the covered area a 1 m ground resolution can be achieved for multi-looked amplitude images. In comparison to the Spot mode, we trade off a number of looks for extra surface area. The Spot mode has 4 looks while SLEA has 2 looks instead. Due to the fewer looks, the speckle noise in the imagery is slightly higher. SLEA is typically used for similar applications as Spot but is chosen when the exact location of the objects to be monitored is less certain or where a wider area coverage is desired for situational awareness.

ICEYE aims to ensure that the resulting imagery for tasks collected with the SLEA imaging mode within the tasking parameters listed in Table [2-6](#table-2-6-tasking-parameters-for-the-slea-imaging-mode) (excluding Time Dominant Incidence Range) will have the collection performance tabulated in Table [2-7](#table-2-7-collection-performance-attributes-for-the-slea-imaging-mode) and product attributes listed in Tables [2-8](#table-2-8-product-attributes-for-slea-amplitude-data-products) and [2-9](#table-2-9-product-attributes-for-slea-complex-data-products), for amplitude and complex data products respectively.


##### _Table 2-6: Tasking parameters for the SLEA  imaging mode_

|             Parameter \ Imaging Mode |  SLEA |
| -----------------------------------: | :---: |
|                Radar Beams Used \[#] |   1   |
|            Nominal Scene Width \[km] |   15  |
|           Nominal Scene Length \[km] |   15  |
|           Maximum Scene Length \[km] |   15  |
|   Nominal Collection Duration \[sec] |   10  |
|   Maximum Collection Duration \[sec] |  10   |
|                         Polarization |   VV  |
|    Performant Incidence Range \[deg] | 20-40 |
| Time Dominant Incidence Range \[deg] |  5-45 |


#####

##### _Table 2-7: Collection performance attributes for the SLEA imaging mode_

|                  Attribute \ Imaging Mode |    SLEA    |
| ----------------------------------------: | :--------: |
|    Noise Equivalent Sigma-Zero \[dBm2/m2] | -18 to -15 |
|             Azimuth Ambiguity Ratio \[dB] |     -17    |
|               Range Ambiguity Ratio \[dB] |     -20    |
|             Geospatial Accuracy \[m RMSE] |      6     |
| ESA Copernicus Contributing Mission Class |    VHR1    |
|                          RGIQE \[bits/m²] |     8.4    |


#####

##### _Table 2-8: Product attributes for SLEA amplitude data products_

|                                                 Product Attribute |                          SLEA                         |
| ----------------------------------------------------------------: | :---------------------------------------------------: |
|                                    Nominal Ground Resolution \[m] |                           1                           |
|                                      Ground Range Resolution \[m] |                       1.5 - 0.9                       |
|                                    Ground Azimuth Resolution \[m] |                           <1                          |
|                                                  Range Looks \[#] |                           1                           |
|                                                Azimuth Looks \[#] |                           2                           |
|              Impulse Response Weighing Function (peak side level) |                Taylor Weighting (-20dB)               |
|                                  Ground Range Sample Spacing \[m] |                          0.5                          |
|                                Ground Azimuth Sample Spacing \[m] |                          0.5                          |
| Product Format(see section [5](#5-data-products-6) for more info) | Cloud Optimized GeoTIFF + JSON(legacy: GeoTIFF + XML) |
|                                            GRD Product Size \[MB] |                       1000-6500                       |
|                                   Dynamic Range \[bits per pixel] |                  16 (uint) 32 (float)                 |
|                                        Radiometrically Calibrated |                          Yes                          |


##### _Table 2-9: Product attributes for SLEA complex data products_

|                                                             Product Attribute |                        SLEA                        |
| ----------------------------------------------------------------------------: | :------------------------------------------------: |
|                                                                Focusing Plane |                     Slant Plane                    |
|                                                  Slant Range Resolution \[m]  |                         0.5                        |
|                                                 Slant Azimuth Resolution \[m] |                         0.5                        |
|                          Impulse Response Weighing Function (peak side level) |                  Uniform (-13.3dB)                 |
|                                               Slant Range Sample Spacing \[m] |                        < 0.4                       |
|                                             Slant Azimuth Sample Spacing \[m] |                        <0.5                        |
| Slant Range Product Format(see section [5](#5-data-products-7) for more info) | Cloud Optimized GeoTIFF + JSON(legacy: HDF5 + XML) |
|                                                    Complex Product Size \[GB] |                       6 to 15                      |
|                                                Dynamic Range (bits per pixel) |                16 (uint) 32 (float)                |


##

## 2.4 Dwell and Dwell Fine

ICEYE **Dwell** and **Dwell Fine** imaging modes are based on a Spotlight collection strategy that utilizes a very long illumination period of 25 seconds; as opposed to a 10 seconds illumination period for Spot. This long illumination period results in very fine azimuth resolution and highly reduced speckle because of multi-looking (20 and 10 looks for Dwell and Dwell Fine respectively). With its small, agile satellite bus baseline, ICEYE is uniquely equipped to achieve such extended illumination periods.

![](https://github.com/iceye-ltd/product-documentation/releases/download/additional-assets/dwell.png)

Applying conventional image formation techniques to this type of SAR collection results in a very fine azimuth resolution and significantly more information density than Spot images. To facilitate the exploitation of this imaging mode, ICEYE offers not only the full resolution [Single Look Complex (SLC)](dataproducts.md#531-single-look-complex-slc-image) and ground projected [Ground Range Detected](dataproducts.md#522-ground-range-detected-grd-image-2) data products but also the novel [Colorized Sub-Aperture Image (CSI)](#541-colorized-sub-aperture-image-csi) and [SAR Video (VID)](#542-sar-video-vid) amplitude data products, all of which are described in Section [5](dataproducts.md#5-data-products). The CSI images and VID products are especially useful for detecting human-made structures and objects such as vehicles and equipment (even if partially obscured by vegetation) as well as to analyze movement.

ICEYE aims to ensure that the resulting imagery for tasks collected with the Dwell and Dwell Fine imaging modes within the tasking parameters listed in Table [2-10](#table-2-10-tasking-parameters-for-standard-iceye-imaging-modes-for-dwell-and-dwell-fine) (excluding Time Dominant Incidence Range) will have the collection performance tabulated in Table [2-11](#table-2-11-collection-performance-attributes-for-dwell-and-dwell-fine-imaging-modes) and product attributes listed in Tables [2-12](#table-2-12-product-attributes-for-dwell-and-dwell-fine-amplitude-data-products) and [2-13](#table-2-13-product-attributes-for-dwell-and-dwell-fine-complex-data-products), for amplitude and complex data products respectively.


##### _Table 2-10: Tasking parameters for Standard ICEYE imaging modes for Dwell and Dwell Fine_

|             Parameter \ Imaging Mode |    Dwell   | Dwell Fine |
| -----------------------------------: | :--------: | :--------: |
|                Radar Beams Used \[#] |      1     |      1     |
|            Nominal Scene Width \[km] |      5     |      5     |
|           Nominal Scene Length \[km] |      5     |      5     |
|           Maximum Scene Length \[km] |      5     |      5     |
|   Nominal Collection Duration \[sec] |     25     |     25     |
|   Maximum Collection Duration \[sec] |     25     |     25     |
|                         Polarization |     VV     |     VV     |
|    Performant Incidence Range \[deg] |    20-40   |    20-40   |
| Time Dominant Incidence Range \[deg] |    5-45    |    5-45    |
|            Squint Angle Range \[deg] | -45 to +45 | -45 to +45 |


#####

##### _Table 2-11: Collection performance attributes for Dwell and Dwell Fine imaging modes_

|                  Attribute \ Imaging Mode |    Dwell   | Dwell Fine |
| ----------------------------------------: | :--------: | :--------: |
|    Noise Equivalent Sigma-Zero \[dBm2/m2] | -18 to -15 | -18 to -15 |
|             Azimuth Ambiguity Ratio \[dB] |     -17    |     -17    |
|               Range Ambiguity Ratio \[dB] |     -20    |     -20    |
|             Geospatial Accuracy \[m RMSE] |      6     |      6     |
| ESA Copernicus Contributing Mission Class |    VHR1    |    VHR1    |
|                                    RNIIRS |     6.4    |     6.7    |
|                          RGIQE \[bits/m²] |     125    |     185    |


#####

##### _Table 2-12: Product attributes for Dwell and Dwell Fine amplitude data products_

|                                                 Product Attribute |                         Dwell                         |                       Dwell Fine                      |
| ----------------------------------------------------------------: | :---------------------------------------------------: | :---------------------------------------------------: |
|                                    Nominal Ground Resolution \[m] |                           1                           |                          0.5                          |
|                                      Ground Range Resolution \[m] |                       1.5 - 0.9                       |                      0.73 - 0.43                      |
|                                    Ground Azimuth Resolution \[m] |                           <1                          |                          <0.5                         |
|                                                  Range Looks \[#] |                           1                           |                           1                           |
|                                                Azimuth Looks \[#] |                           20                          |                           10                          |
|              Impulse Response Weighing Function (peak side level) |                Taylor Weighting (-20dB)               |                Taylor Weighting (-20dB)               |
|                                  Ground Range Sample Spacing \[m] |                          0.5                          |                          0.25                         |
|                                Ground Azimuth Sample Spacing \[m] |                          0.5                          |                          0.25                         |
| Product Format(see section [5](#5-data-products-9) for more info) | Cloud Optimized GeoTIFF + JSON(legacy: GeoTIFF + XML) | Cloud Optimized GeoTIFF + JSON(legacy: GeoTIFF + XML) |
|                                            GRD Product Size \[MB] |                      500 to 1500                      |                      1000 to 3500                     |
|                                   Dynamic Range \[bits per pixel] |                  16 (uint) 32 (float)                 |                  16 (uint) 32 (float)                 |
|                                        Radiometrically Calibrated |                          Yes                          |                          Yes                          |


##### _Table 2-13: Product attributes for Dwell and Dwell Fine complex data products_

|                                                              Product Attribute |                        Dwell                       |                     Dwell Fine                     |
| -----------------------------------------------------------------------------: | :------------------------------------------------: | :------------------------------------------------: |
|                                                                 Focusing Plane |                     Slant Plane                    |                     Slant Plane                    |
|                                                   Slant Range Resolution \[m]  |                         0.5                        |                        0.25                        |
|                                                  Slant Azimuth Resolution \[m] |                        0.05                        |                        0.05                        |
|                           Impulse Response Weighing Function (peak side level) |                  Uniform (-13.3dB)                 |                  Uniform (-13.3dB)                 |
|                                                Slant Range Sample Spacing \[m] |                        < 0.4                       |                        < 0.2                       |
|                                              Slant Azimuth Sample Spacing \[m] |                       < 0.05                       |                       < 0.05                       |
| Slant Range Product Format(see section [5](#5-data-products-10) for more info) | Cloud Optimized GeoTIFF + JSON(legacy: HDF5 + XML) | Cloud Optimized GeoTIFF + JSON(legacy: HDF5 + XML) |
|                                                     Complex Product Size \[GB] |                       8 to 15                      |                      10 to 24                      |
|                                                 Dynamic Range (bits per pixel) |                16 (uint) 32 (float)                |                16 (uint) 32 (float)                |


##

## 2.5 Strip

In the Strip imaging mode the ground swath is illuminated with a continuous sequence of pulses while the antenna beam is fixed in its orientation. The beam is pointed off to the side of the satellite at an angle broadside to the satellite flight path. This results in a long image strip parallel to the flight direction.

![](https://github.com/iceye-ltd/product-documentation/releases/download/additional-assets/strip.png)

ICEYE **Strip** products have a ground resolution of 3 m in range and azimuth and cover an area of 30 km (range) by 50 km (azimuth). The strip length can be extended to as much as 840 km in azimuth if requested as part of a custom order.

Having large area coverage and a moderate resolution, Strip images are useful for situational awareness applications. They allow a user to quickly assess what is occurring in the region. They are particularly useful for tasks such as deforestation monitoring, or sea ice monitoring. Strip is commonly used as a 'first responder' product in times of natural disaster to assess the impact of a flood, earthquake or volcano.

ICEYE aims to ensure that the resulting imagery for tasks collected with the Strip imaging mode within the tasking parameters listed in Table [2-14](#table-2-14-tasking-parameters-for-the-strip-imaging-mode) (excluding Time Dominant Incidence Range) will have the collection performance tabulated in Table [2-15](#table-2-15-collection-performance-attributes-for-the-strip-imaging-mode) and product attributes listed in Tables [2-16](#table-2-16-product-attributes-for-strip-amplitude-data-products) and [2-17](#table-2-17-product-attributes-for-strip-complex-data-products), for amplitude and complex data products respectively.


##### _Table 2-14: Tasking parameters for the Strip  imaging mode_

|             Parameter \ Imaging Mode | Strip |
| -----------------------------------: | :---: |
|                Radar Beams Used \[#] |   1   |
|            Nominal Scene Width \[km] |   30  |
|           Nominal Scene Length \[km] |   50  |
|           Maximum Scene Length \[km] |  840  |
|   Nominal Collection Duration \[sec] |   10  |
|   Maximum Collection Duration \[sec] |  120  |
|                         Polarization |   VV  |
|    Performant Incidence Range \[deg] | 15-35 |
| Time Dominant Incidence Range \[deg] |  5-45 |


#####

##### _Table 2-15: Collection performance attributes for the Strip imaging mode_

|                  Attribute \ Imaging Mode |     Strip    |
| ----------------------------------------: | :----------: |
|    Noise Equivalent Sigma-Zero \[dBm2/m2] | -21.5 to -20 |
|             Azimuth Ambiguity Ratio \[dB] |      -17     |
|               Range Ambiguity Ratio \[dB] |      -20     |
|             Geospatial Accuracy \[m RMSE] |       6      |
| ESA Copernicus Contributing Mission Class |     VHR2     |
|                          RGIQE \[bits/m²] |      0.8     |


#####

##### _Table 2-16: Product attributes for Strip amplitude data products_

|                                                  Product Attribute |                         Strip                         |
| -----------------------------------------------------------------: | :---------------------------------------------------: |
|                                     Nominal Ground Resolution \[m] |                           3                           |
|                                       Ground Range Resolution \[m] |                           <3                          |
|                                     Ground Azimuth Resolution \[m] |                           <3                          |
|                                                   Range Looks \[#] |                           1                           |
|                                                 Azimuth Looks \[#] |                           1                           |
|               Impulse Response Weighing Function (peak side level) |                Taylor Weighting (-20dB)               |
|                                   Ground Range Sample Spacing \[m] |                          2.5                          |
|                                 Ground Azimuth Sample Spacing \[m] |                          2.5                          |
| Product Format(see section [5](#5-data-products-11) for more info) | Cloud Optimized GeoTIFF + JSON(legacy: GeoTIFF + XML) |
|                                             GRD Product Size \[MB] |                        600-1400                       |
|                                    Dynamic Range \[bits per pixel] |                  16 (uint) 32 (float)                 |
|                                         Radiometrically Calibrated |                          Yes                          |


##### _Table 2-17: Product attributes for Strip complex data products_

|                                                              Product Attribute |                        Strip                       |
| -----------------------------------------------------------------------------: | :------------------------------------------------: |
|                                                                 Focusing Plane |                     Slant Plane                    |
|                                                   Slant Range Resolution \[m]  |                     0.5 to 2.5                     |
|                                                  Slant Azimuth Resolution \[m] |                          3                         |
|                           Impulse Response Weighing Function (peak side level) |                  Uniform (-13.3dB)                 |
|                                                Slant Range Sample Spacing \[m] |                     0.4 to 2.4                     |
|                                              Slant Azimuth Sample Spacing \[m] |                         1.6                        |
| Slant Range Product Format(see section [5](#5-data-products-12) for more info) | Cloud Optimized GeoTIFF + JSON(legacy: HDF5 + XML) |
|                                                     Complex Product Size \[GB] |                      2.9 to 6                      |
|                                                 Dynamic Range (bits per pixel) |                16 (uint) 32 (float)                |


##

## 2.6 Scan

ICEYE offers a Scan imaging mode based on the ScanSAR collection strategy. In ScanSAR, each satellite's phased array antenna is used to create multiple beams in the elevation direction. This beam steering illuminates a wide area via multiple adjacent strips, but it means that points on the ground are not illuminated for as long as in the conventional Stripmap collection strategy. This reduces the resolution of the Scan product.

![](https://github.com/iceye-ltd/product-documentation/releases/download/additional-assets/scan.png)

In the conventional Scan mode, ground points are illuminated by different parts of the radar beam resulting in brighter and darker regions in the image. ICEYE employs a refined version of this collection strategy known as Terrain Observation by Progressive Scans (TOPSAR), which additionally electronically steers the beam from backward to forward in the azimuth direction. This ensures consistent image quality across the captured area. **Scan** produces imagery that covers an area of 100 km x 100 km with a resolution better than 15 m. The length of a Scan product can be extended to as much as 840 km in azimuth if requested as part of a custom order.

Having the largest area coverage and a modest resolution, Scan images are highly suited to wide area surveillance and monitoring projects. Being able to operate in all weather and lighting conditions, they provide an excellent opportunity to image the oceans and to detect vessels and monitor shipping lanes.

ICEYE aims to ensure that the resulting imagery for tasks collected with the Scan imaging mode within the tasking parameters listed in Table [2-18](#table-2-18-tasking-parameters-for-the-scan-imaging-mode) (excluding Time Dominant Incidence Range) will have the collection performance tabulated in Table [2-19](#table-2-19-collection-performance-attributes-for-the-scan-imaging-mode) and amplitude product attributes listed in Table [2-20](#table-2-20-product-attributes-for-scan-amplitude-data-products). Note that no complex data products are available for the Scan imaging mode.


##### _Table 2-18: Tasking parameters for the Scan imaging mode_

|             Parameter \ Imaging Mode |  Scan |
| -----------------------------------: | :---: |
|                Radar Beams Used \[#] |   4   |
|            Nominal Scene Width \[km] |  100  |
|           Nominal Scene Length \[km] |  100  |
|           Maximum Scene Length \[km] |  840  |
|   Nominal Collection Duration \[sec] |   15  |
|   Maximum Collection Duration \[sec] |  120  |
|                         Polarization |   VV  |
|    Performant Incidence Range \[deg] | 21-29 |
| Time Dominant Incidence Range \[deg] |  n/a  |


#####

##### _Table 2-19: Collection performance attributes for the Scan imaging mode_

|                  Attribute \ Imaging Mode |      Scan      |
| ----------------------------------------: | :------------: |
|    Noise Equivalent Sigma-Zero \[dBm2/m2] | -22.2 to -21.5 |
|             Azimuth Ambiguity Ratio \[dB] |       -17      |
|               Range Ambiguity Ratio \[dB] |       -20      |
|             Geospatial Accuracy \[m RMSE] |       15       |
| ESA Copernicus Contributing Mission Class |      VHR2      |
|                          RGIQE \[bits/m²] |       0.1      |


#####

##### _Table 2-20: Product attributes for Scan amplitude data products_

|                                                  Product Attribute |                          Scan                         |
| -----------------------------------------------------------------: | :---------------------------------------------------: |
|                                     Nominal Ground Resolution \[m] |                           15                          |
|                                       Ground Range Resolution \[m] |                          <15                          |
|                                     Ground Azimuth Resolution \[m] |                          <15                          |
|                                                   Range Looks \[#] |                           1                           |
|                                                 Azimuth Looks \[#] |                           1                           |
|                                   Ground Range Sample Spacing \[m] |                           6                           |
|                                 Ground Azimuth Sample Spacing \[m] |                           6                           |
| Product Format(see section [5](#5-data-products-13) for more info) | Cloud Optimized GeoTIFF + JSON(legacy: GeoTIFF + XML) |
|                                             GRD Product Size \[MB] |                       700 - 1300                      |
|                                    Dynamic Range \[bits per pixel] |                  16 (uint) 32 (float)                 |
|                                         Radiometrically Calibrated |                           No                          |

