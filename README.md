<!-- title: The Perfect Strangers - Technical Documentation -->
# Technical Documentation <!-- omit from toc -->

[![Website](https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://theperfectstrangers.band/)  [![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.patreon.com/ThePerfectStrangers) [![Youtube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@theperfectstangers) [![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/theperfectstrangersrock) [![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://www.facebook.com/ThePerfectStrangersRock)

All technical documentation related to band, [The Perfect Strangers](https://ThePerfectStrangers.band).

- [Complete Technical Documentation](#complete-technical-documentation)
- [Rider](#rider)
- [Document Style](#document-style)
- [Stage Diagram](#stage-diagram)
  - [Full Band](#full-band)
- [Input List](#input-list)
  - [Full Band](#full-band-1)
    - [Input + Equipment](#input--equipment)
    - [Split](#split)
      - [Modes](#modes)
      - [Splitter Assignments](#splitter-assignments)
        - [Order \& Ports](#order--ports)
        - [Snake Tails](#snake-tails)
    - [Mixer Configuration](#mixer-configuration)
  - [Acoustic](#acoustic)
    - [Input + Equipment](#input--equipment-1)
- [Repository Health](#repository-health)

# Complete Technical Documentation

For a complete PDF that includes the Rider, Stage Diagram, and Input List, click the link below:

<a id="raw-url" href="https://raw.githubusercontent.com/ThePerfectStrangers/TechnicalDocumentation/main/Complete%20Technical%20Documentation/The%20Perfect%20Strangers%20-%20Technical%20Documentation.pdf">![Static Badge](https://img.shields.io/badge/PDF-Complete%20Technical%20Documentation-EC1C24?logo=adobeacrobatreader)
</a>

# Rider

The band uses a rider to ensure the safety of the the public, band members, and their equipment.

<a id="raw-url" href="https://raw.githubusercontent.com/ThePerfectStrangers/TechnicalDocumentation/main/Rider/Rider.pdf">![Static Badge](https://img.shields.io/badge/PDF-Rider-EC1C24?logo=adobeacrobatreader)
</a>

# Document Style

The graphics in this repository use the following color convention for the band members:

<img src="./Assets/BandColorConvention/BandColorConvention.png" width=75%>

# Stage Diagram

These are diagrams relating to the configuration and placement of people and/or equipment on stage.

## Full Band

This is the general layout of the band. It includes the people, microphones, equipment, cable routes, where power is needed, mixing equipment, and speaker placement.

![Full Band Stage Diagram](./Assets/StageDiagram/FullBand/StageDiagram.drawio.png)

<a id="raw-url" href="https://raw.githubusercontent.com/ThePerfectStrangers/TechnicalDocumentation/main/StageDiagram/FullBand/StageDiagram.drawio.pdf">![Static Badge](https://img.shields.io/badge/PDF-StageDiagram-EC1C24?logo=adobeacrobatreader)
</a>

**Note:**  In a situation where the band is not in charge of the PA, the PA speakers located Downstage Right and Downstage Left should be omitted from consideration.


# Input List

This is a list of inputs needed by the band. It includes:
  * The input description
  * Type of equipment (such as microphone)
  * If 48V Phantom Power is required
  * Other notes related to the input channel

48V phantom power and gain control are managed on stage by the band's IEM mixing rig. All channels are targetd for a gain of -18.5. A split is used to send a line-level signal to FOH. More information can be found below regarding the split.

## Full Band

### Input + Equipment

![Input and equipment list](./Assets/InputList/FullBand/Input+Equipment.png)

<a id="raw-url" href="https://raw.githubusercontent.com/ThePerfectStrangers/TechnicalDocumentation/main/InputList\FullBand\InputList.pdf">![Static Badge](https://img.shields.io/badge/PDF-FullBandSetup-EC1C24?logo=adobeacrobatreader)
</a>

### Split

#### Modes

The band requires a 24-channel split. The band can provide 15 feet of labeled split tails (XLR) from the band's IEM box if needed.

When splitting is required, we can support two modes:
1. (Preferred) We run all mics into our IEM box and send a split to the front-of-house (FOH). We will control all gain (staged to -18.5). This is preferred because it reduces the amount of time each band member must spend recalibrating their mix.
2. All mics run to FOH and FOH sends us a split to our IEM box. This method requires the venue/sound company to provide the split.

#### Splitter Assignments

All ports are XLR male.

##### Order & Ports

The splitter ports are ordered as follows:
1. **Drums**: 1-9
2. **Vocals**: 10-16
  * Vocals 6 & 7 may not be required for every show as they are for guest vocalists.
3. **Piano/Keyboards**: 17-18
4. **Guitars**: 19-22
  * (E): Electric
  * (A): Acoustic
5. **Bass**: 23

##### Snake Tails

The snake coming from the split is banded into groups of 4 wires, ordered Green, Blue, Yellow, and Red. Each bundle is represented by a unique color. These colors can be found in the numbering section of the Split Map.

**Note:** All outputs are set as [Input/LC (IN/LC)](https://drewbrashler.com/2017/x32-output-tap/) from the band's mixer. You can find out more details regarding the split labels on the Split Map:

![Split Map](./Assets/InputList/FullBand/SplitMap.png)

<a id="raw-url" href="https://raw.githubusercontent.com/ThePerfectStrangers/TechnicalDocumentation/main/InputList\FullBand\SplitMap.pdf">![Static Badge](https://img.shields.io/badge/PDF-SplitMap-EC1C24?logo=adobeacrobatreader)
</a>

### Mixer Configuration

The band uses a Behringer WING RACK mixer for mixing all IEMs and front-of-house when necessary. If you will be working with the band and using their mixer, you can download the latest configuration from the [Mixer folder](Mixer).

You can view the mixer configuration by using the WING EDIT software provided by Behringer. You can [download it from their website](https://www.behringer.com/wing/wing-rack#documentations).

## Acoustic

The band can perform in smaller venues with an acoustic set up. This setup replaces the full drum set with a smaller percussion setup, removes the need for IEMs and the IEM box, and shrinks the overall stage footprint. This configuration differs per show as it aligns more closely with the set list. For any documentation or requirements, please contact the band directly at [technical@theperfectstrangers.band](mailto:technical@theperfectstrangers.band?subject=Acoustic%20Set%20Up%20for%20The%20Perfect%20Strangers).

### Input + Equipment

<a id="raw-url" href="https://raw.githubusercontent.com/ThePerfectStrangers/TechnicalDocumentation/main/InputList\Acoustic\InputList.pdf">![Static Badge](https://img.shields.io/badge/PDF-AcousticSetup-EC1C24?logo=adobeacrobatreader)
</a>

# Repository Health

This is the status of the backing workflows that automate the creation of repository artifacts, such as PDFs and images. If any of these are failing, then their related artifacts may be out-of-date.

[![Acoustic/Input List Workflow](https://github.com/ThePerfectStrangers/TechnicalDocumentation/actions/workflows/acoustic-input-list-workflow.yml/badge.svg)](https://github.com/ThePerfectStrangers/TechnicalDocumentation/actions/workflows/acoustic-input-list-workflow.yml)

[![Band Color Convention Workflow](https://github.com/ThePerfectStrangers/TechnicalDocumentation/actions/workflows/band-color-convention-workflow.yml/badge.svg)](https://github.com/ThePerfectStrangers/TechnicalDocumentation/actions/workflows/band-color-convention-workflow.yml)

[![Complete Technical Documentation PDF Workflow](https://github.com/ThePerfectStrangers/TechnicalDocumentation/actions/workflows/full-band-complete-technical-documentation-pdf.yml/badge.svg)](https://github.com/ThePerfectStrangers/TechnicalDocumentation/actions/workflows/full-band-complete-technical-documentation-pdf.yml)

[![Draw.io to PNG & PDF Workflow](https://github.com/ThePerfectStrangers/TechnicalDocumentation/actions/workflows/drawio-to-png-and-pdf.yml/badge.svg)](https://github.com/ThePerfectStrangers/TechnicalDocumentation/actions/workflows/drawio-to-png-and-pdf.yml)

[![Full Band/Input List Workflow](https://github.com/ThePerfectStrangers/TechnicalDocumentation/actions/workflows/full-band-input-list-workflow.yml/badge.svg)](https://github.com/ThePerfectStrangers/TechnicalDocumentation/actions/workflows/full-band-input-list-workflow.yml)

[![Full Band/Split Map Workflow](https://github.com/ThePerfectStrangers/TechnicalDocumentation/actions/workflows/full-band-split-map-workflow.yml/badge.svg)](https://github.com/ThePerfectStrangers/TechnicalDocumentation/actions/workflows/full-band-split-map-workflow.yml)

[![Rider Workflow](https://github.com/ThePerfectStrangers/TechnicalDocumentation/actions/workflows/rider-workflow.yml/badge.svg)](https://github.com/ThePerfectStrangers/TechnicalDocumentation/actions/workflows/rider-workflow.yml)

[![Stage Diagram Workflow](https://github.com/ThePerfectStrangers/TechnicalDocumentation/actions/workflows/stage-diagram-workflow.yml/badge.svg)](https://github.com/ThePerfectStrangers/TechnicalDocumentation/actions/workflows/stage-diagram-workflow.yml)