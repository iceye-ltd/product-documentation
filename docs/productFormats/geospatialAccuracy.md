# Geospatial Accuracy

## Background

A SAR system is able to measure the range to a point on the ground very precisely - to a fraction of a wavelength. The sensor can also measure how the range to a point changes as the satellite moves along its trajectory (by comparing pulses) which provides precise information of the along-track location of a pixel. The distance (and change of distance) to each point provides a record of radar cross section measurements as a function of range and along-track position. 

This record is the most accuarate source of SAR data. It is provided as a set of *phase histories* (called *phase history data*). In this form the data is not available to exploit as an image - it is just a record of what the SAR sees as a function of time. To convert the phase history data into an image it is passed through a SAR Image Formation Processor which applies phase corrections to the data to make it look like the ground was observed through a *synthetic* lens or aperture. The output image from the SAR processor is the highest spatial fidelity image *product* available called the single look complex (SLC) image. All other image formats are derived from it. Due to data format conversion and projection mapping, all ground projected (*ground range*) products and derived Level 2 products will always have a lower fidelity. 

On this page we discuss the factors that affect the geospatial accuracy of a SAR Image.

<!-- <figure>
<img src="../img/radarRange_ManimCE_v0.10.0.gif" style="width:100%">
<figcaption align = "center"><em>Figure 1: Radar systems measure range very accurately using precise timing to measure how long it takes a pulse to reflect off an object.</em></figcaption>
</figure> -->

## On-Board Timing Errors
A fundamental source of error for all RADAR systems relates to timing. In radar systems, precise electronic clocks are used to record the passage of time. All clocks have some sort of drift in their accuracy which, if not corrected, affects the measured range and focussing of the imagery. ICEYE satellites apply timing corrections to their internal clocks by periodically synchronising with GNSS (Global Navigation Satellite System) satellites.

## Atmospheric Propagation
As the RADAR pulse propagates through the atmosphere, it undergoes diffraction which curves the path of the pulse adding an unintended increase to the range of an object. The amount of increase depends on the look angle, the location of the satellite and scene and even the time of day. The ICEYE SAR processor attempts to apply path length corrections (typically on the order of a couple of metres) using well established models.

## Orbit Knowledge
A potentially large source of errors comes from not knowing precisely where the sensor is when each pulse is transmitted and received. This is determined by the satellite's orbit knowledge. ICEYE satellites constantly record their GNSS location. This information is transmitted to the ground during ground station telemetry downloads that occur usually once per orbit (sometimes more frequently). Additionally the GNSS data is stored with the wideband radar data for rapid downlink and processing.

Once on the ground the orbit information is passed to ICEYE's orbit determination servers. These refine the orbit, taking into account the satellite's attitude and motion, the solar radiation pressure and the local gravitational field strength. The refinements are then used to improve the image geospatial accuracy and to provide accurate time/position/velocity estimates for future collections.

In the future we plan on further refining the orbit fidelity using post-collected GNSS corrections combined with retroreflectors attached to the satellite.

The Following table summarises the different levels of orbit fidelity. This information is stored in each image's metadata.

<figure markdown>
| Orbit Fidelity | Description | Latency |
|----------------|-------------|---------|
| Predicted      | Uses current / latest orbit solution to predict where the satellite will be at some point in the future. Used for collection planning and feasibility studies. Not usually used for image formation processing as it has the largest errors. | updated 6 Hours before collection |
| Rapid | Uses GNSS stored samples collected during or near to the imaging operation. The spherical error (SE90) of the samples is 3m. This allows imagery to be downlinked during or soon after collection to provide tactical SAR imagery to users with a modest geospatial error. This level is not available on all satellites yet. | Immediate. |
| Precise | This is the default orbit fidelity used for ICEYE satellites. The satellite position/velocity state vectors are refined after the imaging operation using downlinked telemetry and attitude data. | 10-45 minutes after imaging operation |
| Scientific | This uses GNSS corrections applied to the samples taken during imaging to significantly reduce the position velocity error. This is not yet available across the ICEYE Fleet. | 2 to 4 days after collection | 
<figcaption align = "center"><em>Table 1 : Different Levels of Orbit Fidelity in ICEYE SAR Images</em></figcaption>
</figure>

### Orbit Knowledge Metadata

The location of the satellite during any imaging operation is made available by including the satellite and velocity information in the metadata for each image product. The data can be found under the `orbit_state_vector` metadata element. The accuracy of each element is determined by the orbit fidelity used to create the product which can be found in the `orbit_processing_level` metadata element which corresponds so one of the levels in table 1.

## Terrain Height

The most significant source of geospatial error in ICEYE SAR imagery comes, not so much from the inherent properties of the RADAR but from the way the data is measured and exploited. The following animation explains why the measured location of a point in a SAR image is dominated by errors in terrain height information.

<figure>
<img src="../img/explainingGeoErrors_ManimCE_v0.13.1.gif" style="width:100%">
<figcaption align = "center"><em>Figure 2: The geospatial accuracy of a SAR image is a function of the accuracy of the terrain model used.</em></figcaption>
</figure>

It is important to realize that the link between terrain height and geospatial accuracy applies to all oblique imaging system's including optical sensors. Furthermore the geospatial accuracy of optical imaging systems rely on the precise angular measurement of the pointing of the optical imaging system's focal plane. RADAR systems measure the **range** to each point on the ground rather than the **angle**, which is easier to perform precisely (a SAR sensor measures range to a fraction of a wavelength). This means that all things being equal, a SAR satellite's geospatial accuracy is **far more accurate** than an optical imaging satellite.

## Geospatial Metadata
It is interesting to note that the ground projection issue relates to any oblique looking imaging system (such as optical sensors) that are able to take images *off-nadir*. Fortunately a lot of geospatial viewers and exploitation tools have evolved to help the user deal with such issues. Some viewers have approximate terrain models built in and can reduce the location errors using parameters embedded in the metadata of each image. Two common approaches are  *Doppler Centroid Polynomials* and *Rapid Polynomial Coefficients*.

### Doppler Centroid Determination
ICEYE SAR images are *zero-Doppler* based. This means that image pixels are focussed to the zero-Doppler (or *broadside*) position. Because the radar beam covers a range of Doppler frequencies with objects entering the beam having a high Doppler frequency and objects leaving the beam having a low Doppler frequency, the centre point, called the **Doppler Centroid** can be used to find where the radar beam is pointing at any moment. This information together with the orbit state vector information can then be used to determine the precise location in slant range and azimuth of each image sample.

Doppler Centroid (DC) coefficient estimates are throughout the image acquisition. For each azimuth location, the DC dependence in range is described using a polynomial function. The polynomial is valid from the near to the far range of the scene.  The DC coefficients can be obtained by fitting the DC dependence in range from time as:

$$ DC(t)=C_0\left(t-t_{ref}\right)^0+C_1 \left(t-t_{ref}\right)^1+C_2 \left(t-t_{ref}\right)^2+C_3 \left(t-t_{ref}\right)^3$$

where the reference point in time $t_{ref}$ corresponds to the mid-range time, and time varies between $t_{min}$ and $t_{max}$ corresponding to near range (first pixel time) and far range, respectively. 
The mid-range time is calculated as:  

$$ t_{ref}= (t_{min} +t_{max})/2=t_{min}+n_{rs}/(2f_{sr} )$$

where $n_{rs}$ is the number of range samples, and $f_{sr}$ is the range sampling rate.


### Rapid Positioning Capability (and Rational Poynomial Coefficients)

The concept of rapid determination of image pixel coordinates from oblique imagery (RADAR and optical) was first described openly by the US National Imagery and Mapping Agency (NIMA) in STDI-0002 2.1[@nitf] and specifically sections 8.2.4 (the mathematical description of Rational Polynomial Coefficients) and section 8.3.12 that describes how parameters could be stored electronically (Also known as *RPC00 - Rapid Positioning Capability*). The technique was developed to perform image geolocation calculations quicky on US Imagery Analyst IDEX workstations. The acronym *RPC* can refer to either the standard or the coefficients and is therefore a little confusing. At ICEYE we prefer to use plain language and as not everyone understands whether a coefficient is rational or irrational we prefer to use the *Rapid Positioning Capability* definition. 

To help with the determination of precise pixel locations, a RPC model has been implemented into ICEYE's output product files. The model is described in [ [@rpcs] ] which extends the work for the National Imagery Transmission Format (NITF)[@nitf] to GeoTIFFs.  For completeness, the translation of latitude and longitude to image pixel coordinates is described below.
The geometric sensor model describing the physical relationship between image coordinates and ground coordinates is known as a Rigorous Projection Model. A Rigorous Projection Model expresses the mapping of the image space coordinates of rows and columns ($r,c$) onto the object space reference surface geodetic coordinates ( φ, λ, h ).

The approximation used in ICEYE products is a set of rational polynomials that describe the normalized row and column values, ($rn$ , $cn$), as a function of normalized geodetic latitude, longitude, and height, ($P$, $L$, $H$), given a set of normalized polynomial coefficients (`LINE_NUM_COEF_n`, `LINE_DEN_COEF_n`, `SAMP_NUM_COEF_n`, `SAMP_DEN_COEF_n`). Normalized values, rather than actual values are used in order to minimize the introduction of errors during the calculations. The transformation between row and column values ($r$,$c$), and normalized row and column values ($r_n$, $c_n$), and between the geodetic latitude, longitude, and height ( φ, λ, h ), and normalized geodetic latitude, longitude, and height (P, L, H), is defined by a set of normalizing translations (offsets) and scales that ensure all values are contained within the range -1 to +1. The normalization of these parameters is given in Table 2.

If you load ICEYE's images into some GIS Viewers (eg QGIS[@qgis]), then it will automatically perform conversion from image row, column to lat, long, WGS84 altitude.

<figure markdown>
| NORMALISED |	DEFINITION |
|------------|-------------|
| $P$ |	(Latitude - `LAT_OFF`) / `LAT_SCALE` |
| $L$ | (Longitude - `LONG_OFF`) / `LONG_SCALE` |
| $H$ | (Height - `HEIGHT_OFF`) / `HEIGHT_SCALE` |
| $r_n$ | (Row - `LINE_OFF`) / `LINE_SCALE` |
| $c_n$ | (Column - `SAMP_OFF`) / `SAMP_SCALE` |
<figcaption align = "center"><em>Table 2 : Normalization of RPC parameters</em></figcaption>
</figure>

The GeoTIFF encoding of the RPC data in ICEYE data products is provided as a structure of 14 parameters described in Table 3.

The equation to calculate the row and column number from the RPC values is given by:

$$
r_n= \frac{ \sum_{i=1}^{20} LINE\_NUM\_COEF_i ⋅ \rho_i(P,L,H) }
          { \sum_{i=1}^{20} LINE\_DEN\_COEF_i ⋅ \rho_i(P,L,H) }     
$$

$$
c_n = \frac{\sum_{i=1}^{20} SAMP\_NUM\_COEF_i ⋅ \rho_i(P,L,H) }
           {\sum_{i=1}^{20} LINE\_DEN\_COEF_i ⋅ \rho_i(P,L,H) }
$$

Where the rational polynomial numerators and denominators are each a 20-point cubic polynomial function of the form:


| $\sum_{i=1}^{20} C_i ⋅ \rho_i(P,L,H) =$  | | | | |
|---|---|---|---|---|
| | $C_1$	| $+C_6 LH$ | $+C_{11} PLH$ | $+C_{16} P^3$  |
| | $+C_2L$ | $+C_7 PH$ | $+C_{12} L^3$ |	$+C_{17} PH^2$ |
| | $+C_3P$	| $+C_8 L^2$| $+C_{13} LP^2$|	$+C_{18} L^2 H$ |
| | $+C_4H$	| $+C_9 P^2$| $+C_{14} LH^2$|	$+C_{19} P^2 H$ |
| | $+C_5LP$| $+C_{10} H^2$| $+C_{15} L^2P$| $+C_{20} H^3$ |

Where coefficients $C_1…C_{20}$ represent the vector coefficients provided in the product metadata : `LINE_NUM_COEF_n`, `LINE_DEN_COEF_n`, `SAMP_NUM_COEF_n`, `SAMP_DEN_COEF_n`. The image coordinates are in units of pixels. The ground coordinates are latitude and longitude in units of decimal degrees and the height above ellipsoid is in units of meters. The ground coordinates are referenced to WGS84. 

<figure markdown>
| NAME     | DESCRIPTION | VALUE RANGE | UNITS  |
|----------|-------------|-------------|--------|
| LINE_OFF | Line Offset | >= 0        | pixels |
| SAMP_OFF | Sample Offset | >= 0 | pixels |
| LAT_OFF | Geodetic Latitude Offset | -90 to +90 | degrees |
| LONG_OFF | Geodetic Longitude Offset | -180 to +180 | degrees |
| HEIGHT_OFF | Geodetic Height Offset | unlimited | meters |
| LINE_SCALE | Line Scale | > 0 | pixels |
| SAMP_SCALE | Sample Scale | > 0 | pixels |
| LAT_SCALE | Geodetic Latitude Scale |	0 < LAT_SCALE <= 90 | degrees |
| LONG_SCALE | Geodetic Longitude Scale | 0 < LONG_SCALE <= 180 | degrees |
| HEIGHT_SCALE | Geodetic Height Scale | HEIGHT_SCALE > 0 | meters |
| LINE_NUM_COEFF (1-20) | Line Numerator Coefficients. Twenty coefficients for the polynomial in the Numerator of the $r_n$ equation. |	unlimited | |
| LINE_DEN_COEFF (1-20) | Line Denominator Coefficients. Twenty coefficients for the polynomial in the Denominator of the $r_n$ equation. | unlimited | |
| SAMP_NUM_COEFF (1-20)	| Sample Numerator Coefficients. Twenty coefficients for the polynomial in the Numerator of the $c_n$ equation. | unlimited | |
| SAMP_DEN_COEFF (1-20) | Sample Denominator Coefficients. Twenty coefficients for the polynomial in the Denominator of the $c_n$ equation. | unlimited | |	
<figcaption align = "center"><em>Table 3 : RPC metadata parameters in ICEYE Products</em></figcaption>
</figure>

## References
\bibliography