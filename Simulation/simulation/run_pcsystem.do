vlib ieee_proposed
vlib work
vcom -work ieee_proposed VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_float_types_c.vhdl
vcom -work ieee_proposed VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_pkg_c.vhdl
vcom -work ieee_proposed VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_noresized.vhdl
vcom -work ieee_proposed VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_synth.vhdl
vcom -work ieee_proposed VHDLPackages/FixedFloatPackage/ieee_proposed/float_pkg_c.vhdl
vcom -work ieee_proposed VHDLPackages/FixedFloatPackage/ieee_proposed/float_noround_pkg.vhdl
vcom -work ieee_proposed VHDLPackages/FixedFloatPackage/ieee_proposed/float_synth.vhdl
vcom -work work vhdl/SumNode_Float.vhd
vcom -work work vhdl/ProductNode_Float.vhd
vcom -work work vhdl/PCSystem.vhd
vcom -work work vhdl/PCSystem_tb.vhd

vsim -work work PCSystem_tb
run 16180 ns
exit
