# newcas_2024
AutoPC software

# branch main

The main branch of the repo can do all the analysis and generate a combinational ckt for simulation.
Subsequently, the main the branch has files to process the simulated data.

# sqckt branch

This branch contained the optimised hardware that can be implemented on an FPGA platform. This branch code will enable the generation of the same results as shown in the paper.

# UPDATE

Still, lot of explanation on how to run the software for combinational and FPGA CKTs will be added in the coming weeks.
=======

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


# Missing

The whole documentaion of the framework, still from the presented paper it can be underrstood.

Feel free to raise questions in github for clarifications. Also, we are working on hardware schedulers, architectures and other advanced features for next version of the framework.
>>>>>>> bd4706dd82788be6bec9f463881db134c0ccfc53
