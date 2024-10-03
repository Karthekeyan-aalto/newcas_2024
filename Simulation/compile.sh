cd $PWD/simulation
vlib ieee_proposed
vlib work
vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_float_types_c.vhdl
vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_pkg_c.vhdl
vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_noresized.vhdl
vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_synth.vhdl
vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/float_pkg_c.vhdl
vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/float_noround_pkg.vhdl
vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/float_synth.vhdl
vcom -work work $PWD/vhdl/ProductNode_Float.vhd
vcom -work work $PWD/vhdl/SumNode_Float.vhd
vcom -work work $PWD/vhdl/PCSystem.vhd
vcom -work work $PWD/vhdl/PCSystem_tb.vhd
