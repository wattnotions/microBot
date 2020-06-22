EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Motor:Stepper_Motor_bipolar M1
U 1 1 5E6E63B8
P 9750 3050
F 0 "M1" H 9938 3173 50  0000 L CNN
F 1 "Stepper_Motor_bipolar" H 9938 3082 50  0000 L CNN
F 2 "kicad_footprints:micro_stepper1" H 9760 3040 50  0001 C CNN
F 3 "http://www.infineon.com/dgdl/Application-Note-TLE8110EE_driving_UniPolarStepperMotor_V1.1.pdf?fileId=db3a30431be39b97011be5d0aa0a00b0" H 9760 3040 50  0001 C CNN
	1    9750 3050
	1    0    0    -1  
$EndComp
$Comp
L Motor:Stepper_Motor_bipolar M?
U 1 1 5EF0ADEA
P 9750 3650
F 0 "M?" H 9938 3773 50  0000 L CNN
F 1 "Stepper_Motor_bipolar" H 9938 3682 50  0000 L CNN
F 2 "kicad_footprints:micro_stepper1" H 9760 3640 50  0001 C CNN
F 3 "http://www.infineon.com/dgdl/Application-Note-TLE8110EE_driving_UniPolarStepperMotor_V1.1.pdf?fileId=db3a30431be39b97011be5d0aa0a00b0" H 9760 3640 50  0001 C CNN
	1    9750 3650
	1    0    0    -1  
$EndComp
$Comp
L Motor:Stepper_Motor_bipolar M?
U 1 1 5EF0B15F
P 9750 4200
F 0 "M?" H 9938 4323 50  0000 L CNN
F 1 "Stepper_Motor_bipolar" H 9938 4232 50  0000 L CNN
F 2 "kicad_footprints:micro_stepper1" H 9760 4190 50  0001 C CNN
F 3 "http://www.infineon.com/dgdl/Application-Note-TLE8110EE_driving_UniPolarStepperMotor_V1.1.pdf?fileId=db3a30431be39b97011be5d0aa0a00b0" H 9760 4190 50  0001 C CNN
	1    9750 4200
	1    0    0    -1  
$EndComp
$Comp
L Motor:Stepper_Motor_bipolar M?
U 1 1 5EF0B559
P 9750 4750
F 0 "M?" H 9938 4873 50  0000 L CNN
F 1 "Stepper_Motor_bipolar" H 9938 4782 50  0000 L CNN
F 2 "kicad_footprints:micro_stepper1" H 9760 4740 50  0001 C CNN
F 3 "http://www.infineon.com/dgdl/Application-Note-TLE8110EE_driving_UniPolarStepperMotor_V1.1.pdf?fileId=db3a30431be39b97011be5d0aa0a00b0" H 9760 4740 50  0001 C CNN
	1    9750 4750
	1    0    0    -1  
$EndComp
$Comp
L Battery_Management:MCP73812T-420I-OT U?
U 1 1 5EF0FBE9
P 5100 1450
F 0 "U?" H 5544 1496 50  0000 L CNN
F 1 "MCP73812T-420I-OT" H 5544 1405 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23-5" H 5150 1200 50  0001 L CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/22036b.pdf" H 4850 1700 50  0001 C CNN
	1    5100 1450
	1    0    0    -1  
$EndComp
$Comp
L Device:Battery_Cell BT?
U 1 1 5EF109A6
P 3500 1400
F 0 "BT?" H 3618 1496 50  0000 L CNN
F 1 "Battery_Cell" H 3618 1405 50  0000 L CNN
F 2 "" V 3500 1460 50  0001 C CNN
F 3 "~" V 3500 1460 50  0001 C CNN
	1    3500 1400
	1    0    0    -1  
$EndComp
$Comp
L Connector:USB_B_Mini J?
U 1 1 5EF118EB
P 7850 1600
F 0 "J?" H 7907 2067 50  0000 C CNN
F 1 "USB_B_Mini" H 7907 1976 50  0000 C CNN
F 2 "" H 8000 1550 50  0001 C CNN
F 3 "~" H 8000 1550 50  0001 C CNN
	1    7850 1600
	1    0    0    -1  
$EndComp
$Comp
L Interface_USB:FT231XS U?
U 1 1 5EF17383
P 5800 3750
F 0 "U?" H 5800 4831 50  0000 C CNN
F 1 "FT231XS" H 5800 4740 50  0000 C CNN
F 2 "Package_SO:SSOP-20_3.9x8.7mm_P0.635mm" H 6800 2950 50  0001 C CNN
F 3 "https://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT231X.pdf" H 5800 3750 50  0001 C CNN
	1    5800 3750
	1    0    0    -1  
$EndComp
$Comp
L RF_Module:ESP32-WROOM-32 U?
U 1 1 5EF0D093
P 2600 3950
F 0 "U?" H 2600 5531 50  0000 C CNN
F 1 "ESP32-WROOM-32" H 2600 5440 50  0000 C CNN
F 2 "RF_Module:ESP32-WROOM-32" H 2600 2450 50  0001 C CNN
F 3 "https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf" H 2300 4000 50  0001 C CNN
	1    2600 3950
	1    0    0    -1  
$EndComp
$Comp
L Regulator_Linear:LM1117-3.3 U?
U 1 1 5EF11066
P 7100 1300
F 0 "U?" H 7100 1542 50  0000 C CNN
F 1 "LM1117-3.3" H 7100 1451 50  0000 C CNN
F 2 "" H 7100 1300 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm1117.pdf" H 7100 1300 50  0001 C CNN
	1    7100 1300
	1    0    0    -1  
$EndComp
$Comp
L Driver_Motor:DRV8833PW U?
U 1 1 5EF13196
P 8050 3200
F 0 "U?" H 8050 2411 50  0000 C CNN
F 1 "DRV8833PW" H 8050 2320 50  0000 C CNN
F 2 "Package_SO:TSSOP-16_4.4x5mm_P0.65mm" H 8500 3650 50  0001 L CNN
F 3 "http://www.ti.com/lit/ds/symlink/drv8833.pdf" H 7900 3750 50  0001 C CNN
	1    8050 3200
	1    0    0    -1  
$EndComp
$Comp
L Driver_Motor:DRV8833PW U?
U 1 1 5EF140EA
P 8050 5100
F 0 "U?" H 8050 4311 50  0000 C CNN
F 1 "DRV8833PW" H 8050 4220 50  0000 C CNN
F 2 "Package_SO:TSSOP-16_4.4x5mm_P0.65mm" H 8500 5550 50  0001 L CNN
F 3 "http://www.ti.com/lit/ds/symlink/drv8833.pdf" H 7900 5650 50  0001 C CNN
	1    8050 5100
	1    0    0    -1  
$EndComp
$EndSCHEMATC
