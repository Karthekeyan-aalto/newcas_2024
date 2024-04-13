vlib ieee_proposed
vlib work

vcom -work work vhdl/SBRightSHR.vhd
vcom -work work vhdl/MBRightSHR.vhd
vcom -work work vhdl/SB_D_FF.vhd
vcom -work work vhdl/MB_D_FF.vhd

vcom -work work vhdl/FloatLUT.vhd

#vcom -work work vhdl/FPMult_7_14_7_14_7_14_F400_uid2.vhd
#vcom -work work vhdl/FPAdd_7_14_F400_uid2.vhd

vcom -work work vhdl/FPMult_7_14_7_14_7_14_uid2_Freq800_uid3.vhd
vcom -work work vhdl/FPAdd_7_14_Freq800_uid2.vhd

vcom -work work vhdl/InputIEEE_7_14_to_7_14.vhd
vcom -work work vhdl/OutputIEEE_7_14_to_7_14.vhd
vcom -work work vhdl/SPN/msnbc/22/Float/PCSystem/PCSystem_22.vhd
vcom -work work vhdl/PCSystem_MSNBC_SPN_Float_SoC.vhd
vcom -work work vhdl/PCSystem_MSNBC_SPN_Float_SoC_tb.vhd

vsim -work work PCSystem_MSNBC_SPN_Float_SoC_tb

add wave -color orange clk
add wave -color white rst
add wave -color green enable

#add wave -color orange v0a
#add wave -color white v0b

#add wave -color green v1a
#add wave -color orange v1b

#add wave -color white v2a
#add wave -color green v2b

#add wave -color orange v3a

#add wave -color white v3b
#add wave -color green v4a

#add wave -color orange v4b

#add wave -color white v5a
#add wave -color green v5b

#add wave -color orange v6a

#add wave -color white v6b
#add wave -color green v7a

#add wave -color orange v7b

#add wave -color white v8a
#add wave -color green v8b

#add wave -color orange v9a

#add wave -color white v9b
#add wave -color green v10a

#add wave -color orange v10b

#add wave -color white v11a
#add wave -color green v11b

#add wave -color orange v12a

#add wave -color white v12b
#add wave -color green v13a

#add wave -color orange v13b

#add wave -color white v14a
#add wave -color green v14b

#add wave -color white v15a
#add wave -color green v15b

#add wave -color white v16a
#add wave -color green v16b

#add wave -color white topNodeOutput

#add wave -color orange lastWeight
#add wave -color white  lastMultiplierOutput
#add wave -color green topNodeOutput

add wave -color green vout

run 500 ns
#exit
