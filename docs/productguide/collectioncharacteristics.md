# IMAGING COLLECTION CHARACTERISTICS

The following provides additional technical information on the performance of the current ICEYE imaging modes. Our satellites are constantly being improved, but in order to manage expectations, in the tables below we provide the worst-case values across the fleet. Some parameters warrant a more detailed explanation which you can read in the [Notes](#notes-and-explanations) section.

 [Table 2](#complex-image-parameters) provides parameters associated with ICEYE complex images and [Table 3](#amplitude-image-parameters) provides the technical parameters associated with ICEYE Amplitude Images.

## Technical Overview

<figure markdown>
| Parameter      | Strip        |  Spot   | Spot *Extended Area* | Scan          | Comments                            |
|----------------|--------------|---------|--------------------|---------------|-------------------------------------|
| Product Short Name            | 'SM'         | 'SLH'     | 'SLEA' | 'SC'    | [Note 1](#notes-and-explanations)    |
| Radar Beams Used              |  1           | 1         | 1     | 4       | [Note 2](#notes-and-explanations)    |
| Nominal swath width [km]      | 30           | 5         | 15    | 100     | [Note 3](#notes-and-explanations)    |
| Nominal product length (Azimuth Direction) [km] | 50 | 5 | 15    | 100     | [Note 4](#notes-and-explanations)    |
| Nominal collection duration [sec] | 10       | 10        | 10     | 15      |                                      |
| Maximum collection duration [sec] | 35-75    | N/A       | N/A   | 75      | [Note 5](#notes-and-explanations)    |
| Maximum Scene Length [km]         | 500  | 5         | 15     | 500 | [Note 5](#notes-and-explanations)    |
| Noise Equivalent Sigma-Zero [ dBm^2^/m^2^ ]  | -21.5 to -20 | -18 to -15 | -18 to -15 | -22.2 to -21.5 | [Note 6](#notes-and-explanations)    |
| Azimuth Ambiguity Ratio [dB]  | -17          | -17       | -17    | -17     |                                      |
| Range Ambiguity Ratio [dB]    | <-20          | <-20       | <-20    | <-20     |                                      |
| Geospatial Accuracy [m RMSE] | 6            | 6         | 6      | 15      |                                      |
| ESA Copernicus Contributing Mission (CCM) Class[@copernicusClass] | VHR2 | VHR1 | VHR1 | HR1 |                     |
| Polarization                  | VV           | VV        | VV     | VV      |                                      |
| RNIIRS                        | 3.6          | 5.5       | 5.5    | 2.1     | [Note 8](#notes-and-explanations)    |
| RGIQE [bits/$m^2$]               | 0.8          | 22        |  8.4     | 0.1     | [Note 9](#notes-and-explanations)    |
| Performant Incidence Range [deg]  | 15-30    | 20-35     | 20-35  | 21-29   | [Note 12](#notes-and-explanations)   |
| Time Dominant Incidence Range [deg] | 11-43  | 11-56     | 11-56 | N/A      | [Note 13](#notes-and-explanations)   |
<figcaption align = "center"><em>Table 1 : ICEYE Collections Technical Summary</em></figcaption>
</figure>

## Complex Image Parameters
<figure markdown>
| Parameter | Strip | Spot | Comments |
|-----------|-------|------|----------|
| Focusing plane |  Slant Plane  | Slant Plane  |
| Slant range resolution [m] | 0.5 to 2.5 | 0.5 | [Note 7](#notes-and-explanations) |
| Slant azimuth resolution [m] | 3 | 0.25 |   
| Impulse response weighing function (peak side level) | Uniform (-13.3dB) |Uniform (-13.3dB)| |
| Slant Range Sample Spacing [m] | 0.4 to 2.4 | 0.4 | [Note 7](#notes-and-explanations)  | 
| Slant Azimuth Sample Spacing [m] | 1.6 | 0.2 |  
| Slant range product format | HDF5 + XML | HDF5 + XML | |   
| SLC Product Size [GB] | 3.4 to 2.9 | 0.6 to 7.2 |   |
| Dynamic Range (bits per pixel) | 16(uint) 32(Float) | 16(uint) 32(Float) | [Note 10](#notes-and-explanations) |  
<figcaption align = "center"><em>Table 2 : Parameters for ICEYE Complex Images</em></figcaption>
</figure>


## Amplitude Image Parameters
<figure markdown>
| Parameter | Strip | Spot | Scan | Comments |
|-----------|-------|------|------|----------|
| Ground Range Resolution [m]  | 3  | 1.5 to 0.9  | < 15  |  [Note 7](#notes-and-explanations) |
| Ground Azimuth Resolution [m]  | 3  | 1  | < 15  |   |
| Impulse response weighing function (peak side level)  |  Taylor Weighting (-20dB) | Taylor Weighting (-20dB) | Taylor Weighting (-20dB)  |   |
| Ground Range Sample Spacing [m]  | 2.5  | 0.5  | 6  |   |
| Ground Azimuth Sample Spacing [m]  | 2.5  | 0.5  | 6  |   |
| Range Looks  | 1  | 1 to 2  | 1  |   |
| Azimuth Looks  | 1 to 2  | 1 to 4  | 1  |   |
| Product format  | Geotiff + XML | Geotiff + XML | Geotiff + XML  |   |
| GRD Product Size [MB]  | 700  | 250, 2250  | 800  |   |
| Dynamic Range (bits per pixel)  | 16(uint) 32(Float) | 16(uint) 32(Float) | 16(uint) 32(Float) | [Note 12](#notes-and-explanations)   |
<figcaption align = "center"><em>Table 3 : Parameters for ICEYE Amplitude Images</em></figcaption>
</figure>


## Notes and Explanations
1. **Short Name:** For example, Strip mode has 'SM' : ICEYE_X7_GRD_**SM**_36535_20201020T175609
2. **Radar Beams:** The current generation of ICEYE satellites use electronically steered elements to control multiple radar beams. Usually this is only one beam but Scan products use multiple beams to image different ranges (at the cost of reduced resolution) 
3. **Nominal Swath Width:** The actual image size will be slightly larger than this to guarantee that the tasked area is covered.
4. **Nominal Swath Length:** The actual image length may be slightly larger to guarantee that the tasked area is covered. The maximum value can vary from satellite to satellite due to power/data/thermal limitations.
5. **Maximum Collection Duration/Length:** Spot images do not have a maximum collection duration as they image for the required amount of time to obtain a tasked azimuth resolution. For Strip and Scan modes the maximum collection duration (and therefore the maximum image length) is limited by the amount of on-board memory storage or satellite thermal limitations. As different incidence angles have different slant range resolutions in order to provide the same ground range resolution, then the maximum collection duration is also a function of incidence angle. 
6. **NESZ:** The noise equivalent sigma zero values are taken at scene center for near and far range extents.
7. **Slant Range Resolution:** For Strip mode the transmitted bandwidth is varied to make sure that the resolution on the ground remains the same. For Spot mode the maximum bandwidth is transmitted at all times. This means that the slant resolution for Spot images is constant and the ground resolution changes with indidence angle.
8. **RNIIRS:** Radar National Imagery Interpretability Rating Scale is a subjective assessment of Radar Image Quality used primarily by military analysts. The scale is from 0 ("*interpretability of the imagery is precluded by obscuration, degradation, or very poor resolution*") to the highest quality figure of merit, 10 [@rniirs].
9. **RGIQE:** This is the Radar General Image Quality Equation. It is an adaptation of the concept of a General Image Quality Equation [@leachtenauer1997general] Developed by NGA . Unlike the RNIIRS scale which is a largely subjective assessment of image quality, the RGIQE uses maximum channel capacity (measured in bits of information) as a figure of merit. From the Shannon-Hartley Theorem [@shannon1984communication] the maximum information that can be carried in a signal (conventionally called a channel due to the origins in communications) is given by :

    $$ C = B \log_2\left(1+\frac{S}{N}\right) $$

    Where $C$ is measured in bits per second, $B$ is the bandwidth of the system and $\frac{S}{N}$ is the signal to noise ratio.
    Recognising that a resolution cell in a SAR image is ultimately defined in range by the transmitted bandwidth and in azimuth by the Doppler bandwidth, a measure of the maximum information content of a resolution cell in bits/$m^2$ can be formulated :

    $$ I = B_{az} B_{R_{ground}} \log_2\left(1 + \frac{S}{N}\right) $$

    Where $I$ is the information content measured in bits/$m^2$, $B_{az}$ is the Doppler bandwidth used to form the azimuth extent of a pixel and $B_{R_{ground}}$ is the range bandwidth in the ground plane used to form the range extent of a pixel. The noise in this case is made up from all the  noise elements that contribute to reduced image quality in the final image (Thermal noise, quantization noise, sidelobes, ambiguities). In this scale the higher the figure then the more 'information' is available for exploitation within the pixel.

10. **Complex Dynamic Range:** A complex number with 16bit I and 16bit Q values. 32 bit float values can be provided by request.
11. **Amplitude Dynamic Range:** Stored as an unsigned 16 bit integer. 32 bit float values can be provided by request.
12. **Performant Incidence Range:** This is the nominal or standard range of incidence angles that the ICEYE Fleet operates over. The parameters in these tables are correct within this range of angles.
13. **Time  Dominant  Incidence Range:** Being quite small and agile, and having an electronically steered antenna, ICEYE satellites can collect radar imagery from a wide range of angles. Outside of the *Performant Incidence Range*, SAR image quality may be degraded. However in some situations it may be more important to obtain a SAR image quickly rather than wait for an opportunity to image the location with the performant range of angles. For this reason ICEYE offers time dominant tasking as either a Tactical or a Custom order.

## References
\bibliography