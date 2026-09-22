# 3\) Radar Frequency Bands

!!! summary inline end

    - SAR operates by transmitting and receiving electromagnetic radiation in the microwave spectrum or the so-called Super High Frequency (SHF) band, especially the IEEE bands L, S, C, X, and Ku, which cover frequencies from 1 GHz to 18 GHz and wavelengths from 30 cm to 1.67 cm, respectively.

    - The different IEEE bands correspond to different trade-offs between resolution and penetration: shorter wavelengths and higher frequencies provide better resolution but lower penetration and vice versa; microwaves can penetrate not only clouds but also vegetation and even certain upper surface layers, including snow and ice.

    - The X-band (wavelengths within 2.5–3.75 cm) dominates commercial SAR imaging as it offers the optimal combination of high resolution and cloud penetration for spaceborne sensors, making it ideal for urban and infrastructure monitoring.

    - The L-band (wavelengths within 15–30 cm) offers relatively modest resolution but excels at penetration as the waves penetrate forest canopies to reach forest floors, making it valuable for biomass, soil moisture, as well as snow and ice monitoring.

What do the human eye, a smartphone, and a synthetic aperture radar have in common? They are all optimized to receive Electromagnetic Radiation (EMR) from very specific portions of the *electromagnetic spectrum*. This chapter first presents an overview of the EMR spectrum and then explores the characteristics and application areas of the most popular bands used in SAR.

## 3.1) The Electromagnetic Spectrum: Microwaves

The <span class="underline">electromagnetic spectrum</span> is divided into separate spectral *bands* based on frequency and wavelength. The major regions within the electromagnetic spectrum, from low to high frequency, are the radio, microwave, infrared, visible light, ultraviolet, X-ray and gamma ray regions. The <span class="underline">radio spectrum</span> spans frequencies from 3 Hz to 300 GHz. The <span class="underline">microwave spectrum</span> falls within the higher frequency end of the radio spectrum, spanning frequencies from 300 MHz to 300GHz. While lower radio frequencies are used primarily for communication and broadcasting, microwaves are widely used in radar applications.

Table [<span class="underline">3.1</span>](#table-3.1-overview-of-microwave-frequency-band-designations) summarizes the microwave spectrum following the band name designations by the International Telecommunication Union (ITU) and the US Institute of Electrical and Electronics Engineers (IEEE). As shown in the table, the IEEE bands from *L* to *mm* within the broader ITU SHF and EHF radio bands constitute the microwave range used for satellite communication and radar applications. Each of the radio and microwave wavelengths is suited to different, specific applications due to differences in propagation characteristics.

<figure id="table-3.1-overview-of-microwave-frequency-band-designations">
<figcaption><strong>Table 3.1: Overview of Microwave Frequency Band Designations.</strong></figcaption>
<table>
<thead>
<tr>
<th align="left"><strong>ITU Band Name</strong></th>
<th align="left"><strong>IEEE Band Name</strong></th>
<th align="left"><strong>Wavelength [cm]</strong></th>
<th align="left"><strong>Frequency [GHz]</strong></th>
<th align="left"><strong>Remarks</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td align="left" colspan="2"><p><strong>VHF</strong></p><p>Very High Frequency</p></td>
<td align="left">100 - 1000</td>
<td align="left">0.3 - 0.03</td>
<td align="left">Used for example in FM radio, television and many other types of broadcasting and line of sight communication such as in air traffic control and maritime two-way radios on ships.</td>
</tr>
<tr>
<td align="left" colspan="2"><strong>UHF</strong><br>Ultra High Frequency</td>
<td align="left">30 - 100</td>
<td align="left">1 - 0.3</td>
<td align="left"><p>Used in many navigation systems, mobile telephony, two-way radios, as well as digital television broadcasting and industrial microwave ovens.</p><p>This band is at the long wavelength edge of the microwaves spectrum.</p></td>
</tr>
<tr>
<td align="left" rowspan="6"><strong>SHF<br></strong>Super High Frequency</td>
<td align="left"><strong>L</strong><br>Long Wave</td>
<td align="left">15 - 30</td>
<td align="left">2 - 1</td>
<td align="left">Used in satellite-based navigation systems such as GPS and GLONASS. The waves are able to penetrate vegetation better than shorter bands (below).</td>
</tr>
<tr>
<td align="left"><strong>S</strong><br>Short Wave</td>
<td align="left">7.5 - 15</td>
<td align="left">4 - 2</td>
<td align="left">Used for example for air traffic control, wireless LAN, Bluetooth and consumer microwave ovens.</td>
</tr>
<tr>
<td align="left"><strong>C</strong><br>Compromise</td>
<td align="left">3.75 - 7.50</td>
<td align="left">8 - 4</td>
<td align="left">The band originated as a <em>Compromise</em> between the S and X bands and is used for instance for satellite communication and modern radar including SAR.</td>
</tr>
<tr>
<td align="left"><p><strong>X</strong></p><p>Cross</p></td>
<td align="left">2.50 - 3.75</td>
<td align="left">12 - 8</td>
<td align="left">Used for SAR as it offers the best combination of cloud-penetration and ability to generate high resolution imagery from a spaceborne sensor.<br>The abbreviation X refers to <em>cross</em> as in <em>crosshair</em>. The band was already used during WWII in fire control.</td>
</tr>
<tr>
<td align="left"><strong>Ku</strong><br>Kurz-under</td>
<td align="left">1.67 - 2.50</td>
<td align="left">18 - 12</td>
<td align="left">Used primarily for satellite communication, including by direct television broadcast satellites.</td>
</tr>
<tr>
<td align="left"><strong>K</strong><br>Kurz</td>
<td align="left">1.11 - 1.67</td>
<td align="left">27 - 18</td>
<td align="left"><em>Kurz</em> is German for <em>short</em>. The band cannot be used for long-distance applications in the atmosphere as the resonance peak of water vapor is at 22.24 GHz which results in high <em>atmospheric attenuation</em>.</td>
</tr>
<tr>
<td align="left" rowspan="4"><strong>EHF<br></strong>Extremely High Frequency</td>
<td align="left"><strong>Ka</strong><br>Kurz-above</td>
<td align="left">0.75 - 1.11</td>
<td align="left">40 - 27</td>
<td align="left">Used for high-bandwidth satellite up-links and close-range targeting radars aboard military airplanes as well as for vehicle speed detection by law enforcement.</td>
</tr>
<tr>
<td align="left"><strong>V</strong></td>
<td align="left">0.40 - 0.75</td>
<td align="left">75 - 40</td>
<td align="left">Used mostly in radar and other scientific research. However, this band is also used by the 2021 Wi-Fi standard IEEE 802.11ay to achieve data transfer rates of 20 to 40 Gbit/s in open spaces.<br>This V-band should not be confused with the VHF band in the 1-10 m wavelength range.</td>
</tr>
<tr>
<td align="left"><strong>W</strong><br>(successor to V)</td>
<td align="left">0.27 - 0.40</td>
<td align="left">110 - 75</td>
<td align="left" rowspan="2">Used for similar purposes as the two above bands. A curiosity is that an Active Denial System developed by the U.S. Air Force called the Silent Guardian emits 3 mm wavelength radiation at an output power of 30 kW to repel unarmoured personnel.</td>
</tr>
<tr>
<td align="left"><strong>mm</strong> or <strong>G</strong><br>Millimeter Wave</td>
<td align="left">0.10 - 0.27</td>
<td align="left">300 - 110</td>
</tr>
<tr>
<td align="left" colspan="2"><p><strong>THF</strong></p><p>Tremendously High Frequency</p></td>
<td align="left">0.01 - 0.10</td>
<td align="left">3000 - 300</td>
<td align="left">Used for instance in experimental medical imaging, molecular dynamics, as well as condensed-matter physics.</td>
</tr>
</tbody>
</table>
</figure>

As indicated by Table [<span class="underline">3.1</span>](#table-3.1-overview-of-microwave-frequency-band-designations), the wavelength of electromagnetic radiation multiplied by its frequency always equals its propagation speed: \(\lambda f = v\). As you might also remember, the speed of light and other EMR in vacuum is \(v = c = 299,792,458\) meters per second. In air and other denser mediums, interactions with the charged particles in the medium slow the propagation speed, but the frequency stays unchanged.

## 3.2) Popular Frequency Bands for SAR

The most commonly used frequency bands for Synthetic Aperture Radar (SAR) are X, C, L, and S bands. Each band corresponds to a specific wavelength range, which influences several key aspects of SAR performance.

From an engineering standpoint, wavelength affects antenna design: longer wavelengths require larger antennas to achieve the same azimuth beamwidth as shorter wavelengths. Additionally, shorter wavelengths make it easier to achieve wide signal bandwidths in hardware, since they allow for large absolute bandwidths with relatively small fractional bandwidths. The choice of frequency band typically reflects a trade-off between penetration depth, target interaction, and practical constraints such as antenna size, available bandwidth, and platform altitude.

Microwaves are longer than visible wavelengths, which enables them to pass through clouds instead of scattering off water present in clouds. This is why most clouds are “invisible” in SAR images. It should be noted that in some cases, strong, heavy rain can attenuate the radar signal. This may result in a reduction in backscatter and a lower signal to noise ratio.

Table [<span class="underline">3.2</span>](#table-3.2-the-most-popular-sar-frequency-bands) tabulates the characteristics and typical application areas of the frequency bands commonly used for SAR.

<figure id="table-3.2-the-most-popular-sar-frequency-bands">
<figcaption><strong>Table 3.2: The Most Popular SAR Frequency Bands.</strong></figcaption>
<table>
<thead>
<tr>
<th align="left"><strong>IEEE Band</strong></th>
<th align="left"><strong>Wavelength [cm]</strong></th>
<th align="left"><strong>Frequency [GHz]</strong></th>
<th align="left"><strong>Characteristics</strong></th>
<th align="left"><strong>Typical SAR Applications</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Ku</strong><br>Kurz-under</td>
<td align="left">1.67 - 2.5</td>
<td align="left">18 - 12</td>
<td align="left">Potential for very high resolution;<br>Susceptible to atmospheric interference; Very low penetration</td>
<td align="left">Airport surveillance</td>
</tr>
<tr>
<td align="left"><p><strong>X</strong></p><p>Cross</p></td>
<td align="left">2.5 - 3.75</td>
<td align="left">12 - 8</td>
<td align="left">High Resolution (even below 1 m); Low penetration (blocked by vegetation and ice) and fast coherence decay in forested areas</td>
<td align="left">Urban and infrastructure as well as ice and snow monitoring</td>
</tr>
<tr>
<td align="left"><strong>C</strong><br>Compromise</td>
<td align="left">3.75 - 7.5</td>
<td align="left">8 - 4</td>
<td align="left">Somewhat high resolution;<br>Penetrates light vegetation and snow</td>
<td align="left">Mapping and change detection; Maritime navigation</td>
</tr>
<tr>
<td align="left"><strong>S</strong><br>Short Wave</td>
<td align="left">7.5 - 15</td>
<td align="left">4 - 2</td>
<td align="left">Moderate resolution;<br>Penetrates vegetation and ice</td>
<td align="left">Agriculture monitoring</td>
</tr>
<tr>
<td align="left"><strong>L</strong><br>Long Wave</td>
<td align="left">15 - 30</td>
<td align="left">2 - 1</td>
<td align="left">Lower resolution;<br>High penetration (reaches forest floors)</td>
<td align="left">Soil moisture and geophysical monitoring; Biomass and vegetation mapping</td>
</tr>
<tr>
<td align="left"><strong>P</strong></td>
<td align="left">30 - 130</td>
<td align="left">0.23 - 1</td>
<td align="left">Low resolution; very high penetration capabilities</td>
<td align="left">Forest monitoring, biomass estimation, imaging subsurface geology</td>
</tr>
</tbody>
</table>
</figure>

## 3.3) Penetration

As outlined in the above table, different radar bands are suited to different use cases. This relates to penetration, or the ability of a radar signal to pass through different materials. The amount of penetration depends on multiple factors, including radar wavelength and material properties. Longer wavelengths like L-band or P-band can penetrate tree canopy, vegetation, and dry soil because they interact less with small features and are less sensitive to water content. Shorter wavelengths, like X-band, will interact more with small surface features, and therefore penetrate less deeply. The tradeoff is that X-band is capable of generating high resolution imagery, where L and P-band are not. Figure [<span class="underline">3.1</span>](#figure-3.1-differences-in-penetration-capacity) illustrates how different wave wavelengths interact with surface features such as types of vegetation, dry sediment, and ice.

<figure id="figure-3.1-differences-in-penetration-capacity">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image14.png">
<figcaption><strong>Figure 3.1: Differences in Penetration Capacity.</strong> This figure illustrates how three commonly used wavelength bands for SAR interact differently with different surface features.</figcaption>
</figure>

!!! note
    History was made in 2025, due to the launch of the world’s first ever dual-frequency SAR satellite – NISAR – developed jointly by NASA (United States) and ISRO (India). The satellite wields two SAR sensors: one working at a frequency of 1.25 GHz (L-band), and the other at 3.20 GHz (S-band). The mission is to map the elevation of Earth's land and ice masses four to six times a month at resolutions of 5 to 10 meters and observe and measure some of the world’s most complex natural processes including those affecting the Antarctic cryosphere. In addition to being the world’s first dual-band SAR satellite, it is on record as the world's most expensive Earth-imaging satellite with total costs estimated as exceeding 1.5 billion USD. See the [related Wikipedia article: NISAR (satellite)](https://en.wikipedia.org/wiki/NISAR_(satellite)).
