--------------------------------------------------------------------------------
--                    Normalizer_ZO_24_24_15_Freq600_uid6
-- VHDL generated for Kintex7 @ 600MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, (2007-2020)
--------------------------------------------------------------------------------
-- Pipeline depth: 4 cycles
-- Clock period (ns): 1.66667
-- Target frequency (MHz): 600
-- Input signals: X OZb
-- Output signals: Count R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Normalizer_ZO_24_24_15_Freq600_uid6 is
    port (clk,enable : in std_logic;
          X : in  std_logic_vector(23 downto 0);
          OZb : in  std_logic;
          Count : out  std_logic_vector(3 downto 0);
          R : out  std_logic_vector(23 downto 0)   );
end entity;

architecture arch of Normalizer_ZO_24_24_15_Freq600_uid6 is
signal level4, level4_d1 :  std_logic_vector(23 downto 0);
signal sozb, sozb_d1, sozb_d2, sozb_d3 :  std_logic;
signal count3, count3_d1, count3_d2, count3_d3 :  std_logic;
signal level3, level3_d1 :  std_logic_vector(23 downto 0);
signal count2, count2_d1, count2_d2 :  std_logic;
signal level2, level2_d1 :  std_logic_vector(23 downto 0);
signal count1, count1_d1 :  std_logic;
signal level1, level1_d1 :  std_logic_vector(23 downto 0);
signal count0, count0_d1 :  std_logic;
signal level0 :  std_logic_vector(23 downto 0);
signal sCount :  std_logic_vector(3 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            level4_d1 <=  level4;
            sozb_d1 <=  sozb;
            sozb_d2 <=  sozb_d1;
            sozb_d3 <=  sozb_d2;
            count3_d1 <=  count3;
            count3_d2 <=  count3_d1;
            count3_d3 <=  count3_d2;
            level3_d1 <=  level3;
            count2_d1 <=  count2;
            count2_d2 <=  count2_d1;
            level2_d1 <=  level2;
            count1_d1 <=  count1;
            level1_d1 <=  level1;
            count0_d1 <=  count0;
         end if;
      end process;
   level4 <= X ;
   sozb<= OZb;
   count3<= '1' when level4(23 downto 16) = (23 downto 16=>sozb) else '0';
   level3<= level4_d1(23 downto 0) when count3_d1='0' else level4_d1(15 downto 0) & (7 downto 0 => '0');

   count2<= '1' when level3(23 downto 20) = (23 downto 20=>sozb_d1) else '0';
   level2<= level3_d1(23 downto 0) when count2_d1='0' else level3_d1(19 downto 0) & (3 downto 0 => '0');

   count1<= '1' when level2(23 downto 22) = (23 downto 22=>sozb_d2) else '0';
   level1<= level2_d1(23 downto 0) when count1_d1='0' else level2_d1(21 downto 0) & (1 downto 0 => '0');

   count0<= '1' when level1(23 downto 23) = (23 downto 23=>sozb_d3) else '0';
   level0<= level1_d1(23 downto 0) when count0_d1='0' else level1_d1(22 downto 0) & (0 downto 0 => '0');

   R <= level0;
   sCount <= count3_d3 & count2_d2 & count1_d1 & count0;
   Count <= sCount;
end architecture;

--------------------------------------------------------------------------------
--                        Posit2PIF_26_9_Freq600_uid4
-- VHDL generated for Kintex7 @ 600MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Oregane Desrentes 2019
--------------------------------------------------------------------------------
-- Pipeline depth: 5 cycles
-- Clock period (ns): 1.66667
-- Target frequency (MHz): 600
-- Input signals: I
-- Output signals: O

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Posit2PIF_26_9_Freq600_uid4 is
    port (clk,enable : in std_logic;
          I : in  std_logic_vector(25 downto 0);
          O : out  std_logic_vector(33 downto 0)   );
end entity;

architecture arch of Posit2PIF_26_9_Freq600_uid4 is
   component Normalizer_ZO_24_24_15_Freq600_uid6 is
      port ( clk,enable : in std_logic;
             X : in  std_logic_vector(23 downto 0);
             OZb : in  std_logic;
             Count : out  std_logic_vector(3 downto 0);
             R : out  std_logic_vector(23 downto 0)   );
   end component;

signal s, s_d1, s_d2, s_d3, s_d4, s_d5 :  std_logic;
signal count_type :  std_logic;
signal remainder :  std_logic_vector(23 downto 0);
signal not_s, not_s_d1 :  std_logic;
signal zero_NAR, zero_NAR_d1 :  std_logic;
signal is_NAR, is_NAR_d1, is_NAR_d2, is_NAR_d3, is_NAR_d4 :  std_logic;
signal is_not_zero :  std_logic;
signal implicit_bit, implicit_bit_d1, implicit_bit_d2, implicit_bit_d3, implicit_bit_d4 :  std_logic;
signal neg_count :  std_logic;
signal lzCount, lzCount_d1 :  std_logic_vector(3 downto 0);
signal usefulBits :  std_logic_vector(23 downto 0);
signal extended_neg_count, extended_neg_count_d1, extended_neg_count_d2, extended_neg_count_d3, extended_neg_count_d4 :  std_logic_vector(5 downto 0);
signal comp2_range_count :  std_logic_vector(5 downto 0);
signal fraction, fraction_d1 :  std_logic_vector(13 downto 0);
signal partialExponent :  std_logic_vector(8 downto 0);
signal us_partialExponent :  std_logic_vector(8 downto 0);
signal exponent, exponent_d1 :  std_logic_vector(14 downto 0);
signal biased_exponent :  std_logic_vector(14 downto 0);
signal extended_is_not_zero, extended_is_not_zero_d1, extended_is_not_zero_d2, extended_is_not_zero_d3, extended_is_not_zero_d4 :  std_logic_vector(14 downto 0);
signal final_biased_exponent :  std_logic_vector(14 downto 0);
signal round, round_d1, round_d2, round_d3, round_d4, round_d5 :  std_logic;
signal sticky, sticky_d1, sticky_d2, sticky_d3, sticky_d4, sticky_d5 :  std_logic;
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            s_d1 <=  s;
            s_d2 <=  s_d1;
            s_d3 <=  s_d2;
            s_d4 <=  s_d3;
            s_d5 <=  s_d4;
            not_s_d1 <=  not_s;
            zero_NAR_d1 <=  zero_NAR;
            is_NAR_d1 <=  is_NAR;
            is_NAR_d2 <=  is_NAR_d1;
            is_NAR_d3 <=  is_NAR_d2;
            is_NAR_d4 <=  is_NAR_d3;
            implicit_bit_d1 <=  implicit_bit;
            implicit_bit_d2 <=  implicit_bit_d1;
            implicit_bit_d3 <=  implicit_bit_d2;
            implicit_bit_d4 <=  implicit_bit_d3;
            lzCount_d1 <=  lzCount;
            extended_neg_count_d1 <=  extended_neg_count;
            extended_neg_count_d2 <=  extended_neg_count_d1;
            extended_neg_count_d3 <=  extended_neg_count_d2;
            extended_neg_count_d4 <=  extended_neg_count_d3;
            fraction_d1 <=  fraction;
            exponent_d1 <=  exponent;
            extended_is_not_zero_d1 <=  extended_is_not_zero;
            extended_is_not_zero_d2 <=  extended_is_not_zero_d1;
            extended_is_not_zero_d3 <=  extended_is_not_zero_d2;
            extended_is_not_zero_d4 <=  extended_is_not_zero_d3;
            round_d1 <=  round;
            round_d2 <=  round_d1;
            round_d3 <=  round_d2;
            round_d4 <=  round_d3;
            round_d5 <=  round_d4;
            sticky_d1 <=  sticky;
            sticky_d2 <=  sticky_d1;
            sticky_d3 <=  sticky_d2;
            sticky_d4 <=  sticky_d3;
            sticky_d5 <=  sticky_d4;
         end if;
      end process;
--------------------------- Start of vhdl generation ---------------------------
s<= I(25);
count_type<= I(24);
remainder<= I(23 downto 0);
not_s<= not s;
zero_NAR <= not count_type when remainder="000000000000000000000000" else '0';
is_NAR<= zero_NAR_d1 and s_d1;
is_not_zero<= not(zero_NAR_d1 and not_s_d1);
implicit_bit<= is_not_zero and not_s_d1;
neg_count<= not (s xor count_type);
   lzoc: Normalizer_ZO_24_24_15_Freq600_uid6
      port map ( clk  => clk,
                 enable => enable,
                 OZb => count_type,
                 X => remainder,
                 Count => lzCount,
                 R => usefulBits);
with neg_count  select  extended_neg_count <= 
   "000000" when '0', 
   "111111" when '1', 
   "------" when others;
comp2_range_count<= extended_neg_count_d4 xor ("00" & lzCount_d1);
fraction<= usefulBits(13 downto 0);
partialExponent<= usefulBits(22 downto 14);
with s_d4  select  us_partialExponent<= 
   partialExponent when '0',
   not partialExponent when '1',
   "---------" when others;
exponent<= comp2_range_count & us_partialExponent;
biased_exponent<= exponent_d1 + 12289;
with is_not_zero  select   extended_is_not_zero <= 
   "000000000000000" when '0', 
   "111111111111111" when '1', 
   "---------------" when others;
final_biased_exponent<= extended_is_not_zero_d4 and biased_exponent;
round<= '0';
sticky<= '0';
O <= is_NAR_d4 & s_d5 & final_biased_exponent & implicit_bit_d4 & fraction_d1 & round_d5 & sticky_d5;
---------------------------- End of vhdl generation ----------------------------
end architecture;

--------------------------------------------------------------------------------
--                    Normalizer_ZO_24_24_15_Freq600_uid10
-- VHDL generated for Kintex7 @ 600MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, (2007-2020)
--------------------------------------------------------------------------------
-- Pipeline depth: 4 cycles
-- Clock period (ns): 1.66667
-- Target frequency (MHz): 600
-- Input signals: X OZb
-- Output signals: Count R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Normalizer_ZO_24_24_15_Freq600_uid10 is
    port (clk,enable : in std_logic;
          X : in  std_logic_vector(23 downto 0);
          OZb : in  std_logic;
          Count : out  std_logic_vector(3 downto 0);
          R : out  std_logic_vector(23 downto 0)   );
end entity;

architecture arch of Normalizer_ZO_24_24_15_Freq600_uid10 is
signal level4, level4_d1 :  std_logic_vector(23 downto 0);
signal sozb, sozb_d1, sozb_d2, sozb_d3 :  std_logic;
signal count3, count3_d1, count3_d2, count3_d3 :  std_logic;
signal level3, level3_d1 :  std_logic_vector(23 downto 0);
signal count2, count2_d1, count2_d2 :  std_logic;
signal level2, level2_d1 :  std_logic_vector(23 downto 0);
signal count1, count1_d1 :  std_logic;
signal level1, level1_d1 :  std_logic_vector(23 downto 0);
signal count0, count0_d1 :  std_logic;
signal level0 :  std_logic_vector(23 downto 0);
signal sCount :  std_logic_vector(3 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            level4_d1 <=  level4;
            sozb_d1 <=  sozb;
            sozb_d2 <=  sozb_d1;
            sozb_d3 <=  sozb_d2;
            count3_d1 <=  count3;
            count3_d2 <=  count3_d1;
            count3_d3 <=  count3_d2;
            level3_d1 <=  level3;
            count2_d1 <=  count2;
            count2_d2 <=  count2_d1;
            level2_d1 <=  level2;
            count1_d1 <=  count1;
            level1_d1 <=  level1;
            count0_d1 <=  count0;
         end if;
      end process;
   level4 <= X ;
   sozb<= OZb;
   count3<= '1' when level4(23 downto 16) = (23 downto 16=>sozb) else '0';
   level3<= level4_d1(23 downto 0) when count3_d1='0' else level4_d1(15 downto 0) & (7 downto 0 => '0');

   count2<= '1' when level3(23 downto 20) = (23 downto 20=>sozb_d1) else '0';
   level2<= level3_d1(23 downto 0) when count2_d1='0' else level3_d1(19 downto 0) & (3 downto 0 => '0');

   count1<= '1' when level2(23 downto 22) = (23 downto 22=>sozb_d2) else '0';
   level1<= level2_d1(23 downto 0) when count1_d1='0' else level2_d1(21 downto 0) & (1 downto 0 => '0');

   count0<= '1' when level1(23 downto 23) = (23 downto 23=>sozb_d3) else '0';
   level0<= level1_d1(23 downto 0) when count0_d1='0' else level1_d1(22 downto 0) & (0 downto 0 => '0');

   R <= level0;
   sCount <= count3_d3 & count2_d2 & count1_d1 & count0;
   Count <= sCount;
end architecture;

--------------------------------------------------------------------------------
--                        Posit2PIF_26_9_Freq600_uid8
-- VHDL generated for Kintex7 @ 600MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Oregane Desrentes 2019
--------------------------------------------------------------------------------
-- Pipeline depth: 5 cycles
-- Clock period (ns): 1.66667
-- Target frequency (MHz): 600
-- Input signals: I
-- Output signals: O

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Posit2PIF_26_9_Freq600_uid8 is
    port (clk,enable : in std_logic;
          I : in  std_logic_vector(25 downto 0);
          O : out  std_logic_vector(33 downto 0)   );
end entity;

architecture arch of Posit2PIF_26_9_Freq600_uid8 is
   component Normalizer_ZO_24_24_15_Freq600_uid10 is
      port ( clk,enable : in std_logic;
             X : in  std_logic_vector(23 downto 0);
             OZb : in  std_logic;
             Count : out  std_logic_vector(3 downto 0);
             R : out  std_logic_vector(23 downto 0)   );
   end component;

signal s, s_d1, s_d2, s_d3, s_d4, s_d5 :  std_logic;
signal count_type :  std_logic;
signal remainder :  std_logic_vector(23 downto 0);
signal not_s, not_s_d1 :  std_logic;
signal zero_NAR, zero_NAR_d1 :  std_logic;
signal is_NAR, is_NAR_d1, is_NAR_d2, is_NAR_d3, is_NAR_d4 :  std_logic;
signal is_not_zero :  std_logic;
signal implicit_bit, implicit_bit_d1, implicit_bit_d2, implicit_bit_d3, implicit_bit_d4 :  std_logic;
signal neg_count :  std_logic;
signal lzCount, lzCount_d1 :  std_logic_vector(3 downto 0);
signal usefulBits :  std_logic_vector(23 downto 0);
signal extended_neg_count, extended_neg_count_d1, extended_neg_count_d2, extended_neg_count_d3, extended_neg_count_d4 :  std_logic_vector(5 downto 0);
signal comp2_range_count :  std_logic_vector(5 downto 0);
signal fraction, fraction_d1 :  std_logic_vector(13 downto 0);
signal partialExponent :  std_logic_vector(8 downto 0);
signal us_partialExponent :  std_logic_vector(8 downto 0);
signal exponent, exponent_d1 :  std_logic_vector(14 downto 0);
signal biased_exponent :  std_logic_vector(14 downto 0);
signal extended_is_not_zero, extended_is_not_zero_d1, extended_is_not_zero_d2, extended_is_not_zero_d3, extended_is_not_zero_d4 :  std_logic_vector(14 downto 0);
signal final_biased_exponent :  std_logic_vector(14 downto 0);
signal round, round_d1, round_d2, round_d3, round_d4, round_d5 :  std_logic;
signal sticky, sticky_d1, sticky_d2, sticky_d3, sticky_d4, sticky_d5 :  std_logic;
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            s_d1 <=  s;
            s_d2 <=  s_d1;
            s_d3 <=  s_d2;
            s_d4 <=  s_d3;
            s_d5 <=  s_d4;
            not_s_d1 <=  not_s;
            zero_NAR_d1 <=  zero_NAR;
            is_NAR_d1 <=  is_NAR;
            is_NAR_d2 <=  is_NAR_d1;
            is_NAR_d3 <=  is_NAR_d2;
            is_NAR_d4 <=  is_NAR_d3;
            implicit_bit_d1 <=  implicit_bit;
            implicit_bit_d2 <=  implicit_bit_d1;
            implicit_bit_d3 <=  implicit_bit_d2;
            implicit_bit_d4 <=  implicit_bit_d3;
            lzCount_d1 <=  lzCount;
            extended_neg_count_d1 <=  extended_neg_count;
            extended_neg_count_d2 <=  extended_neg_count_d1;
            extended_neg_count_d3 <=  extended_neg_count_d2;
            extended_neg_count_d4 <=  extended_neg_count_d3;
            fraction_d1 <=  fraction;
            exponent_d1 <=  exponent;
            extended_is_not_zero_d1 <=  extended_is_not_zero;
            extended_is_not_zero_d2 <=  extended_is_not_zero_d1;
            extended_is_not_zero_d3 <=  extended_is_not_zero_d2;
            extended_is_not_zero_d4 <=  extended_is_not_zero_d3;
            round_d1 <=  round;
            round_d2 <=  round_d1;
            round_d3 <=  round_d2;
            round_d4 <=  round_d3;
            round_d5 <=  round_d4;
            sticky_d1 <=  sticky;
            sticky_d2 <=  sticky_d1;
            sticky_d3 <=  sticky_d2;
            sticky_d4 <=  sticky_d3;
            sticky_d5 <=  sticky_d4;
         end if;
      end process;
--------------------------- Start of vhdl generation ---------------------------
s<= I(25);
count_type<= I(24);
remainder<= I(23 downto 0);
not_s<= not s;
zero_NAR <= not count_type when remainder="000000000000000000000000" else '0';
is_NAR<= zero_NAR_d1 and s_d1;
is_not_zero<= not(zero_NAR_d1 and not_s_d1);
implicit_bit<= is_not_zero and not_s_d1;
neg_count<= not (s xor count_type);
   lzoc: Normalizer_ZO_24_24_15_Freq600_uid10
      port map ( clk  => clk,
                 enable => enable,
                 OZb => count_type,
                 X => remainder,
                 Count => lzCount,
                 R => usefulBits);
with neg_count  select  extended_neg_count <= 
   "000000" when '0', 
   "111111" when '1', 
   "------" when others;
comp2_range_count<= extended_neg_count_d4 xor ("00" & lzCount_d1);
fraction<= usefulBits(13 downto 0);
partialExponent<= usefulBits(22 downto 14);
with s_d4  select  us_partialExponent<= 
   partialExponent when '0',
   not partialExponent when '1',
   "---------" when others;
exponent<= comp2_range_count & us_partialExponent;
biased_exponent<= exponent_d1 + 12289;
with is_not_zero  select   extended_is_not_zero <= 
   "000000000000000" when '0', 
   "111111111111111" when '1', 
   "---------------" when others;
final_biased_exponent<= extended_is_not_zero_d4 and biased_exponent;
round<= '0';
sticky<= '0';
O <= is_NAR_d4 & s_d5 & final_biased_exponent & implicit_bit_d4 & fraction_d1 & round_d5 & sticky_d5;
---------------------------- End of vhdl generation ----------------------------
end architecture;

--------------------------------------------------------------------------------
--                RightShifterSticky18_by_max_18_Freq600_uid14
-- VHDL generated for Kintex7 @ 600MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca (2008-2011), Florent de Dinechin (2008-2019)
--------------------------------------------------------------------------------
-- Pipeline depth: 4 cycles
-- Clock period (ns): 1.66667
-- Target frequency (MHz): 600
-- Input signals: X S padBit
-- Output signals: R Sticky

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity RightShifterSticky18_by_max_18_Freq600_uid14 is
    port (clk,enable : in std_logic;
          X : in  std_logic_vector(17 downto 0);
          S : in  std_logic_vector(4 downto 0);
          padBit : in  std_logic;
          R : out  std_logic_vector(17 downto 0);
          Sticky : out  std_logic   );
end entity;

architecture arch of RightShifterSticky18_by_max_18_Freq600_uid14 is
signal ps, ps_d1, ps_d2, ps_d3, ps_d4 :  std_logic_vector(4 downto 0);
signal Xpadded :  std_logic_vector(17 downto 0);
signal level5, level5_d1, level5_d2, level5_d3 :  std_logic_vector(17 downto 0);
signal stk4, stk4_d1 :  std_logic;
signal level4, level4_d1, level4_d2 :  std_logic_vector(17 downto 0);
signal stk3, stk3_d1 :  std_logic;
signal level3, level3_d1, level3_d2 :  std_logic_vector(17 downto 0);
signal stk2 :  std_logic;
signal level2, level2_d1, level2_d2 :  std_logic_vector(17 downto 0);
signal stk1, stk1_d1 :  std_logic;
signal level1, level1_d1, level1_d2, level1_d3 :  std_logic_vector(17 downto 0);
signal stk0 :  std_logic;
signal level0 :  std_logic_vector(17 downto 0);
signal padBit_d1, padBit_d2, padBit_d3 :  std_logic;
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            ps_d1 <=  ps;
            ps_d2 <=  ps_d1;
            ps_d3 <=  ps_d2;
            ps_d4 <=  ps_d3;
            level5_d1 <=  level5;
            level5_d2 <=  level5_d1;
            level5_d3 <=  level5_d2;
            stk4_d1 <=  stk4;
            level4_d1 <=  level4;
            level4_d2 <=  level4_d1;
            stk3_d1 <=  stk3;
            level3_d1 <=  level3;
            level3_d2 <=  level3_d1;
            level2_d1 <=  level2;
            level2_d2 <=  level2_d1;
            stk1_d1 <=  stk1;
            level1_d1 <=  level1;
            level1_d2 <=  level1_d1;
            level1_d3 <=  level1_d2;
            padBit_d1 <=  padBit;
            padBit_d2 <=  padBit_d1;
            padBit_d3 <=  padBit_d2;
         end if;
      end process;
   ps<= S;
   Xpadded <= X;
   level5<= Xpadded;
   stk4 <= '1' when (level5_d3(15 downto 0)/="0000000000000000" and ps_d1(4)='1')   else '0';
   level4 <=  level5_d2 when  ps(4)='0'    else (15 downto 0 => padBit_d2) & level5_d2(17 downto 16);
   stk3 <= '1' when (level4_d2(7 downto 0)/="00000000" and ps_d2(3)='1') or stk4_d1 ='1'   else '0';
   level3 <=  level4_d1 when  ps_d1(3)='0'    else (7 downto 0 => padBit_d3) & level4_d1(17 downto 8);
   stk2 <= '1' when (level3_d2(3 downto 0)/="0000" and ps_d3(2)='1') or stk3_d1 ='1'   else '0';
   level2 <=  level3 when  ps_d1(2)='0'    else (3 downto 0 => padBit_d3) & level3(17 downto 4);
   stk1 <= '1' when (level2_d2(1 downto 0)/="00" and ps_d3(1)='1') or stk2 ='1'   else '0';
   level1 <=  level2 when  ps_d1(1)='0'    else (1 downto 0 => padBit_d3) & level2(17 downto 2);
   stk0 <= '1' when (level1_d3(0 downto 0)/="0" and ps_d4(0)='1') or stk1_d1 ='1'   else '0';
   level0 <=  level1 when  ps_d1(0)='0'    else (0 downto 0 => padBit_d3) & level1(17 downto 1);
   R <= level0;
   Sticky <= stk0;
end architecture;

--------------------------------------------------------------------------------
--                    Normalizer_ZO_20_20_31_Freq600_uid16
-- VHDL generated for Kintex7 @ 600MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, (2007-2020)
--------------------------------------------------------------------------------
-- Pipeline depth: 5 cycles
-- Clock period (ns): 1.66667
-- Target frequency (MHz): 600
-- Input signals: X OZb
-- Output signals: Count R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Normalizer_ZO_20_20_31_Freq600_uid16 is
    port (clk,enable : in std_logic;
          X : in  std_logic_vector(19 downto 0);
          OZb : in  std_logic;
          Count : out  std_logic_vector(4 downto 0);
          R : out  std_logic_vector(19 downto 0)   );
end entity;

architecture arch of Normalizer_ZO_20_20_31_Freq600_uid16 is
signal level5, level5_d1 :  std_logic_vector(19 downto 0);
signal sozb, sozb_d1, sozb_d2, sozb_d3, sozb_d4, sozb_d5 :  std_logic;
signal count4, count4_d1, count4_d2, count4_d3, count4_d4 :  std_logic;
signal level4, level4_d1 :  std_logic_vector(19 downto 0);
signal count3, count3_d1, count3_d2, count3_d3 :  std_logic;
signal level3, level3_d1 :  std_logic_vector(19 downto 0);
signal count2, count2_d1, count2_d2 :  std_logic;
signal level2, level2_d1 :  std_logic_vector(19 downto 0);
signal count1, count1_d1 :  std_logic;
signal level1, level1_d1 :  std_logic_vector(19 downto 0);
signal count0 :  std_logic;
signal level0 :  std_logic_vector(19 downto 0);
signal sCount :  std_logic_vector(4 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            level5_d1 <=  level5;
            sozb_d1 <=  sozb;
            sozb_d2 <=  sozb_d1;
            sozb_d3 <=  sozb_d2;
            sozb_d4 <=  sozb_d3;
            sozb_d5 <=  sozb_d4;
            count4_d1 <=  count4;
            count4_d2 <=  count4_d1;
            count4_d3 <=  count4_d2;
            count4_d4 <=  count4_d3;
            level4_d1 <=  level4;
            count3_d1 <=  count3;
            count3_d2 <=  count3_d1;
            count3_d3 <=  count3_d2;
            level3_d1 <=  level3;
            count2_d1 <=  count2;
            count2_d2 <=  count2_d1;
            level2_d1 <=  level2;
            count1_d1 <=  count1;
            level1_d1 <=  level1;
         end if;
      end process;
   level5 <= X ;
   sozb<= OZb;
   count4<= '1' when level5_d1(19 downto 4) = (19 downto 4=>sozb_d1) else '0';
   level4<= level5_d1(19 downto 0) when count4='0' else level5_d1(3 downto 0) & (15 downto 0 => '0');

   count3<= '1' when level4_d1(19 downto 12) = (19 downto 12=>sozb_d2) else '0';
   level3<= level4_d1(19 downto 0) when count3='0' else level4_d1(11 downto 0) & (7 downto 0 => '0');

   count2<= '1' when level3_d1(19 downto 16) = (19 downto 16=>sozb_d3) else '0';
   level2<= level3_d1(19 downto 0) when count2='0' else level3_d1(15 downto 0) & (3 downto 0 => '0');

   count1<= '1' when level2_d1(19 downto 18) = (19 downto 18=>sozb_d4) else '0';
   level1<= level2_d1(19 downto 0) when count1='0' else level2_d1(17 downto 0) & (1 downto 0 => '0');

   count0<= '1' when level1_d1(19 downto 19) = (19 downto 19=>sozb_d5) else '0';
   level0<= level1_d1(19 downto 0) when count0='0' else level1_d1(18 downto 0) & (0 downto 0 => '0');

   R <= level0;
   sCount <= count4_d4 & count3_d3 & count2_d2 & count1_d1 & count0;
   Count <= sCount;
end architecture;

--------------------------------------------------------------------------------
--                         PIFAdd_15_14_Freq600_uid12
-- VHDL generated for Kintex7 @ 600MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Oregane Desrentes 2019
--------------------------------------------------------------------------------
-- Pipeline depth: 15 cycles
-- Clock period (ns): 1.66667
-- Target frequency (MHz): 600
-- Input signals: X Y
-- Output signals: R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PIFAdd_15_14_Freq600_uid12 is
    port (clk,enable : in std_logic;
          X : in  std_logic_vector(33 downto 0);
          Y : in  std_logic_vector(33 downto 0);
          R : out  std_logic_vector(33 downto 0)   );
end entity;

architecture arch of PIFAdd_15_14_Freq600_uid12 is
   component RightShifterSticky18_by_max_18_Freq600_uid14 is
      port ( clk,enable : in std_logic;
             X : in  std_logic_vector(17 downto 0);
             S : in  std_logic_vector(4 downto 0);
             padBit : in  std_logic;
             R : out  std_logic_vector(17 downto 0);
             Sticky : out  std_logic   );
   end component;

   component Normalizer_ZO_20_20_31_Freq600_uid16 is
      port ( clk,enable : in std_logic;
             X : in  std_logic_vector(19 downto 0);
             OZb : in  std_logic;
             Count : out  std_logic_vector(4 downto 0);
             R : out  std_logic_vector(19 downto 0)   );
   end component;

signal X_is_NAR :  std_logic;
signal X_s, X_s_d1 :  std_logic;
signal X_exponent, X_exponent_d1 :  std_logic_vector(14 downto 0);
signal X_fraction, X_fraction_d1 :  std_logic_vector(14 downto 0);
signal Y_is_NAR :  std_logic;
signal Y_s, Y_s_d1 :  std_logic;
signal Y_exponent, Y_exponent_d1 :  std_logic_vector(14 downto 0);
signal Y_fraction, Y_fraction_d1 :  std_logic_vector(14 downto 0);
signal is_larger_exp :  std_logic;
signal larger_exp, larger_exp_d1, larger_exp_d2, larger_exp_d3, larger_exp_d4, larger_exp_d5, larger_exp_d6, larger_exp_d7, larger_exp_d8, larger_exp_d9, larger_exp_d10, larger_exp_d11, larger_exp_d12, larger_exp_d13 :  std_logic_vector(14 downto 0);
signal smaller_exp, smaller_exp_d1 :  std_logic_vector(14 downto 0);
signal larger_mantissa, larger_mantissa_d1 :  std_logic_vector(15 downto 0);
signal smaller_mantissa :  std_logic_vector(15 downto 0);
signal larger_sign, larger_sign_d1 :  std_logic;
signal pad, pad_d1, pad_d2, pad_d3, pad_d4, pad_d5, pad_d6, pad_d7 :  std_logic;
signal offset, offset_d1 :  std_logic_vector(15 downto 0);
signal sup_offset, sup_offset_d1 :  std_logic_vector(10 downto 0);
signal saturate :  std_logic;
signal inf_offset :  std_logic_vector(4 downto 0);
signal input_shifter :  std_logic_vector(17 downto 0);
signal shifted_frac, shifted_frac_d1, shifted_frac_d2, shifted_frac_d3, shifted_frac_d4 :  std_logic_vector(17 downto 0);
signal sticky, sticky_d1 :  std_logic;
signal shifted_frac_trunc, shifted_frac_trunc_d1, shifted_frac_trunc_d2, shifted_frac_trunc_d3, shifted_frac_trunc_d4 :  std_logic_vector(16 downto 0);
signal padded_larger_mantissa, padded_larger_mantissa_d1, padded_larger_mantissa_d2, padded_larger_mantissa_d3, padded_larger_mantissa_d4, padded_larger_mantissa_d5, padded_larger_mantissa_d6 :  std_logic_vector(17 downto 0);
signal add_mantissa :  std_logic_vector(19 downto 0);
signal count_type, count_type_d1, count_type_d2, count_type_d3, count_type_d4, count_type_d5, count_type_d6, count_type_d7 :  std_logic;
signal lzCount, lzCount_d1 :  std_logic_vector(4 downto 0);
signal significand, significand_d1 :  std_logic_vector(19 downto 0);
signal exponent, exponent_d1 :  std_logic_vector(14 downto 0);
signal round, round_d1, round_d2 :  std_logic;
signal not_sticky, not_sticky_d1 :  std_logic;
signal pre_is_zero, pre_is_zero_d1 :  std_logic;
signal fraction, fraction_d1, fraction_d2 :  std_logic_vector(14 downto 0);
signal fraction_is_zero, fraction_is_zero_d1 :  std_logic;
signal is_zero :  std_logic;
signal s :  std_logic;
signal final_exponent :  std_logic_vector(14 downto 0);
signal is_NAR, is_NAR_d1, is_NAR_d2, is_NAR_d3, is_NAR_d4, is_NAR_d5, is_NAR_d6, is_NAR_d7, is_NAR_d8, is_NAR_d9, is_NAR_d10, is_NAR_d11, is_NAR_d12, is_NAR_d13, is_NAR_d14 :  std_logic;
signal X_d1 :  std_logic_vector(33 downto 0);
signal Y_d1 :  std_logic_vector(33 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            X_s_d1 <=  X_s;
            X_exponent_d1 <=  X_exponent;
            X_fraction_d1 <=  X_fraction;
            Y_s_d1 <=  Y_s;
            Y_exponent_d1 <=  Y_exponent;
            Y_fraction_d1 <=  Y_fraction;
            larger_exp_d1 <=  larger_exp;
            larger_exp_d2 <=  larger_exp_d1;
            larger_exp_d3 <=  larger_exp_d2;
            larger_exp_d4 <=  larger_exp_d3;
            larger_exp_d5 <=  larger_exp_d4;
            larger_exp_d6 <=  larger_exp_d5;
            larger_exp_d7 <=  larger_exp_d6;
            larger_exp_d8 <=  larger_exp_d7;
            larger_exp_d9 <=  larger_exp_d8;
            larger_exp_d10 <=  larger_exp_d9;
            larger_exp_d11 <=  larger_exp_d10;
            larger_exp_d12 <=  larger_exp_d11;
            larger_exp_d13 <=  larger_exp_d12;
            smaller_exp_d1 <=  smaller_exp;
            larger_mantissa_d1 <=  larger_mantissa;
            larger_sign_d1 <=  larger_sign;
            pad_d1 <=  pad;
            pad_d2 <=  pad_d1;
            pad_d3 <=  pad_d2;
            pad_d4 <=  pad_d3;
            pad_d5 <=  pad_d4;
            pad_d6 <=  pad_d5;
            pad_d7 <=  pad_d6;
            offset_d1 <=  offset;
            sup_offset_d1 <=  sup_offset;
            shifted_frac_d1 <=  shifted_frac;
            shifted_frac_d2 <=  shifted_frac_d1;
            shifted_frac_d3 <=  shifted_frac_d2;
            shifted_frac_d4 <=  shifted_frac_d3;
            sticky_d1 <=  sticky;
            shifted_frac_trunc_d1 <=  shifted_frac_trunc;
            shifted_frac_trunc_d2 <=  shifted_frac_trunc_d1;
            shifted_frac_trunc_d3 <=  shifted_frac_trunc_d2;
            shifted_frac_trunc_d4 <=  shifted_frac_trunc_d3;
            padded_larger_mantissa_d1 <=  padded_larger_mantissa;
            padded_larger_mantissa_d2 <=  padded_larger_mantissa_d1;
            padded_larger_mantissa_d3 <=  padded_larger_mantissa_d2;
            padded_larger_mantissa_d4 <=  padded_larger_mantissa_d3;
            padded_larger_mantissa_d5 <=  padded_larger_mantissa_d4;
            padded_larger_mantissa_d6 <=  padded_larger_mantissa_d5;
            count_type_d1 <=  count_type;
            count_type_d2 <=  count_type_d1;
            count_type_d3 <=  count_type_d2;
            count_type_d4 <=  count_type_d3;
            count_type_d5 <=  count_type_d4;
            count_type_d6 <=  count_type_d5;
            count_type_d7 <=  count_type_d6;
            lzCount_d1 <=  lzCount;
            significand_d1 <=  significand;
            exponent_d1 <=  exponent;
            round_d1 <=  round;
            round_d2 <=  round_d1;
            not_sticky_d1 <=  not_sticky;
            pre_is_zero_d1 <=  pre_is_zero;
            fraction_d1 <=  fraction;
            fraction_d2 <=  fraction_d1;
            fraction_is_zero_d1 <=  fraction_is_zero;
            is_NAR_d1 <=  is_NAR;
            is_NAR_d2 <=  is_NAR_d1;
            is_NAR_d3 <=  is_NAR_d2;
            is_NAR_d4 <=  is_NAR_d3;
            is_NAR_d5 <=  is_NAR_d4;
            is_NAR_d6 <=  is_NAR_d5;
            is_NAR_d7 <=  is_NAR_d6;
            is_NAR_d8 <=  is_NAR_d7;
            is_NAR_d9 <=  is_NAR_d8;
            is_NAR_d10 <=  is_NAR_d9;
            is_NAR_d11 <=  is_NAR_d10;
            is_NAR_d12 <=  is_NAR_d11;
            is_NAR_d13 <=  is_NAR_d12;
            is_NAR_d14 <=  is_NAR_d13;
            X_d1 <=  X;
            Y_d1 <=  Y;
         end if;
      end process;
--------------------------- Start of vhdl generation ---------------------------
X_is_NAR<= X(33);
X_s<= X(32);
X_exponent<= X(31 downto 17);
X_fraction<= X(16 downto 2);
Y_is_NAR<= Y(33);
Y_s<= Y(32);
Y_exponent<= Y(31 downto 17);
Y_fraction<= Y(16 downto 2);
is_larger_exp<= '1' when X_exponent_d1 > Y_exponent_d1 else '0';
with is_larger_exp  select  larger_exp<= 
   X_exponent_d1 when '1',
   Y_exponent_d1 when '0',
   "---------------" when others;
with is_larger_exp  select  smaller_exp<= 
   Y_exponent_d1 when '1',
   X_exponent_d1 when '0',
   "---------------" when others;
with is_larger_exp  select  larger_mantissa<= 
   X_s_d1 & X_fraction_d1 when '1',
   Y_s_d1 & Y_fraction_d1 when '0',
   "----------------" when others;
with is_larger_exp  select  smaller_mantissa<= 
   Y_s_d1 & Y_fraction_d1 when '1',
   X_s_d1 & X_fraction_d1 when '0',
   "----------------" when others;
with is_larger_exp  select  larger_sign<= 
   X_s_d1 when '1',
   Y_s_d1 when '0',
   '-' when others;
with is_larger_exp  select  pad<= 
   Y_s_d1 when '1',
   X_s_d1 when '0',
   '-' when others;
offset <= ('0' & larger_exp_d1) - ('0' & smaller_exp_d1);
sup_offset <= offset(15 downto 5);
saturate <= '0' when sup_offset_d1 = "00000000000" else '1';
with saturate  select  inf_offset<=
   "11111" when '1',
   offset_d1(4 downto 0) when '0',
   "-----" when others;
input_shifter <= smaller_mantissa & "00";
   mantissa_shift: RightShifterSticky18_by_max_18_Freq600_uid14
      port map ( clk  => clk,
                 enable => enable,
                 S => inf_offset,
                 X => input_shifter,
                 padBit => pad,
                 R => shifted_frac,
                 Sticky => sticky);
shifted_frac_trunc<= shifted_frac(17 downto 1);
with larger_sign_d1  select  padded_larger_mantissa<= 
   "0" & larger_mantissa_d1 & '0' when '0',
   "1" & larger_mantissa_d1 & '0' when '1',
   "------------------" when others;
add_mantissa<= ((padded_larger_mantissa_d6) + (pad_d7 & shifted_frac_trunc_d4)) & shifted_frac_d4(0) & sticky_d1;
count_type<= add_mantissa(19);
   norm: Normalizer_ZO_20_20_31_Freq600_uid16
      port map ( clk  => clk,
                 enable => enable,
                 OZb => count_type,
                 X => add_mantissa,
                 Count => lzCount,
                 R => significand);
exponent <= larger_exp_d13 + 2 - lzCount_d1;
round<= significand(4);
not_sticky<= '1' when significand_d1(3 downto 0) = "0000" else '0';
pre_is_zero<= (not round_d1) or (not_sticky and round_d1);
fraction<= significand(19 downto 5);
fraction_is_zero<= '1' when fraction_d1 = "000000000000000" else '0';
is_zero<= not count_type_d7 and fraction_is_zero_d1 and pre_is_zero_d1;
with is_zero  select  s<= 
   '0' when '1',
   not fraction_d2(14) when '0',
   '-' when others;
with is_zero  select  final_exponent<= 
   "000000000000000" when '1',
   exponent_d1 when '0',
   "000000000000000" when others;
is_NAR <= X_d1(33) or Y_d1(33);
R <= is_NAR_d14 & s & final_exponent & fraction_d2 & round_d2 & (not not_sticky_d1);
end architecture;

--------------------------------------------------------------------------------
--                RightShifterSticky26_by_max_26_Freq600_uid20
-- VHDL generated for Kintex7 @ 600MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca (2008-2011), Florent de Dinechin (2008-2019)
--------------------------------------------------------------------------------
-- Pipeline depth: 4 cycles
-- Clock period (ns): 1.66667
-- Target frequency (MHz): 600
-- Input signals: X S padBit
-- Output signals: R Sticky

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity RightShifterSticky26_by_max_26_Freq600_uid20 is
    port (clk,enable : in std_logic;
          X : in  std_logic_vector(25 downto 0);
          S : in  std_logic_vector(4 downto 0);
          padBit : in  std_logic;
          R : out  std_logic_vector(25 downto 0);
          Sticky : out  std_logic   );
end entity;

architecture arch of RightShifterSticky26_by_max_26_Freq600_uid20 is
signal ps, ps_d1, ps_d2, ps_d3, ps_d4, ps_d5 :  std_logic_vector(4 downto 0);
signal Xpadded :  std_logic_vector(25 downto 0);
signal level5, level5_d1 :  std_logic_vector(25 downto 0);
signal stk4 :  std_logic;
signal level4, level4_d1 :  std_logic_vector(25 downto 0);
signal stk3, stk3_d1 :  std_logic;
signal level3, level3_d1, level3_d2 :  std_logic_vector(25 downto 0);
signal stk2, stk2_d1 :  std_logic;
signal level2, level2_d1, level2_d2, level2_d3 :  std_logic_vector(25 downto 0);
signal stk1, stk1_d1 :  std_logic;
signal level1, level1_d1, level1_d2, level1_d3 :  std_logic_vector(25 downto 0);
signal stk0 :  std_logic;
signal level0 :  std_logic_vector(25 downto 0);
signal padBit_d1, padBit_d2 :  std_logic;
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            ps_d1 <=  ps;
            ps_d2 <=  ps_d1;
            ps_d3 <=  ps_d2;
            ps_d4 <=  ps_d3;
            ps_d5 <=  ps_d4;
            level5_d1 <=  level5;
            level4_d1 <=  level4;
            stk3_d1 <=  stk3;
            level3_d1 <=  level3;
            level3_d2 <=  level3_d1;
            stk2_d1 <=  stk2;
            level2_d1 <=  level2;
            level2_d2 <=  level2_d1;
            level2_d3 <=  level2_d2;
            stk1_d1 <=  stk1;
            level1_d1 <=  level1;
            level1_d2 <=  level1_d1;
            level1_d3 <=  level1_d2;
            padBit_d1 <=  padBit;
            padBit_d2 <=  padBit_d1;
         end if;
      end process;
   ps<= S;
   Xpadded <= X;
   level5<= Xpadded;
   stk4 <= '1' when (level5_d1(15 downto 0)/="0000000000000000" and ps_d2(4)='1')   else '0';
   level4 <=  level5 when  ps_d1(4)='0'    else (15 downto 0 => padBit_d1) & level5(25 downto 16);
   stk3 <= '1' when (level4_d1(7 downto 0)/="00000000" and ps_d2(3)='1') or stk4 ='1'   else '0';
   level3 <=  level4 when  ps_d1(3)='0'    else (7 downto 0 => padBit_d1) & level4(25 downto 8);
   stk2 <= '1' when (level3_d2(3 downto 0)/="0000" and ps_d3(2)='1') or stk3_d1 ='1'   else '0';
   level2 <=  level3 when  ps_d1(2)='0'    else (3 downto 0 => padBit_d1) & level3(25 downto 4);
   stk1 <= '1' when (level2_d3(1 downto 0)/="00" and ps_d4(1)='1') or stk2_d1 ='1'   else '0';
   level1 <=  level2_d1 when  ps_d2(1)='0'    else (1 downto 0 => padBit_d2) & level2_d1(25 downto 2);
   stk0 <= '1' when (level1_d3(0 downto 0)/="0" and ps_d5(0)='1') or stk1_d1 ='1'   else '0';
   level0 <=  level1 when  ps_d2(0)='0'    else (0 downto 0 => padBit_d2) & level1(25 downto 1);
   R <= level0;
   Sticky <= stk0;
end architecture;

--------------------------------------------------------------------------------
--                        PIF2Posit_26_9_Freq600_uid18
-- VHDL generated for Kintex7 @ 600MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Oregane Desrentes 2019
--------------------------------------------------------------------------------
-- Pipeline depth: 7 cycles
-- Clock period (ns): 1.66667
-- Target frequency (MHz): 600
-- Input signals: I
-- Output signals: O

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PIF2Posit_26_9_Freq600_uid18 is
    port (clk,enable : in std_logic;
          I : in  std_logic_vector(33 downto 0);
          O : out  std_logic_vector(25 downto 0)   );
end entity;

architecture arch of PIF2Posit_26_9_Freq600_uid18 is
   component RightShifterSticky26_by_max_26_Freq600_uid20 is
      port ( clk,enable : in std_logic;
             X : in  std_logic_vector(25 downto 0);
             S : in  std_logic_vector(4 downto 0);
             padBit : in  std_logic;
             R : out  std_logic_vector(25 downto 0);
             Sticky : out  std_logic   );
   end component;

signal is_NAR, is_NAR_d1, is_NAR_d2, is_NAR_d3, is_NAR_d4, is_NAR_d5, is_NAR_d6, is_NAR_d7 :  std_logic;
signal s, s_d1, s_d2, s_d3, s_d4, s_d5, s_d6, s_d7 :  std_logic;
signal biased_exponent, biased_exponent_d1 :  std_logic_vector(14 downto 0);
signal fraction, fraction_d1, fraction_d2 :  std_logic_vector(14 downto 0);
signal is_zero, is_zero_d1, is_zero_d2, is_zero_d3, is_zero_d4, is_zero_d5, is_zero_d6 :  std_logic;
signal exponent :  std_logic_vector(14 downto 0);
signal partial_exponent :  std_logic_vector(8 downto 0);
signal partial_exponent_us, partial_exponent_us_d1 :  std_logic_vector(8 downto 0);
signal bin_regime :  std_logic_vector(4 downto 0);
signal first_regime :  std_logic;
signal regime :  std_logic_vector(4 downto 0);
signal pad, pad_d1 :  std_logic;
signal start_regime :  std_logic_vector(1 downto 0);
signal input_shifter :  std_logic_vector(25 downto 0);
signal extended_posit :  std_logic_vector(25 downto 0);
signal pre_sticky :  std_logic;
signal truncated_posit, truncated_posit_d1, truncated_posit_d2, truncated_posit_d3, truncated_posit_d4 :  std_logic_vector(24 downto 0);
signal lsb, lsb_d1, lsb_d2, lsb_d3 :  std_logic;
signal guard, guard_d1, guard_d2, guard_d3 :  std_logic;
signal sticky :  std_logic;
signal round_bit, round_bit_d1 :  std_logic;
signal rounded_reg_exp_frac :  std_logic_vector(24 downto 0);
signal rounded_posit :  std_logic_vector(25 downto 0);
signal rounded_posit_zero :  std_logic_vector(25 downto 0);
signal I_d1, I_d2, I_d3, I_d4, I_d5, I_d6 :  std_logic_vector(33 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            is_NAR_d1 <=  is_NAR;
            is_NAR_d2 <=  is_NAR_d1;
            is_NAR_d3 <=  is_NAR_d2;
            is_NAR_d4 <=  is_NAR_d3;
            is_NAR_d5 <=  is_NAR_d4;
            is_NAR_d6 <=  is_NAR_d5;
            is_NAR_d7 <=  is_NAR_d6;
            s_d1 <=  s;
            s_d2 <=  s_d1;
            s_d3 <=  s_d2;
            s_d4 <=  s_d3;
            s_d5 <=  s_d4;
            s_d6 <=  s_d5;
            s_d7 <=  s_d6;
            biased_exponent_d1 <=  biased_exponent;
            fraction_d1 <=  fraction;
            fraction_d2 <=  fraction_d1;
            is_zero_d1 <=  is_zero;
            is_zero_d2 <=  is_zero_d1;
            is_zero_d3 <=  is_zero_d2;
            is_zero_d4 <=  is_zero_d3;
            is_zero_d5 <=  is_zero_d4;
            is_zero_d6 <=  is_zero_d5;
            partial_exponent_us_d1 <=  partial_exponent_us;
            pad_d1 <=  pad;
            truncated_posit_d1 <=  truncated_posit;
            truncated_posit_d2 <=  truncated_posit_d1;
            truncated_posit_d3 <=  truncated_posit_d2;
            truncated_posit_d4 <=  truncated_posit_d3;
            lsb_d1 <=  lsb;
            lsb_d2 <=  lsb_d1;
            lsb_d3 <=  lsb_d2;
            guard_d1 <=  guard;
            guard_d2 <=  guard_d1;
            guard_d3 <=  guard_d2;
            round_bit_d1 <=  round_bit;
            I_d1 <=  I;
            I_d2 <=  I_d1;
            I_d3 <=  I_d2;
            I_d4 <=  I_d3;
            I_d5 <=  I_d4;
            I_d6 <=  I_d5;
         end if;
      end process;
--------------------------- Start of vhdl generation ---------------------------
is_NAR<= I(33);
s<= I(32);
biased_exponent<= I(31 downto 17);
fraction<= I(15 downto 1);
is_zero<= '1' when I_d1(33 downto 0) = "0000000000000000000000000000000000" else '0';
exponent<= biased_exponent_d1 - 12289;
partial_exponent<= exponent(8 downto 0);
with s_d1  select  partial_exponent_us <= 
   partial_exponent when '0',
   not partial_exponent when '1',
   "---------" when others;
bin_regime<= exponent(13 downto 9);
first_regime<= exponent(14);
with first_regime  select  regime <= 
   bin_regime when '0', 
   not bin_regime when '1', 
   "-----" when others;
pad<= not(first_regime xor s_d1);
with pad_d1  select  start_regime <= 
   "01" when '0', 
   "10" when '1', 
   "--" when others;
input_shifter<= start_regime & partial_exponent_us_d1 & fraction_d2;
   rshift: RightShifterSticky26_by_max_26_Freq600_uid20
      port map ( clk  => clk,
                 enable => enable,
                 S => regime,
                 X => input_shifter,
                 padBit => pad,
                 R => extended_posit,
                 Sticky => pre_sticky);
truncated_posit<= extended_posit(25 downto 1);
lsb<= extended_posit(1);
guard<= extended_posit(0);
sticky<= I_d6(0) or pre_sticky;
round_bit<= guard_d3 and (sticky or lsb_d3);
rounded_reg_exp_frac<= truncated_posit_d4 + round_bit_d1;
rounded_posit<= s_d7 & rounded_reg_exp_frac;
rounded_posit_zero<= rounded_posit when is_zero_d6= '0' else "00000000000000000000000000";
O <= rounded_posit_zero when is_NAR_d7 = '0' else "10000000000000000000000000";
---------------------------- End of vhdl generation ----------------------------
end architecture;

--------------------------------------------------------------------------------
--                         PositAdd_26_9_Freq600_uid2
-- VHDL generated for Kintex7 @ 600MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Oregane Desrentes 2019
--------------------------------------------------------------------------------
-- Pipeline depth: 27 cycles
-- Clock period (ns): 1.66667
-- Target frequency (MHz): 600
-- Input signals: X Y
-- Output signals: R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PositAdd_26_9_Freq600_uid2 is
    port (clk,enable : in std_logic;
          X : in  std_logic_vector(25 downto 0);
          Y : in  std_logic_vector(25 downto 0);
          R : out  std_logic_vector(25 downto 0)   );
end entity;

architecture arch of PositAdd_26_9_Freq600_uid2 is
   component Posit2PIF_26_9_Freq600_uid4 is
      port ( clk,enable : in std_logic;
             I : in  std_logic_vector(25 downto 0);
             O : out  std_logic_vector(33 downto 0)   );
   end component;

   component Posit2PIF_26_9_Freq600_uid8 is
      port ( clk,enable : in std_logic;
             I : in  std_logic_vector(25 downto 0);
             O : out  std_logic_vector(33 downto 0)   );
   end component;

   component PIFAdd_15_14_Freq600_uid12 is
      port ( clk,enable : in std_logic;
             X : in  std_logic_vector(33 downto 0);
             Y : in  std_logic_vector(33 downto 0);
             R : out  std_logic_vector(33 downto 0)   );
   end component;

   component PIF2Posit_26_9_Freq600_uid18 is
      port ( clk,enable : in std_logic;
             I : in  std_logic_vector(33 downto 0);
             O : out  std_logic_vector(25 downto 0)   );
   end component;

signal X_PIF :  std_logic_vector(33 downto 0);
signal Y_PIF :  std_logic_vector(33 downto 0);
signal R_PIF :  std_logic_vector(33 downto 0);
begin
--------------------------- Start of vhdl generation ---------------------------
   X_conversion: Posit2PIF_26_9_Freq600_uid4
      port map ( clk  => clk,
                 enable => enable,
                 I => X,
                 O => X_PIF);
   Y_conversion: Posit2PIF_26_9_Freq600_uid8
      port map ( clk  => clk,
                 enable => enable,
                 I => Y,
                 O => Y_PIF);
   Addition: PIFAdd_15_14_Freq600_uid12
      port map ( clk  => clk,
                 enable => enable,
                 X => X_PIF,
                 Y => Y_PIF,
                 R => R_PIF);
   R_conversion: PIF2Posit_26_9_Freq600_uid18
      port map ( clk  => clk,
                 enable => enable,
                 I => R_PIF,
                 O => R);
---------------------------- End of vhdl generation ----------------------------
end architecture;

