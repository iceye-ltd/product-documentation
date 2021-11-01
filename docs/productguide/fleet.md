# THE ICEYE FLEET

The ICEYE global imaging service uses an innovative satellite and sensor design based on advancements in small satellite technologies and an adaptable New Space approach. The ICEYE constellation is constantly evolving. We began 2021 with seven operating satellites and we’ll finish the year with thirteen systems. There will be more than ten more units added in 2022. The ICEYE constellation is optimized for persistent monitoring: rapidly repeatable access of any location on Earth, with flexible tasking for very high resolution spots as well as wide area scans.

<figure>
<img src="../img/iceye-gen2-satellite.png" style="width:100%">
<figcaption align = "center"><em>Figure 1: ICEYE Generation 2 Satellite</em></figcaption>
</figure>

The following describes the current fleet and their orbital configuration.

## SAR Sensor Parameters
The ICEYE sensors are X-band radars, each with an active phased array antenna and electronic beam steering. The innate mechanical agility of these low-mass satellites and their electronic steering enable fast and precise pointing of radar pulses to the ground. The satellites can also image to the right or left side of the satellite track. Technical parameters of the current sensors are listed in Table 1.

| SENSOR PARAMETER      | SPECIFICATION |
|-----------------------|---------------|
| Carrier frequency     | 9.65 GHz (X-band) |
| Antenna size          | 3.2 meters (along-track) x 0.4 meters |
| PRF                   | 2-10 kHz |
| Look direction        | both LEFT and RIGHT |
| Range Bandwidth       | 37.6-299 MHz |
| Peak Radiated Power   | 3.2 kW |
| Polarization          | VV |
| Incidence angle range | 15-35 (mode dependent) |
| Mass                  | 85 kg |
| Communication [radar payload data downlink] | X-band 140 Mbits/s|

<center>*Table 1: ICEYE Generation 2 satellite system parameters*</center> 

## Orbits

At present, the LTANs of the ICEYE constellation are not uniformly spaced. This means that the time to revisit a location on the equator varies over a period of days. The mean revisit rate at the equator is 20 hours and the mean time to access a location on the equator is 12 hours. At higher and lower latitudes, the rates are more frequent. Table 2 lists the orbital parameters of the current SAR instruments.
Each satellite is in a sun-synchronous orbit with 15 revolutions per day. Their ground track repeat cycles vary between 1 and 22 days, depending on the satellite. Each orbital plane is phased around the Earth with a different local time of the ascending node (LTAN). This means that the overall constellation can observe a location at different times of the day. This has an advantage over dawn-dusk sun-synchronous orbits, in which the local time of collection is always close to sunrise or sunset.

| Orbit Parameters ||
|-----------|-------|
| Nominal Altitude| 560 to 580 km|
| Orbit Parameters | Value |
| Inclination| 97.7\degree (sun-synchronous)|
| Orbits / Day| 15|
|Ground track repeat  | 1 - 22 days|
| Constellation mean revisit at equator| 20 hours|
| Constellation mean time to access at equator| 12 hours|
| Nodal crossing (LTAN)| 22:30, 15:05, 14:04, 21:36|
| Satellite Catalog Numbers|43800,44390,46497,46496,47510,47506 |
| Orbit maintenance |Ion Propulsion |

<center>*Table 2: Constellation Parameters*</center> 

Each satellite has the ability to slowly adjust their orbits throughout their operating life. Adjustment is usually performed in the orbital plane by raising or lowering the satellite's altitude. This changes the orbital period, which in turn changes the ground track repeat period. Over the next 12 months, the fleet will gradually be adjusted into one-day repeating coherent ground tracks. This provides novel opportunities to combine data collections of the same area whilst maintaining rapid access times.

The location of each ICEYE satellite is publicly available. The current configuration of the constellation can be found using the satellite catalog numbers in Table 2 and one of the excellent online orbital elements tools  such as [celestrak](http://www.celestrak.com)[@celestrak] or [n2yo](https://www.n2yo.com/?s=43800\%7C44390\%7C44389\%7C46497\%7C46496\%7C47510\%7C47506)[@n2yo], which provides a live view of the current ICEYE constellation.  

## References
\bibliography
