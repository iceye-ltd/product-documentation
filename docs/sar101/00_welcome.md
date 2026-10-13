# Welcome

This is a learning resource intended to help anyone interested in SAR understand basic SAR fundamentals, theory, and terminology. As an introductory document, it was not written to be comprehensive, yet we believe it provides a foundation on which one can begin their journey through the world of SAR.

!!! note inline end

    The first version of this overview was excerpted with permission from [<span class="underline">The Essentials of SAR</span>](https://www.amazon.com/dp/B09CGKTLZV/ref=cm_sw_em_r_mt_dp_H9NDBJSVREXRK5PA4Z58), by Thomas P. Ager[<sup><span class="underline">1</span></sup>](https://sar.iceye.com/5.2.0/foundations/OverviewOfSAR/overviewOfSAR/#fn:1). \!

For those for whom superficial understanding is sufficient at this point, boldly browse the material: We have tried to leverage clear structuring, descriptive headings, illustrations and other elements to help you optimize your time use.

For those for whom this document is not enough, we urge you to see the list of references and further reading materials at the end\!

Note: While ICEYE specific examples and information appear throughout this document, this material is intended to cover the ideas on which SAR sensors and processors are generally based.

## Why Learn About SAR?

Synthetic Aperture Radar (SAR) is an outstanding remote sensing technique due to several exceptional capabilities, including:

  - **Clear Images In Any Weather**: As a radar-based active sensing technique SAR enables the formation of crisp images, day or night, in almost all weather conditions.

  - **High Resolution Independent of Distance**: One of the outstanding characteristics of SAR is that it is capable of high resolution regardless of how far away the sensor is from the ground. SAR sensors can provide very high resolution, even from space.

  - **Variable Resolution and Coverage**: With a phased array sensor, such as those operated by ICEYE, SAR illumination is controlled electronically, and it can be manipulated to vary resolution and coverage. With a phased array sensor, images can be collected over small areas at high resolution, over medium-sized areas at moderate resolution, or over large areas at coarse resolution.

  - **Precision Geolocation**: SAR measurements are inherently precise. Properly calibrated images can have geolocation accuracy less than the scale of a single pixel for well-defined features.

  - **Coherent Illumination and Diverse Products**: The controlled nature of SAR imaging enables the formation of images and many other products. These include sub-aperture image stacks that highlight glinting features and motion, dense elevation models, precise measurements of surface motion, and amplitude and coherent change images or series.

The SAR101: Foundations material describes why and how all these remarkable capabilities are possible with SAR. It also addresses the fundamental limitations and challenges inherent to SAR imagery, because only by understanding both the advantages and disadvantages can SAR imagery be effectively utilized for demanding applications.

<figure id="figure-1-paris">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image1-paris.jpeg">
<figcaption><strong>Figure 1: Paris.</strong> This SAR image over Paris, France, features the Arc de Triomphe on the left, the Eiffel Tower in the center, and the Seine river flowing between them. Flat surfaces appear dark and smooth while the metallic Eiffel Tower and other buildings are pronounced. As with all SAR images, it is difficult to tell if this image was acquired day or night, under clear skies or a storm - this is due to the remarkable all-weather collection capabilities of SAR. </figcaption>
</figure>

## Document Structure

SAR101: Foundations is structured into three parts that build on each other.

### Part 1: What SAR is All About?

**Part 1** consists of the first five chapters which describe the big picture of what SAR imaging is and how it works. While some information offered in these chapters can be considered basic background information, it must be understood to truly grasp topics in subsequent chapters.

  - **Chapter [<span class="underline">1</span>](01_introduction.md) Introduction to SAR** outlines the basic idea of SAR imaging by explaining core concepts and terms such as RADAR, real aperture radar, near and far range, range and azimuth resolution, ultimately describing the innovation of synthetic aperture radar.

  - **Chapter [<span class="underline">2</span>](02_satellite_orbits_and_constellations.md) Satellite Orbits and Constellations** explores the spaceborne nature of SAR by defining terms such as the sun-synchronous orbit and satellite constellation, illustrating how SAR systems function over space and time.

  - **Chapter [<span class="underline">3</span>](03_radar_frequency_bands.md) Radar Frequency Bands** offers an overview on electromagnetic radiation and its spectral diversity and clarifies what different bands are, and how they differ in terms of resolution, penetration, and coherence when used in SAR imaging.

  - **Chapter [<span class="underline">4</span>](04_antennas_and_sar_geometry.md) Antennas and SAR Geometry** dives into how active phased array antennas used in SAR work and the relationship between beamwidth and illumination power. Imaging geometry related terms and angles are also visually illustrated and defined.

  - **Chapter [<span class="underline">5</span>](05_collection_strategies.md) Collection Strategies** describes the three established technical approaches to collecting SAR data, as well as the corresponding trade-offs and use cases.

### Part 2: How are SAR Images Formed?

The chapters comprising **Part 2** focus on building understanding of SAR image resolution and quality, and interpretation. These are highly relevant for anyone working with SAR imagery.

  - **Chapter [<span class="underline">6</span>](06_spatial_resolution_and_geospatial_accuracy.md) Spatial Resolution and Geospatial Accuracy** covers the physical determinants of spatial resolution and geospatial accuracy of SAR images. We discuss how waveform modulation, pulse repetition frequency, pulse bandwidth, and incidence angle all impact slant, azimuth, range and ground resolutions. The impulse response function, nominal resolution, geolocation accuracy, and orthorectification are also discussed in this chapter.

  - **Chapter [<span class="underline">7</span>](07_separating_signals_from_noise.md) Separating Signals from Noise** introduces the Radar Range Equation and Signal-to-Noise Ratio (SNR), explains how signal power fades with range and system losses and how processing gains from pulse compression and coherent integration counter high noise floors. The chapter also defines many related concepts and terms.

  - **Chapter [<span class="underline">8</span>](08_sar_imagery_and_interpretation_considerations.md) SAR Imagery & Interpretation Considerations** explains the meaning of detection in SAR, and how SAR data actually consists of amplitude and phase value pairs. Backscatter, polarization and different scattering mechanisms and geometric distortions are discussed. The phenomena of speckle is illustrated and two notable image quality metrics are described.

### Part 3: How is SAR Data Packaged and Used?

**Part 3** focuses on data processing and analysis as well as data products. While the earlier chapters provide a great foundation for understanding SAR and related terminology, these final chapters are most relevant for the application oriented readers who want to understand how SAR can be practically utilized:

  - **Chapter [<span class="underline">9</span>](09_data_processing_and_analysis.md) Data Processing and Analysis** describes the process of converting SAR data into different data product levels, and defines several related terms. It explains processing choices relating to sampling and sample arrangement, axis alignment, multi-looking, and projection surfaces. It also lists some common SAR data analysis and utilization techniques.

  - **Chapter [<span class="underline">10</span>](10_data_products.md) Data Products** presents the most established data products on the market, from the early compensated phase history data products to newer colorized sub-aperture stack images and SAR Video.

<figure id="figure-2-diversity">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image2-diversity.jpeg">
<figcaption><strong>Figure 2: Diversity.</strong> A SAR image featuring a mountainous scene with agricultural and residential infrastructure. High quality SAR imagery can enable numerous detection, analysis, monitoring and planning use cases that may be instrumental in operations and research and sometimes also save countless lives.</figcaption>
</figure>

## Complementary Resources

The SAR101: Foundations material is offered together with other complementary information resources:

  - The [<span class="underline">Data Product Specification</span>](../productspecification/introduction.md) provides a business and application oriented overview and specification of the actual SAR data products that ICEYE offers. Compared to the SAR101, the specification documentation is more directly useful when starting to leverage SAR in partnership with ICEYE. However, to fully understand everything in it, studying SAR101 may be required.

  - The [<span class="underline">Technical Documentation</span>](../techdocs/00_welcome.md) is tailored to more advanced users of SAR, and provides information which is often more technical and generally more specific to ICEYE offerings. While SAR101 is curated to be read sequentially from top to bottom, the Technical Documentation is a collection of mostly independent articles that can be consumed in any order. They are intended for experienced users and SAR experts, who often are only interested in very specific portions of the documentation, and are sometimes already familiar with the other resources.

  - The [<span class="underline">Archives</span>](../archive/archive.md) provides documentation that is deemed deprecated but is nonetheless offered in case of interest.

  - The [<span class="underline">Glossary</span>](../glossary.md) defines many terms that are used in these documents and are relevant to SAR. The definitions are intended to help reduce confusion and inefficiency in SAR related communication.

## Feedback

All this material is written to serve your information needs. Any feedback that helps us improve this material is appreciated.
