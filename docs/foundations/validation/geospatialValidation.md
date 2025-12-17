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

Geometrically, the object's position is found by calculating the intersection between a sphere of radius that corresponds to the range of the object (1), a cone defined by the Doppler frequency at a certain time (2) and the reference ellipsoid (see Fig. 1). There are two locations where all three parametric surface meet - one on the left side of the sensor and one on the right, which is why SAR systems only image on one side.

<figure markdown>
![doppler intersection for a SAR](img/circleIntersection.png){width="600"}
<figcaption align = "center"><em>Figure 1: The location of an object in a SAR image is defined by the intersection of a range-sphere, a Doppler-cone and a reflecting-surface.</em></figcaption>
</figure>

To calculate the geolocation accuracy of a SAR image, the following steps are performed :

1. The first step is the selection of calibration objects, usually corner reflectors (CRs), each with a known geographical location. For this purpose, both publicly available corner reflectors and ICEYE's own dedicated corner reflectors are used. The object position $R_o=[x_o, y_o, z_o]$ is used in the following step to calculate the expected target position in range and azimuth $(I_r,I_a)$ in the image.
2. The second step is to determine the location of the sensor as a function of time by using the orbital state vectors provided in the metadata of each image. ICEYE’s orbital state vectors provide position and velocity at one-second intervals, which is not sufficiently precise to determine the exact azimuth position for every image line, so the state vectors are interpolated.
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
![measured geolocation error in ICEYE Imagery](img/geolocationError2.png){width="600"}
<figcaption align = "center"><em>Figure 2: The sensor's location accuracy is determined by comparing the measured image location to the actual location of a calibration object.</em></figcaption>
</figure>

## 2025 Rosamond Validation: Spotlight & Stripmap Imaging Modes
### Test Site

During December 2025, a geolocation validation was performed using the Rosamond Corner Reflector Array (RCRA) in California, USA[@rosamond]. At this location, there are 38 Corner Reflectors, each in one of four dimensions (0.7 m, 2.4 m, 2.8 m and 4.8 m). Fig. 3.

<figure markdown>
![Rosamond corner array in ICEYE Imagery](img/rosamondCRs.png){width="600"}
<figcaption align = "center"><em>Figure 3: Test site in the Rosamond Corner Reflector Array</em></figcaption>
</figure>

### Datasets

As part of a dedicated calibration campaign, 521 SAR images were acquired over the Rosamond reflector site during June–November 2025, using both Stripmap and Spotlight imaging modes in non-squinted imaging geometry. Fig. 4. shows the image distribution across satellite generations and imaging modes. 

<figure markdown>
![ICEYE Imagery calibration histogram](img/imageCount2.png){width="600"}
<figcaption align = "center"><em>Figure 4: Number of images used in this analysis across satellite generations and imaging modes.</em></figcaption>
</figure>

### Results
All collected scenes were processed and analyzed to evaluate geolocation accuracy for the full ICEYE constellation and for individual satellite generations, as summarized in Table 1. The fleet-wide mean error in the slant range direction and that in the azimuth direction are both under 0.4 m, with a standard deviation value of less than 2.1 m. The Root Mean Square Error (RMSE) for each generation group is less than 2.6 m in the slant range direction and the differences among generations are smaller than 1.3 m. In the azimuth direction, the RMSE for each generation are each less than 3.2 m, and the latest generations perform progressively better than the previous ones. This is a result of consistent improvements in onboard timing accuracy / precision in each newer satellite generation.

<figure markdown>
|Satellite	| #Images	| #CR Observations	| Range Error: μ±σ (m)	| Range Error: RMSE (m)	| Azimuth Error: μ±σ (m) |	Azimuth Error: RMSE (m) |
|:--------------|:---------:|:-----------------:|:---------------------:|:---------------------:|:----------------------:|:------------------------:|
| GEN-2	    | 100	    | 1918	            | -0.65±1.14              | 1.31                   | 0.12±2.34 	             | 2.35                      |
| GEN-3	    | 83	    | 1571	            | 0.66±1.30	            | 1.46	                | 1.84±2.52	             | 3.12                      |
| GEN-3.5	    | 274	    | 5434	            | 0.66±2.27              | 2.36                   | 0.27±1.61 	             | 1.63                      |
| GEN-4	    | 52	    | 1200	            | -1.25±2.28	            | 2.60	                | -0.43±1.52	             | 1.58                      |
| All	    | 521	    | 10398	            | 0.19±2.09	            | 2.10	                | 0.36±2.04	             | 2.07                      |
<figcaption align = "center"><em>Table 1: ICEYE fleet geolocation accuracy assessment results June 2025 to November 2025: Generations.</em></figcaption>
</figure>

The geolocation accuracy per imaging mode is summarized in Table 2.

<figure markdown>
|Imaging Mode	| #Images	| #CR Observations	| Range Error: μ±σ (m)	| Range Error: RMSE (m)	| Azimuth Error: μ±σ (m) |	Azimuth Error: RMSE (m) |
|:--------------|:---------:|:-----------------:|:---------------------:|:---------------------:|:----------------------:|:------------------------:|
| Spotlight	    | 448	    | 9048	            | 0.23±2.13              | 2.14                   | 0.43±2.06 	             | 2.10                      |
| Stripmap	    | 61	    | 1075	            | -0.22±1.78	            | 1.81	                | 0.20±1.69	             | 1.71                      |
<figcaption align = "center"><em>Table 2: ICEYE fleet geolocation accuracy assessment results June 2025 to November 2025: Imaging Modes.</em></figcaption>
</figure>

The error distribution for all the assessed points is shown in Figure 5, where the estimated Circular Error 90-percentile (CE90) value is 4.6m at the slant plane.

<figure markdown>
![Error distribution of the assessed points](img/2dError.png){width="400"}
<figcaption align = "center"><em>Figure 5: 2D Error distribution of the assessed points: the estimated CE90 is 4.6m.</em></figcaption>
</figure>

The geolocation accuracy for each month during the campaign can be seen in Figure 6. The RMSE values for both directions exhibit a downward trend from June to September and stay consistent afterwards.

<figure markdown>
![Geolocation Accuracy by Months](img/metricsMonths.png){width="600"}
<figcaption align = "center"><em>Figure 6: Geolocation Accuracy by Months.</em></figcaption>
</figure>

## Conclusions
The measurement of geospatial accuracy of SAR images is subject to multiple error sources, including uncertainties in terrain height, orbit knowledge, atmospheric propagation model, and sensor related uncertainties such as position along track, lever arms between GPS and antenna phase center, timing across track, and thermal variations.

The geolocation accuracy from stripmap images are very similar to that from spotlight images in both range and azimuth directions.


## References
\bibliography