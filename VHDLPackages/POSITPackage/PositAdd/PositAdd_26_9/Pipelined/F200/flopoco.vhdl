--------------------------------------------------------------------------------
--                    Normalizer_ZO_24_24_15_Freq200_uid6
-- VHDL generated for Kintex7 @ 200MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, (2007-2020)
--------------------------------------------------------------------------------
-- Pipeline depth: 1 cycles
-- Clock period (ns): 5
-- Target frequency (MHz): 200
-- Input signals: X OZb
-- Output signals: Count R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Normalizer_ZO_24_24_15_Freq200_uid6 is
    port (clk,enable : in std_logic;
          X : in  std_logic_vector(23 downto 0);
          OZb : in  std_logic;
          Count : out  std_logic_vector(3 downto 0);
          R : out  std_logic_vector(23 downto 0)   );
end entity;

architecture arch of Normalizer_ZO_24_24_15_Freq200_uid6 is
signal level4 :  std_logic_vector(23 downto 0);
signal sozb, sozb_d1 :  std_logic;
signal count3, count3_d1 :  std_logic;
signal level3 :  std_logic_vector(23 downto 0);
signal count2, count2_d1 :  std_logic;
signal level2 :  std_logic_vector(23 downto 0);
signal count1, count1_d1 :  std_logic;
signal level1, level1_d1 :  std_logic_vector(23 downto 0);
signal count0 :  std_logic;
signal level0 :  std_logic_vector(23 downto 0);
signal sCount :  std_logic_vector(3 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            sozb_d1 <=  sozb;
            count3_d1 <=  count3;
            count2_d1 <=  count2;
            count1_d1 <=  count1;
            level1_d1 <=  level1;
         end if;
      end process;
   level4 <= X ;
   sozb<= OZb;
   count3<= '1' when level4(23 downto 16) = (23 downto 16=>sozb) else '0';
   level3<= level4(23 downto 0) when count3='0' else level4(15 downto 0) & (7 downto 0 => '0');

   count2<= '1' when level3(23 downto 20) = (23 downto 20=>sozb) else '0';
   level2<= level3(23 downto 0) when count2='0' else level3(19 downto 0) & (3 downto 0 => '0');

   count1<= '1' when level2(23 downto 22) = (23 downto 22=>sozb) else '0';
   level1<= level2(23 downto 0) when count1='0' else level2(21 downto 0) & (1 downto 0 => '0');

   count0<= '1' when level1_d1(23 downto 23) = (23 downto 23=>sozb_d1) else '0';
   level0<= level1_d1(23 downto 0) when count0='0' else level1_d1(22 downto 0) & (0 downto 0 => '0');

   R <= level0;
   sCount <= count3_d1 & count2_d1 & count1_d1 & count0;
   Count <= sCount;
end architecture;

--------------------------------------------------------------------------------
--                        Posit2PIF_26_9_Freq200_uid4
-- VHDL generated for Kintex7 @ 200MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Oregane Desrentes 2019
--------------------------------------------------------------------------------
-- Pipeline depth: 1 cycles
-- Clock period (ns): 5
-- Target frequency (MHz): 200
-- Input signals: I
-- Output signals: O

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Posit2PIF_26_9_Freq200_uid4 is
    port (clk,enable : in std_logic;
          I : in  std_logic_vector(25 downto 0);
          O : out  std_logic_vector(33 downto 0)   );
end entity;

architecture arch of Posit2PIF_26_9_Freq200_uid4 is
   component Normalizer_ZO_24_24_15_Freq200_uid6 is
      port ( clk,enable : in std_logic;
             X : in  std_logic_vector(23 downto 0);
             OZb : in  std_logic;
             Count : out  std_logic_vector(3 downto 0);
             R : out  std_logic_vector(23 downto 0)   );
   end component;

signal s, s_d1 :  std_logic;
signal count_type :  std_logic;
signal remainder :  std_logic_vector(23 downto 0);
signal not_s :  std_logic;
signal zero_NAR :  std_logic;
signal is_NAR, is_NAR_d1 :  std_logic;
signal is_not_zero :  std_logic;
signal implicit_bit, implicit_bit_d1 :  std_logic;
signal neg_count :  std_logic;
signal lzCount :  std_logic_vector(3 downto 0);
signal usefulBits :  std_logic_vector(23 downto 0);
signal extended_neg_count, extended_neg_count_d1 :  std_logic_vector(5 downto 0);
signal comp2_range_count :  std_logic_vector(5 downto 0);
signal fraction :  std_logic_vector(13 downto 0);
signal partialExponent :  std_logic_vector(8 downto 0);
signal us_partialExponent :  std_logic_vector(8 downto 0);
signal exponent :  std_logic_vector(14 downto 0);
signal biased_exponent :  std_logic_vector(14 downto 0);
signal extended_is_not_zero, extended_is_not_zero_d1 :  std_logic_vector(14 downto 0);
signal final_biased_exponent :  std_logic_vector(14 downto 0);
signal round, round_d1 :  std_logic;
signal sticky, sticky_d1 :  std_logic;
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            s_d1 <=  s;
            is_NAR_d1 <=  is_NAR;
            implicit_bit_d1 <=  implicit_bit;
            extended_neg_count_d1 <=  extended_neg_count;
            extended_is_not_zero_d1 <=  extended_is_not_zero;
            round_d1 <=  round;
            sticky_d1 <=  sticky;
         end if;
      end process;
--------------------------- Start of vhdl generation ---------------------------
s<= I(25);
count_type<= I(24);
remainder<= I(23 downto 0);
not_s<= not s;
zero_NAR <= not count_type when remainder="000000000000000000000000" else '0';
is_NAR<= zero_NAR and s;
is_not_zero<= not(zero_NAR and not_s);
implicit_bit<= is_not_zero and not_s;
neg_count<= not (s xor count_type);
   lzoc: Normalizer_ZO_24_24_15_Freq200_uid6
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
comp2_range_count<= extended_neg_count_d1 xor ("00" & lzCount);
fraction<= usefulBits(13 downto 0);
partialExponent<= usefulBits(22 downto 14);
with s_d1  select  us_partialExponent<= 
   partialExponent when '0',
   not partialExponent when '1',
   "---------" when others;
exponent<= comp2_range_count & us_partialExponent;
biased_exponent<= exponent + 12289;
with is_not_zero  select   extended_is_not_zero <= 
   "000000000000000" when '0', 
   "111111111111111" when '1', 
   "---------------" when others;
final_biased_exponent<= extended_is_not_zero_d1 and biased_exponent;
round<= '0';
sticky<= '0';
O <= is_NAR_d1 & s_d1 & final_biased_exponent & implicit_bit_d1 & fraction & round_d1 & sticky_d1;
---------------------------- End of vhdl generation ----------------------------
end architecture;

--------------------------------------------------------------------------------
--                    Normalizer_ZO_24_24_15_Freq200_uid10
-- VHDL generated for Kintex7 @ 200MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, (2007-2020)
--------------------------------------------------------------------------------
-- Pipeline depth: 1 cycles
-- Clock period (ns): 5
-- Target frequency (MHz): 200
-- Input signals: X OZb
-- Output signals: Count R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Normalizer_ZO_24_24_15_Freq200_uid10 is
    port (clk,enable : in std_logic;
          X : in  std_logic_vector(23 downto 0);
          OZb : in  std_logic;
          Count : out  std_logic_vector(3 downto 0);
          R : out  std_logic_vector(23 downto 0)   );
end entity;

architecture arch of Normalizer_ZO_24_24_15_Freq200_uid10 is
signal level4 :  std_logic_vector(23 downto 0);
signal sozb, sozb_d1 :  std_logic;
signal count3, count3_d1 :  std_logic;
signal level3 :  std_logic_vector(23 downto 0);
signal count2, count2_d1 :  std_logic;
signal level2 :  std_logic_vector(23 downto 0);
signal count1, count1_d1 :  std_logic;
signal level1, level1_d1 :  std_logic_vector(23 downto 0);
signal count0 :  std_logic;
signal level0 :  std_logic_vector(23 downto 0);
signal sCount :  std_logic_vector(3 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            sozb_d1 <=  sozb;
            count3_d1 <=  count3;
            count2_d1 <=  count2;
            count1_d1 <=  count1;
            level1_d1 <=  level1;
         end if;
      end process;
   level4 <= X ;
   sozb<= OZb;
   count3<= '1' when level4(23 downto 16) = (23 downto 16=>sozb) else '0';
   level3<= level4(23 downto 0) when count3='0' else level4(15 downto 0) & (7 downto 0 => '0');

   count2<= '1' when level3(23 downto 20) = (23 downto 20=>sozb) else '0';
   level2<= level3(23 downto 0) when count2='0' else level3(19 downto 0) & (3 downto 0 => '0');

   count1<= '1' when level2(23 downto 22) = (23 downto 22=>sozb) else '0';
   level1<= level2(23 downto 0) when count1='0' else level2(21 downto 0) & (1 downto 0 => '0');

   count0<= '1' when level1_d1(23 downto 23) = (23 downto 23=>sozb_d1) else '0';
   level0<= level1_d1(23 downto 0) when count0='0' else level1_d1(22 downto 0) & (0 downto 0 => '0');

   R <= level0;
   sCount <= count3_d1 & count2_d1 & count1_d1 & count0;
   Count <= sCount;
end architecture;

--------------------------------------------------------------------------------
--                        Posit2PIF_26_9_Freq200_uid8
-- VHDL generated for Kintex7 @ 200MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Oregane Desrentes 2019
--------------------------------------------------------------------------------
-- Pipeline depth: 1 cycles
-- Clock period (ns): 5
-- Target frequency (MHz): 200
-- Input signals: I
-- Output signals: O

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Posit2PIF_26_9_Freq200_uid8 is
    port (clk,enable : in std_logic;
          I : in  std_logic_vector(25 downto 0);
          O : out  std_logic_vector(33 downto 0)   );
end entity;

architecture arch of Posit2PIF_26_9_Freq200_uid8 is
   component Normalizer_ZO_24_24_15_Freq200_uid10 is
      port ( clk,enable : in std_logic;
             X : in  std_logic_vector(23 downto 0);
             OZb : in  std_logic;
             Count : out  std_logic_vector(3 downto 0);
             R : out  std_logic_vector(23 downto 0)   );
   end component;

signal s, s_d1 :  std_logic;
signal count_type :  std_logic;
signal remainder :  std_logic_vector(23 downto 0);
signal not_s :  std_logic;
signal zero_NAR :  std_logic;
signal is_NAR, is_NAR_d1 :  std_logic;
signal is_not_zero :  std_logic;
signal implicit_bit, implicit_bit_d1 :  std_logic;
signal neg_count :  std_logic;
signal lzCount :  std_logic_vector(3 downto 0);
signal usefulBits :  std_logic_vector(23 downto 0);
signal extended_neg_count, extended_neg_count_d1 :  std_logic_vector(5 downto 0);
signal comp2_range_count :  std_logic_vector(5 downto 0);
signal fraction :  std_logic_vector(13 downto 0);
signal partialExponent :  std_logic_vector(8 downto 0);
signal us_partialExponent :  std_logic_vector(8 downto 0);
signal exponent :  std_logic_vector(14 downto 0);
signal biased_exponent :  std_logic_vector(14 downto 0);
signal extended_is_not_zero, extended_is_not_zero_d1 :  std_logic_vector(14 downto 0);
signal final_biased_exponent :  std_logic_vector(14 downto 0);
signal round, round_d1 :  std_logic;
signal sticky, sticky_d1 :  std_logic;
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            s_d1 <=  s;
            is_NAR_d1 <=  is_NAR;
            implicit_bit_d1 <=  implicit_bit;
            extended_neg_count_d1 <=  extended_neg_count;
            extended_is_not_zero_d1 <=  extended_is_not_zero;
            round_d1 <=  round;
            sticky_d1 <=  sticky;
         end if;
      end process;
--------------------------- Start of vhdl generation ---------------------------
s<= I(25);
count_type<= I(24);
remainder<= I(23 downto 0);
not_s<= not s;
zero_NAR <= not count_type when remainder="000000000000000000000000" else '0';
is_NAR<= zero_NAR and s;
is_not_zero<= not(zero_NAR and not_s);
implicit_bit<= is_not_zero and not_s;
neg_count<= not (s xor count_type);
   lzoc: Normalizer_ZO_24_24_15_Freq200_uid10
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
comp2_range_count<= extended_neg_count_d1 xor ("00" & lzCount);
fraction<= usefulBits(13 downto 0);
partialExponent<= usefulBits(22 downto 14);
with s_d1  select  us_partialExponent<= 
   partialExponent when '0',
   not partialExponent when '1',
   "---------" when others;
exponent<= comp2_range_count & us_partialExponent;
biased_exponent<= exponent + 12289;
with is_not_zero  select   extended_is_not_zero <= 
   "000000000000000" when '0', 
   "111111111111111" when '1', 
   "---------------" when others;
final_biased_exponent<= extended_is_not_zero_d1 and biased_exponent;
round<= '0';
sticky<= '0';
O <= is_NAR_d1 & s_d1 & final_biased_exponent & implicit_bit_d1 & fraction & round_d1 & sticky_d1;
---------------------------- End of vhdl generation ----------------------------
end architecture;

--------------------------------------------------------------------------------
--                RightShifterSticky18_by_max_18_Freq200_uid14
-- VHDL generated for Kintex7 @ 200MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca (2008-2011), Florent de Dinechin (2008-2019)
--------------------------------------------------------------------------------
-- Pipeline depth: 1 cycles
-- Clock period (ns): 5
-- Target frequency (MHz): 200
-- Input signals: X S padBit
-- Output signals: R Sticky

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity RightShifterSticky18_by_max_18_Freq200_uid14 is
    port (clk,enable : in std_logic;
          X : in  std_logic_vector(17 downto 0);
          S : in  std_logic_vector(4 downto 0);
          padBit : in  std_logic;
          R : out  std_logic_vector(17 downto 0);
          Sticky : out  std_logic   );
end entity;

architecture arch of RightShifterSticky18_by_max_18_Freq200_uid14 is
signal ps, ps_d1 :  std_logic_vector(4 downto 0);
signal Xpadded :  std_logic_vector(17 downto 0);
signal level5 :  std_logic_vector(17 downto 0);
signal stk4, stk4_d1 :  std_logic;
signal level4, level4_d1 :  std_logic_vector(17 downto 0);
signal stk3 :  std_logic;
signal level3, level3_d1 :  std_logic_vector(17 downto 0);
signal stk2 :  std_logic;
signal level2, level2_d1 :  std_logic_vector(17 downto 0);
signal stk1 :  std_logic;
signal level1, level1_d1 :  std_logic_vector(17 downto 0);
signal stk0 :  std_logic;
signal level0 :  std_logic_vector(17 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            ps_d1 <=  ps;
            stk4_d1 <=  stk4;
            level4_d1 <=  level4;
            level3_d1 <=  level3;
            level2_d1 <=  level2;
            level1_d1 <=  level1;
         end if;
      end process;
   ps<= S;
   Xpadded <= X;
   level5<= Xpadded;
   stk4 <= '1' when (level5(15 downto 0)/="0000000000000000" and ps(4)='1')   else '0';
   level4 <=  level5 when  ps(4)='0'    else (15 downto 0 => padBit) & level5(17 downto 16);
   stk3 <= '1' when (level4_d1(7 downto 0)/="00000000" and ps_d1(3)='1') or stk4_d1 ='1'   else '0';
   level3 <=  level4 when  ps(3)='0'    else (7 downto 0 => padBit) & level4(17 downto 8);
   stk2 <= '1' when (level3_d1(3 downto 0)/="0000" and ps_d1(2)='1') or stk3 ='1'   else '0';
   level2 <=  level3 when  ps(2)='0'    else (3 downto 0 => padBit) & level3(17 downto 4);
   stk1 <= '1' when (level2_d1(1 downto 0)/="00" and ps_d1(1)='1') or stk2 ='1'   else '0';
   level1 <=  level2 when  ps(1)='0'    else (1 downto 0 => padBit) & level2(17 downto 2);
   stk0 <= '1' when (level1_d1(0 downto 0)/="0" and ps_d1(0)='1') or stk1 ='1'   else '0';
   level0 <=  level1 when  ps(0)='0'    else (0 downto 0 => padBit) & level1(17 downto 1);
   R <= level0;
   Sticky <= stk0;
end architecture;

--------------------------------------------------------------------------------
--                    Normalizer_ZO_20_20_31_Freq200_uid16
-- VHDL generated for Kintex7 @ 200MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, (2007-2020)
--------------------------------------------------------------------------------
-- Pipeline depth: 1 cycles
-- Clock period (ns): 5
-- Target frequency (MHz): 200
-- Input signals: X OZb
-- Output signals: Count R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Normalizer_ZO_20_20_31_Freq200_uid16 is
    port (clk,enable : in std_logic;
          X : in  std_logic_vector(19 downto 0);
          OZb : in  std_logic;
          Count : out  std_logic_vector(4 downto 0);
          R : out  std_logic_vector(19 downto 0)   );
end entity;

architecture arch of Normalizer_ZO_20_20_31_Freq200_uid16 is
signal level5 :  std_logic_vector(19 downto 0);
signal sozb, sozb_d1 :  std_logic;
signal count4, count4_d1 :  std_logic;
signal level4 :  std_logic_vector(19 downto 0);
signal count3, count3_d1 :  std_logic;
signal level3, level3_d1 :  std_logic_vector(19 downto 0);
signal count2, count2_d1 :  std_logic;
signal level2 :  std_logic_vector(19 downto 0);
signal count1 :  std_logic;
signal level1 :  std_logic_vector(19 downto 0);
signal count0 :  std_logic;
signal level0 :  std_logic_vector(19 downto 0);
signal sCount :  std_logic_vector(4 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            sozb_d1 <=  sozb;
            count4_d1 <=  count4;
            count3_d1 <=  count3;
            level3_d1 <=  level3;
            count2_d1 <=  count2;
         end if;
      end process;
   level5 <= X ;
   sozb<= OZb;
   count4<= '1' when level5(19 downto 4) = (19 downto 4=>sozb) else '0';
   level4<= level5(19 downto 0) when count4='0' else level5(3 downto 0) & (15 downto 0 => '0');

   count3<= '1' when level4(19 downto 12) = (19 downto 12=>sozb) else '0';
   level3<= level4(19 downto 0) when count3='0' else level4(11 downto 0) & (7 downto 0 => '0');

   count2<= '1' when level3(19 downto 16) = (19 downto 16=>sozb) else '0';
   level2<= level3_d1(19 downto 0) when count2_d1='0' else level3_d1(15 downto 0) & (3 downto 0 => '0');

   count1<= '1' when level2(19 downto 18) = (19 downto 18=>sozb_d1) else '0';
   level1<= level2(19 downto 0) when count1='0' else level2(17 downto 0) & (1 downto 0 => '0');

   count0<= '1' when level1(19 downto 19) = (19 downto 19=>sozb_d1) else '0';
   level0<= level1(19 downto 0) when count0='0' else level1(18 downto 0) & (0 downto 0 => '0');

   R <= level0;
   sCount <= count4_d1 & count3_d1 & count2_d1 & count1 & count0;
   Count <= sCount;
end architecture;

--------------------------------------------------------------------------------
--                         PIFAdd_15_14_Freq200_uid12
-- VHDL generated for Kintex7 @ 200MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Oregane Desrentes 2019
--------------------------------------------------------------------------------
-- Pipeline depth: 5 cycles
-- Clock period (ns): 5
-- Target frequency (MHz): 200
-- Input signals: X Y
-- Output signals: R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PIFAdd_15_14_Freq200_uid12 is
    port (clk,enable : in std_logic;
          X : in  std_logic_vector(33 downto 0);
          Y : in  std_logic_vector(33 downto 0);
          R : out  std_logic_vector(33 downto 0)   );
end entity;

architecture arch of PIFAdd_15_14_Freq200_uid12 is
   component RightShifterSticky18_by_max_18_Freq200_uid14 is
      port ( clk,enable : in std_logic;
             X : in  std_logic_vector(17 downto 0);
             S : in  std_logic_vector(4 downto 0);
             padBit : in  std_logic;
             R : out  std_logic_vector(17 downto 0);
             Sticky : out  std_logic   );
   end component;

   component Normalizer_ZO_20_20_31_Freq200_uid16 is
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
signal is_larger_exp, is_larger_exp_d1 :  std_logic;
signal larger_exp, larger_exp_d1, larger_exp_d2, larger_exp_d3 :  std_logic_vector(14 downto 0);
signal smaller_exp :  std_logic_vector(14 downto 0);
signal larger_mantissa :  std_logic_vector(15 downto 0);
signal smaller_mantissa :  std_logic_vector(15 downto 0);
signal larger_sign :  std_logic;
signal pad, pad_d1, pad_d2 :  std_logic;
signal offset :  std_logic_vector(15 downto 0);
signal sup_offset :  std_logic_vector(10 downto 0);
signal saturate :  std_logic;
signal inf_offset :  std_logic_vector(4 downto 0);
signal input_shifter :  std_logic_vector(17 downto 0);
signal shifted_frac, shifted_frac_d1, shifted_frac_d2 :  std_logic_vector(17 downto 0);
signal sticky, sticky_d1 :  std_logic;
signal shifted_frac_trunc, shifted_frac_trunc_d1, shifted_frac_trunc_d2 :  std_logic_vector(16 downto 0);
signal padded_larger_mantissa, padded_larger_mantissa_d1, padded_larger_mantissa_d2 :  std_logic_vector(17 downto 0);
signal add_mantissa :  std_logic_vector(19 downto 0);
signal count_type, count_type_d1, count_type_d2 :  std_logic;
signal lzCount :  std_logic_vector(4 downto 0);
signal significand :  std_logic_vector(19 downto 0);
signal exponent, exponent_d1 :  std_logic_vector(14 downto 0);
signal round, round_d1 :  std_logic;
signal not_sticky, not_sticky_d1 :  std_logic;
signal pre_is_zero :  std_logic;
signal fraction, fraction_d1 :  std_logic_vector(14 downto 0);
signal fraction_is_zero, fraction_is_zero_d1 :  std_logic;
signal is_zero :  std_logic;
signal s :  std_logic;
signal final_exponent :  std_logic_vector(14 downto 0);
signal is_NAR, is_NAR_d1, is_NAR_d2, is_NAR_d3, is_NAR_d4, is_NAR_d5 :  std_logic;
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable ='1' then
            X_s_d1 <=  X_s;
            X_exponent_d1 <=  X_exponent;
            X_fraction_d1 <=  X_fraction;
            Y_s_d1 <=  Y_s;
            Y_exponent_d1 <=  Y_exponent;
            Y_fraction_d1 <=  Y_fraction;
            is_larger_exp_d1 <=  is_larger_exp;
            larger_exp_d1 <=  larger_exp;
            larger_exp_d2 <=  larger_exp_d1;
            larger_exp_d3 <=  larger_exp_d2;
            pad_d1 <=  pad;
            pad_d2 <=  pad_d1;
            shifted_frac_d1 <=  shifted_frac;
            shifted_frac_d2 <=  shifted_frac_d1;
            sticky_d1 <=  sticky;
            shifted_frac_trunc_d1 <=  shifted_frac_trunc;
            shifted_frac_trunc_d2 <=  shifted_frac_trunc_d1;
            padded_larger_mantissa_d1 <=  padded_larger_mantissa;
            padded_larger_mantissa_d2 <=  padded_larger_mantissa_d1;
            count_type_d1 <=  count_type;
            count_type_d2 <=  count_type_d1;
            exponent_d1 <=  exponent;
            round_d1 <=  round;
            not_sticky_d1 <=  not_sticky;
            fraction_d1 <=  fraction;
            fraction_is_zero_d1 <=  fraction_is_zero;
            is_NAR_d1 <=  is_NAR;
            is_NAR_d2 <=  is_NAR_d1;
            is_NAR_d3 <=  is_NAR_d2;
            is_NAR_d4 <=  is_NAR_d3;
            is_NAR_d5 <=  is_NAR_d4;
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
is_larger_exp<= '1' when X_exponent > Y_exponent else '0';
with is_larger_exp_d1  select  larger_exp<= 
   X_exponent_d1 when '1',
   Y_exponent_d1 when '0',
   "---------------" when others;
with is_larger_exp_d1  select  smaller_exp<= 
   Y_exponent_d1 when '1',
   X_exponent_d1 when '0',
   "---------------" when others;
with is_larger_exp_d1  select  larger_mantissa<= 
   X_s_d1 & X_fraction_d1 when '1',
   Y_s_d1 & Y_fraction_d1 when '0',
   "----------------" when others;
with is_larger_exp_d1  select  smaller_mantissa<= 
   Y_s_d1 & Y_fraction_d1 when '1',
   X_s_d1 & X_fraction_d1 when '0',
   "----------------" when others;
with is_larger_exp_d1  select  larger_sign<= 
   X_s_d1 when '1',
   Y_s_d1 when '0',
   '-' when others;
with is_larger_exp_d1  select  pad<= 
   Y_s_d1 when '1',
   X_s_d1 when '0',
   '-' when others;
offset <= ('0' & larger_exp) - ('0' & smaller_exp);
sup_offset <= offset(15 downto 5);
saturate <= '0' when sup_offset = "00000000000" else '1';
with saturate  select  inf_offset<=
   "11111" when '1',
   offset(4 downto 0) when '0',
   "-----" when others;
input_shifter <= smaller_mantissa & "00";
   mantissa_shift: RightShifterSticky18_by_max_18_Freq200_uid14
      port map ( clk  => clk,
                 enable => enable,
                 S => inf_offset,
                 X => input_shifter,
                 padBit => pad,
                 R => shifted_frac,
                 Sticky => sticky);
shifted_frac_trunc<= shifted_frac(17 downto 1);
with larger_sign  select  padded_larger_mantissa<= 
   "0" & larger_mantissa & '0' when '0',
   "1" & larger_mantissa & '0' when '1',
   "------------------" when others;
add_mantissa<= ((padded_larger_mantissa_d2) + (pad_d2 & shifted_frac_trunc_d2)) & shifted_frac_d2(0) & sticky_d1;
count_type<= add_mantissa(19);
   norm: Normalizer_ZO_20_20_31_Freq200_uid16
      port map ( clk  => clk,
                 enable => enable,
                 OZb => count_type,
                 X => add_mantissa,
                 Count => lzCount,
                 R => significand);
exponent <= larger_exp_d3 + 2 - lzCount;
round<= significand(4);
not_sticky<= '1' when significand(3 downto 0) = "0000" else '0';
pre_is_zero<= (not round_d1) or (not_sticky_d1 and round_d1);
fraction<= significand(19 downto 5);
fraction_is_zero<= '1' when fraction = "000000000000000" else '0';
is_zero<= not count_type_d2 and fraction_is_zero_d1 and pre_is_zero;
with is_zero  select  s<= 
   '0' when '1',
   not fraction_d1(14) when '0',
   '-' when others;
with is_zero  select  final_exponent<= 
   "000000000000000" when '1',
   exponent_d1 when '0',
   "000000000000000" when others;
is_NAR <= X(33) or Y(33);
R <= is_NAR_d5 & s & final_exponent & fraction_d1 & round_d1 & (not not_sticky_d1);
end architecture;

--------------------------------------------------------------------------------
--                RightShifterSticky26_by_max_26_Freq200_uid20
-- VHDL generated for Kintex7 @ 200MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca (2008-2011), Florent de Dinechin (2008-2019)
--------------------------------------------------------------------------------
-- Pipeline depth: 1 cycles
-- Clock period (ns): 5
-- Target frequency (MHz): 200
-- Input signals: X S padBit
-- Output signals: R Sticky

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity RightShifterSticky26_by_max_26_Freq200_uid20 is
    port (clk,enable : in std_logic;
          X : in  std_logic_vector(25 downto 0);
          S : in  std_logic_vector(4 downto 0);
          padBit : in  std_logic;
          R : out  std_logic_vector(25 downto 0);
          Sticky : out  std_logic   );
end entity;

architecture arch of RightShifterSticky26_by_max_26_Freq200_uid20 is
signal ps, ps_d1 :  std_logic_vector(4 downto 0);
signal Xpadded :  std_logic_vector(25 downto 0);
signal level5 :  std_logic_vector(25 downto 0);
signal stk4, stk4_d1 :  std_logic;
signal level4, level4_d1 :  std_logic_vector(25 downto 0);
signal stk3 :  std_logic;
signal level3, level3_d1 :  std_logic_vector(25 downto 0);
signal stk2 :  std_logic;
signal level2, level2_d1 :  std_logic_vector(25 downto 0);
signal stk1 :  std_logic;
signal level1, level1_d1 :  std_logic_vector(25 downto 0);
signal stk0 :  std_logic;
signal level0 :  std_logic_vector(25 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            ps_d1 <=  ps;
            stk4_d1 <=  stk4;
            level4_d1 <=  level4;
            level3_d1 <=  level3;
            level2_d1 <=  level2;
            level1_d1 <=  level1;
         end if;
      end process;
   ps<= S;
   Xpadded <= X;
   level5<= Xpadded;
   stk4 <= '1' when (level5(15 downto 0)/="0000000000000000" and ps(4)='1')   else '0';
   level4 <=  level5 when  ps(4)='0'    else (15 downto 0 => padBit) & level5(25 downto 16);
   stk3 <= '1' when (level4_d1(7 downto 0)/="00000000" and ps_d1(3)='1') or stk4_d1 ='1'   else '0';
   level3 <=  level4 when  ps(3)='0'    else (7 downto 0 => padBit) & level4(25 downto 8);
   stk2 <= '1' when (level3_d1(3 downto 0)/="0000" and ps_d1(2)='1') or stk3 ='1'   else '0';
   level2 <=  level3 when  ps(2)='0'    else (3 downto 0 => padBit) & level3(25 downto 4);
   stk1 <= '1' when (level2_d1(1 downto 0)/="00" and ps_d1(1)='1') or stk2 ='1'   else '0';
   level1 <=  level2 when  ps(1)='0'    else (1 downto 0 => padBit) & level2(25 downto 2);
   stk0 <= '1' when (level1_d1(0 downto 0)/="0" and ps_d1(0)='1') or stk1 ='1'   else '0';
   level0 <=  level1 when  ps(0)='0'    else (0 downto 0 => padBit) & level1(25 downto 1);
   R <= level0;
   Sticky <= stk0;
end architecture;

--------------------------------------------------------------------------------
--                        PIF2Posit_26_9_Freq200_uid18
-- VHDL generated for Kintex7 @ 200MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Oregane Desrentes 2019
--------------------------------------------------------------------------------
-- Pipeline depth: 2 cycles
-- Clock period (ns): 5
-- Target frequency (MHz): 200
-- Input signals: I
-- Output signals: O

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PIF2Posit_26_9_Freq200_uid18 is
    port (clk,enable : in std_logic;
          I : in  std_logic_vector(33 downto 0);
          O : out  std_logic_vector(25 downto 0)   );
end entity;

architecture arch of PIF2Posit_26_9_Freq200_uid18 is
   component RightShifterSticky26_by_max_26_Freq200_uid20 is
      port ( clk,enable : in std_logic;
             X : in  std_logic_vector(25 downto 0);
             S : in  std_logic_vector(4 downto 0);
             padBit : in  std_logic;
             R : out  std_logic_vector(25 downto 0);
             Sticky : out  std_logic   );
   end component;

signal is_NAR, is_NAR_d1, is_NAR_d2 :  std_logic;
signal s, s_d1, s_d2 :  std_logic;
signal biased_exponent :  std_logic_vector(14 downto 0);
signal fraction :  std_logic_vector(14 downto 0);
signal is_zero, is_zero_d1, is_zero_d2 :  std_logic;
signal exponent :  std_logic_vector(14 downto 0);
signal partial_exponent :  std_logic_vector(8 downto 0);
signal partial_exponent_us :  std_logic_vector(8 downto 0);
signal bin_regime :  std_logic_vector(4 downto 0);
signal first_regime :  std_logic;
signal regime :  std_logic_vector(4 downto 0);
signal pad :  std_logic;
signal start_regime :  std_logic_vector(1 downto 0);
signal input_shifter :  std_logic_vector(25 downto 0);
signal extended_posit :  std_logic_vector(25 downto 0);
signal pre_sticky :  std_logic;
signal truncated_posit, truncated_posit_d1, truncated_posit_d2 :  std_logic_vector(24 downto 0);
signal lsb, lsb_d1, lsb_d2 :  std_logic;
signal guard, guard_d1, guard_d2 :  std_logic;
signal sticky, sticky_d1 :  std_logic;
signal round_bit :  std_logic;
signal rounded_reg_exp_frac :  std_logic_vector(24 downto 0);
signal rounded_posit :  std_logic_vector(25 downto 0);
signal rounded_posit_zero :  std_logic_vector(25 downto 0);
signal I_d1 :  std_logic_vector(33 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' and enable = '1' then
            is_NAR_d1 <=  is_NAR;
            is_NAR_d2 <=  is_NAR_d1;
            s_d1 <=  s;
            s_d2 <=  s_d1;
            is_zero_d1 <=  is_zero;
            is_zero_d2 <=  is_zero_d1;
            truncated_posit_d1 <=  truncated_posit;
            truncated_posit_d2 <=  truncated_posit_d1;
            lsb_d1 <=  lsb;
            lsb_d2 <=  lsb_d1;
            guard_d1 <=  guard;
            guard_d2 <=  guard_d1;
            sticky_d1 <=  sticky;
            I_d1 <=  I;
         end if;
      end process;
--------------------------- Start of vhdl generation ---------------------------
is_NAR<= I(33);
s<= I(32);
biased_exponent<= I(31 downto 17);
fraction<= I(15 downto 1);
is_zero<= '1' when I(33 downto 0) = "0000000000000000000000000000000000" else '0';
exponent<= biased_exponent - 12289;
partial_exponent<= exponent(8 downto 0);
with s  select  partial_exponent_us <= 
   partial_exponent when '0',
   not partial_exponent when '1',
   "---------" when others;
bin_regime<= exponent(13 downto 9);
first_regime<= exponent(14);
with first_regime  select  regime <= 
   bin_regime when '0', 
   not bin_regime when '1', 
   "-----" when others;
pad<= not(first_regime xor s);
with pad  select  start_regime <= 
   "01" when '0', 
   "10" when '1', 
   "--" when others;
input_shifter<= start_regime & partial_exponent_us & fraction;
   rshift: RightShifterSticky26_by_max_26_Freq200_uid20
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
sticky<= I_d1(0) or pre_sticky;
round_bit<= guard_d2 and (sticky_d1 or lsb_d2);
rounded_reg_exp_frac<= truncated_posit_d2 + round_bit;
rounded_posit<= s_d2 & rounded_reg_exp_frac;
rounded_posit_zero<= rounded_posit when is_zero_d2= '0' else "00000000000000000000000000";
O <= rounded_posit_zero when is_NAR_d2 = '0' else "10000000000000000000000000";
---------------------------- End of vhdl generation ----------------------------
end architecture;

--------------------------------------------------------------------------------
--                         PositAdd_26_9_Freq200_uid2
-- VHDL generated for Kintex7 @ 200MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Oregane Desrentes 2019
--------------------------------------------------------------------------------
-- Pipeline depth: 8 cycles
-- Clock period (ns): 5
-- Target frequency (MHz): 200
-- Input signals: X Y
-- Output signals: R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PositAdd_26_9_Freq200_uid2 is
    port (clk,enable : in std_logic;
          X : in  std_logic_vector(25 downto 0);
          Y : in  std_logic_vector(25 downto 0);
          R : out  std_logic_vector(25 downto 0)   );
end entity;

architecture arch of PositAdd_26_9_Freq200_uid2 is
   component Posit2PIF_26_9_Freq200_uid4 is
      port ( clk,enable: in std_logic;
             I : in  std_logic_vector(25 downto 0);
             O : out  std_logic_vector(33 downto 0)   );
   end component;

   component Posit2PIF_26_9_Freq200_uid8 is
      port ( clk,enable : in std_logic;
             I : in  std_logic_vector(25 downto 0);
             O : out  std_logic_vector(33 downto 0)   );
   end component;

   component PIFAdd_15_14_Freq200_uid12 is
      port ( clk,enable : in std_logic;
             X : in  std_logic_vector(33 downto 0);
             Y : in  std_logic_vector(33 downto 0);
             R : out  std_logic_vector(33 downto 0)   );
   end component;

   component PIF2Posit_26_9_Freq200_uid18 is
      port ( clk,enable : in std_logic;
             I : in  std_logic_vector(33 downto 0);
             O : out  std_logic_vector(25 downto 0)   );
   end component;

signal X_PIF :  std_logic_vector(33 downto 0);
signal Y_PIF :  std_logic_vector(33 downto 0);
signal R_PIF :  std_logic_vector(33 downto 0);
begin
--------------------------- Start of vhdl generation ---------------------------
   X_conversion: Posit2PIF_26_9_Freq200_uid4
      port map ( clk  => clk,
                 enable => enable,
                 I => X,
                 O => X_PIF);
   Y_conversion: Posit2PIF_26_9_Freq200_uid8
      port map ( clk  => clk,
                 enable => enable,
                 I => Y,
                 O => Y_PIF);
   Addition: PIFAdd_15_14_Freq200_uid12
      port map ( clk  => clk,
                 enable => enable,
                 X => X_PIF,
                 Y => Y_PIF,
                 R => R_PIF);
   R_conversion: PIF2Posit_26_9_Freq200_uid18
      port map ( clk  => clk,
                 enable => enable,
                 I => R_PIF,
                 O => R);
---------------------------- End of vhdl generation ----------------------------
end architecture;

