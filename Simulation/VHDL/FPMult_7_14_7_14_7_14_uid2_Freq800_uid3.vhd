--------------------------------------------------------------------------------
--                        DSPBlock_15x15_Freq800_uid9
-- VHDL generated for Virtex6 @ 800MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: 
--------------------------------------------------------------------------------
-- Pipeline depth: 1 cycles
-- Clock period (ns): 1.25
-- Target frequency (MHz): 800
-- Input signals: X Y
-- Output signals: R

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
library std;
use std.textio.all;
library work;

entity DSPBlock_15x15_Freq800_uid9 is
    port (clk : in std_logic;
          X : in  std_logic_vector(14 downto 0);
          Y : in  std_logic_vector(14 downto 0);
          R : out  std_logic_vector(29 downto 0)   );
end entity;

architecture arch of DSPBlock_15x15_Freq800_uid9 is
signal Mint :  std_logic_vector(29 downto 0);
signal M :  std_logic_vector(29 downto 0);
signal Rtmp :  std_logic_vector(29 downto 0);
signal X_d1 :  std_logic_vector(14 downto 0);
signal Y_d1 :  std_logic_vector(14 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            X_d1 <=  X;
            Y_d1 <=  Y;
         end if;
      end process;
   Mint <= std_logic_vector(unsigned(X_d1) * unsigned(Y_d1)); -- multiplier
   M <= Mint(29 downto 0);
   Rtmp <= M;
   R <= Rtmp;
end architecture;

--------------------------------------------------------------------------------
--                         IntMultiplier_Freq800_uid5
-- VHDL generated for Virtex6 @ 800MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Martin Kumm, Florent de Dinechin, Kinga Illyes, Bogdan Popa, Bogdan Pasca, 2012
--------------------------------------------------------------------------------
-- Pipeline depth: 1 cycles
-- Clock period (ns): 1.25
-- Target frequency (MHz): 800
-- Input signals: X Y
-- Output signals: R

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
library std;
use std.textio.all;
library work;

entity IntMultiplier_Freq800_uid5 is
    port (clk : in std_logic;
          X : in  std_logic_vector(14 downto 0);
          Y : in  std_logic_vector(14 downto 0);
          R : out  std_logic_vector(29 downto 0)   );
end entity;

architecture arch of IntMultiplier_Freq800_uid5 is
   component DSPBlock_15x15_Freq800_uid9 is
      port ( clk : in std_logic;
             X : in  std_logic_vector(14 downto 0);
             Y : in  std_logic_vector(14 downto 0);
             R : out  std_logic_vector(29 downto 0)   );
   end component;

signal XX_m6 :  std_logic_vector(14 downto 0);
signal YY_m6 :  std_logic_vector(14 downto 0);
signal tile_0_X :  std_logic_vector(14 downto 0);
signal tile_0_Y :  std_logic_vector(14 downto 0);
signal tile_0_output :  std_logic_vector(29 downto 0);
signal tile_0_filtered_output :  unsigned(29-0 downto 0);
signal bh7_w0_0 :  std_logic;
signal bh7_w1_0 :  std_logic;
signal bh7_w2_0 :  std_logic;
signal bh7_w3_0 :  std_logic;
signal bh7_w4_0 :  std_logic;
signal bh7_w5_0 :  std_logic;
signal bh7_w6_0 :  std_logic;
signal bh7_w7_0 :  std_logic;
signal bh7_w8_0 :  std_logic;
signal bh7_w9_0 :  std_logic;
signal bh7_w10_0 :  std_logic;
signal bh7_w11_0 :  std_logic;
signal bh7_w12_0 :  std_logic;
signal bh7_w13_0 :  std_logic;
signal bh7_w14_0 :  std_logic;
signal bh7_w15_0 :  std_logic;
signal bh7_w16_0 :  std_logic;
signal bh7_w17_0 :  std_logic;
signal bh7_w18_0 :  std_logic;
signal bh7_w19_0 :  std_logic;
signal bh7_w20_0 :  std_logic;
signal bh7_w21_0 :  std_logic;
signal bh7_w22_0 :  std_logic;
signal bh7_w23_0 :  std_logic;
signal bh7_w24_0 :  std_logic;
signal bh7_w25_0 :  std_logic;
signal bh7_w26_0 :  std_logic;
signal bh7_w27_0 :  std_logic;
signal bh7_w28_0 :  std_logic;
signal bh7_w29_0 :  std_logic;
signal tmp_bitheapResult_bh7_29 :  std_logic_vector(29 downto 0);
signal bitheapResult_bh7 :  std_logic_vector(29 downto 0);
begin
   XX_m6 <= X ;
   YY_m6 <= Y ;
   tile_0_X <= X(14 downto 0);
   tile_0_Y <= Y(14 downto 0);
   tile_0_mult: DSPBlock_15x15_Freq800_uid9
      port map ( clk  => clk,
                 X => tile_0_X,
                 Y => tile_0_Y,
                 R => tile_0_output);

   tile_0_filtered_output <= unsigned(tile_0_output(29 downto 0));
   bh7_w0_0 <= tile_0_filtered_output(0);
   bh7_w1_0 <= tile_0_filtered_output(1);
   bh7_w2_0 <= tile_0_filtered_output(2);
   bh7_w3_0 <= tile_0_filtered_output(3);
   bh7_w4_0 <= tile_0_filtered_output(4);
   bh7_w5_0 <= tile_0_filtered_output(5);
   bh7_w6_0 <= tile_0_filtered_output(6);
   bh7_w7_0 <= tile_0_filtered_output(7);
   bh7_w8_0 <= tile_0_filtered_output(8);
   bh7_w9_0 <= tile_0_filtered_output(9);
   bh7_w10_0 <= tile_0_filtered_output(10);
   bh7_w11_0 <= tile_0_filtered_output(11);
   bh7_w12_0 <= tile_0_filtered_output(12);
   bh7_w13_0 <= tile_0_filtered_output(13);
   bh7_w14_0 <= tile_0_filtered_output(14);
   bh7_w15_0 <= tile_0_filtered_output(15);
   bh7_w16_0 <= tile_0_filtered_output(16);
   bh7_w17_0 <= tile_0_filtered_output(17);
   bh7_w18_0 <= tile_0_filtered_output(18);
   bh7_w19_0 <= tile_0_filtered_output(19);
   bh7_w20_0 <= tile_0_filtered_output(20);
   bh7_w21_0 <= tile_0_filtered_output(21);
   bh7_w22_0 <= tile_0_filtered_output(22);
   bh7_w23_0 <= tile_0_filtered_output(23);
   bh7_w24_0 <= tile_0_filtered_output(24);
   bh7_w25_0 <= tile_0_filtered_output(25);
   bh7_w26_0 <= tile_0_filtered_output(26);
   bh7_w27_0 <= tile_0_filtered_output(27);
   bh7_w28_0 <= tile_0_filtered_output(28);
   bh7_w29_0 <= tile_0_filtered_output(29);

   -- Adding the constant bits 
      -- All the constant bits are zero, nothing to add

   tmp_bitheapResult_bh7_29 <= bh7_w29_0 & bh7_w28_0 & bh7_w27_0 & bh7_w26_0 & bh7_w25_0 & bh7_w24_0 & bh7_w23_0 & bh7_w22_0 & bh7_w21_0 & bh7_w20_0 & bh7_w19_0 & bh7_w18_0 & bh7_w17_0 & bh7_w16_0 & bh7_w15_0 & bh7_w14_0 & bh7_w13_0 & bh7_w12_0 & bh7_w11_0 & bh7_w10_0 & bh7_w9_0 & bh7_w8_0 & bh7_w7_0 & bh7_w6_0 & bh7_w5_0 & bh7_w4_0 & bh7_w3_0 & bh7_w2_0 & bh7_w1_0 & bh7_w0_0;
   bitheapResult_bh7 <= tmp_bitheapResult_bh7_29;
   R <= bitheapResult_bh7(29 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                         IntAdder_23_Freq800_uid13
-- VHDL generated for Virtex6 @ 800MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca, Florent de Dinechin (2008-2016)
--------------------------------------------------------------------------------
-- Pipeline depth: 2 cycles
-- Clock period (ns): 1.25
-- Target frequency (MHz): 800
-- Input signals: X Y Cin
-- Output signals: R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity IntAdder_23_Freq800_uid13 is
    port (clk : in std_logic;
          X : in  std_logic_vector(22 downto 0);
          Y : in  std_logic_vector(22 downto 0);
          Cin : in  std_logic;
          R : out  std_logic_vector(22 downto 0)   );
end entity;

architecture arch of IntAdder_23_Freq800_uid13 is
signal Cin_1, Cin_1_d1 :  std_logic;
signal X_1, X_1_d1, X_1_d2 :  std_logic_vector(15 downto 0);
signal Y_1, Y_1_d1, Y_1_d2, Y_1_d3 :  std_logic_vector(15 downto 0);
signal S_1 :  std_logic_vector(15 downto 0);
signal R_1, R_1_d1 :  std_logic_vector(14 downto 0);
signal Cin_2, Cin_2_d1 :  std_logic;
signal X_2, X_2_d1, X_2_d2, X_2_d3 :  std_logic_vector(8 downto 0);
signal Y_2, Y_2_d1, Y_2_d2, Y_2_d3, Y_2_d4 :  std_logic_vector(8 downto 0);
signal S_2 :  std_logic_vector(8 downto 0);
signal R_2 :  std_logic_vector(7 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            Cin_1_d1 <=  Cin_1;
            X_1_d1 <=  X_1;
            X_1_d2 <=  X_1_d1;
            Y_1_d1 <=  Y_1;
            Y_1_d2 <=  Y_1_d1;
            Y_1_d3 <=  Y_1_d2;
            R_1_d1 <=  R_1;
            Cin_2_d1 <=  Cin_2;
            X_2_d1 <=  X_2;
            X_2_d2 <=  X_2_d1;
            X_2_d3 <=  X_2_d2;
            Y_2_d1 <=  Y_2;
            Y_2_d2 <=  Y_2_d1;
            Y_2_d3 <=  Y_2_d2;
            Y_2_d4 <=  Y_2_d3;
         end if;
      end process;
   Cin_1 <= Cin;
   X_1 <= '0' & X(14 downto 0);
   Y_1 <= '0' & Y(14 downto 0);
   S_1 <= X_1_d2 + Y_1_d3 + Cin_1_d1;
   R_1 <= S_1(14 downto 0);
   Cin_2 <= S_1(15);
   X_2 <= '0' & X(22 downto 15);
   Y_2 <= '0' & Y(22 downto 15);
   S_2 <= X_2_d3 + Y_2_d4 + Cin_2_d1;
   R_2 <= S_2(7 downto 0);
   R <= R_2 & R_1_d1 ;
end architecture;

--------------------------------------------------------------------------------
--                  FPMult_7_14_7_14_7_14_uid2_Freq800_uid3
-- VHDL generated for Virtex6 @ 800MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca, Florent de Dinechin 2008-2021
--------------------------------------------------------------------------------
-- Pipeline depth: 4 cycles
-- Clock period (ns): 1.25
-- Target frequency (MHz): 800
-- Input signals: X Y
-- Output signals: R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity FPMult_7_14_7_14_7_14_uid2_Freq800_uid3 is
    port (clk : in std_logic;
          X : in  std_logic_vector(7+14+2 downto 0);
          Y : in  std_logic_vector(7+14+2 downto 0);
          R : out  std_logic_vector(7+14+2 downto 0)   );
end entity;

architecture arch of FPMult_7_14_7_14_7_14_uid2_Freq800_uid3 is
   component IntMultiplier_Freq800_uid5 is
      port ( clk : in std_logic;
             X : in  std_logic_vector(14 downto 0);
             Y : in  std_logic_vector(14 downto 0);
             R : out  std_logic_vector(29 downto 0)   );
   end component;

   component IntAdder_23_Freq800_uid13 is
      port ( clk : in std_logic;
             X : in  std_logic_vector(22 downto 0);
             Y : in  std_logic_vector(22 downto 0);
             Cin : in  std_logic;
             R : out  std_logic_vector(22 downto 0)   );
   end component;

signal sign, sign_d1, sign_d2, sign_d3, sign_d4 :  std_logic;
signal expX :  std_logic_vector(6 downto 0);
signal expY :  std_logic_vector(6 downto 0);
signal expSumPreSub, expSumPreSub_d1 :  std_logic_vector(8 downto 0);
signal bias, bias_d1 :  std_logic_vector(8 downto 0);
signal expSum :  std_logic_vector(8 downto 0);
signal sigX :  std_logic_vector(14 downto 0);
signal sigY :  std_logic_vector(14 downto 0);
signal sigProd :  std_logic_vector(29 downto 0);
signal excSel :  std_logic_vector(3 downto 0);
signal exc, exc_d1, exc_d2, exc_d3, exc_d4 :  std_logic_vector(1 downto 0);
signal norm :  std_logic;
signal expPostNorm :  std_logic_vector(8 downto 0);
signal sigProdExt, sigProdExt_d1 :  std_logic_vector(29 downto 0);
signal expSig :  std_logic_vector(22 downto 0);
signal sticky, sticky_d1 :  std_logic;
signal guard :  std_logic;
signal round :  std_logic;
signal expSigPostRound :  std_logic_vector(22 downto 0);
signal excPostNorm :  std_logic_vector(1 downto 0);
signal finalExc :  std_logic_vector(1 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            sign_d1 <=  sign;
            sign_d2 <=  sign_d1;
            sign_d3 <=  sign_d2;
            sign_d4 <=  sign_d3;
            expSumPreSub_d1 <=  expSumPreSub;
            bias_d1 <=  bias;
            exc_d1 <=  exc;
            exc_d2 <=  exc_d1;
            exc_d3 <=  exc_d2;
            exc_d4 <=  exc_d3;
            sigProdExt_d1 <=  sigProdExt;
            sticky_d1 <=  sticky;
         end if;
      end process;
   sign <= X(21) xor Y(21);
   expX <= X(20 downto 14);
   expY <= Y(20 downto 14);
   expSumPreSub <= ("00" & expX) + ("00" & expY);
   bias <= CONV_STD_LOGIC_VECTOR(63,9);
   expSum <= expSumPreSub_d1 - bias_d1;
   sigX <= "1" & X(13 downto 0);
   sigY <= "1" & Y(13 downto 0);
   SignificandMultiplication: IntMultiplier_Freq800_uid5
      port map ( clk  => clk,
                 X => sigX,
                 Y => sigY,
                 R => sigProd);
   excSel <= X(23 downto 22) & Y(23 downto 22);
   with excSel  select  
   exc <= "00" when  "0000" | "0001" | "0100", 
          "01" when "0101",
          "10" when "0110" | "1001" | "1010" ,
          "11" when others;
   norm <= sigProd(29);
   -- exponent update
   expPostNorm <= expSum + ("00000000" & norm);
   -- significand normalization shift
   sigProdExt <= sigProd(28 downto 0) & "0" when norm='1' else
                         sigProd(27 downto 0) & "00";
   expSig <= expPostNorm & sigProdExt(29 downto 16);
   sticky <= sigProdExt(15);
   guard <= '0' when sigProdExt_d1(14 downto 0)="000000000000000" else '1';
   round <= sticky_d1 and ( (guard and not(sigProdExt_d1(16))) or (sigProdExt_d1(16) ))  ;
   RoundingAdder: IntAdder_23_Freq800_uid13
      port map ( clk  => clk,
                 Cin => round,
                 X => expSig,
                 Y => "00000000000000000000000",
                 R => expSigPostRound);
   with expSigPostRound(22 downto 21)  select 
   excPostNorm <=  "01"  when  "00",
                               "10"             when "01", 
                               "00"             when "11"|"10",
                               "11"             when others;
   with exc_d4  select  
   finalExc <= exc_d4 when  "11"|"10"|"00",
                       excPostNorm when others; 
   R <= finalExc & sign_d4 & expSigPostRound(20 downto 0);
end architecture;

