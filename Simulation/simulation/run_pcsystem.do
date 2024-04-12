vlib ieee_proposed
vlib work
vcom -work work vhdl/PositMult_24_7_comb_uid2.vhd
vcom -work work vhdl/PositAdd_24_7_F0_uid2.vhd
vcom -work work vhdl/PCSystem.vhd
vcom -work work vhdl/PCSystem_tb.vhd

vsim -work work PCSystem_tb
run 10000 ns
exit
