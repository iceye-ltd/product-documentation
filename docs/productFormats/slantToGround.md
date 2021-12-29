
## Ground Range To Slant Range Conversion
For ground projected products, the ground range to slant range (GRSR) conversion can be performed using the GRSR polynomial coefficients (`GRSR_Coefficients`) stored in the metadata. Once applied, the slant range location of a specific pixel in the ground range can be calculated from:

$$
R_{slant}(j)=\sum_{k=0}^{p+1} C_k ((j-1)\delta_r)^k,\qquad j=[1...n]
$$

Where:

* $R_{slant}(j)$ is the slant range for the $j$-th ground range pixel
* $p$ is the order of the ground range to slant range polynomial (`grsr_poly_order` in the metadata)
* $C_k$ is the $k$-th polynomial coefficient
* $\delta_r$ is the ground range spacing (`range_spacing` in the metadata)

## Ground Range To Incidence Angle Conversion
The nominal incidence angle (the incidence angle for a given slant range intersecting the WGS84 ellipsoid. Not to be confused with the *local incidence angle* that takes into account the terrain relief) can be calculated from the ground range using the `Incidence_Angle_Coefficients` in the metadata and:

$$
\theta(j)=\sum_{k=0}^{p+1} C_k ((j-1)\delta_r)^k,\qquad j=[1...n]
$$

Where:

* $\theta(j)$ is the incidence angle for the $j$-th ground range pixel
* $p$ is the order of the ground range to incidence angle polynomial (`incidence_angle_poly_order` in the metadata)
* $C_k$ is the $k$-th polynomial coefficient
* $\delta_r$ is the ground range spacing (`range_spacing` in the metadata)

