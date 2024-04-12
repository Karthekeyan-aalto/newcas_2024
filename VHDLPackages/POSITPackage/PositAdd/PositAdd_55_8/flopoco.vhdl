--------------------------------------------------------------------------------
--                       Normalizer_ZO_53_53_31_F0_uid6
-- VHDL generated for Kintex7 @ 0MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, (2007-2020)
--------------------------------------------------------------------------------
-- combinatorial
-- Clock period (ns): inf
-- Target frequency (MHz): 0
-- Input signals: X OZb
-- Output signals: Count R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Normalizer_ZO_53_53_31_F0_uid6 is
    port (X : in  std_logic_vector(52 downto 0);
          OZb : in  std_logic;
          Count : out  std_logic_vector(4 downto 0);
          R : out  std_logic_vector(52 downto 0)   );
end entity;

architecture arch of Normalizer_ZO_53_53_31_F0_uid6 is
signal level5 :  std_logic_vector(52 downto 0);
signal sozb :  std_logic;
signal count4 :  std_logic;
signal level4 :  std_logic_vector(52 downto 0);
signal count3 :  std_logic;
signal level3 :  std_logic_vector(52 downto 0);
signal count2 :  std_logic;
signal level2 :  std_logic_vector(52 downto 0);
signal count1 :  std_logic;
signal level1 :  std_logic_vector(52 downto 0);
signal count0 :  std_logic;
signal level0 :  std_logic_vector(52 downto 0);
signal sCount :  std_logic_vector(4 downto 0);
begin
   level5 <= X ;
   sozb<= OZb;
   count4<= '1' when level5(52 downto 37) = (52 downto 37=>sozb) else '0';
   level4<= level5(52 downto 0) when count4='0' else level5(36 downto 0) & (15 downto 0 => '0');

   count3<= '1' when level4(52 downto 45) = (52 downto 45=>sozb) else '0';
   level3<= level4(52 downto 0) when count3='0' else level4(44 downto 0) & (7 downto 0 => '0');

   count2<= '1' when level3(52 downto 49) = (52 downto 49=>sozb) else '0';
   level2<= level3(52 downto 0) when count2='0' else level3(48 downto 0) & (3 downto 0 => '0');

   count1<= '1' when level2(52 downto 51) = (52 downto 51=>sozb) else '0';
   level1<= level2(52 downto 0) when count1='0' else level2(50 downto 0) & (1 downto 0 => '0');

   count0<= '1' when level1(52 downto 52) = (52 downto 52=>sozb) else '0';
   level0<= level1(52 downto 0) when count0='0' else level1(51 downto 0) & (0 downto 0 => '0');

   R <= level0;
   sCount <= count4 & count3 & count2 & count1 & count0;
   Count <= sCount;
end architecture;

--------------------------------------------------------------------------------
--                           Posit2PIF_55_8_F0_uid4
-- VHDL generated for Kintex7 @ 0MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Oregane Desrentes 2019
--------------------------------------------------------------------------------
-- combinatorial
-- Clock period (ns): inf
-- Target frequency (MHz): 0
-- Input signals: I
-- Output signals: O

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Posit2PIF_55_8_F0_uid4 is
    port (I : in  std_logic_vector(54 downto 0);
          O : out  std_logic_vector(63 downto 0)   );
end entity;

architecture arch of Posit2PIF_55_8_F0_uid4 is
   component Normalizer_ZO_53_53_31_F0_uid6 is
      port ( X : in  std_logic_vector(52 downto 0);
             OZb : in  std_logic;
             Count : out  std_logic_vector(4 downto 0);
             R : out  std_logic_vector(52 downto 0)   );
   end component;

signal s :  std_logic;
signal count_type :  std_logic;
signal remainder :  std_logic_vector(52 downto 0);
signal not_s :  std_logic;
signal zero_NAR :  std_logic;
signal is_NAR :  std_logic;
signal is_not_zero :  std_logic;
signal implicit_bit :  std_logic;
signal neg_count :  std_logic;
signal lzCount :  std_logic_vector(4 downto 0);
signal usefulBits :  std_logic_vector(52 downto 0);
signal extended_neg_count :  std_logic_vector(6 downto 0);
signal comp2_range_count :  std_logic_vector(6 downto 0);
signal fraction :  std_logic_vector(43 downto 0);
signal partialExponent :  std_logic_vector(7 downto 0);
signal us_partialExponent :  std_logic_vector(7 downto 0);
signal exponent :  std_logic_vector(14 downto 0);
signal biased_exponent :  std_logic_vector(14 downto 0);
signal extended_is_not_zero :  std_logic_vector(14 downto 0);
signal final_biased_exponent :  std_logic_vector(14 downto 0);
signal round :  std_logic;
signal sticky :  std_logic;
begin
--------------------------- Start of vhdl generation ---------------------------
s<= I(54);
count_type<= I(53);
remainder<= I(52 downto 0);
not_s<= not s;
zero_NAR <= not count_type when remainder="00000000000000000000000000000000000000000000000000000" else '0';
is_NAR<= zero_NAR and s;
is_not_zero<= not(zero_NAR and not_s);
implicit_bit<= is_not_zero and not_s;
neg_count<= not (s xor count_type);
   lzoc: Normalizer_ZO_53_53_31_F0_uid6
      port map ( OZb => count_type,
                 X => remainder,
                 Count => lzCount,
                 R => usefulBits);
with neg_count  select  extended_neg_count <= 
   "0000000" when '0', 
   "1111111" when '1', 
   "-------" when others;
comp2_range_count<= extended_neg_count xor ("00" & lzCount);
fraction<= usefulBits(43 downto 0);
partialExponent<= usefulBits(51 downto 44);
with s  select  us_partialExponent<= 
   partialExponent when '0',
   not partialExponent when '1',
   "--------" when others;
exponent<= comp2_range_count & us_partialExponent;
biased_exponent<= exponent + 13569;
with is_not_zero  select   extended_is_not_zero <= 
   "000000000000000" when '0', 
   "111111111111111" when '1', 
   "---------------" when others;
final_biased_exponent<= extended_is_not_zero and biased_exponent;
round<= '0';
sticky<= '0';
O <= is_NAR & s & final_biased_exponent & implicit_bit & fraction & round & sticky;
---------------------------- End of vhdl generation ----------------------------
end architecture;

--------------------------------------------------------------------------------
--                      Normalizer_ZO_53_53_31_F0_uid10
-- VHDL generated for Kintex7 @ 0MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, (2007-2020)
--------------------------------------------------------------------------------
-- combinatorial
-- Clock period (ns): inf
-- Target frequency (MHz): 0
-- Input signals: X OZb
-- Output signals: Count R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Normalizer_ZO_53_53_31_F0_uid10 is
    port (X : in  std_logic_vector(52 downto 0);
          OZb : in  std_logic;
          Count : out  std_logic_vector(4 downto 0);
          R : out  std_logic_vector(52 downto 0)   );
end entity;

architecture arch of Normalizer_ZO_53_53_31_F0_uid10 is
signal level5 :  std_logic_vector(52 downto 0);
signal sozb :  std_logic;
signal count4 :  std_logic;
signal level4 :  std_logic_vector(52 downto 0);
signal count3 :  std_logic;
signal level3 :  std_logic_vector(52 downto 0);
signal count2 :  std_logic;
signal level2 :  std_logic_vector(52 downto 0);
signal count1 :  std_logic;
signal level1 :  std_logic_vector(52 downto 0);
signal count0 :  std_logic;
signal level0 :  std_logic_vector(52 downto 0);
signal sCount :  std_logic_vector(4 downto 0);
begin
   level5 <= X ;
   sozb<= OZb;
   count4<= '1' when level5(52 downto 37) = (52 downto 37=>sozb) else '0';
   level4<= level5(52 downto 0) when count4='0' else level5(36 downto 0) & (15 downto 0 => '0');

   count3<= '1' when level4(52 downto 45) = (52 downto 45=>sozb) else '0';
   level3<= level4(52 downto 0) when count3='0' else level4(44 downto 0) & (7 downto 0 => '0');

   count2<= '1' when level3(52 downto 49) = (52 downto 49=>sozb) else '0';
   level2<= level3(52 downto 0) when count2='0' else level3(48 downto 0) & (3 downto 0 => '0');

   count1<= '1' when level2(52 downto 51) = (52 downto 51=>sozb) else '0';
   level1<= level2(52 downto 0) when count1='0' else level2(50 downto 0) & (1 downto 0 => '0');

   count0<= '1' when level1(52 downto 52) = (52 downto 52=>sozb) else '0';
   level0<= level1(52 downto 0) when count0='0' else level1(51 downto 0) & (0 downto 0 => '0');

   R <= level0;
   sCount <= count4 & count3 & count2 & count1 & count0;
   Count <= sCount;
end architecture;

--------------------------------------------------------------------------------
--                           Posit2PIF_55_8_F0_uid8
-- VHDL generated for Kintex7 @ 0MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Oregane Desrentes 2019
--------------------------------------------------------------------------------
-- combinatorial
-- Clock period (ns): inf
-- Target frequency (MHz): 0
-- Input signals: I
-- Output signals: O

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Posit2PIF_55_8_F0_uid8 is
    port (I : in  std_logic_vector(54 downto 0);
          O : out  std_logic_vector(63 downto 0)   );
end entity;

architecture arch of Posit2PIF_55_8_F0_uid8 is
   component Normalizer_ZO_53_53_31_F0_uid10 is
      port ( X : in  std_logic_vector(52 downto 0);
             OZb : in  std_logic;
             Count : out  std_logic_vector(4 downto 0);
             R : out  std_logic_vector(52 downto 0)   );
   end component;

signal s :  std_logic;
signal count_type :  std_logic;
signal remainder :  std_logic_vector(52 downto 0);
signal not_s :  std_logic;
signal zero_NAR :  std_logic;
signal is_NAR :  std_logic;
signal is_not_zero :  std_logic;
signal implicit_bit :  std_logic;
signal neg_count :  std_logic;
signal lzCount :  std_logic_vector(4 downto 0);
signal usefulBits :  std_logic_vector(52 downto 0);
signal extended_neg_count :  std_logic_vector(6 downto 0);
signal comp2_range_count :  std_logic_vector(6 downto 0);
signal fraction :  std_logic_vector(43 downto 0);
signal partialExponent :  std_logic_vector(7 downto 0);
signal us_partialExponent :  std_logic_vector(7 downto 0);
signal exponent :  std_logic_vector(14 downto 0);
signal biased_exponent :  std_logic_vector(14 downto 0);
signal extended_is_not_zero :  std_logic_vector(14 downto 0);
signal final_biased_exponent :  std_logic_vector(14 downto 0);
signal round :  std_logic;
signal sticky :  std_logic;
begin
--------------------------- Start of vhdl generation ---------------------------
s<= I(54);
count_type<= I(53);
remainder<= I(52 downto 0);
not_s<= not s;
zero_NAR <= not count_type when remainder="00000000000000000000000000000000000000000000000000000" else '0';
is_NAR<= zero_NAR and s;
is_not_zero<= not(zero_NAR and not_s);
implicit_bit<= is_not_zero and not_s;
neg_count<= not (s xor count_type);
   lzoc: Normalizer_ZO_53_53_31_F0_uid10
      port map ( OZb => count_type,
                 X => remainder,
                 Count => lzCount,
                 R => usefulBits);
with neg_count  select  extended_neg_count <= 
   "0000000" when '0', 
   "1111111" when '1', 
   "-------" when others;
comp2_range_count<= extended_neg_count xor ("00" & lzCount);
fraction<= usefulBits(43 downto 0);
partialExponent<= usefulBits(51 downto 44);
with s  select  us_partialExponent<= 
   partialExponent when '0',
   not partialExponent when '1',
   "--------" when others;
exponent<= comp2_range_count & us_partialExponent;
biased_exponent<= exponent + 13569;
with is_not_zero  select   extended_is_not_zero <= 
   "000000000000000" when '0', 
   "111111111111111" when '1', 
   "---------------" when others;
final_biased_exponent<= extended_is_not_zero and biased_exponent;
round<= '0';
sticky<= '0';
O <= is_NAR & s & final_biased_exponent & implicit_bit & fraction & round & sticky;
---------------------------- End of vhdl generation ----------------------------
end architecture;

--------------------------------------------------------------------------------
--                  RightShifterSticky48_by_max_48_F0_uid14
-- VHDL generated for Kintex7 @ 0MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca (2008-2011), Florent de Dinechin (2008-2019)
--------------------------------------------------------------------------------
-- combinatorial
-- Clock period (ns): inf
-- Target frequency (MHz): 0
-- Input signals: X S padBit
-- Output signals: R Sticky

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity RightShifterSticky48_by_max_48_F0_uid14 is
    port (X : in  std_logic_vector(47 downto 0);
          S : in  std_logic_vector(5 downto 0);
          padBit : in  std_logic;
          R : out  std_logic_vector(47 downto 0);
          Sticky : out  std_logic   );
end entity;

architecture arch of RightShifterSticky48_by_max_48_F0_uid14 is
signal ps :  std_logic_vector(5 downto 0);
signal Xpadded :  std_logic_vector(47 downto 0);
signal level6 :  std_logic_vector(47 downto 0);
signal stk5 :  std_logic;
signal level5 :  std_logic_vector(47 downto 0);
signal stk4 :  std_logic;
signal level4 :  std_logic_vector(47 downto 0);
signal stk3 :  std_logic;
signal level3 :  std_logic_vector(47 downto 0);
signal stk2 :  std_logic;
signal level2 :  std_logic_vector(47 downto 0);
signal stk1 :  std_logic;
signal level1 :  std_logic_vector(47 downto 0);
signal stk0 :  std_logic;
signal level0 :  std_logic_vector(47 downto 0);
begin
   ps<= S;
   Xpadded <= X;
   level6<= Xpadded;
   stk5 <= '1' when (level6(31 downto 0)/="00000000000000000000000000000000" and ps(5)='1')   else '0';
   level5 <=  level6 when  ps(5)='0'    else (31 downto 0 => padBit) & level6(47 downto 32);
   stk4 <= '1' when (level5(15 downto 0)/="0000000000000000" and ps(4)='1') or stk5 ='1'   else '0';
   level4 <=  level5 when  ps(4)='0'    else (15 downto 0 => padBit) & level5(47 downto 16);
   stk3 <= '1' when (level4(7 downto 0)/="00000000" and ps(3)='1') or stk4 ='1'   else '0';
   level3 <=  level4 when  ps(3)='0'    else (7 downto 0 => padBit) & level4(47 downto 8);
   stk2 <= '1' when (level3(3 downto 0)/="0000" and ps(2)='1') or stk3 ='1'   else '0';
   level2 <=  level3 when  ps(2)='0'    else (3 downto 0 => padBit) & level3(47 downto 4);
   stk1 <= '1' when (level2(1 downto 0)/="00" and ps(1)='1') or stk2 ='1'   else '0';
   level1 <=  level2 when  ps(1)='0'    else (1 downto 0 => padBit) & level2(47 downto 2);
   stk0 <= '1' when (level1(0 downto 0)/="0" and ps(0)='1') or stk1 ='1'   else '0';
   level0 <=  level1 when  ps(0)='0'    else (0 downto 0 => padBit) & level1(47 downto 1);
   R <= level0;
   Sticky <= stk0;
end architecture;

--------------------------------------------------------------------------------
--                      Normalizer_ZO_50_50_63_F0_uid16
-- VHDL generated for Kintex7 @ 0MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, (2007-2020)
--------------------------------------------------------------------------------
-- combinatorial
-- Clock period (ns): inf
-- Target frequency (MHz): 0
-- Input signals: X OZb
-- Output signals: Count R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Normalizer_ZO_50_50_63_F0_uid16 is
    port (X : in  std_logic_vector(49 downto 0);
          OZb : in  std_logic;
          Count : out  std_logic_vector(5 downto 0);
          R : out  std_logic_vector(49 downto 0)   );
end entity;

architecture arch of Normalizer_ZO_50_50_63_F0_uid16 is
signal level6 :  std_logic_vector(49 downto 0);
signal sozb :  std_logic;
signal count5 :  std_logic;
signal level5 :  std_logic_vector(49 downto 0);
signal count4 :  std_logic;
signal level4 :  std_logic_vector(49 downto 0);
signal count3 :  std_logic;
signal level3 :  std_logic_vector(49 downto 0);
signal count2 :  std_logic;
signal level2 :  std_logic_vector(49 downto 0);
signal count1 :  std_logic;
signal level1 :  std_logic_vector(49 downto 0);
signal count0 :  std_logic;
signal level0 :  std_logic_vector(49 downto 0);
signal sCount :  std_logic_vector(5 downto 0);
begin
   level6 <= X ;
   sozb<= OZb;
   count5<= '1' when level6(49 downto 18) = (49 downto 18=>sozb) else '0';
   level5<= level6(49 downto 0) when count5='0' else level6(17 downto 0) & (31 downto 0 => '0');

   count4<= '1' when level5(49 downto 34) = (49 downto 34=>sozb) else '0';
   level4<= level5(49 downto 0) when count4='0' else level5(33 downto 0) & (15 downto 0 => '0');

   count3<= '1' when level4(49 downto 42) = (49 downto 42=>sozb) else '0';
   level3<= level4(49 downto 0) when count3='0' else level4(41 downto 0) & (7 downto 0 => '0');

   count2<= '1' when level3(49 downto 46) = (49 downto 46=>sozb) else '0';
   level2<= level3(49 downto 0) when count2='0' else level3(45 downto 0) & (3 downto 0 => '0');

   count1<= '1' when level2(49 downto 48) = (49 downto 48=>sozb) else '0';
   level1<= level2(49 downto 0) when count1='0' else level2(47 downto 0) & (1 downto 0 => '0');

   count0<= '1' when level1(49 downto 49) = (49 downto 49=>sozb) else '0';
   level0<= level1(49 downto 0) when count0='0' else level1(48 downto 0) & (0 downto 0 => '0');

   R <= level0;
   sCount <= count5 & count4 & count3 & count2 & count1 & count0;
   Count <= sCount;
end architecture;

--------------------------------------------------------------------------------
--                           PIFAdd_15_44_F0_uid12
-- VHDL generated for Kintex7 @ 0MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Oregane Desrentes 2019
--------------------------------------------------------------------------------
-- combinatorial
-- Clock period (ns): inf
-- Target frequency (MHz): 0
-- Input signals: X Y
-- Output signals: R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PIFAdd_15_44_F0_uid12 is
    port (X : in  std_logic_vector(63 downto 0);
          Y : in  std_logic_vector(63 downto 0);
          R : out  std_logic_vector(63 downto 0)   );
end entity;

architecture arch of PIFAdd_15_44_F0_uid12 is
   component RightShifterSticky48_by_max_48_F0_uid14 is
      port ( X : in  std_logic_vector(47 downto 0);
             S : in  std_logic_vector(5 downto 0);
             padBit : in  std_logic;
             R : out  std_logic_vector(47 downto 0);
             Sticky : out  std_logic   );
   end component;

   component Normalizer_ZO_50_50_63_F0_uid16 is
      port ( X : in  std_logic_vector(49 downto 0);
             OZb : in  std_logic;
             Count : out  std_logic_vector(5 downto 0);
             R : out  std_logic_vector(49 downto 0)   );
   end component;

signal X_is_NAR :  std_logic;
signal X_s :  std_logic;
signal X_exponent :  std_logic_vector(14 downto 0);
signal X_fraction :  std_logic_vector(44 downto 0);
signal Y_is_NAR :  std_logic;
signal Y_s :  std_logic;
signal Y_exponent :  std_logic_vector(14 downto 0);
signal Y_fraction :  std_logic_vector(44 downto 0);
signal is_larger_exp :  std_logic;
signal larger_exp :  std_logic_vector(14 downto 0);
signal smaller_exp :  std_logic_vector(14 downto 0);
signal larger_mantissa :  std_logic_vector(45 downto 0);
signal smaller_mantissa :  std_logic_vector(45 downto 0);
signal larger_sign :  std_logic;
signal pad :  std_logic;
signal offset :  std_logic_vector(15 downto 0);
signal sup_offset :  std_logic_vector(9 downto 0);
signal saturate :  std_logic;
signal inf_offset :  std_logic_vector(5 downto 0);
signal input_shifter :  std_logic_vector(47 downto 0);
signal shifted_frac :  std_logic_vector(47 downto 0);
signal sticky :  std_logic;
signal shifted_frac_trunc :  std_logic_vector(46 downto 0);
signal padded_larger_mantissa :  std_logic_vector(47 downto 0);
signal add_mantissa :  std_logic_vector(49 downto 0);
signal count_type :  std_logic;
signal lzCount :  std_logic_vector(5 downto 0);
signal significand :  std_logic_vector(49 downto 0);
signal exponent :  std_logic_vector(14 downto 0);
signal round :  std_logic;
signal not_sticky :  std_logic;
signal pre_is_zero :  std_logic;
signal fraction :  std_logic_vector(44 downto 0);
signal fraction_is_zero :  std_logic;
signal is_zero :  std_logic;
signal s :  std_logic;
signal final_exponent :  std_logic_vector(14 downto 0);
signal is_NAR :  std_logic;
begin
--------------------------- Start of vhdl generation ---------------------------
X_is_NAR<= X(63);
X_s<= X(62);
X_exponent<= X(61 downto 47);
X_fraction<= X(46 downto 2);
Y_is_NAR<= Y(63);
Y_s<= Y(62);
Y_exponent<= Y(61 downto 47);
Y_fraction<= Y(46 downto 2);
is_larger_exp<= '1' when X_exponent > Y_exponent else '0';
with is_larger_exp  select  larger_exp<= 
   X_exponent when '1',
   Y_exponent when '0',
   "---------------" when others;
with is_larger_exp  select  smaller_exp<= 
   Y_exponent when '1',
   X_exponent when '0',
   "---------------" when others;
with is_larger_exp  select  larger_mantissa<= 
   X_s & X_fraction when '1',
   Y_s & Y_fraction when '0',
   "----------------------------------------------" when others;
with is_larger_exp  select  smaller_mantissa<= 
   Y_s & Y_fraction when '1',
   X_s & X_fraction when '0',
   "----------------------------------------------" when others;
with is_larger_exp  select  larger_sign<= 
   X_s when '1',
   Y_s when '0',
   '-' when others;
with is_larger_exp  select  pad<= 
   Y_s when '1',
   X_s when '0',
   '-' when others;
offset <= ('0' & larger_exp) - ('0' & smaller_exp);
sup_offset <= offset(15 downto 6);
saturate <= '0' when sup_offset = "0000000000" else '1';
with saturate  select  inf_offset<=
   "111111" when '1',
   offset(5 downto 0) when '0',
   "------" when others;
input_shifter <= smaller_mantissa & "00";
   mantissa_shift: RightShifterSticky48_by_max_48_F0_uid14
      port map ( S => inf_offset,
                 X => input_shifter,
                 padBit => pad,
                 R => shifted_frac,
                 Sticky => sticky);
shifted_frac_trunc<= shifted_frac(47 downto 1);
with larger_sign  select  padded_larger_mantissa<= 
   "0" & larger_mantissa & '0' when '0',
   "1" & larger_mantissa & '0' when '1',
   "------------------------------------------------" when others;
add_mantissa<= ((padded_larger_mantissa) + (pad & shifted_frac_trunc)) & shifted_frac(0) & sticky;
count_type<= add_mantissa(49);
   norm: Normalizer_ZO_50_50_63_F0_uid16
      port map ( OZb => count_type,
                 X => add_mantissa,
                 Count => lzCount,
                 R => significand);
exponent <= larger_exp + 2 - lzCount;
round<= significand(4);
not_sticky<= '1' when significand(3 downto 0) = "0000" else '0';
pre_is_zero<= (not round) or (not_sticky and round);
fraction<= significand(49 downto 5);
fraction_is_zero<= '1' when fraction = "000000000000000000000000000000000000000000000" else '0';
is_zero<= not count_type and fraction_is_zero and pre_is_zero;
with is_zero  select  s<= 
   '0' when '1',
   not fraction(44) when '0',
   '-' when others;
with is_zero  select  final_exponent<= 
   "000000000000000" when '1',
   exponent when '0',
   "000000000000000" when others;
is_NAR <= X(63) or Y(63);
R <= is_NAR & s & final_exponent & fraction & round & (not not_sticky);
end architecture;

--------------------------------------------------------------------------------
--                  RightShifterSticky55_by_max_55_F0_uid20
-- VHDL generated for Kintex7 @ 0MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca (2008-2011), Florent de Dinechin (2008-2019)
--------------------------------------------------------------------------------
-- combinatorial
-- Clock period (ns): inf
-- Target frequency (MHz): 0
-- Input signals: X S padBit
-- Output signals: R Sticky

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity RightShifterSticky55_by_max_55_F0_uid20 is
    port (X : in  std_logic_vector(54 downto 0);
          S : in  std_logic_vector(5 downto 0);
          padBit : in  std_logic;
          R : out  std_logic_vector(54 downto 0);
          Sticky : out  std_logic   );
end entity;

architecture arch of RightShifterSticky55_by_max_55_F0_uid20 is
signal ps :  std_logic_vector(5 downto 0);
signal Xpadded :  std_logic_vector(54 downto 0);
signal level6 :  std_logic_vector(54 downto 0);
signal stk5 :  std_logic;
signal level5 :  std_logic_vector(54 downto 0);
signal stk4 :  std_logic;
signal level4 :  std_logic_vector(54 downto 0);
signal stk3 :  std_logic;
signal level3 :  std_logic_vector(54 downto 0);
signal stk2 :  std_logic;
signal level2 :  std_logic_vector(54 downto 0);
signal stk1 :  std_logic;
signal level1 :  std_logic_vector(54 downto 0);
signal stk0 :  std_logic;
signal level0 :  std_logic_vector(54 downto 0);
begin
   ps<= S;
   Xpadded <= X;
   level6<= Xpadded;
   stk5 <= '1' when (level6(31 downto 0)/="00000000000000000000000000000000" and ps(5)='1')   else '0';
   level5 <=  level6 when  ps(5)='0'    else (31 downto 0 => padBit) & level6(54 downto 32);
   stk4 <= '1' when (level5(15 downto 0)/="0000000000000000" and ps(4)='1') or stk5 ='1'   else '0';
   level4 <=  level5 when  ps(4)='0'    else (15 downto 0 => padBit) & level5(54 downto 16);
   stk3 <= '1' when (level4(7 downto 0)/="00000000" and ps(3)='1') or stk4 ='1'   else '0';
   level3 <=  level4 when  ps(3)='0'    else (7 downto 0 => padBit) & level4(54 downto 8);
   stk2 <= '1' when (level3(3 downto 0)/="0000" and ps(2)='1') or stk3 ='1'   else '0';
   level2 <=  level3 when  ps(2)='0'    else (3 downto 0 => padBit) & level3(54 downto 4);
   stk1 <= '1' when (level2(1 downto 0)/="00" and ps(1)='1') or stk2 ='1'   else '0';
   level1 <=  level2 when  ps(1)='0'    else (1 downto 0 => padBit) & level2(54 downto 2);
   stk0 <= '1' when (level1(0 downto 0)/="0" and ps(0)='1') or stk1 ='1'   else '0';
   level0 <=  level1 when  ps(0)='0'    else (0 downto 0 => padBit) & level1(54 downto 1);
   R <= level0;
   Sticky <= stk0;
end architecture;

--------------------------------------------------------------------------------
--                          PIF2Posit_55_8_F0_uid18
-- VHDL generated for Kintex7 @ 0MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Oregane Desrentes 2019
--------------------------------------------------------------------------------
-- combinatorial
-- Clock period (ns): inf
-- Target frequency (MHz): 0
-- Input signals: I
-- Output signals: O

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PIF2Posit_55_8_F0_uid18 is
    port (I : in  std_logic_vector(63 downto 0);
          O : out  std_logic_vector(54 downto 0)   );
end entity;

architecture arch of PIF2Posit_55_8_F0_uid18 is
   component RightShifterSticky55_by_max_55_F0_uid20 is
      port ( X : in  std_logic_vector(54 downto 0);
             S : in  std_logic_vector(5 downto 0);
             padBit : in  std_logic;
             R : out  std_logic_vector(54 downto 0);
             Sticky : out  std_logic   );
   end component;

signal is_NAR :  std_logic;
signal s :  std_logic;
signal biased_exponent :  std_logic_vector(14 downto 0);
signal fraction :  std_logic_vector(44 downto 0);
signal is_zero :  std_logic;
signal exponent :  std_logic_vector(14 downto 0);
signal partial_exponent :  std_logic_vector(7 downto 0);
signal partial_exponent_us :  std_logic_vector(7 downto 0);
signal bin_regime :  std_logic_vector(5 downto 0);
signal first_regime :  std_logic;
signal regime :  std_logic_vector(5 downto 0);
signal pad :  std_logic;
signal start_regime :  std_logic_vector(1 downto 0);
signal input_shifter :  std_logic_vector(54 downto 0);
signal extended_posit :  std_logic_vector(54 downto 0);
signal pre_sticky :  std_logic;
signal truncated_posit :  std_logic_vector(53 downto 0);
signal lsb :  std_logic;
signal guard :  std_logic;
signal sticky :  std_logic;
signal round_bit :  std_logic;
signal rounded_reg_exp_frac :  std_logic_vector(53 downto 0);
signal rounded_posit :  std_logic_vector(54 downto 0);
signal rounded_posit_zero :  std_logic_vector(54 downto 0);
begin
--------------------------- Start of vhdl generation ---------------------------
is_NAR<= I(63);
s<= I(62);
biased_exponent<= I(61 downto 47);
fraction<= I(45 downto 1);
is_zero<= '1' when I(63 downto 0) = "0000000000000000000000000000000000000000000000000000000000000000" else '0';
exponent<= biased_exponent - 13569;
partial_exponent<= exponent(7 downto 0);
with s  select  partial_exponent_us <= 
   partial_exponent when '0',
   not partial_exponent when '1',
   "--------" when others;
bin_regime<= exponent(13 downto 8);
first_regime<= exponent(14);
with first_regime  select  regime <= 
   bin_regime when '0', 
   not bin_regime when '1', 
   "------" when others;
pad<= not(first_regime xor s);
with pad  select  start_regime <= 
   "01" when '0', 
   "10" when '1', 
   "--" when others;
input_shifter<= start_regime & partial_exponent_us & fraction;
   rshift: RightShifterSticky55_by_max_55_F0_uid20
      port map ( S => regime,
                 X => input_shifter,
                 padBit => pad,
                 R => extended_posit,
                 Sticky => pre_sticky);
truncated_posit<= extended_posit(54 downto 1);
lsb<= extended_posit(1);
guard<= extended_posit(0);
sticky<= I(0) or pre_sticky;
round_bit<= guard and (sticky or lsb);
rounded_reg_exp_frac<= truncated_posit + round_bit;
rounded_posit<= s & rounded_reg_exp_frac;
rounded_posit_zero<= rounded_posit when is_zero= '0' else "0000000000000000000000000000000000000000000000000000000";
O <= rounded_posit_zero when is_NAR = '0' else "1000000000000000000000000000000000000000000000000000000";
---------------------------- End of vhdl generation ----------------------------
end architecture;

--------------------------------------------------------------------------------
--                           PositAdd_55_8_F0_uid2
-- VHDL generated for Kintex7 @ 0MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Oregane Desrentes 2019
--------------------------------------------------------------------------------
-- combinatorial
-- Clock period (ns): inf
-- Target frequency (MHz): 0
-- Input signals: X Y
-- Output signals: R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PositAdd_55_8_F0_uid2 is
    port (X : in  std_logic_vector(54 downto 0);
          Y : in  std_logic_vector(54 downto 0);
          R : out  std_logic_vector(54 downto 0)   );
end entity;

architecture arch of PositAdd_55_8_F0_uid2 is
   component Posit2PIF_55_8_F0_uid4 is
      port ( I : in  std_logic_vector(54 downto 0);
             O : out  std_logic_vector(63 downto 0)   );
   end component;

   component Posit2PIF_55_8_F0_uid8 is
      port ( I : in  std_logic_vector(54 downto 0);
             O : out  std_logic_vector(63 downto 0)   );
   end component;

   component PIFAdd_15_44_F0_uid12 is
      port ( X : in  std_logic_vector(63 downto 0);
             Y : in  std_logic_vector(63 downto 0);
             R : out  std_logic_vector(63 downto 0)   );
   end component;

   component PIF2Posit_55_8_F0_uid18 is
      port ( I : in  std_logic_vector(63 downto 0);
             O : out  std_logic_vector(54 downto 0)   );
   end component;

signal X_PIF :  std_logic_vector(63 downto 0);
signal Y_PIF :  std_logic_vector(63 downto 0);
signal R_PIF :  std_logic_vector(63 downto 0);
begin
--------------------------- Start of vhdl generation ---------------------------
   X_conversion: Posit2PIF_55_8_F0_uid4
      port map ( I => X,
                 O => X_PIF);
   Y_conversion: Posit2PIF_55_8_F0_uid8
      port map ( I => Y,
                 O => Y_PIF);
   Addition: PIFAdd_15_44_F0_uid12
      port map ( X => X_PIF,
                 Y => Y_PIF,
                 R => R_PIF);
   R_conversion: PIF2Posit_55_8_F0_uid18
      port map ( I => R_PIF,
                 O => R);
---------------------------- End of vhdl generation ----------------------------
end architecture;

