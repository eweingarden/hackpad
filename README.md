# My Hackpad

## Description

A 3-key macropad built with a Seeed XIAO RP2040 and MX switches. Keys are mapped to 1, 2, and 3. Built as part of Hack Club's Hackpad YSWS program.

## Photos

!\[Alt text]([images/case.png](https://github.com/eweingarden/hackpad/blob/main/images/case.png))

!\[Alt text][(images/schematic.png)](https://github.com/eweingarden/hackpad/blob/main/images/schematic.png)

!\[Alt text][(images/pcb.png)](https://github.com/eweingarden/hackpad/blob/main/images/pcb.png)





## Bill of Materials (BOM)

|Part|Quantity|
|-|-|
|Seeed XIAO RP2040|1|
|MX Switches|3|
|1N4148 Diodes|3|
|M3 Screws|4|
|M3 Nuts|4|
|PCB (2-layer, JLCPCB)|1|
|3D Printed Case (top + bottom)|1|
|Soldering Iron|1|

## Firmware

Uses KMK on CircuitPython. Copy the `kmk` folder and `main.py` onto the CIRCUITPY drive.

## How to Build

1. Solder diodes first (watch polarity)
2. Solder XIAO RP2040
3. Clip switches into top plate
4. Solder switches to PCB
5. Flash firmware
6. Screw case together with M3 screws

