# Glossary

The following section briefly defines some important terms used in this document. 

1. **COSP**: ICEYE Customer Operations and Satellite Planning team. It handles customer operations including both standard and custom orders from receipt to fulfillment. Ensures ICEYE constellation of satellites is effectively utilized such as to best fulfill customer expectations. They also inform customers of any issues with their orders. All new customers will receive a COSP contact email during onboarding.  Customer Service can also be reached via the [Contact page at ICEYE website](https://www.iceye.com/contact).

2. **Data product**: A deliverable set of data files.  A standard data product adheres to the specification described in this document.

3. **ESA Copernicus Contributing Mission Class:** Imagery data classification based on resolution defined by the [European Space Agency Copernicus Program](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Copernicus_Contributing_Missions).

4. **Ground Resolution:** Refers to the smallest distance between two scatterers on the ground that can be distinguished as separate entities in the radar image. It is usually lower than the Slant Range Resolution as it is the result of projecting the SAR data captured in the slant plane into the ground plane. Its two components are:

   1. **Ground Range Resolution:** The ability to distinguish two objects on the ground in the range direction, which is perpendicular to the radar's flight path. It depends on the bandwidth of the radar signal and the incidence angle.

   2. **Ground Azimuth Resolution:** The ability to distinguish two objects on the ground in the azimuth direction, which is parallel to the radar's flight path.

5. **Incidence angle:** The angle between the radar signal’s line of sight (the path from the satellite to the target) and the perpendicular (normal) to the Earth’s surface at the point where the radar beam hits the ground. 

6. **Nominal Ground Resolution:** The expected ground resolution of amplitude data products resulting from SAR data acquired utilizing a specific imaging mode. This specification utilizes an incidence angle of 30 degrees to define nominal ground resolution for all imaging modes that utilize the Spotlight collection strategy. This is because, when utilizing this collection strategy, the ground resolution is typically limited by the incidence angle. This specification also provides a range of ground resolutions expected for the entire performance incidence angle range for these imaging modes. 

7. **Nominal Swath Width:** The nominal swath width is the size of the image footprint in the range direction. The delivered image size in the range direction will be slightly larger than the Nominal Swath Width to ensure that the tasked area is fully covered.

8. **Nominal Swath Length:** The nominal swath length is the size of the image footprint in the azimuth direction.  The delivered image length may be slightly larger than the Nominal Swath Length to ensure that the tasked area is covered. 

9. **Noise Equivalent Sigma Zero (NESZ):** Noise Equivalent Sigma Zero describes the noise floor of an image. All received signals have to be stronger than the NESZ value to rise above the noise level, so it is best for NESZ to be as low as possible. The noise equivalent sigma zero values are taken at scene center for near and far range extents.

10. **Performant Incidence Angle Range:** The range of incidence angles within which the satellite's sensor can deliver optimal performance for each imaging mode. Images acquired within the performant incidence angle range are intended to meet the product specifications. 

11. **Radar Beam:** Refers to the radar signal emitted from a SAR system. ICEYE satellites use electronically steered elements to control multiple radar beams. All imaging modes with the exception of Scan mode use only one beam.  Scan mode uses multiple beams to image different ranges (at the cost of reduced resolution).

12. **Radiometric Calibration**: Radiometric calibration is the process of ensuring that the pixel values of the data products can be directly related to the power of the returned SAR signal. A calibration factor is applied to the pixel data in order to be able to calculate its mean radar cross section, which is a true measure of the radar reflectivity. All modes with the exception of Scan mode are radiometrically calibrated. While Scan imagery is visually and spatially exploitable, there may be errors when converting image sample values to a mean radar cross section values.

13. **RGIQE:** Radar General Image Quality Equation (RGIQE) is an adaptation of the concept of a General Image Quality Equation developed by NGA. Unlike the RNIIRS scale which is a largely subjective assessment of image quality, the RGIQE uses maximum channel capacity (measured in bits of information) as an objective figure of merit. A higher RGIQE value demonstrates that more 'information' is available for exploitation within the pixel vs. a lower RGIQE.

14. **RMSE**: The _RMSE_ is the Root Mean Square Error of all the measured calibration points from all the satellites. In Section [2.1](#21-introduction) there is more explanation of how ICEYE uses RMSE to express the Geospatial Accuracy of its image products. 

15. **RNIIRS:** Radar National Imagery Interpretability Rating Scale (RNIIRS) is a subjective assessment of Radar Image Quality used primarily by military analysts. The RNIIRS scale provides a means for comparing the quality of SAR images.  The RNIIRS scale spans from 0 (the lowest quality:  "_interpretability of the imagery is precluded by obscuration, degradation, or very poor resolution_") to 10 (highest quality figure of merit).

16. **Slant Range Resolution:**  Ability of the radar system to distinguish between two objects located at different distances along the slant range, which is the line-of-sight distance from the radar antenna to the target on the ground. Resolution of the radar image in the direction of the radar beam.

17. **Time Dominant Incidence Angle Range:** The range of incidence angles within which the satellite sensor can produce an image in order to meet specific temporal or revisit requirements utilizing a specific imaging mode. This range ensures that the satellite can capture images of a target area within a specified time window, even if it means compromising slightly on image quality or resolution. Images acquired within the **Time Dominant Incidence Angle Range** but outside the **Performant Incidence Angle Range** of an imaging mode are not intended to meet the product specifications. 