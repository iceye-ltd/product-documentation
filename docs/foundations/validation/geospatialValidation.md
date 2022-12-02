# Verification and Validation of Geospatial Measurements

Verification and validation of geospatial measurements on SAR imagery is an integral part of ICEYE's quality control process. Below you will find our latest validation report. More reports will be added as they become available.

## Method
'*Geolocation*' is the name of the process used to find the univocal correspondence between image pixels and their position on the Earth's surface. In this section we introduce a geolocation algorithm that we use to measure the geospatial accuracy of ICEYE imagery. 

The purpose of geolocation is to calculate the difference between an observed objects's location measured from SAR imagery and its actual, ground-truth, location. The true '*ground truth*' location of an object can be specified in a geocentric rotating coordinate system such as ECEF (Earth-centred, Earth-fixed) as having the coordinate $R_o=[x_o,y_o,z_o]$. The satellite's location in this same reference system changes with time and is given by $R_s(t)=[x_s(t),y_s(t),z_s(t)]$ and has a velocity given by $V_s(t)=[v_{sx}(t),v_{sy}(t),v_{sz}(t)]$. From these, the *slant range* from the satellite to the object as a function of time $s_r(t)$ is given by (1):

$$
s_r(t) = (x_s(t) - x_o)^2 + (y_s(t)-y_o)^2 + (z_s(t)-z_o)^2 \qquad (1)
$$

As the satellite transits past the object, the phase of its radar response varies providing the object's signature with a characteristic spatial Doppler frequency shift given by (2):

$$
f_D(t) = - \frac{2}{\lambda s_r(t)} (\mathbf{R_s(t)} - \mathbf{R_o}) \cdot (\mathbf{V_s(t)} - \mathbf{V_o}) \qquad (2)
$$

Geometrically, the objects position is found by calculating the intersection between a sphere of radius that corresponds to the range of the object (1), a cone defined by the Doppler frequency at a certain time (2) and the reference ellipsoid (see Fig. 1). There are two locations where all three parametric surface meet - one on the left side of the sensor and one on the right, which is why SAR systems only image on one side.

<figure markdown>
![doppler intersection for a SAR](img/circleIntersection.png){width="600"}
<figcaption align = "center"><em>Figure 1: The location of an object in a SAR image is defined by the intersection of a range-sphere, a Doppler-cone and a reflecting-surface.</em></figcaption>
</figure>

To calculate the geolocation accuracy of a SAR image the following steps are performed :

1. The first step is the selection of calibration objects, usually corner reflectors, each with a known geographical location. For this purpose both publicly available corner reflectors and ICEYE's own dedicated corner reflectors are used. The object position $R_o=[x_o, y_o, z_o]$ is used in the following step to calculate the expected target position in range and azimuth $(I_r,I_a)$ in the image.
2. The second step is to determine the location of the sensor as a function of time by using the orbital state vectors provided in the metadata of each image.  ICEYE orbital state vectors provide position and velocity every second which does not have the fidelity to accurately locate each azimuth location in the image and so the state vectors are interpolated.
3. The *expected* range and azimuth position of the corner reflector $(I_r,I_a)$ is then calculated using Eq. (1) and Eq. (2). The azimuth position of the object corresponds to the time of closest approach between the object and the sensor which is the instant that the Doppler frequency shift of the object observed from the sensor is zero. (By convention ICEYE SAR images are processed to the zero Doppler location/time). The expected range position is calculated using the distance $\mathbf{R_s(t)}-\mathbf{R_o}$ when the Doppler shift is zero. ie:

$$ 
- \frac{2}{\lambda s_r(t)} (\mathbf{R_s(t)} - \mathbf{R_o}) \cdot (\mathbf{V_s(t)} - \mathbf{V_o}) = 0 \qquad (3) 
$$

4. The *measured* range and azimuth position $(M_r,M_a)$ of the calibration object is calculated by oversampling the SAR image and fitting the expected two-dimensional imaging response function to the object and measuring the location of the peak. This can be seen in Figure 2. The geolocation error in pixels is given by: 

$$
\begin{aligned}
\Delta R_g = I_r - M_r \\
\Delta A_z = I_a - M_a 
\end{aligned} \qquad (4)
$$

<figure markdown>
![measured geolocation error in ICEYE Imagery](img/geolocationError1.png){width="600"}
<figcaption align = "center"><em>Figure 2: The sensors location accuracy is determined by comparing the measured image location to the actual location of a calibratioin object.</em></figcaption>
</figure>

## Rosamond Validation - April 2022: Spotlight & Stripmap
### Test Site

During April 2022, a geolocation validation was performed using the Rosamond Corner Reflector Array (RCRA) area in California, USA[@rosamond]. At this location there are 38 Corner Reflectors, each in one of four dimensions (0.7 m, 2.4 m, 2.8 m and 4.8 m). Fig. 3.

<figure markdown>
![Rosamond corner array in ICEYE Imagery](img/rosamondCRs.png){width="600"}
<figcaption align = "center"><em>Figure 3: Test site in the Rosamond Corner Reflector Array</em></figcaption>
</figure>

### Datasets

The geolocation accuracy was assessed based on 167 spot images taken between 22 August 2019 and 15 March 2022, and 304 strip images taken between 10 March 2019 and 01 June 2022. Fig. 4. shows a histogram with the number of images and their distribution among the different satellites operating in the ICEYE fleet over that period. Although there are fewer images for the newer satellites (the ones with larger number in the name), this report will continue to be updated to include more images from all satellites.

<figure markdown>
![ICEYE Imagery calibration histogram](img/imageCount1.png){width="600"}
<figcaption align = "center"><em>Figure 4: Number of images used in this analysis across the ICEYE fleet.</em></figcaption>
</figure>

### Results
An overview of the validation results is provided in Table 1. The overall geolocation accuracy in both the range direction and azimuth direction is better than 4m RMSE and is consistent between the two imaging modes. The results also show a ~3.0m systematic bias in the range direction, and about ~0.8m bias in the azimuth direction. The cause of these biases are currently under investigation and will be addressed in the following months. The detailed results can be found [here](img/resultsSL1.csv) for Spotlight images and [here](img/resultsSM1.csv) for Stripmap images (see also [this](img/resultsSM1.csv_Readme.txt) this description of the columns in the results).

<figure markdown>
|Imaging Mode	| #Images	| #CR Observations	| Range Error: μ±σ (m)	| Range Error: RMSE (m)	| Azimuth Error: μ±σ (m) |	Azimuth Error: RMSE (m) |
|:--------------|:---------:|:-----------------:|:---------------------:|:---------------------:|:----------------------:|:------------------------:|
| Spotlight	    | 167	    | 2354	            | -2.8±1.7              | 3.2                   | -0.9±3.2 	             | 3.3                      |
| Stripmap	    | 304	    | 3388	            | -3.2±1.8	            | 3.6	                | -0.7±3.1	             | 3.1                      |
<figcaption align = "center"><em>Table 1: ICEYE fleet geolocation accuracy assessment results March 2019 to June 2022.</em></figcaption>
</figure>

The measured geolocation accuracy for each satellite for Spot images is shown in Fig. 5, and from Strip images is shown in Fig. 6.

<figure markdown>
![ICEYE Imagery Spot geolocation accuracy](img/RMSESpotlight1.png){width="600"}
<figcaption align = "center"><em>Figure 5: Geolocation error: Spot images August 2019 to March 2022.</em></figcaption>
</figure>

<figure markdown>
![ICEYE Imagery Strip geolocation accuracy](img/RMSEStripmap1.png){width="600"}
<figcaption align = "center"><em>Figure 6: Geolocation error: Strip images March 2019 to June 2022.</em></figcaption>
</figure>

## Conclusions
The measurement of geospatial accuracy of SAR images is subject to multiple error sources, including uncertainties in terrain height, orbit knowledge, atmospheric propagation model, and sensor related uncertainties such as position along track, lever arms between GPS and antenna phase center, timing across track, and thermal variations. In some cases, orbit positional errors may introduce gross geospatial errors (larger than 50m in this analysis). Such errors are identified by ICEYE's QC procedures and are reprocessed before customer delivery. As such those images are currently not included in this analysis.

ICEYE’s satellite capabilities are constantly evolving, with older satellites being more prone to on-board timing errors. Newer satellites have improved on this and thus have better geospatial accuracy.

The geolocation accuracy from stripmap images are very similar to that from spotlight images in both range and azimuth directions.

The results also show a clear systematic bias in both range and azimuth directions that will be addressed in the following months to improve these values further.

## References
\bibliography