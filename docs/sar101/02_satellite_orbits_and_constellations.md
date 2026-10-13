# 2\) Satellite Orbits and Constellations

!!! summary

    - Most SAR and Earth Observation (EO) satellites operate in a Low Earth Orbit (LEO) at an altitude of 500–800 km, providing an optimal balance of coverage, resolution, and orbital mechanics.

    - Sun-Synchronous Orbit (SSO) is preferred for EO because it ensures satellites pass over locations at the same local time each day, providing consistent imaging conditions and enabling effective change detection.

    - Modern SAR satellites typically employ ion propulsion thrusters to maintain the desired orbital parameters despite gravitational perturbations, and solar panels to have sufficient energy at all times.

    - Satellites often belong to a fleet that is operated as a constellation to enable revisit capabilities and flexible, reliable coverage that a single satellite could never provide.

Satellites used for communication and Earth observation—including those carrying Synthetic Aperture Radar (SAR) instruments—operate in orbit around the Earth. In other words, they follow a <span class="underline">geocentric orbit</span>, meaning the Earth is at the center of their motion. The most common geocentric orbits are visualized in Figure [<span class="underline">2.1</span>](#figure-2.1-most-common-geocentric-orbits). This chapter introduces facts relating to the spaceborne nature of SAR systems, satellites and constellations.

<figure id="figure-2.1-most-common-geocentric-orbits">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image10.png">
<figcaption><strong>Figure 2.1: Most Common Geocentric Orbits.</strong> Note that this illustration is not to scale.</figcaption>
</figure>

Note that there are a few basic terms that are essential when describing orbits: For geocentric orbits, <span class="underline">altitude</span> is the distance between the satellite and the Earth’s surface or sea level. With elliptic orbits this varies from the so-called perigee (closest point) to the apogee (farthest point). <span class="underline">Period</span> is the duration of one full orbit cycle. <span class="underline">Inclination</span> is the angle of the orbit relative to the equator and the poles which have inclinations of 0° and 90°, correspondingly. For example, in Figure [<span class="underline">2.1</span>](#figure-2.1-most-common-geocentric-orbits), the GEO and LEO satellites are portrayed at roughly 0° and 30° inclinations, respectively.

## 2.1) Geocentric Orbit Classes and Geometries

The most common geocentric orbits that are visualized in Figure [<span class="underline">2.1</span>](#figure-2.1-most-common-geocentric-orbits) are also defined in Table [<span class="underline">2.1</span>](#table-2.1-geocentric-orbit-classes-by-altitude). These orbits are grouped according to their altitude above Earth’s surface, which is a primary factor influencing orbital velocity, coverage, communication latency, and radiation environment. The table also includes the High Earth Orbit (HEO) which is less commonly used for Earth imaging. HEO, Medium Earth Orbit (MEO) and Low Earth Orbit (LEO) form three distinct altitude zones with boundaries at 2,000 and 35,786 km from the equator. For scale, the Moon orbits the Earth at a distance of around 384 million meters, which is over 10 times farther than the MEO-HEO boundary.

<figure id="table-2.1-geocentric-orbit-classes-by-altitude">
<figcaption><strong>Table 2.1: Geocentric Orbit Classes by Altitude</strong></figcaption>
<table>
<thead>
<tr>
<th align="left"><strong>Abbreviation and Name</strong></th>
<th align="left"><strong>Definition</strong></th>
<th align="left"><strong>Remarks</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>LEO</strong><br>Low Earth Orbit</td>
<td align="left">A geocentric orbit with an altitude between 160 and 2,000 km above sea level, typically resulting in orbital periods of 90-130 min for near-circular orbits.</td>
<td align="left">Most human-made objects in space are in LEO, with the altitudes between 500 and 900 km being most popular.</td>
</tr>
<tr>
<td align="left"><strong>MEO</strong><br>Medium Earth Orbit</td>
<td align="left">A geocentric orbit with an altitude between 2,000 and 35,786 km above sea level, resulting in orbital periods between 2 and 24 hours.</td>
<td align="left">Global navigation system satellite constellations (i.e., GPS) are in MEO with an orbital period of about 12 hours, passing the same two spots on the equator twice daily.</td>
</tr>
<tr>
<td align="left"><strong>HEO</strong><br>High Earth Orbit</td>
<td align="left">A geocentric orbit with an apogee (farthest point) farther than 35,786 km away from Earth’s surface.</td>
<td align="left">Ideal for outward focused satellites such as those intended for deep space observation.</td>
</tr>
</tbody>
</table>
</figure>

Orbits in MEO and HEO are less popular than LEO for Earth observation. In HEO, the gravitational pull towards Earth is so low that the orbital velocities have to also be very low, leading to orbital periods of days instead of minutes. Additionally, communication latency is significant (\>240 ms), and the Earth’s magnetic fields no longer protect the satellites from radiation. These issues do not impact satellites in LEO.

In addition to altitude, geocentric orbits can also be classified by their inclination and motion relative to Earth’s rotation and the Sun. These characteristics determine how the satellite’s ground track evolves over time and strongly influence revisit patterns, viewing geometry, and temporal consistency of observations. Table [<span class="underline">2.2</span>](#table-2.2-common-geocentric-orbit-geometries) therefore introduces several commonly used orbit geometries, which can be combined with different altitude classes depending on mission objectives.

<figure id="table-2.2-common-geocentric-orbit-geometries">
<figcaption><strong>Table 2.2: Common Geocentric Orbit Geometries.</strong></figcaption>
<table>
<thead>
<tr>
<th align="left"><strong>Abbreviation and Name</strong></th>
<th align="left"><strong>Definition</strong></th>
<th align="left"><strong>Remarks</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>SSO</strong><br>Sun-Synchronous Orbit</td>
<td align="left">A special kind of near-polar orbit where the satellite travels over or near the Earth's north and south poles as the planet rotates beneath it. What makes SSO unique is that the passes of the satellite over a specific point of the Earth happen at roughly the same local time of day on each orbit.</td>
<td align="left">Popular for optical and infrared imaging, reconnaissance, and weather satellites because the sun-synchronicity provides consistent lighting. Also popular for SAR satellites because of the time-synchronicity.</td>
</tr>
<tr>
<td align="left"><strong>MIO</strong><br>Mid-Inclined Orbit</td>
<td align="left">An orbit with an inclination that is neither near-equatorial nor near-polar, typically covering latitudes up to a limited range in both hemispheres rather than the entire globe.</td>
<td align="left">Mid-inclined orbits are often used when frequent revisits are needed over specific latitude bands, such as mid-latitude regions where most of the world’s population and infrastructure are located.</td>
</tr>
<tr>
<td align="left"><strong>GEO</strong><br>Geostationary Orbit</td>
<td align="left">A circular geosynchronous orbit 35,786 km above the equator, and following the direction of Earth's rotation.</td>
<td align="left">Popular for communications, weather and navigation satellites that need to always remain directly above a pre-specified fixed location.</td>
</tr>
</tbody>
</table>
</figure>

While LEO is the most popular altitude class for SAR satellites, SSO and MIO defined in Table [<span class="underline">2.2</span>](#table-2.2-common-geocentric-orbit-geometries) are the most popular geometries. These are discussed further in Section 2.2.

## 2.2) Sun-Synchronous and Mid-Inclined Orbits For Earth Observation

<span class="underline">Earth Observation (EO)</span> is the collection of data on Earth's physical, chemical, and biological systems using remote sensing (like SAR satellites) and/or local measurements (like weather measurement stations). Earth observation is essential for monitoring and analyzing natural and anthropogenic environments, especially to identify and track changes and trends.

Most SAR and other EO (here EO means earth observation, not specifically electro-optical) satellites orbit the Earth in Sun-Synchronous Orbit (SSO), defined in Table [<span class="underline">2.2</span>](#table-2.2-common-geocentric-orbit-geometries), within the LEO region at an altitude ranging from 500 to 800 km above the Earth's surface and an orbital velocity (speed) of 7-8 km/s. While orbits are often well known and predictable, they are not constant. This is partly due to gravitational perturbations due to the non-uniform shape of the Earth. The altitude of a satellite and its orbital speed vary during orbit. However, the altitude, velocity, inclination, and other parameters (see Table [<span class="underline">2.3</span>](#table-2.3-orbit-parameters-for-iceyes-sar-satellite-constellation) below) of a satellite in SSO are calculated and constantly monitored and adjusted – in ICEYE’s case with ion propulsion thrusters – to maintain the desired SSO.

SSO is achieved by choosing an <span class="underline">orbit inclination</span> that is <span class="underline">near-polar</span> (typically between 96° and 100°), so that the satellites orbit near-vertically and pass both the South and North poles at every cycle. Together with the chosen orbit altitude and velocity, the high inclination leads to a <span class="underline">nodal precession</span>, or the slow movement of the orbital plane around the rotational axis of the Earth, as illustrated in Figure [<span class="underline">2.2</span>](#figure-2.2-animation-of-a-sun-synchronous-orbit).

<figure id="figure-2.2-animation-of-a-sun-synchronous-orbit">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/sun-synchronous_orbit_3d.gif">
<figcaption><strong>Figure 2.2: Animation of a Sun-Synchronous Orbit.</strong> As shown here, the orbital plane precesses so that the satellite crosses each latitude at the same local solar time—in this case near dawn and dusk—providing consistent illumination conditions for Earth observation.</figcaption>
</figure>

As summarized in Table [<span class="underline">2.2</span>](#table-2.2-common-geocentric-orbit-geometries), a satellite in SSO appears fixed with respect to the sun as the Earth completes its orbit. When a satellite is in SSO, any point on Earth it passes will be passed again at roughly the same local time every day. This time-synchronicity is valuable in many SAR imaging use cases where it is preferable to compare images from the exact same location and approximately the same time of day across many different dates. Another benefit is that the solar arrays that power the satellite constantly face the sun in the same orientation which reduces the need for large batteries.

<span class="underline">Mid-Inclined Orbits (MIOs)</span>, also defined in Table [<span class="underline">2.2</span>](#table-2.2-common-geocentric-orbit-geometries), do not provide the sun and time synchronicity that SSOs provide, but since their orbits are more horizontal or equatorial than SSO orbits, they spend a higher fraction of their orbit time above populous regions rather than the poles. This enables frequent coverage over latitudes where most of the world’s population and infrastructure are located.

## 2.3) Satellite Constellations and Repeat Imaging

Most SAR satellites belong to a fleet of satellites, often referred to as a constellation. While a <span class="underline">satellite fleet</span> refers to a group of satellites from the same manufacturer or operator, a <span class="underline">satellite constellation</span> refers to a fleet where the individual satellites are organized into sets of complementary orbital planes and operated in tandem as a single system to fulfill a shared mission or objective.

To provide an example, ICEYE operates the world’s largest commercial SAR satellite constellation, with the ability to rapidly provide high-resolution coverage of any location on the surface of the Earth. Table [<span class="underline">2.3</span>](#table-2.3-orbit-parameters-for-iceyes-sar-satellite-constellation) provides some more information about the orbits of ICEYE SAR satellites. Further information is available online at the page [<span class="underline">The ICEYE Fleet</span>](https://sar.iceye.com/5.0/productguide/fleet/).

<figure id="table-2.3-orbit-parameters-for-iceyes-sar-satellite-constellation">
<figcaption><strong>Table 2.3: Orbit Parameters for ICEYE's SAR Satellite Constellation.</strong></figcaption>
<table>
<thead>
<tr>
<th align="left"><strong>Parameter</strong></th>
<th align="left"><strong>Value</strong></th>
<th align="left"><strong>Explanation</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Nominal Altitude</td>
<td align="left">400 - 600 km</td>
<td align="left">The distance between Earth’s sea level and the satellite orbits.</td>
</tr>
<tr>
<td align="left">Inclination</td>
<td align="left">97.7° (sun-synchronous) and 45 (mid-inclination)</td>
<td align="left">The angle of the orbits relative to the equator and the poles which have inclinations of 0° and 90°, correspondingly.</td>
</tr>
<tr>
<td align="left">Orbits / Day</td>
<td align="left">15</td>
<td align="left">The number of full cycles the satellites fly through each day.</td>
</tr>
<tr>
<td align="left">Ground Track Repeat</td>
<td align="left">1 - 22 days</td>
<td align="left">The duration cycle for repeating the exact same path on the surface of the Earth (the path drawn on the surface by a line that connects the satellite with the center of the Earth).</td>
</tr>
<tr>
<td align="left">Orbit Maintenance</td>
<td align="left">Ion Propulsion</td>
<td align="left">ICEYE satellites use ion propulsion to maintain or slowly adjust their orbits as desired.</td>
</tr>
</tbody>
</table>
</figure>

A sufficiently large constellation allows, among other things, reliable and fast repeat imaging. <span class="underline">Repeat imaging</span> is the imaging of a specific location on multiple separate occasions.

A <span class="underline">ground track repeat orbit</span> is a periodic orbit in which, after a fixed number of orbits (N) and a fixed number of Earth rotations (M; days), the satellite starts to repeat the same orbit path. That is, it is starting to fly over the almost exact same ground track on the Earth’s surface again.

However, as described in Table [<span class="underline">2.3</span>](#table-2.3-orbit-parameters-for-iceyes-sar-satellite-constellation), the parameters N and M vary by satellite, and in the case of ICEYE, M is between 1 to 22 (Earth rotations, ie. days) and N is between 15-330 (orbits around the Earth), assuming every satellite does exactly 15 orbits per day as per the table. Figure [<span class="underline">2.3</span>](#figure-2.3-ground-track-repeat-orbit) visualizes the ground track and imaging swath of a satellite with a one day cycle length during which it performs 10 orbits. Monitoring with daily ground track repeat-pass images is illustrated in Figure [<span class="underline">2.4</span>](#figure-2.4-ground-track-repeat-pass-imaging).

<figure id="figure-2.3-ground-track-repeat-orbit">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image12.png">
<figcaption><strong>Figure 2.3: Ground Track Repeat Orbit.</strong> This illustrates a satellite on a Sun Synchronous orbit with a ground track that is approximately 1257 km in length that is repeated daily. The illustration also shows a 220 km swath which the satellite could image during its orbit.</figcaption>
</figure>

The benefit of a short ground track repeat cycle time is that it enables high frequency repeat imaging. <span class="underline">Daily coherent ground track repeat imaging</span> occurs when a satellite is able to image a target from the same point in its cycle with the same viewing geometry, once a day, for multiple days in a row. Coherent change detection techniques (see [<span class="underline">9.8</span>](09_data_processing_and_analysis.md#98-other-phase-based-techniques)) can usually be applied to images collected in such an orbit.

However, most SAR satellites follow longer cycle times, because they allow the satellites to cover a higher proportion of the Earth’s surface during each cycle. Note that the ground track illustrated in Figure [<span class="underline">2.3</span>](#figure-2.3-ground-track-repeat-orbit) had a cycle time of just one day. If the total swath area of a satellite on a 21 day cycle time was illustrated in the image, the image would be almost entirely green. In practice, a constellation would need a very large number of satellites to achieve global imaging coverage if all of them were constrained to very short, repetitive orbits.

Note that not all repeat imaging is ground track repeat imaging. <span class="underline">Ground track repeat imaging</span> is repeat data collection recorded from the exact same point in the periodic cycle of a repeat orbit. If the same target is imaged at different points in the cycle or by different satellites in different orbits it is still considered repeat imaging, but the characteristics of the image are often so different that capabilities such as coherent change detection and InSAR detection are not possible.

<figure id="figure-2.4-ground-track-repeat-pass-imaging">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/iceye_rotterdam_port_cars.gif">
<figcaption><strong>Figure 2.4: Ground Track Repeat-Pass Imaging.</strong> This sequence of repeat-pass images from ICEYE shows activity relating to cargo ship logistics over 17 days in an area of the Rotterdam port.</figcaption>
</figure>

!!! history
    For decades, SAR satellites were exclusively single missions. Then came tandem missions where the synergy of two similar satellites could be utilized. The European Space Agency operated ERS-1 and ERS-2 between 1995 and 1996 which enabled the creation of high-quality digital elevation models with interferometric SAR (see Section [<span class="underline">9.7</span>](09_data_processing_and_analysis.md#97-phase-based-interferometric-techniques)), and in 2007 the first true four-satellite constellation was launched, the COSMO-SkyMed by the Italian Space Agency. It pioneered many constellation tasking concepts and provided daily revisit times. Currently, the world’s largest and most modern commercial SAR satellite constellation is owned and operated by ICEYE.

## 2.4) Orbit Pass Directions and Look Side

We have already learned about the different orbits SAR sensors can take advantage of, including Sun-Synchronous Orbit (SSO) and Mid Inclination Orbit (MIO). While orbiting the Earth, satellites travel both northward (ascending) and southward (descending). SAR satellites also can point to the left or to the right, called the <span class="underline">look side</span>—this means there are four basic geometries with which a SAR image can be collected: ascending left, ascending right, descending left, or descending right. We will cover imaging geometry in more detail in Section [<span class="underline">4.3</span>](04_antennas_and_sar_geometry.md#43-imaging-geometry-and-related-angles). The orbit pass and look side will impact the way ground features appear in a SAR image, especially in areas with high topography. Considering orbit pass and look side is also important for certain advanced applications of SAR, such as CCD and ACD (covered in more detail in Section [<span class="underline">9.8</span>](09_data_processing_and_analysis.md#98-other-phase-based-techniques)).

<figure id="figure-2.5-orbit-pass-directions-and-look-side">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image11.png">
<figcaption><strong>Figure 2.5: Orbit Pass Directions and Look Side.</strong> In this illustration (not to scale) of a near-polar orbit, we can see what each of the basic geometries look like, and examples of an approximated ground footprint. Red shows the orbit pass direction, green shows the look side of the satellite.</figcaption>
</figure>

## 2.5) Field of Regard

<span class="underline">Field of Regard</span> is the maximum ground area a SAR sensor can image by steering the sensor, either mechanically or electronically. Field of Regard is separate from Field of View, which is the ground area a sensor can image at some moment in time. The Field of Regard is thus the union of all positions to which the Field of View can be steered. It is important to note that field of view tends to be a term reserved for optical satellites, not SAR, due to the nature of SAR collection. Field of regard is impacted by sensor design parameters such as antenna size and transmit power, which are discussed in more detail in Section [<span class="underline">4.2</span>](04_antennas_and_sar_geometry.md#42-beamwidth-and-illumination-power).
