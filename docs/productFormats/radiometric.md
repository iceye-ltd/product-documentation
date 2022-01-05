
## Calibration and Projection Conversion

The grey-scale values that you see and measure in a SAR image do not directly correspond to a scientific measurement of the radar cross section of the an area of the ground. In most cases this does not matter as users just want to look at the spatial distribution of scattering objects (and sometimes their relative radar reflectivity). SAR is a scientific instrument though and some applications can obtain additional information of the ground's properties by having a true measure of the radar reflectivity in a pixel (mean radar cross section). To unlock this information, a **calibration factor** needs to be applied to the data. This next section will provide information on how this can be achieved. First however we need to have a short discussion on mean radar cross section.

### Different Types of Mean Radar Cross Section

An object's ability to scatter energy back towards the radar is called its *radar cross section* (RCS). It is not a fixed property and its value can change under different situations:

* The orientation of the object with respect to the RADAR
* The shape of the object
* The frequency / wavelength of the RADAR compared to the size of the object
* The material that the object is made from 
    * (and specifically its ability to support an electromagnetic field - called its *dielectric constant*; metal = radar reflective; plastic = not radar reflective)
* Polarization

The units of RCS are $m^2$ as it represents the cross-section in the direction of the RADAR of a hypothetical sphere that would reflect the same amount of energy that is observed by the RADAR from the object. The symbol for RCS is by convention $\sigma$.

In the real world though we rarely have only one scattering object in a resolution cell (and almost never a 1m metal sphere), so in reality a pixel in a SAR image contains many hundreds of scattering objects and has a *mean* RADAR cross section. To identify this from a single object RCS we use the symbol $\sigma_0$. 

<figure>
<img src="../img/sigma-beta-gamma-explained.png" style="width:100%">
<figcaption align = "center"><em>Figure 1: The relationship between β0, γ0 and σ0</em></figcaption>
</figure>

When looking at terrain with a SAR sensor, the orientation of the ground compared to the resolution cell has a large impact on the perceived mean RCS. The slant plane area of a pixel is constant but when projected onto the ground, the area of the terrain that contributes to the mean RCS changes with incidence angle. This leads to a 'brightning effect' at lower incidence angles in the slant plane image as each pixel's ground area increases. This means that the observed mean RCS values in the SLC image represent the **RADAR brightness** rather than the terrain mean RCS $\sigma_0$. The RADAR brightness is denoted by $\beta_0$.

Another noticeable and sometimes undesirable effect is that of local terrain topography. Terrain slopes than are oriented towards the satellite have a larger radar backscatter towards the RADAR than leeward slopes inclined away from the radar that tend to reflect radar energy away. If the actual reflective properties of the terrain are needed then this relief effect can be *flattened* to create a $\gamma_0$ image.

The relationship between these three properties can be seen in Figure 1.


### Calibration Correction

Calibration of ICEYE's sensors is performed using the Amazon and Congo forests for radiometric and beam calibration and using point target calibration sites for impulse response and geolocation calibration. The conversion to radar brightness ($\beta_0$) values are provided through the application of a calibration factor (CF) annotated as `calibration_factor` in the product metadata:

$$ \beta_0 = CF|DN_{SLC}|^2 $$

$$ \beta_0 = CF\frac{|DN_{GRD}|^2}{\sin(\theta)} $$
 
For amplitude scenes, a conversion to $\sigma_0$ has already been applied using the incidence angle calculated from the ellipsoid model. This simplifies the calculation of the radar backscatter to :

$$
\sigma_0 = CF |DN_{GRD}|^2 
$$

$$
\sigma_{0dB} = 10\log_{10}(\sigma_0) 
$$

$$
|DN_{GRD}|^2 = |DN_{SLC}|^2 \sin(\theta)
$$

If the processing of $\beta_0$ is required from the amplitude image for further orthorectification to $\sigma_0$ or $\gamma_0$ values using a local DEM, then the conversion to radar brightness can be performed using the incidence angle information annotated in the metadata (see [Ground Range To Incidence Angle Conversion](../slantToGround#ground-range-to-incidence-angle-conversion)). 

($\gamma_0$) values can be obtained using the $\beta_0$ values and a local digital elevation model.  
To assist in viewing analysis and projection, all amplitude products are projected onto the WGS84 Reference Ellipsoid.

