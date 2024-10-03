LIBRARY ieee; 
LIBRARY ieee_proposed; 
USE ieee.std_logic_1164.all; 
USE ieee.std_logic_arith.all; 
USE ieee.std_logic_unsigned.all; 
USE ieee.std_logic_textio.all; 
 
LIBRARY std; 
USE std.textio.all; 
USE ieee_proposed.fixed_pkg.all; 
USE ieee_proposed.fixed_float_types.all; 
USE ieee_proposed.float_pkg.all; 
ENTITY PCSystem_22 IS
    GENERIC (MantissaBits :INTEGER := 15 ; ExponentBits :INTEGER := 7 ; NumberOfBits :INTEGER := 22 ; FlopocoBits :INTEGER := 2);
    PORT (
    clk:IN std_logic;
    rst:IN std_logic;
    enable:IN std_logic;
    v1:IN std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    v2:IN std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    v3:IN std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    v4:IN std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    v5:IN std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    v6:IN std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    v7:IN std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    v8:IN std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    vout:OUT std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0)
);
END PCSystem_22;

ARCHITECTURE rtl of PCSystem_22 IS

        SIGNAL mb_D_FFMultiplier2_13_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier13_Output_19 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL flopocoMultiplier13WeightOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier13WeightOutput :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL flopocoMultiplier13WeightInput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF13_19MultiplicandStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF13_19MultiplicandStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mbRightSHR13_19Output :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL mb_D_FFMultiplier2_6_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier6_Output_9 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL flopocoMultiplier6WeightOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier6WeightOutput :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL flopocoMultiplier6WeightInput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF6_9MultiplicandStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF6_9MultiplicandStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mbRightSHR6_9Output :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL mb_D_FFAdder3_Input1_5_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Adder5_Output_18 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF5_18AugendStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF5_18AugendStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF5_18AddendStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF5_18AddendStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFAdder3_Input2_5_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFAdder3_Input1_2_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Adder2_Output_8 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF2_8AugendStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF2_8AugendStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF2_8AddendStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF2_8AddendStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFAdder3_Input2_2_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFMultiplier4_12_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier12_Output_17 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL flopocoMultiplier12WeightOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier12WeightOutput :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL flopocoMultiplier12WeightInput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF12_17MultiplicandStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF12_17MultiplicandStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mbRightSHR12_17Output :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL mb_D_FFMultiplier4_9_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier9_Output_13 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL flopocoMultiplier9WeightOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier9WeightOutput :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL flopocoMultiplier9WeightInput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF9_13MultiplicandStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF9_13MultiplicandStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mbRightSHR9_13Output :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL mb_D_FFMultiplier4_5_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier5_Output_7 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL flopocoMultiplier5WeightOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier5WeightOutput :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL flopocoMultiplier5WeightInput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF5_7MultiplicandStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF5_7MultiplicandStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mbRightSHR5_7Output :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL mb_D_FFMultiplier4_2_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier2_Output_3 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL flopocoMultiplier2WeightOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier2WeightOutput :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL flopocoMultiplier2WeightInput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF2_3MultiplicandStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF2_3MultiplicandStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mbRightSHR2_3Output :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL mb_D_FFAdder5_Input1_4_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Adder4_Output_16 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF4_16AugendStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF4_16AugendStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF4_16AddendStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF4_16AddendStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFAdder5_Input2_4_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFAdder5_Input1_3_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Adder3_Output_12 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF3_12AugendStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF3_12AugendStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF3_12AddendStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF3_12AddendStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFAdder5_Input2_3_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFAdder5_Input1_1_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Adder1_Output_6 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF1_6AugendStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF1_6AugendStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF1_6AddendStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF1_6AddendStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFAdder5_Input2_1_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFAdder5_Input1_0_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Adder0_Output_2 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF0_2AugendStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF0_2AugendStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF0_2AddendStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF0_2AddendStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFAdder5_Input2_0_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFMultiplier6_11_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFMultiplier6_11_0Input :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier11_Output_15 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL flopocoMultiplier11WeightOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier11WeightOutput :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL flopocoMultiplier11WeightInput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF11_15MultiplicandStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF11_15MultiplicandStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mbRightSHR11_15Output :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL mb_D_FFMultiplier6_10_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFMultiplier6_10_0Input :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier10_Output_14 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL flopocoMultiplier10WeightOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier10WeightOutput :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL flopocoMultiplier10WeightInput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF10_14MultiplicandStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF10_14MultiplicandStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mbRightSHR10_14Output :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL mb_D_FFMultiplier6_8_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFMultiplier6_8_0Input :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier8_Output_11 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL flopocoMultiplier8WeightOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier8WeightOutput :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL flopocoMultiplier8WeightInput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF8_11MultiplicandStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF8_11MultiplicandStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mbRightSHR8_11Output :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL mb_D_FFMultiplier6_7_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFMultiplier6_7_0Input :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier7_Output_10 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL flopocoMultiplier7WeightOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier7WeightOutput :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL flopocoMultiplier7WeightInput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF7_10MultiplicandStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF7_10MultiplicandStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mbRightSHR7_10Output :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL mb_D_FFMultiplier6_4_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFMultiplier6_4_0Input :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier4_Output_5 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL flopocoMultiplier4WeightOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier4WeightOutput :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL flopocoMultiplier4WeightInput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF4_5MultiplicandStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF4_5MultiplicandStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mbRightSHR4_5Output :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL mb_D_FFMultiplier6_3_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFMultiplier6_3_0Input :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier3_Output_4 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL flopocoMultiplier3WeightOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier3WeightOutput :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL flopocoMultiplier3WeightInput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF3_4MultiplicandStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF3_4MultiplicandStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mbRightSHR3_4Output :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL mb_D_FFMultiplier6_1_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFMultiplier6_1_0Input :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier1_Output_1 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL flopocoMultiplier1WeightOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier1WeightOutput :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL flopocoMultiplier1WeightInput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF1_1MultiplicandStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF1_1MultiplicandStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mbRightSHR1_1Output :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL mb_D_FFMultiplier6_0_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFMultiplier6_0_0Input :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier0_Output_0 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL flopocoMultiplier0WeightOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier0WeightOutput :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL flopocoMultiplier0WeightInput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF0_0MultiplicandStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF0_0MultiplicandStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mbRightSHR0_0Output :std_logic_vector(NumberOfBits-1 DOWNTO 0);

        SIGNAL mb_D_FFAdder1_Input1_6_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Adder6_Output_20 :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF6_20AugendStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF6_20AugendStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF6_20AddendStage1Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FF6_20AddendStage2Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFAdder1_Input2_6_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL mb_D_FFAdder1_Output_6_0Output :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        SIGNAL Multiplier0Weight :std_logic_vector(NumberOfBits-1 DOWNTO 0):= to_slv(to_float(0.45,exponentBits,mantissaBits-1));
        SIGNAL Multiplier1Weight :std_logic_vector(NumberOfBits-1 DOWNTO 0):= to_slv(to_float(0.33,exponentBits,mantissaBits-1));
        SIGNAL Multiplier2Weight :std_logic_vector(NumberOfBits-1 DOWNTO 0):= to_slv(to_float(0.95,exponentBits,mantissaBits-1));
        SIGNAL Multiplier3Weight :std_logic_vector(NumberOfBits-1 DOWNTO 0):= to_slv(to_float(0.13,exponentBits,mantissaBits-1));
        SIGNAL Multiplier4Weight :std_logic_vector(NumberOfBits-1 DOWNTO 0):= to_slv(to_float(0.29,exponentBits,mantissaBits-1));
        SIGNAL Multiplier5Weight :std_logic_vector(NumberOfBits-1 DOWNTO 0):= to_slv(to_float(0.59,exponentBits,mantissaBits-1));
        SIGNAL Multiplier6Weight :std_logic_vector(NumberOfBits-1 DOWNTO 0):= to_slv(to_float(0.75,exponentBits,mantissaBits-1));
        SIGNAL Multiplier7Weight :std_logic_vector(NumberOfBits-1 DOWNTO 0):= to_slv(to_float(0.56,exponentBits,mantissaBits-1));
        SIGNAL Multiplier8Weight :std_logic_vector(NumberOfBits-1 DOWNTO 0):= to_slv(to_float(0.25,exponentBits,mantissaBits-1));
        SIGNAL Multiplier9Weight :std_logic_vector(NumberOfBits-1 DOWNTO 0):= to_slv(to_float(0.31,exponentBits,mantissaBits-1));
        SIGNAL Multiplier10Weight :std_logic_vector(NumberOfBits-1 DOWNTO 0):= to_slv(to_float(0.41,exponentBits,mantissaBits-1));
        SIGNAL Multiplier11Weight :std_logic_vector(NumberOfBits-1 DOWNTO 0):= to_slv(to_float(0.35,exponentBits,mantissaBits-1));
        SIGNAL Multiplier12Weight :std_logic_vector(NumberOfBits-1 DOWNTO 0):= to_slv(to_float(0.23,exponentBits,mantissaBits-1));
        SIGNAL Multiplier13Weight :std_logic_vector(NumberOfBits-1 DOWNTO 0):= to_slv(to_float(0.57,exponentBits,mantissaBits-1));
        
BEGIN
    PROCESS (clk,rst) IS
    BEGIN 
        IF rst = '1' THEN
    mb_D_FFMultiplier6_11_0Input <= (others=>'0');
            mb_D_FFMultiplier6_10_0Input <= (others=>'0');
            mb_D_FFMultiplier6_8_0Input <= (others=>'0');
            mb_D_FFMultiplier6_7_0Input <= (others=>'0');
            mb_D_FFMultiplier6_4_0Input <= (others=>'0');
            mb_D_FFMultiplier6_3_0Input <= (others=>'0');
            mb_D_FFMultiplier6_1_0Input <= (others=>'0');
            mb_D_FFMultiplier6_0_0Input <= (others=>'0');
        ELSIF rising_edge(clk) and rst = '0' and enable = '1' THEN
            mb_D_FFMultiplier6_11_0Input <= v1;
            mb_D_FFMultiplier6_10_0Input <= v2;
            mb_D_FFMultiplier6_8_0Input <= v3;
            mb_D_FFMultiplier6_7_0Input <= v4;
            mb_D_FFMultiplier6_4_0Input <= v5;
            mb_D_FFMultiplier6_3_0Input <= v6;
            mb_D_FFMultiplier6_1_0Input <= v7;
            mb_D_FFMultiplier6_0_0Input <= v8;
        END IF;

    END PROCESS;

    MB_D_FF_Float_Multiplier6_0_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier6_0_0Input, mb_D_FFMultiplier6_0_0Output);

    MB_D_FF_Float_0_0_MultiplicandStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier6_0_0Output, mb_D_FF0_0MultiplicandStage1Output);

    MB_D_FF_Float_0_0_MultiplicandStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF0_0MultiplicandStage1Output, mb_D_FF0_0MultiplicandStage2Output);

    MB_D_FF_Float_0_0_ConverterInput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits)
    PORT MAP (clk, rst, mbRightSHR0_0Output, Multiplier0WeightOutput);

    InputIEEE_Float_0_0: entity work.InputIEEE_7_14_to_7_14(arch)
        PORT MAP (clk, Multiplier0WeightOutput, flopocoMultiplier0WeightOutput);

    MB_D_FF_Float_0_0_ConverterOutput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, flopocoMultiplier0WeightOutput, flopocoMultiplier0WeightInput);

    Multiplier_Float_0: entity work.FPMult_7_14_7_14_7_14_uid2_Freq800_uid3(arch)
    PORT MAP (clk, mb_D_FF0_0MultiplicandStage2Output, flopocoMultiplier0WeightInput, Multiplier0_Output_0);

    MBRightSHR_Float_0_0: entity work.MBRightSHR(rtl)
    GENERIC MAP (4, NumberOfBits)
    PORT MAP (clk, rst, Multiplier0Weight, mbRightSHR0_0Output);

    MB_D_FF_Float_Multiplier6_1_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier6_1_0Input, mb_D_FFMultiplier6_1_0Output);

    MB_D_FF_Float_1_1_MultiplicandStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier6_1_0Output, mb_D_FF1_1MultiplicandStage1Output);

    MB_D_FF_Float_1_1_MultiplicandStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF1_1MultiplicandStage1Output, mb_D_FF1_1MultiplicandStage2Output);

    MB_D_FF_Float_1_1_ConverterInput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits)
    PORT MAP (clk, rst, mbRightSHR1_1Output, Multiplier1WeightOutput);

    InputIEEE_Float_1_1: entity work.InputIEEE_7_14_to_7_14(arch)
        PORT MAP (clk, Multiplier1WeightOutput, flopocoMultiplier1WeightOutput);

    MB_D_FF_Float_1_1_ConverterOutput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, flopocoMultiplier1WeightOutput, flopocoMultiplier1WeightInput);

    Multiplier_Float_1: entity work.FPMult_7_14_7_14_7_14_uid2_Freq800_uid3(arch)
    PORT MAP (clk, mb_D_FF1_1MultiplicandStage2Output, flopocoMultiplier1WeightInput, Multiplier1_Output_1);

    MBRightSHR_Float_1_1: entity work.MBRightSHR(rtl)
    GENERIC MAP (4, NumberOfBits)
    PORT MAP (clk, rst, Multiplier1Weight, mbRightSHR1_1Output);

    MB_D_FF_Float_Adder5_Input1_0_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Multiplier1_Output_1, mb_D_FFAdder5_Input1_0_0Output);

    MB_D_FF_Float_0_2_AugendStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFAdder5_Input1_0_0Output, mb_D_FF0_2AugendStage1Output);

    MB_D_FF_Float_0_2_AugendStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF0_2AugendStage1Output, mb_D_FF0_2AugendStage2Output);

    Adder_Float_0: entity work.FPAdd_7_14_Freq800_uid2(arch)
    PORT MAP (clk, mb_D_FF0_2AugendStage2Output, mb_D_FF0_2AddendStage2Output, Adder0_Output_2);

    MB_D_FF_Float_Adder5_Input2_0_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Multiplier0_Output_0, mb_D_FFAdder5_Input2_0_0Output);

    MB_D_FF_Float_0_2_AddendStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFAdder5_Input2_0_0Output, mb_D_FF0_2AddendStage1Output);

    MB_D_FF_Float_0_2_AddendStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF0_2AddendStage1Output, mb_D_FF0_2AddendStage2Output);

    MB_D_FF_Float_Multiplier4_2_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Adder0_Output_2, mb_D_FFMultiplier4_2_0Output);

    MB_D_FF_Float_2_3_MultiplicandStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier4_2_0Output, mb_D_FF2_3MultiplicandStage1Output);

    MB_D_FF_Float_2_3_MultiplicandStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF2_3MultiplicandStage1Output, mb_D_FF2_3MultiplicandStage2Output);

    MB_D_FF_Float_2_3_ConverterInput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits)
    PORT MAP (clk, rst, mbRightSHR2_3Output, Multiplier2WeightOutput);

    InputIEEE_Float_2_3: entity work.InputIEEE_7_14_to_7_14(arch)
        PORT MAP (clk, Multiplier2WeightOutput, flopocoMultiplier2WeightOutput);

    MB_D_FF_Float_2_3_ConverterOutput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, flopocoMultiplier2WeightOutput, flopocoMultiplier2WeightInput);

    Multiplier_Float_2: entity work.FPMult_7_14_7_14_7_14_uid2_Freq800_uid3(arch)
    PORT MAP (clk, mb_D_FF2_3MultiplicandStage2Output, flopocoMultiplier2WeightInput, Multiplier2_Output_3);

    MBRightSHR_Float_2_3: entity work.MBRightSHR(rtl)
    GENERIC MAP (36, NumberOfBits)
    PORT MAP (clk, rst, Multiplier2Weight, mbRightSHR2_3Output);

    MB_D_FF_Float_Multiplier6_3_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier6_3_0Input, mb_D_FFMultiplier6_3_0Output);

    MB_D_FF_Float_3_4_MultiplicandStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier6_3_0Output, mb_D_FF3_4MultiplicandStage1Output);

    MB_D_FF_Float_3_4_MultiplicandStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF3_4MultiplicandStage1Output, mb_D_FF3_4MultiplicandStage2Output);

    MB_D_FF_Float_3_4_ConverterInput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits)
    PORT MAP (clk, rst, mbRightSHR3_4Output, Multiplier3WeightOutput);

    InputIEEE_Float_3_4: entity work.InputIEEE_7_14_to_7_14(arch)
        PORT MAP (clk, Multiplier3WeightOutput, flopocoMultiplier3WeightOutput);

    MB_D_FF_Float_3_4_ConverterOutput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, flopocoMultiplier3WeightOutput, flopocoMultiplier3WeightInput);

    Multiplier_Float_3: entity work.FPMult_7_14_7_14_7_14_uid2_Freq800_uid3(arch)
    PORT MAP (clk, mb_D_FF3_4MultiplicandStage2Output, flopocoMultiplier3WeightInput, Multiplier3_Output_4);

    MBRightSHR_Float_3_4: entity work.MBRightSHR(rtl)
    GENERIC MAP (4, NumberOfBits)
    PORT MAP (clk, rst, Multiplier3Weight, mbRightSHR3_4Output);

    MB_D_FF_Float_Multiplier6_4_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier6_4_0Input, mb_D_FFMultiplier6_4_0Output);

    MB_D_FF_Float_4_5_MultiplicandStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier6_4_0Output, mb_D_FF4_5MultiplicandStage1Output);

    MB_D_FF_Float_4_5_MultiplicandStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF4_5MultiplicandStage1Output, mb_D_FF4_5MultiplicandStage2Output);

    MB_D_FF_Float_4_5_ConverterInput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits)
    PORT MAP (clk, rst, mbRightSHR4_5Output, Multiplier4WeightOutput);

    InputIEEE_Float_4_5: entity work.InputIEEE_7_14_to_7_14(arch)
        PORT MAP (clk, Multiplier4WeightOutput, flopocoMultiplier4WeightOutput);

    MB_D_FF_Float_4_5_ConverterOutput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, flopocoMultiplier4WeightOutput, flopocoMultiplier4WeightInput);

    Multiplier_Float_4: entity work.FPMult_7_14_7_14_7_14_uid2_Freq800_uid3(arch)
    PORT MAP (clk, mb_D_FF4_5MultiplicandStage2Output, flopocoMultiplier4WeightInput, Multiplier4_Output_5);

    MBRightSHR_Float_4_5: entity work.MBRightSHR(rtl)
    GENERIC MAP (4, NumberOfBits)
    PORT MAP (clk, rst, Multiplier4Weight, mbRightSHR4_5Output);

    MB_D_FF_Float_Adder5_Input1_1_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Multiplier4_Output_5, mb_D_FFAdder5_Input1_1_0Output);

    MB_D_FF_Float_1_6_AugendStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFAdder5_Input1_1_0Output, mb_D_FF1_6AugendStage1Output);

    MB_D_FF_Float_1_6_AugendStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF1_6AugendStage1Output, mb_D_FF1_6AugendStage2Output);

    Adder_Float_1: entity work.FPAdd_7_14_Freq800_uid2(arch)
    PORT MAP (clk, mb_D_FF1_6AugendStage2Output, mb_D_FF1_6AddendStage2Output, Adder1_Output_6);

    MB_D_FF_Float_Adder5_Input2_1_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Multiplier3_Output_4, mb_D_FFAdder5_Input2_1_0Output);

    MB_D_FF_Float_1_6_AddendStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFAdder5_Input2_1_0Output, mb_D_FF1_6AddendStage1Output);

    MB_D_FF_Float_1_6_AddendStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF1_6AddendStage1Output, mb_D_FF1_6AddendStage2Output);

    MB_D_FF_Float_Multiplier4_5_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Adder1_Output_6, mb_D_FFMultiplier4_5_0Output);

    MB_D_FF_Float_5_7_MultiplicandStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier4_5_0Output, mb_D_FF5_7MultiplicandStage1Output);

    MB_D_FF_Float_5_7_MultiplicandStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF5_7MultiplicandStage1Output, mb_D_FF5_7MultiplicandStage2Output);

    MB_D_FF_Float_5_7_ConverterInput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits)
    PORT MAP (clk, rst, mbRightSHR5_7Output, Multiplier5WeightOutput);

    InputIEEE_Float_5_7: entity work.InputIEEE_7_14_to_7_14(arch)
        PORT MAP (clk, Multiplier5WeightOutput, flopocoMultiplier5WeightOutput);

    MB_D_FF_Float_5_7_ConverterOutput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, flopocoMultiplier5WeightOutput, flopocoMultiplier5WeightInput);

    Multiplier_Float_5: entity work.FPMult_7_14_7_14_7_14_uid2_Freq800_uid3(arch)
    PORT MAP (clk, mb_D_FF5_7MultiplicandStage2Output, flopocoMultiplier5WeightInput, Multiplier5_Output_7);

    MBRightSHR_Float_5_7: entity work.MBRightSHR(rtl)
    GENERIC MAP (36, NumberOfBits)
    PORT MAP (clk, rst, Multiplier5Weight, mbRightSHR5_7Output);

    MB_D_FF_Float_Adder3_Input1_2_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Multiplier5_Output_7, mb_D_FFAdder3_Input1_2_0Output);

    MB_D_FF_Float_2_8_AugendStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFAdder3_Input1_2_0Output, mb_D_FF2_8AugendStage1Output);

    MB_D_FF_Float_2_8_AugendStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF2_8AugendStage1Output, mb_D_FF2_8AugendStage2Output);

    Adder_Float_2: entity work.FPAdd_7_14_Freq800_uid2(arch)
    PORT MAP (clk, mb_D_FF2_8AugendStage2Output, mb_D_FF2_8AddendStage2Output, Adder2_Output_8);

    MB_D_FF_Float_Adder3_Input2_2_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Multiplier2_Output_3, mb_D_FFAdder3_Input2_2_0Output);

    MB_D_FF_Float_2_8_AddendStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFAdder3_Input2_2_0Output, mb_D_FF2_8AddendStage1Output);

    MB_D_FF_Float_2_8_AddendStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF2_8AddendStage1Output, mb_D_FF2_8AddendStage2Output);

    MB_D_FF_Float_Multiplier2_6_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Adder2_Output_8, mb_D_FFMultiplier2_6_0Output);

    MB_D_FF_Float_6_9_MultiplicandStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier2_6_0Output, mb_D_FF6_9MultiplicandStage1Output);

    MB_D_FF_Float_6_9_MultiplicandStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF6_9MultiplicandStage1Output, mb_D_FF6_9MultiplicandStage2Output);

    MB_D_FF_Float_6_9_ConverterInput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits)
    PORT MAP (clk, rst, mbRightSHR6_9Output, Multiplier6WeightOutput);

    InputIEEE_Float_6_9: entity work.InputIEEE_7_14_to_7_14(arch)
        PORT MAP (clk, Multiplier6WeightOutput, flopocoMultiplier6WeightOutput);

    MB_D_FF_Float_6_9_ConverterOutput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, flopocoMultiplier6WeightOutput, flopocoMultiplier6WeightInput);

    Multiplier_Float_6: entity work.FPMult_7_14_7_14_7_14_uid2_Freq800_uid3(arch)
    PORT MAP (clk, mb_D_FF6_9MultiplicandStage2Output, flopocoMultiplier6WeightInput, Multiplier6_Output_9);

    MBRightSHR_Float_6_9: entity work.MBRightSHR(rtl)
    GENERIC MAP (68, NumberOfBits)
    PORT MAP (clk, rst, Multiplier6Weight, mbRightSHR6_9Output);

    MB_D_FF_Float_Multiplier6_7_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier6_7_0Input, mb_D_FFMultiplier6_7_0Output);

    MB_D_FF_Float_7_10_MultiplicandStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier6_7_0Output, mb_D_FF7_10MultiplicandStage1Output);

    MB_D_FF_Float_7_10_MultiplicandStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF7_10MultiplicandStage1Output, mb_D_FF7_10MultiplicandStage2Output);

    MB_D_FF_Float_7_10_ConverterInput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits)
    PORT MAP (clk, rst, mbRightSHR7_10Output, Multiplier7WeightOutput);

    InputIEEE_Float_7_10: entity work.InputIEEE_7_14_to_7_14(arch)
        PORT MAP (clk, Multiplier7WeightOutput, flopocoMultiplier7WeightOutput);

    MB_D_FF_Float_7_10_ConverterOutput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, flopocoMultiplier7WeightOutput, flopocoMultiplier7WeightInput);

    Multiplier_Float_7: entity work.FPMult_7_14_7_14_7_14_uid2_Freq800_uid3(arch)
    PORT MAP (clk, mb_D_FF7_10MultiplicandStage2Output, flopocoMultiplier7WeightInput, Multiplier7_Output_10);

    MBRightSHR_Float_7_10: entity work.MBRightSHR(rtl)
    GENERIC MAP (4, NumberOfBits)
    PORT MAP (clk, rst, Multiplier7Weight, mbRightSHR7_10Output);

    MB_D_FF_Float_Multiplier6_8_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier6_8_0Input, mb_D_FFMultiplier6_8_0Output);

    MB_D_FF_Float_8_11_MultiplicandStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier6_8_0Output, mb_D_FF8_11MultiplicandStage1Output);

    MB_D_FF_Float_8_11_MultiplicandStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF8_11MultiplicandStage1Output, mb_D_FF8_11MultiplicandStage2Output);

    MB_D_FF_Float_8_11_ConverterInput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits)
    PORT MAP (clk, rst, mbRightSHR8_11Output, Multiplier8WeightOutput);

    InputIEEE_Float_8_11: entity work.InputIEEE_7_14_to_7_14(arch)
        PORT MAP (clk, Multiplier8WeightOutput, flopocoMultiplier8WeightOutput);

    MB_D_FF_Float_8_11_ConverterOutput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, flopocoMultiplier8WeightOutput, flopocoMultiplier8WeightInput);

    Multiplier_Float_8: entity work.FPMult_7_14_7_14_7_14_uid2_Freq800_uid3(arch)
    PORT MAP (clk, mb_D_FF8_11MultiplicandStage2Output, flopocoMultiplier8WeightInput, Multiplier8_Output_11);

    MBRightSHR_Float_8_11: entity work.MBRightSHR(rtl)
    GENERIC MAP (4, NumberOfBits)
    PORT MAP (clk, rst, Multiplier8Weight, mbRightSHR8_11Output);

    MB_D_FF_Float_Adder5_Input1_3_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Multiplier8_Output_11, mb_D_FFAdder5_Input1_3_0Output);

    MB_D_FF_Float_3_12_AugendStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFAdder5_Input1_3_0Output, mb_D_FF3_12AugendStage1Output);

    MB_D_FF_Float_3_12_AugendStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF3_12AugendStage1Output, mb_D_FF3_12AugendStage2Output);

    Adder_Float_3: entity work.FPAdd_7_14_Freq800_uid2(arch)
    PORT MAP (clk, mb_D_FF3_12AugendStage2Output, mb_D_FF3_12AddendStage2Output, Adder3_Output_12);

    MB_D_FF_Float_Adder5_Input2_3_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Multiplier7_Output_10, mb_D_FFAdder5_Input2_3_0Output);

    MB_D_FF_Float_3_12_AddendStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFAdder5_Input2_3_0Output, mb_D_FF3_12AddendStage1Output);

    MB_D_FF_Float_3_12_AddendStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF3_12AddendStage1Output, mb_D_FF3_12AddendStage2Output);

    MB_D_FF_Float_Multiplier4_9_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Adder3_Output_12, mb_D_FFMultiplier4_9_0Output);

    MB_D_FF_Float_9_13_MultiplicandStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier4_9_0Output, mb_D_FF9_13MultiplicandStage1Output);

    MB_D_FF_Float_9_13_MultiplicandStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF9_13MultiplicandStage1Output, mb_D_FF9_13MultiplicandStage2Output);

    MB_D_FF_Float_9_13_ConverterInput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits)
    PORT MAP (clk, rst, mbRightSHR9_13Output, Multiplier9WeightOutput);

    InputIEEE_Float_9_13: entity work.InputIEEE_7_14_to_7_14(arch)
        PORT MAP (clk, Multiplier9WeightOutput, flopocoMultiplier9WeightOutput);

    MB_D_FF_Float_9_13_ConverterOutput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, flopocoMultiplier9WeightOutput, flopocoMultiplier9WeightInput);

    Multiplier_Float_9: entity work.FPMult_7_14_7_14_7_14_uid2_Freq800_uid3(arch)
    PORT MAP (clk, mb_D_FF9_13MultiplicandStage2Output, flopocoMultiplier9WeightInput, Multiplier9_Output_13);

    MBRightSHR_Float_9_13: entity work.MBRightSHR(rtl)
    GENERIC MAP (36, NumberOfBits)
    PORT MAP (clk, rst, Multiplier9Weight, mbRightSHR9_13Output);

    MB_D_FF_Float_Multiplier6_10_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier6_10_0Input, mb_D_FFMultiplier6_10_0Output);

    MB_D_FF_Float_10_14_MultiplicandStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier6_10_0Output, mb_D_FF10_14MultiplicandStage1Output);

    MB_D_FF_Float_10_14_MultiplicandStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF10_14MultiplicandStage1Output, mb_D_FF10_14MultiplicandStage2Output);

    MB_D_FF_Float_10_14_ConverterInput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits)
    PORT MAP (clk, rst, mbRightSHR10_14Output, Multiplier10WeightOutput);

    InputIEEE_Float_10_14: entity work.InputIEEE_7_14_to_7_14(arch)
        PORT MAP (clk, Multiplier10WeightOutput, flopocoMultiplier10WeightOutput);

    MB_D_FF_Float_10_14_ConverterOutput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, flopocoMultiplier10WeightOutput, flopocoMultiplier10WeightInput);

    Multiplier_Float_10: entity work.FPMult_7_14_7_14_7_14_uid2_Freq800_uid3(arch)
    PORT MAP (clk, mb_D_FF10_14MultiplicandStage2Output, flopocoMultiplier10WeightInput, Multiplier10_Output_14);

    MBRightSHR_Float_10_14: entity work.MBRightSHR(rtl)
    GENERIC MAP (4, NumberOfBits)
    PORT MAP (clk, rst, Multiplier10Weight, mbRightSHR10_14Output);

    MB_D_FF_Float_Multiplier6_11_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier6_11_0Input, mb_D_FFMultiplier6_11_0Output);

    MB_D_FF_Float_11_15_MultiplicandStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier6_11_0Output, mb_D_FF11_15MultiplicandStage1Output);

    MB_D_FF_Float_11_15_MultiplicandStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF11_15MultiplicandStage1Output, mb_D_FF11_15MultiplicandStage2Output);

    MB_D_FF_Float_11_15_ConverterInput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits)
    PORT MAP (clk, rst, mbRightSHR11_15Output, Multiplier11WeightOutput);

    InputIEEE_Float_11_15: entity work.InputIEEE_7_14_to_7_14(arch)
        PORT MAP (clk, Multiplier11WeightOutput, flopocoMultiplier11WeightOutput);

    MB_D_FF_Float_11_15_ConverterOutput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, flopocoMultiplier11WeightOutput, flopocoMultiplier11WeightInput);

    Multiplier_Float_11: entity work.FPMult_7_14_7_14_7_14_uid2_Freq800_uid3(arch)
    PORT MAP (clk, mb_D_FF11_15MultiplicandStage2Output, flopocoMultiplier11WeightInput, Multiplier11_Output_15);

    MBRightSHR_Float_11_15: entity work.MBRightSHR(rtl)
    GENERIC MAP (4, NumberOfBits)
    PORT MAP (clk, rst, Multiplier11Weight, mbRightSHR11_15Output);

    MB_D_FF_Float_Adder5_Input1_4_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Multiplier11_Output_15, mb_D_FFAdder5_Input1_4_0Output);

    MB_D_FF_Float_4_16_AugendStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFAdder5_Input1_4_0Output, mb_D_FF4_16AugendStage1Output);

    MB_D_FF_Float_4_16_AugendStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF4_16AugendStage1Output, mb_D_FF4_16AugendStage2Output);

    Adder_Float_4: entity work.FPAdd_7_14_Freq800_uid2(arch)
    PORT MAP (clk, mb_D_FF4_16AugendStage2Output, mb_D_FF4_16AddendStage2Output, Adder4_Output_16);

    MB_D_FF_Float_Adder5_Input2_4_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Multiplier10_Output_14, mb_D_FFAdder5_Input2_4_0Output);

    MB_D_FF_Float_4_16_AddendStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFAdder5_Input2_4_0Output, mb_D_FF4_16AddendStage1Output);

    MB_D_FF_Float_4_16_AddendStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF4_16AddendStage1Output, mb_D_FF4_16AddendStage2Output);

    MB_D_FF_Float_Multiplier4_12_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Adder4_Output_16, mb_D_FFMultiplier4_12_0Output);

    MB_D_FF_Float_12_17_MultiplicandStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier4_12_0Output, mb_D_FF12_17MultiplicandStage1Output);

    MB_D_FF_Float_12_17_MultiplicandStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF12_17MultiplicandStage1Output, mb_D_FF12_17MultiplicandStage2Output);

    MB_D_FF_Float_12_17_ConverterInput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits)
    PORT MAP (clk, rst, mbRightSHR12_17Output, Multiplier12WeightOutput);

    InputIEEE_Float_12_17: entity work.InputIEEE_7_14_to_7_14(arch)
        PORT MAP (clk, Multiplier12WeightOutput, flopocoMultiplier12WeightOutput);

    MB_D_FF_Float_12_17_ConverterOutput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, flopocoMultiplier12WeightOutput, flopocoMultiplier12WeightInput);

    Multiplier_Float_12: entity work.FPMult_7_14_7_14_7_14_uid2_Freq800_uid3(arch)
    PORT MAP (clk, mb_D_FF12_17MultiplicandStage2Output, flopocoMultiplier12WeightInput, Multiplier12_Output_17);

    MBRightSHR_Float_12_17: entity work.MBRightSHR(rtl)
    GENERIC MAP (36, NumberOfBits)
    PORT MAP (clk, rst, Multiplier12Weight, mbRightSHR12_17Output);

    MB_D_FF_Float_Adder3_Input1_5_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Multiplier12_Output_17, mb_D_FFAdder3_Input1_5_0Output);

    MB_D_FF_Float_5_18_AugendStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFAdder3_Input1_5_0Output, mb_D_FF5_18AugendStage1Output);

    MB_D_FF_Float_5_18_AugendStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF5_18AugendStage1Output, mb_D_FF5_18AugendStage2Output);

    Adder_Float_5: entity work.FPAdd_7_14_Freq800_uid2(arch)
    PORT MAP (clk, mb_D_FF5_18AugendStage2Output, mb_D_FF5_18AddendStage2Output, Adder5_Output_18);

    MB_D_FF_Float_Adder3_Input2_5_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Multiplier9_Output_13, mb_D_FFAdder3_Input2_5_0Output);

    MB_D_FF_Float_5_18_AddendStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFAdder3_Input2_5_0Output, mb_D_FF5_18AddendStage1Output);

    MB_D_FF_Float_5_18_AddendStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF5_18AddendStage1Output, mb_D_FF5_18AddendStage2Output);

    MB_D_FF_Float_Multiplier2_13_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Adder5_Output_18, mb_D_FFMultiplier2_13_0Output);

    MB_D_FF_Float_13_19_MultiplicandStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFMultiplier2_13_0Output, mb_D_FF13_19MultiplicandStage1Output);

    MB_D_FF_Float_13_19_MultiplicandStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF13_19MultiplicandStage1Output, mb_D_FF13_19MultiplicandStage2Output);

    MB_D_FF_Float_13_19_ConverterInput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits)
    PORT MAP (clk, rst, mbRightSHR13_19Output, Multiplier13WeightOutput);

    InputIEEE_Float_13_19: entity work.InputIEEE_7_14_to_7_14(arch)
        PORT MAP (clk, Multiplier13WeightOutput, flopocoMultiplier13WeightOutput);

    MB_D_FF_Float_13_19_ConverterOutput: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, flopocoMultiplier13WeightOutput, flopocoMultiplier13WeightInput);

    Multiplier_Float_13: entity work.FPMult_7_14_7_14_7_14_uid2_Freq800_uid3(arch)
    PORT MAP (clk, mb_D_FF13_19MultiplicandStage2Output, flopocoMultiplier13WeightInput, Multiplier13_Output_19);

    MBRightSHR_Float_13_19: entity work.MBRightSHR(rtl)
    GENERIC MAP (68, NumberOfBits)
    PORT MAP (clk, rst, Multiplier13Weight, mbRightSHR13_19Output);

    MB_D_FF_Float_Adder1_Input1_6_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Multiplier13_Output_19, mb_D_FFAdder1_Input1_6_0Output);

    MB_D_FF_Float_6_20_AugendStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFAdder1_Input1_6_0Output, mb_D_FF6_20AugendStage1Output);

    MB_D_FF_Float_6_20_AugendStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF6_20AugendStage1Output, mb_D_FF6_20AugendStage2Output);

    Adder_Float_6: entity work.FPAdd_7_14_Freq800_uid2(arch)
    PORT MAP (clk, mb_D_FF6_20AugendStage2Output, mb_D_FF6_20AddendStage2Output, Adder6_Output_20);

    MB_D_FF_Float_Adder1_Input2_6_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Multiplier6_Output_9, mb_D_FFAdder1_Input2_6_0Output);

    MB_D_FF_Float_6_20_AddendStage1Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FFAdder1_Input2_6_0Output, mb_D_FF6_20AddendStage1Output);

    MB_D_FF_Float_6_20_AddendStage2Register: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, mb_D_FF6_20AddendStage1Output, mb_D_FF6_20AddendStage2Output);

    MB_D_FF_Float_Adder1_Output_6_0: entity work.MB_D_FF(rtl)
    GENERIC MAP (NumberOfBits+FlopocoBits)
    PORT MAP (clk, rst, Adder6_Output_20, mb_D_FFAdder1_Output_6_0Output);

    vout <= mb_D_FFAdder1_Output_6_0Output;
 
END ARCHITECTURE;
