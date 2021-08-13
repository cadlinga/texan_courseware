---
layout: default
title: Electrical System
nav_order: 1
grand_parent: Ground School
parent: Electrical System and Lighting
---

## Electrical System

### Avionics


![](./../../images/battery.png "Battery")

The T-6B fully integrated CMC or Flight Visions avionics system uses two powerful mission computers. Integrated navigation and mission data is displayed on the large, 25° Total Field of View (TFOV) Head-Up Display (HUD) and on three high-fidelity 5in x 7in multifunction displays (MFDs). Any one of the three MFDs can access the navigation and mission management pages for the avionics and training systems.

The Up-Front Control Panel (UFCP) provides central control of navigation, air-to-air and air-to-ground master modes from the front and rear cockpits. It also supports radio communication and navigation aid management, weapon selection and programming, waypoint management and designation of markpoints.

The Primary Flight Display (PFD) provides the controls and displays required to manage and present primary flight information to the pilots including attitude, airspeed, altitude and flight path direction.

The Tactical Situation Display (TSD) enhances situational awareness by presenting a scalable plan view of the key elements required for terminal, en route, area and tactical navigation.

The colour digital moving map display (MAP) presents the aircraft’s relationship to the outside physical environment. It also provides key flight, navigation and tactical display of information to give the crew a high degree of situational awareness during flight.

An Engine Instrument and Crew Alerting System (EICAS) provides aircraft and engine system information including status of the engine, propeller, hydraulic, fuel, trim and flap.

The avionics suite also includes a data transfer system for navigation and operation planning and a digital video recorder for mission debrief.

### Starter/Generator 

The aircraft has a 28 Vdc 300A starter/generator. During start, this is configured as a motor to drive the gas generator via the Accessory Gearbox. Once the start cycle has progressed to the point where electrical power tothe starter is no longer needed (about 50% N1), it is automatically configured as a generator.

![](./../../images/generator.png "Generator")

A voltage sense circuit immediately after the generator will not allow its connection to the rest of the electrical system if the generator output voltage is too high (this would overheat the battery). If the front cockpit generator switch is ON, then the rear cockpit switch will be at the OFF position (ie, both switches cannot be ON at the same time). If the rear cockpit switch is now placed to the ON position, it will take control of the generator and then magnetically de-latch the switch in the front cockpit and vice versa. This is so that control of the generator can be transferred between cockpits without any power interruption.

During the PRE-TAKEOFF CHECKS,battery charging must be less than +50 A.

With the BUS TIE switch at NORM, the generator powers all aircraft busbars. With the BUS TIE switch at OPEN or if the bus tie fails open, the generator will only power the generator busbars with the battery powering all the battery busbars for about 30 minutes in this case.

### Auxillary Battery 

The aircraft has an auxiliary battery in the LH Avionics bay, rated at 24 Vdc 5 Ah. Power to the FWD and AFT AUX BAT BUSbars is normally supplied through a CB on the FWD BAT BUSbar (see schematic).

With the AUX BAT switch ON, the Auxiliary Battery is “armed” to power the AUX BAT BUSbars in the event of a FWD BAT BUSbar failure. The sensing circuit within the Auxiliary Battery and the relay system are extremely fast and power to those busbars will not be interrupted during this failure.

![](./../../images/aux_battery.png "Auxillary Battery")

The Inertial Reference System, Backup Flight Instrument, COM2 and the Remote V/UHF head (front cockpit, RH console) are all powered from the FWD AUX BAT BUSbar, enabling an IMC recovery to be flown in the event of a BAT BUS failure or BAT and GEN failures. The Auxiliary Battery will power these systems for approximately 30 minutes.

During the INITIAL CHECKS, the Auxiliary Battery is tested by selecting the spring-loaded AUX BAT TEST switch to TESTfor 5 seconds. The adjacent green LED should remain lit for the entire test period. If it does not come on at all, then the battery is at less than 50% charge and it is U/S. The Auxliary Battery has 5 internal cells, each of which is automatically testedin turn. If a cell is U/S, the LED will extinguish and then come on again if the next cell is serviceable. If this happens, then the battery is U/S.

### External Power 

An External Power source can be connected via a NATO-standard, 3-pin, 28 Vdc plug socket behind a small panel on the lower fuselage, aft of the port wing trailing edge. The BAT MASTER switch must be ON for the hold-on relay to engage. There is no caption on the EICAS to tell the pilot that external power is connected; the only indication is anincrease in voltage displayed on the EICAS.

![](./../../images/ext_power.png "External Power")

After start, the external power must be disconnected before the aircraft’s generator is engaged. Failure to do so could cause damage to the external power set. Again, the only indication that the external power has been removed is a drop in displayed voltage on the EICAS

### Circuit Breakers

There are two circuit breaker panels in each cockpit. Battery busbar circuits are on the LH consoles and generator busbar circuits are on the RH consoles. There is a further CB panel in the nose bay, port side, aft which accommodates circuits on the HOT BAT BUS and HOT GEN BUS and which is, clearly, inaccessible during flight.

![](./../../images/cbs.png "Circuit Breakers")

Each CB has a label on the panel, identifying the circuit that it protects and a number denoting the maximum current (Amps) that it will pass before popping.

Several of the CBs that are often used (by the engineers during ground servicing), have black collars around them. This makes them easier to identify and easier to pull.

All CBs should be in for flight.
