# IEEE NEWCAS_2024
The repository is the priliminary version of AutoPC software, that generates FPGA compatible hardware for Xilinx FPGAs.

This work was presented during June 2024, at IEEE NEWCAS, Canada.

# How to use
Currently, AutoPC supports three number systems
1. Fixed Point Number System
2. Floating Point Number System
3. Posit Number System
   
To find the required number of bits for a given number system, change directory to the top module (i.e., ./newcas_2024/) and run python3 ___init__.py.

The final number of bits, can be found inside the logs. And, the logs can be found in ./newcas_2024/Data/Logs/



To generate hardware for Xilinx FPGAs, change directory to ./newcas_2024/Operations/FLPPCOperation/ and then run python3 __init__.py.

The generated hardware can be found inside ./newcas_2024/Simulation/VHDL/"PC_type"/"respective_model"/"selected_number_system"/"total_number_of_bits"/PCSystem/PCSystem.vhdl.

For instance:

if the selected PC type is AC and selected model is nltcs and number system is float requiring 20 total number of bits for the hardware implementation.

The location of the generated hw will be in ./newcas_2024/Simulation/VHDL/AC/nltcs/Float/20/PCSystem/PCSystem.vhdl.

