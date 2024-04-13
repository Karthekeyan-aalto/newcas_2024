cd $PWD/simulation
vlib work
vlib ieee_proposed
vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_float_types_c.vhdl
vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_pkg_c.vhdl
vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_noresized.vhdl
vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/fixed_synth.vhdl
vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/float_pkg_c.vhdl
vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/float_noround_pkg.vhdl
vcom -work ieee_proposed $PWD/VHDLPackages/FixedFloatPackage/ieee_proposed/float_synth.vhdl
vcom -work work $PWD/vhdl/SBRightSHR.vhd
vcom -work work $PWD/vhdl/MBRightSHR.vhd
vcom -work work $PWD/vhdl/SB_D_FF.vhd
vcom -work work $PWD/vhdl/MB_D_FF.vhd
vcom -work work $PWD/vhdl/FloatLUT.vhd
vcom -work work $PWD/vhdl/InputIEEE_7_14_to_7_14.vhd
vcom -work work $PWD/vhdl/OutputIEEE_7_14_to_7_14.vhd
#vcom -work work $PWD/vhdl/FPAdd_7_14_F400_uid2.vhd
#vcom -work work $PWD/vhdl/FPMult_7_14_7_14_7_14_F400_uid2.vhd

vcom -work work vhdl/FPMult_7_14_7_14_7_14_uid2_Freq800_uid3.vhd
vcom -work work vhdl/FPAdd_7_14_Freq800_uid2.vhd

vcom -work work $PWD/vhdl/AC/msnbc_tw5/22/Float/PCSystem/PCSystem_22.vhd
vcom -work work $PWD/vhdl/PCSystem_MSNBC_AC_Float_SoC.vhd
vcom -work work $PWD/vhdl/PCSystem_MSNBC_AC_Float_SoC_tb.vhd
#vcom -work work $PWD/vhdl/PCSystem_tb.vhd
