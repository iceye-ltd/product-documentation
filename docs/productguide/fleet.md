# THE ICEYE FLEET

The ICEYE global imaging service uses an innovative satellite and sensor design based on advancements in small satellite technologies and an adaptable New Space approach. The ICEYE constellation is constantly evolving and it is optimized for persistent monitoring with fast and repeatable access to any location on Earth. Our flexible collection supports high resolution imaging over small areas as well as reduced resolution scans of wide areas. 

As of early 2022 there are 12 operating satellites with 6 satellites constantly supporting imaging operations. (The other 6 are either going through commissioning, orbit refinement or have been retired from imaging operations.)An additional 8 satellites are on the 2022 launch roster.

Our goal is to provide global access from a fleet of satellites, each in a coherent daily ground track repeat orbit (*CD-GTR*). This means that any location can be imaged multiple times from nearly the same orbital location using the same imaging geometry. The repeat cycle for these coherent collections is 24 hours or less. During the coming year our global coherent imaging plan will be implemented as we move more satellites into their allocated repeating ground tracks.

<figure>
<img src="../img/iceye-gen2-satellite.png" style="width:100%">
<figcaption align = "center"><em>Figure 1: ICEYE Generation 2 Satellite</em></figcaption>
</figure>

## SAR Sensor Parameters
The ICEYE sensors are X-band radars, each with an active phased array antenna and electronic beam steering. The innate mechanical agility of these low-mass satellites and their electronic steering enable fast and precise pointing of radar pulses to the ground. The satellites can also image to the right or left side of the satellite track. Technical parameters of the current sensors are listed in Table 1.

| SENSOR PARAMETER      | SPECIFICATION |
|-----------------------|---------------|
| Carrier frequency     | 9.65 GHz (X-band) |
| Antenna size          | 3.2 meters (along-track) x 0.4 meters |
| PRF                   | 2-6 kHz |
| Look direction        | both LEFT and RIGHT |
| Range Bandwidth       | 37.6-299 MHz |
| Peak Radiated Power   | 3.2 kW |
| Polarization          | VV |
| Incidence angle range | 15-35 (mode dependent) |
| Mass                  | 85 kg |
| Communication [radar payload data downlink] | X-band 140 Mbits/s|

<center>*Table 1: ICEYE Generation 2 satellite system parameters*</center> 

## Orbits

At present,  ICEYE satellites are all in sun-synchronous orbits with 15 orbits per day, but the orbits are not uniformly spaced. This means that the time to revisit a location on the equator varies over a period of days. The mean revisit rate at the equator is 20 hours and the mean time to access a location on the equator is 12 hours. At higher and lower latitudes, the rates are more frequent. Table 2 lists the orbital parameters of the current SAR instruments. Their ground track repeat cycles vary between 1 and 22 days. Each orbital plane is phased around the Earth with a different local time of the ascending node (LTAN) so that the overall constellation can observe a location at different times of the day. This has an advantage over dawn-dusk sun-synchronous orbits, in which the local time of collection is always close to sunrise or sunset.

<figure markdown>
| Orbit Parameters ||
|-----------|-------|
| Nominal Altitude| 560 to 580 km|
| Orbit Parameters | Value |
| Inclination| 97.7° (sun-synchronous)|
| Orbits / Day| 15|
|Ground track repeat  | 1 - 22 days|
| Constellation mean revisit at equator| 20 hours|
| Constellation mean time to access at equator| 12 hours|
| Orbit maintenance |Ion Propulsion |
<figcaption align = "center"><em>Table 2: Constellation Parameters</em></figcaption>
</figure>

<figure markdown>
|  Satellite Name    |  Launch Date  |  NORAD ID  |  LTAN      | Status |
|--------------------|---------------|------------|------------|--------|
|  <a href="https://www.n2yo.com/?s=43114" target=”_blank”>ICEYE-X1</a> |  2018-01-12   |  43114     |  22:22:05  |<span style="color:red">Out of operations |
|  <a href="https://www.n2yo.com/?s=43800" target=”_blank”>ICEYE-X2</a> |  2018-12-03   |  43800     |  22:05:36  |<span style="color:green">Operational|
|  <a href="https://www.n2yo.com/?s=44390" target=”_blank”>ICEYE-X4</a> |  2019-07-05   |  44390     |  15:17:33  |<span style="color:orange">Maintenance |
|  <a href="https://www.n2yo.com/?s=44389" target=”_blank”>ICEYE-X5</a> |  2019-07-05   |  44389     |  15:18:45  |<span style="color:red">Out of operations  |
|  <a href="https://www.n2yo.com/?s=46497" target=”_blank”>ICEYE-X6</a> |  2020-09-28   |  46497     |  13:23:08  |<span style="color:green">Operational|
|  <a href="https://www.n2yo.com/?s=46496" target=”_blank”>ICEYE-X7</a> |  2020-09-28   |  46496     |  13:20:12  |<span style="color:green">Operational|
|  <a href="https://www.n2yo.com/?s=47510" target=”_blank”>ICEYE-X8</a> |  2021-01-24   |  47510     |  21:29:19  |<span style="color:green">Operational|
|  <a href="https://www.n2yo.com/?s=47506" target=”_blank”>ICEYE-X9</a> |  2021-01-24   |  47506     |  21:30:06  |<span style="color:green">Operational|
| <a href="https://www.n2yo.com/?s=48918" target=”_blank”>ICEYE-X11</a> |  2021-06-30   |  48918     |  02:07:01  |<span style="color:green">Operational|
| <a href="https://www.n2yo.com/?s=48914" target=”_blank”>ICEYE-X12</a> |  2021-06-30   |  48914     |  02:06:42  |<span style="color:orange">Maintenance|
| <a href="https://www.n2yo.com/?s=48916" target=”_blank”>ICEYE-X13</a> |  2021-06-30   |  48916     |  02:06:41  |<span style="color:orange">Maintenance|
| <a href="https://www.n2yo.com/?s=48917" target=”_blank”>ICEYE-X15</a> |  2021-06-30   |  48917     |  02:07:07  |<span style="color:orange">Maintenance|
| <a href="https://www.n2yo.com/?s=51070" target=”_blank”>ICEYE-X14</a> |  2021-06-30   |  51070     |  02:07:07  |[ICEYE US]|
| <a href="https://www.n2yo.com/?s=51008" target=”_blank”>ICEYE-X16</a> |  2021-06-30   |  51008     |  02:07:07  |<span style="color:orange">Maintenance|
<figcaption align = "center"><em>Table 3: ICEYE satellites status and LTANs. </em></figcaption>
</figure>
!!! info 
    Click on a satellite name in Table 3 to open a new tab showing where the satellite is now on [n2yo](https://www.n2yo.com/)[@n2yo]

Each satellite has the ability to slowly adjust its orbits throughout its operating life. The adjustment is usually performed in the orbital plane by raising or lowering the satellite's altitude. This changes the orbital period, which in turn changes the ground track repeat period. Over the next 12 months, the fleet will gradually be adjusted into one-day repeating coherent ground tracks. This provides novel opportunities to combine identical data collections of the same area whilst maintaining rapid access times.

<figure markdown>
![placeholder](img/muldrow.gif){width="600"}
<figcaption align = "center"><em>Figure 2: Coherent Daily Ground Track Repeat imagery reveals unprecedented levels of intelligence such as the flow rate of The Muldrow Glacier USA between 16th and 30th April 2021.</em></figcaption>
</figure> 

The satellite orbital agility is provided via a set of ion thrusters positioned around the satellite. These provede a near limitless supply of manoevring thrust, and also ensure that the constellation can be rapidly configured to increase the coverage rate of certain geographic regions in response to world events.

The location of each ICEYE satellite is publicly available. The current configuration of the constellation can be found using the satellite catalog numbers in Table 3 and one of the excellent online orbital elements tools such as [celestrak](http://www.celestrak.com)[@celestrak] or [n2yo](https://www.n2yo.com/)[@n2yo], which provide a live view of the current ICEYE constellation.  

## References
\bibliography
