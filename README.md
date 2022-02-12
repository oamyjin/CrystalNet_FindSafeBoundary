# CrystalNet_FindSafeBoundary

Project page of finding the safe boundary in CrystalNet:https://www.microsoft.com/en-us/research/wp-content/uploads/2017/10/p599-liu.pdf

# Usage
`find_safe_dc_boundary.py` reads input files, implements the algorithm to find the safe boundary and output the result file.

Command: `python find_safe_dc_boundary.py -g <real_topology_file> -d <must-have_devices_file> -o <all_emulated_devices_file>`

Example: `python find_safe_dc_boundary.py -g topology.txt -d devices.txt -o emu_devices.txt` 
 find all devices to be emulated according to the *topology.txt* file and *devices.txt* which contains must-have devices, and generate *emu_devices.txt* to store the results.
 
# File Format

## topology.txt
Input file

The first line is: `<the total number of devices in the topology>`

Any other line is a link, represented as a device pair: `<upper device, device>`

## devices.txt
Input file

The id of the devices must be emulated: `<device_1, device_2, ...>`

## emu_devices.txt
Output file

The first line is: `<the total number of emulated devices, the percentage of emulated devices among all>`

The second line shows the device ids of all emulated ones: `<device_1, device_2, ...>`
 
