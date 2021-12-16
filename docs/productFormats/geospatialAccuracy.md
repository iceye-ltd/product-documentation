# Geospatial Accuracy

## Background

Being a *range-measuring* sensor A SAR system measures the range to a pixel in a SAR image very precisely. The sensor can also measure how the range to a pixel changes as the satellite moves along its trajectory (by comparing pulses) which provides precise information of the along-track location of a pixel. 
This distance (and change of distance) to each point is measured more accurately than a fraction of a wavelength and provides a table of radar cross section measurements as a function of range and along-track position. 

This table is the most accuarate source of SAR measurement available. In its purest form it is captured in the single look complex (SLC) image with other image formats being derived from it. Ground projected products and derived Level 2 products will always have a lower fidelity. 

On this page we discuss the factors that affect the geospatial accuracy of a SAR Product.

<figure>-
<img src="../img/radarRange_ManimCE_v0.10.0.gif" style="width:100%">
<figcaption align = "center"><em>Figure 1: Radar systems measure range very accurately using precise timing to measure how long it takes a pulse to reflect off an object.</em></figcaption>
</figure>

## On-Board Timing Errors
A fundamental source of error for all RADAR systems relates to timing. In radar systems, precise electronic clocks are used to record the passage of time. All clocks have some sort of drift in their accuracy which, if not corrected, affects the measured range and focussing of the imagery. ICEYE satellites apply timing corrections to their internal clocks by periodically synchronising with GNSS (Global Navigation Satellite System) satellites.

## Atmospheric Propagation
As the RADAR pulse propagates through the atmosphere, it undergoes diffraction which curves the path of the pulse adding an unintended increase to the range of an object. The amount of increase depends on the look angle, the location of the satellite and scene and even the time of day. The ICEYE SAR processor attempts to apply path length corrections (typically on the order of a couple of metres) using well established models.

## Orbit Knowledge
A potentially large source of errors comes from not knowing precisely where the sensor is when each pulse is transmitted and received.

different sources :

* Predicted
* Rapid
* Precise
* Scientific

## Terrain Height

## Rational Poynomial Coefficients

## Doppler Centroid Determination