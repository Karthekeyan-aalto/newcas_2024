--------------------------------------------------------------------------------
--                RightShifterSticky15_by_max_17_Freq800_uid4
-- VHDL generated for Virtex6 @ 800MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca (2008-2011), Florent de Dinechin (2008-2019)
--------------------------------------------------------------------------------
-- Pipeline depth: 8 cycles
-- Clock period (ns): 1.25
-- Target frequency (MHz): 800
-- Input signals: X S
-- Output signals: R Sticky

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity RightShifterSticky15_by_max_17_Freq800_uid4 is
    port (clk : in std_logic;
          X : in  std_logic_vector(14 downto 0);
          S : in  std_logic_vector(4 downto 0);
          R : out  std_logic_vector(16 downto 0);
          Sticky : out  std_logic   );
end entity;

architecture arch of RightShifterSticky15_by_max_17_Freq800_uid4 is
signal ps, ps_d1, ps_d2, ps_d3, ps_d4, ps_d5, ps_d6, ps_d7, ps_d8 :  std_logic_vector(4 downto 0);
signal Xpadded :  std_logic_vector(16 downto 0);
signal level5, level5_d1, level5_d2, level5_d3 :  std_logic_vector(16 downto 0);
signal stk4, stk4_d1 :  std_logic;
signal level4, level4_d1, level4_d2, level4_d3 :  std_logic_vector(16 downto 0);
signal stk3, stk3_d1, stk3_d2 :  std_logic;
signal level3, level3_d1, level3_d2, level3_d3, level3_d4 :  std_logic_vector(16 downto 0);
signal stk2, stk2_d1 :  std_logic;
signal level2, level2_d1, level2_d2, level2_d3, level2_d4, level2_d5 :  std_logic_vector(16 downto 0);
signal stk1, stk1_d1, stk1_d2 :  std_logic;
signal level1, level1_d1, level1_d2, level1_d3, level1_d4, level1_d5, level1_d6, level1_d7 :  std_logic_vector(16 downto 0);
signal stk0 :  std_logic;
signal level0 :  std_logic_vector(16 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            ps_d1 <=  ps;
            ps_d2 <=  ps_d1;
            ps_d3 <=  ps_d2;
            ps_d4 <=  ps_d3;
            ps_d5 <=  ps_d4;
            ps_d6 <=  ps_d5;
            ps_d7 <=  ps_d6;
            ps_d8 <=  ps_d7;
            level5_d1 <=  level5;
            level5_d2 <=  level5_d1;
            level5_d3 <=  level5_d2;
            stk4_d1 <=  stk4;
            level4_d1 <=  level4;
            level4_d2 <=  level4_d1;
            level4_d3 <=  level4_d2;
            stk3_d1 <=  stk3;
            stk3_d2 <=  stk3_d1;
            level3_d1 <=  level3;
            level3_d2 <=  level3_d1;
            level3_d3 <=  level3_d2;
            level3_d4 <=  level3_d3;
            stk2_d1 <=  stk2;
            level2_d1 <=  level2;
            level2_d2 <=  level2_d1;
            level2_d3 <=  level2_d2;
            level2_d4 <=  level2_d3;
            level2_d5 <=  level2_d4;
            stk1_d1 <=  stk1;
            stk1_d2 <=  stk1_d1;
            level1_d1 <=  level1;
            level1_d2 <=  level1_d1;
            level1_d3 <=  level1_d2;
            level1_d4 <=  level1_d3;
            level1_d5 <=  level1_d4;
            level1_d6 <=  level1_d5;
            level1_d7 <=  level1_d6;
         end if;
      end process;
   ps<= S;
   Xpadded <= X&(1 downto 0 => '0');
   level5<= Xpadded;
   stk4 <= '1' when (level5_d3(15 downto 0)/="0000000000000000" and ps_d2(4)='1')   else '0';
   level4 <=  level5_d1 when  ps(4)='0'    else (15 downto 0 => '0') & level5_d1(16 downto 16);
   stk3 <= '1' when (level4_d3(7 downto 0)/="00000000" and ps_d3(3)='1') or stk4_d1 ='1'   else '0';
   level3 <=  level4_d1 when  ps_d1(3)='0'    else (7 downto 0 => '0') & level4_d1(16 downto 8);
   stk2 <= '1' when (level3_d4(3 downto 0)/="0000" and ps_d5(2)='1') or stk3_d2 ='1'   else '0';
   level2 <=  level3 when  ps_d1(2)='0'    else (3 downto 0 => '0') & level3(16 downto 4);
   stk1 <= '1' when (level2_d5(1 downto 0)/="00" and ps_d6(1)='1') or stk2_d1 ='1'   else '0';
   level1 <=  level2 when  ps_d1(1)='0'    else (1 downto 0 => '0') & level2(16 downto 2);
   stk0 <= '1' when (level1_d7(0 downto 0)/="0" and ps_d8(0)='1') or stk1_d2 ='1'   else '0';
   level0 <=  level1 when  ps_d1(0)='0'    else (0 downto 0 => '0') & level1(16 downto 1);
   R <= level0;
   Sticky <= stk0;
end architecture;

--------------------------------------------------------------------------------
--                          IntAdder_18_Freq800_uid6
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

entity IntAdder_18_Freq800_uid6 is
    port (clk : in std_logic;
          X : in  std_logic_vector(17 downto 0);
          Y : in  std_logic_vector(17 downto 0);
          Cin : in  std_logic;
          R : out  std_logic_vector(17 downto 0)   );
end entity;

architecture arch of IntAdder_18_Freq800_uid6 is
signal Cin_1, Cin_1_d1 :  std_logic;
signal X_1, X_1_d1, X_1_d2, X_1_d3, X_1_d4, X_1_d5, X_1_d6, X_1_d7, X_1_d8, X_1_d9, X_1_d10 :  std_logic_vector(15 downto 0);
signal Y_1, Y_1_d1, Y_1_d2, Y_1_d3, Y_1_d4, Y_1_d5, Y_1_d6, Y_1_d7, Y_1_d8 :  std_logic_vector(15 downto 0);
signal S_1 :  std_logic_vector(15 downto 0);
signal R_1, R_1_d1 :  std_logic_vector(14 downto 0);
signal Cin_2, Cin_2_d1 :  std_logic;
signal X_2, X_2_d1, X_2_d2, X_2_d3, X_2_d4, X_2_d5, X_2_d6, X_2_d7, X_2_d8, X_2_d9, X_2_d10, X_2_d11 :  std_logic_vector(3 downto 0);
signal Y_2, Y_2_d1, Y_2_d2, Y_2_d3, Y_2_d4, Y_2_d5, Y_2_d6, Y_2_d7, Y_2_d8, Y_2_d9 :  std_logic_vector(3 downto 0);
signal S_2 :  std_logic_vector(3 downto 0);
signal R_2 :  std_logic_vector(2 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            Cin_1_d1 <=  Cin_1;
            X_1_d1 <=  X_1;
            X_1_d2 <=  X_1_d1;
            X_1_d3 <=  X_1_d2;
            X_1_d4 <=  X_1_d3;
            X_1_d5 <=  X_1_d4;
            X_1_d6 <=  X_1_d5;
            X_1_d7 <=  X_1_d6;
            X_1_d8 <=  X_1_d7;
            X_1_d9 <=  X_1_d8;
            X_1_d10 <=  X_1_d9;
            Y_1_d1 <=  Y_1;
            Y_1_d2 <=  Y_1_d1;
            Y_1_d3 <=  Y_1_d2;
            Y_1_d4 <=  Y_1_d3;
            Y_1_d5 <=  Y_1_d4;
            Y_1_d6 <=  Y_1_d5;
            Y_1_d7 <=  Y_1_d6;
            Y_1_d8 <=  Y_1_d7;
            R_1_d1 <=  R_1;
            Cin_2_d1 <=  Cin_2;
            X_2_d1 <=  X_2;
            X_2_d2 <=  X_2_d1;
            X_2_d3 <=  X_2_d2;
            X_2_d4 <=  X_2_d3;
            X_2_d5 <=  X_2_d4;
            X_2_d6 <=  X_2_d5;
            X_2_d7 <=  X_2_d6;
            X_2_d8 <=  X_2_d7;
            X_2_d9 <=  X_2_d8;
            X_2_d10 <=  X_2_d9;
            X_2_d11 <=  X_2_d10;
            Y_2_d1 <=  Y_2;
            Y_2_d2 <=  Y_2_d1;
            Y_2_d3 <=  Y_2_d2;
            Y_2_d4 <=  Y_2_d3;
            Y_2_d5 <=  Y_2_d4;
            Y_2_d6 <=  Y_2_d5;
            Y_2_d7 <=  Y_2_d6;
            Y_2_d8 <=  Y_2_d7;
            Y_2_d9 <=  Y_2_d8;
         end if;
      end process;
   Cin_1 <= Cin;
   X_1 <= '0' & X(14 downto 0);
   Y_1 <= '0' & Y(14 downto 0);
   S_1 <= X_1_d10 + Y_1_d8 + Cin_1_d1;
   R_1 <= S_1(14 downto 0);
   Cin_2 <= S_1(15);
   X_2 <= '0' & X(17 downto 15);
   Y_2 <= '0' & Y(17 downto 15);
   S_2 <= X_2_d11 + Y_2_d9 + Cin_2_d1;
   R_2 <= S_2(2 downto 0);
   R <= R_2 & R_1_d1 ;
end architecture;

--------------------------------------------------------------------------------
--                     Normalizer_Z_19_19_19_Freq800_uid8
-- VHDL generated for Virtex6 @ 800MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, (2007-2020)
--------------------------------------------------------------------------------
-- Pipeline depth: 7 cycles
-- Clock period (ns): 1.25
-- Target frequency (MHz): 800
-- Input signals: X
-- Output signals: Count R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Normalizer_Z_19_19_19_Freq800_uid8 is
    port (clk : in std_logic;
          X : in  std_logic_vector(18 downto 0);
          Count : out  std_logic_vector(4 downto 0);
          R : out  std_logic_vector(18 downto 0)   );
end entity;

architecture arch of Normalizer_Z_19_19_19_Freq800_uid8 is
signal level5, level5_d1 :  std_logic_vector(18 downto 0);
signal count4, count4_d1, count4_d2, count4_d3, count4_d4, count4_d5, count4_d6 :  std_logic;
signal level4, level4_d1, level4_d2 :  std_logic_vector(18 downto 0);
signal count3, count3_d1, count3_d2, count3_d3, count3_d4, count3_d5 :  std_logic;
signal level3, level3_d1 :  std_logic_vector(18 downto 0);
signal count2, count2_d1, count2_d2, count2_d3 :  std_logic;
signal level2, level2_d1, level2_d2 :  std_logic_vector(18 downto 0);
signal count1, count1_d1, count1_d2 :  std_logic;
signal level1, level1_d1 :  std_logic_vector(18 downto 0);
signal count0 :  std_logic;
signal level0 :  std_logic_vector(18 downto 0);
signal sCount :  std_logic_vector(4 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            level5_d1 <=  level5;
            count4_d1 <=  count4;
            count4_d2 <=  count4_d1;
            count4_d3 <=  count4_d2;
            count4_d4 <=  count4_d3;
            count4_d5 <=  count4_d4;
            count4_d6 <=  count4_d5;
            level4_d1 <=  level4;
            level4_d2 <=  level4_d1;
            count3_d1 <=  count3;
            count3_d2 <=  count3_d1;
            count3_d3 <=  count3_d2;
            count3_d4 <=  count3_d3;
            count3_d5 <=  count3_d4;
            level3_d1 <=  level3;
            count2_d1 <=  count2;
            count2_d2 <=  count2_d1;
            count2_d3 <=  count2_d2;
            level2_d1 <=  level2;
            level2_d2 <=  level2_d1;
            count1_d1 <=  count1;
            count1_d2 <=  count1_d1;
            level1_d1 <=  level1;
         end if;
      end process;
   level5 <= X ;
   count4<= '1' when level5_d1(18 downto 3) = (18 downto 3=>'0') else '0';
   level4<= level5_d1(18 downto 0) when count4='0' else level5_d1(2 downto 0) & (15 downto 0 => '0');

   count3<= '1' when level4_d1(18 downto 11) = (18 downto 11=>'0') else '0';
   level3<= level4_d2(18 downto 0) when count3_d1='0' else level4_d2(10 downto 0) & (7 downto 0 => '0');

   count2<= '1' when level3_d1(18 downto 15) = (18 downto 15=>'0') else '0';
   level2<= level3_d1(18 downto 0) when count2='0' else level3_d1(14 downto 0) & (3 downto 0 => '0');

   count1<= '1' when level2_d1(18 downto 17) = (18 downto 17=>'0') else '0';
   level1<= level2_d2(18 downto 0) when count1_d1='0' else level2_d2(16 downto 0) & (1 downto 0 => '0');

   count0<= '1' when level1_d1(18 downto 18) = (18 downto 18=>'0') else '0';
   level0<= level1_d1(18 downto 0) when count0='0' else level1_d1(17 downto 0) & (0 downto 0 => '0');

   R <= level0;
   sCount <= count4_d6 & count3_d5 & count2_d3 & count1_d2 & count0;
   Count <= sCount;
end architecture;

--------------------------------------------------------------------------------
--                         IntAdder_24_Freq800_uid11
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

entity IntAdder_24_Freq800_uid11 is
    port (clk : in std_logic;
          X : in  std_logic_vector(23 downto 0);
          Y : in  std_logic_vector(23 downto 0);
          Cin : in  std_logic;
          R : out  std_logic_vector(23 downto 0)   );
end entity;

architecture arch of IntAdder_24_Freq800_uid11 is
signal Cin_1, Cin_1_d1 :  std_logic;
signal X_1, X_1_d1 :  std_logic_vector(15 downto 0);
signal Y_1, Y_1_d1, Y_1_d2, Y_1_d3, Y_1_d4, Y_1_d5, Y_1_d6, Y_1_d7, Y_1_d8, Y_1_d9, Y_1_d10, Y_1_d11, Y_1_d12, Y_1_d13, Y_1_d14, Y_1_d15, Y_1_d16, Y_1_d17, Y_1_d18, Y_1_d19, Y_1_d20, Y_1_d21 :  std_logic_vector(15 downto 0);
signal S_1 :  std_logic_vector(15 downto 0);
signal R_1, R_1_d1 :  std_logic_vector(14 downto 0);
signal Cin_2, Cin_2_d1 :  std_logic;
signal X_2, X_2_d1, X_2_d2 :  std_logic_vector(9 downto 0);
signal Y_2, Y_2_d1, Y_2_d2, Y_2_d3, Y_2_d4, Y_2_d5, Y_2_d6, Y_2_d7, Y_2_d8, Y_2_d9, Y_2_d10, Y_2_d11, Y_2_d12, Y_2_d13, Y_2_d14, Y_2_d15, Y_2_d16, Y_2_d17, Y_2_d18, Y_2_d19, Y_2_d20, Y_2_d21, Y_2_d22 :  std_logic_vector(9 downto 0);
signal S_2 :  std_logic_vector(9 downto 0);
signal R_2 :  std_logic_vector(8 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            Cin_1_d1 <=  Cin_1;
            X_1_d1 <=  X_1;
            Y_1_d1 <=  Y_1;
            Y_1_d2 <=  Y_1_d1;
            Y_1_d3 <=  Y_1_d2;
            Y_1_d4 <=  Y_1_d3;
            Y_1_d5 <=  Y_1_d4;
            Y_1_d6 <=  Y_1_d5;
            Y_1_d7 <=  Y_1_d6;
            Y_1_d8 <=  Y_1_d7;
            Y_1_d9 <=  Y_1_d8;
            Y_1_d10 <=  Y_1_d9;
            Y_1_d11 <=  Y_1_d10;
            Y_1_d12 <=  Y_1_d11;
            Y_1_d13 <=  Y_1_d12;
            Y_1_d14 <=  Y_1_d13;
            Y_1_d15 <=  Y_1_d14;
            Y_1_d16 <=  Y_1_d15;
            Y_1_d17 <=  Y_1_d16;
            Y_1_d18 <=  Y_1_d17;
            Y_1_d19 <=  Y_1_d18;
            Y_1_d20 <=  Y_1_d19;
            Y_1_d21 <=  Y_1_d20;
            R_1_d1 <=  R_1;
            Cin_2_d1 <=  Cin_2;
            X_2_d1 <=  X_2;
            X_2_d2 <=  X_2_d1;
            Y_2_d1 <=  Y_2;
            Y_2_d2 <=  Y_2_d1;
            Y_2_d3 <=  Y_2_d2;
            Y_2_d4 <=  Y_2_d3;
            Y_2_d5 <=  Y_2_d4;
            Y_2_d6 <=  Y_2_d5;
            Y_2_d7 <=  Y_2_d6;
            Y_2_d8 <=  Y_2_d7;
            Y_2_d9 <=  Y_2_d8;
            Y_2_d10 <=  Y_2_d9;
            Y_2_d11 <=  Y_2_d10;
            Y_2_d12 <=  Y_2_d11;
            Y_2_d13 <=  Y_2_d12;
            Y_2_d14 <=  Y_2_d13;
            Y_2_d15 <=  Y_2_d14;
            Y_2_d16 <=  Y_2_d15;
            Y_2_d17 <=  Y_2_d16;
            Y_2_d18 <=  Y_2_d17;
            Y_2_d19 <=  Y_2_d18;
            Y_2_d20 <=  Y_2_d19;
            Y_2_d21 <=  Y_2_d20;
            Y_2_d22 <=  Y_2_d21;
         end if;
      end process;
   Cin_1 <= Cin;
   X_1 <= '0' & X(14 downto 0);
   Y_1 <= '0' & Y(14 downto 0);
   S_1 <= X_1_d1 + Y_1_d21 + Cin_1_d1;
   R_1 <= S_1(14 downto 0);
   Cin_2 <= S_1(15);
   X_2 <= '0' & X(23 downto 15);
   Y_2 <= '0' & Y(23 downto 15);
   S_2 <= X_2_d2 + Y_2_d22 + Cin_2_d1;
   R_2 <= S_2(8 downto 0);
   R <= R_2 & R_1_d1 ;
end architecture;

--------------------------------------------------------------------------------
--                          FPAdd_7_14_Freq800_uid2
-- VHDL generated for Virtex6 @ 800MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, Bogdan Pasca (2010-2017)
--------------------------------------------------------------------------------
-- Pipeline depth: 22 cycles
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

entity FPAdd_7_14_Freq800_uid2 is
    port (clk : in std_logic;
          X : in  std_logic_vector(7+14+2 downto 0);
          Y : in  std_logic_vector(7+14+2 downto 0);
          R : out  std_logic_vector(7+14+2 downto 0)   );
end entity;

architecture arch of FPAdd_7_14_Freq800_uid2 is
   component RightShifterSticky15_by_max_17_Freq800_uid4 is
      port ( clk : in std_logic;
             X : in  std_logic_vector(14 downto 0);
             S : in  std_logic_vector(4 downto 0);
             R : out  std_logic_vector(16 downto 0);
             Sticky : out  std_logic   );
   end component;

   component IntAdder_18_Freq800_uid6 is
      port ( clk : in std_logic;
             X : in  std_logic_vector(17 downto 0);
             Y : in  std_logic_vector(17 downto 0);
             Cin : in  std_logic;
             R : out  std_logic_vector(17 downto 0)   );
   end component;

   component Normalizer_Z_19_19_19_Freq800_uid8 is
      port ( clk : in std_logic;
             X : in  std_logic_vector(18 downto 0);
             Count : out  std_logic_vector(4 downto 0);
             R : out  std_logic_vector(18 downto 0)   );
   end component;

   component IntAdder_24_Freq800_uid11 is
      port ( clk : in std_logic;
             X : in  std_logic_vector(23 downto 0);
             Y : in  std_logic_vector(23 downto 0);
             Cin : in  std_logic;
             R : out  std_logic_vector(23 downto 0)   );
   end component;

signal excExpFracX :  std_logic_vector(22 downto 0);
signal excExpFracY :  std_logic_vector(22 downto 0);
signal swap, swap_d1 :  std_logic;
signal eXmeY, eXmeY_d1 :  std_logic_vector(6 downto 0);
signal eYmeX, eYmeX_d1 :  std_logic_vector(6 downto 0);
signal expDiff, expDiff_d1 :  std_logic_vector(6 downto 0);
signal newX :  std_logic_vector(23 downto 0);
signal newY :  std_logic_vector(23 downto 0);
signal expX, expX_d1 :  std_logic_vector(6 downto 0);
signal excX :  std_logic_vector(1 downto 0);
signal excY :  std_logic_vector(1 downto 0);
signal signX :  std_logic;
signal signY :  std_logic;
signal EffSub, EffSub_d1, EffSub_d2, EffSub_d3, EffSub_d4, EffSub_d5, EffSub_d6, EffSub_d7, EffSub_d8, EffSub_d9, EffSub_d10, EffSub_d11, EffSub_d12, EffSub_d13, EffSub_d14, EffSub_d15, EffSub_d16, EffSub_d17, EffSub_d18, EffSub_d19, EffSub_d20, EffSub_d21 :  std_logic;
signal sXsYExnXY :  std_logic_vector(5 downto 0);
signal sdExnXY :  std_logic_vector(3 downto 0);
signal fracY :  std_logic_vector(14 downto 0);
signal excRt, excRt_d1, excRt_d2, excRt_d3, excRt_d4, excRt_d5, excRt_d6, excRt_d7, excRt_d8, excRt_d9, excRt_d10, excRt_d11, excRt_d12, excRt_d13, excRt_d14, excRt_d15, excRt_d16, excRt_d17, excRt_d18, excRt_d19, excRt_d20, excRt_d21 :  std_logic_vector(1 downto 0);
signal signR, signR_d1, signR_d2, signR_d3, signR_d4, signR_d5, signR_d6, signR_d7, signR_d8, signR_d9, signR_d10, signR_d11, signR_d12, signR_d13, signR_d14, signR_d15, signR_d16, signR_d17, signR_d18 :  std_logic;
signal shiftedOut :  std_logic;
signal shiftVal :  std_logic_vector(4 downto 0);
signal shiftedFracY :  std_logic_vector(16 downto 0);
signal sticky, sticky_d1, sticky_d2 :  std_logic;
signal fracYpad :  std_logic_vector(17 downto 0);
signal EffSubVector, EffSubVector_d1, EffSubVector_d2 :  std_logic_vector(17 downto 0);
signal fracYpadXorOp :  std_logic_vector(17 downto 0);
signal fracXpad :  std_logic_vector(17 downto 0);
signal cInSigAdd :  std_logic;
signal fracAddResult :  std_logic_vector(17 downto 0);
signal fracSticky :  std_logic_vector(18 downto 0);
signal nZerosNew, nZerosNew_d1 :  std_logic_vector(4 downto 0);
signal shiftedFrac, shiftedFrac_d1 :  std_logic_vector(18 downto 0);
signal extendedExpInc, extendedExpInc_d1, extendedExpInc_d2, extendedExpInc_d3, extendedExpInc_d4, extendedExpInc_d5, extendedExpInc_d6, extendedExpInc_d7, extendedExpInc_d8, extendedExpInc_d9, extendedExpInc_d10, extendedExpInc_d11, extendedExpInc_d12, extendedExpInc_d13, extendedExpInc_d14, extendedExpInc_d15, extendedExpInc_d16, extendedExpInc_d17, extendedExpInc_d18 :  std_logic_vector(7 downto 0);
signal updatedExp :  std_logic_vector(8 downto 0);
signal eqdiffsign, eqdiffsign_d1, eqdiffsign_d2, eqdiffsign_d3 :  std_logic;
signal expFrac :  std_logic_vector(23 downto 0);
signal stk, stk_d1 :  std_logic;
signal rnd, rnd_d1 :  std_logic;
signal lsb, lsb_d1 :  std_logic;
signal needToRound :  std_logic;
signal RoundedExpFrac :  std_logic_vector(23 downto 0);
signal upExc :  std_logic_vector(1 downto 0);
signal fracR :  std_logic_vector(13 downto 0);
signal expR :  std_logic_vector(6 downto 0);
signal exExpExc :  std_logic_vector(3 downto 0);
signal excRt2 :  std_logic_vector(1 downto 0);
signal excR :  std_logic_vector(1 downto 0);
signal signR2, signR2_d1, signR2_d2, signR2_d3 :  std_logic;
signal computedR :  std_logic_vector(23 downto 0);
signal X_d1 :  std_logic_vector(7+14+2 downto 0);
signal Y_d1 :  std_logic_vector(7+14+2 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            swap_d1 <=  swap;
            eXmeY_d1 <=  eXmeY;
            eYmeX_d1 <=  eYmeX;
            expDiff_d1 <=  expDiff;
            expX_d1 <=  expX;
            EffSub_d1 <=  EffSub;
            EffSub_d2 <=  EffSub_d1;
            EffSub_d3 <=  EffSub_d2;
            EffSub_d4 <=  EffSub_d3;
            EffSub_d5 <=  EffSub_d4;
            EffSub_d6 <=  EffSub_d5;
            EffSub_d7 <=  EffSub_d6;
            EffSub_d8 <=  EffSub_d7;
            EffSub_d9 <=  EffSub_d8;
            EffSub_d10 <=  EffSub_d9;
            EffSub_d11 <=  EffSub_d10;
            EffSub_d12 <=  EffSub_d11;
            EffSub_d13 <=  EffSub_d12;
            EffSub_d14 <=  EffSub_d13;
            EffSub_d15 <=  EffSub_d14;
            EffSub_d16 <=  EffSub_d15;
            EffSub_d17 <=  EffSub_d16;
            EffSub_d18 <=  EffSub_d17;
            EffSub_d19 <=  EffSub_d18;
            EffSub_d20 <=  EffSub_d19;
            EffSub_d21 <=  EffSub_d20;
            excRt_d1 <=  excRt;
            excRt_d2 <=  excRt_d1;
            excRt_d3 <=  excRt_d2;
            excRt_d4 <=  excRt_d3;
            excRt_d5 <=  excRt_d4;
            excRt_d6 <=  excRt_d5;
            excRt_d7 <=  excRt_d6;
            excRt_d8 <=  excRt_d7;
            excRt_d9 <=  excRt_d8;
            excRt_d10 <=  excRt_d9;
            excRt_d11 <=  excRt_d10;
            excRt_d12 <=  excRt_d11;
            excRt_d13 <=  excRt_d12;
            excRt_d14 <=  excRt_d13;
            excRt_d15 <=  excRt_d14;
            excRt_d16 <=  excRt_d15;
            excRt_d17 <=  excRt_d16;
            excRt_d18 <=  excRt_d17;
            excRt_d19 <=  excRt_d18;
            excRt_d20 <=  excRt_d19;
            excRt_d21 <=  excRt_d20;
            signR_d1 <=  signR;
            signR_d2 <=  signR_d1;
            signR_d3 <=  signR_d2;
            signR_d4 <=  signR_d3;
            signR_d5 <=  signR_d4;
            signR_d6 <=  signR_d5;
            signR_d7 <=  signR_d6;
            signR_d8 <=  signR_d7;
            signR_d9 <=  signR_d8;
            signR_d10 <=  signR_d9;
            signR_d11 <=  signR_d10;
            signR_d12 <=  signR_d11;
            signR_d13 <=  signR_d12;
            signR_d14 <=  signR_d13;
            signR_d15 <=  signR_d14;
            signR_d16 <=  signR_d15;
            signR_d17 <=  signR_d16;
            signR_d18 <=  signR_d17;
            sticky_d1 <=  sticky;
            sticky_d2 <=  sticky_d1;
            EffSubVector_d1 <=  EffSubVector;
            EffSubVector_d2 <=  EffSubVector_d1;
            nZerosNew_d1 <=  nZerosNew;
            shiftedFrac_d1 <=  shiftedFrac;
            extendedExpInc_d1 <=  extendedExpInc;
            extendedExpInc_d2 <=  extendedExpInc_d1;
            extendedExpInc_d3 <=  extendedExpInc_d2;
            extendedExpInc_d4 <=  extendedExpInc_d3;
            extendedExpInc_d5 <=  extendedExpInc_d4;
            extendedExpInc_d6 <=  extendedExpInc_d5;
            extendedExpInc_d7 <=  extendedExpInc_d6;
            extendedExpInc_d8 <=  extendedExpInc_d7;
            extendedExpInc_d9 <=  extendedExpInc_d8;
            extendedExpInc_d10 <=  extendedExpInc_d9;
            extendedExpInc_d11 <=  extendedExpInc_d10;
            extendedExpInc_d12 <=  extendedExpInc_d11;
            extendedExpInc_d13 <=  extendedExpInc_d12;
            extendedExpInc_d14 <=  extendedExpInc_d13;
            extendedExpInc_d15 <=  extendedExpInc_d14;
            extendedExpInc_d16 <=  extendedExpInc_d15;
            extendedExpInc_d17 <=  extendedExpInc_d16;
            extendedExpInc_d18 <=  extendedExpInc_d17;
            eqdiffsign_d1 <=  eqdiffsign;
            eqdiffsign_d2 <=  eqdiffsign_d1;
            eqdiffsign_d3 <=  eqdiffsign_d2;
            stk_d1 <=  stk;
            rnd_d1 <=  rnd;
            lsb_d1 <=  lsb;
            signR2_d1 <=  signR2;
            signR2_d2 <=  signR2_d1;
            signR2_d3 <=  signR2_d2;
            X_d1 <=  X;
            Y_d1 <=  Y;
         end if;
      end process;
   excExpFracX <= X(23 downto 22) & X(20 downto 0);
   excExpFracY <= Y(23 downto 22) & Y(20 downto 0);
   swap <= '1' when excExpFracX < excExpFracY else '0';
   -- exponent difference
   eXmeY <= (X(20 downto 14)) - (Y(20 downto 14));
   eYmeX <= (Y(20 downto 14)) - (X(20 downto 14));
   expDiff <= eXmeY_d1 when swap_d1 = '0' else eYmeX_d1;
   -- input swap so that |X|>|Y|
   newX <= X_d1 when swap_d1 = '0' else Y_d1;
   newY <= Y_d1 when swap_d1 = '0' else X_d1;
   -- now we decompose the inputs into their sign, exponent, fraction
   expX<= newX(20 downto 14);
   excX<= newX(23 downto 22);
   excY<= newY(23 downto 22);
   signX<= newX(21);
   signY<= newY(21);
   EffSub <= signX xor signY;
   sXsYExnXY <= signX & signY & excX & excY;
   sdExnXY <= excX & excY;
   fracY <= "000000000000000" when excY="00" else ('1' & newY(13 downto 0));
   -- Exception management logic
   with sXsYExnXY  select  
   excRt <= "00" when "000000"|"010000"|"100000"|"110000",
      "01" when "000101"|"010101"|"100101"|"110101"|"000100"|"010100"|"100100"|"110100"|"000001"|"010001"|"100001"|"110001",
      "10" when "111010"|"001010"|"001000"|"011000"|"101000"|"111000"|"000010"|"010010"|"100010"|"110010"|"001001"|"011001"|"101001"|"111001"|"000110"|"010110"|"100110"|"110110", 
      "11" when others;
   signR<= '0' when (sXsYExnXY="100000" or sXsYExnXY="010000") else signX;
   shiftedOut <= '1' when (expDiff_d1 > 16) else '0';
   shiftVal <= expDiff_d1(4 downto 0) when shiftedOut='0' else CONV_STD_LOGIC_VECTOR(17,5);
   RightShifterComponent: RightShifterSticky15_by_max_17_Freq800_uid4
      port map ( clk  => clk,
                 S => shiftVal,
                 X => fracY,
                 R => shiftedFracY,
                 Sticky => sticky);
   fracYpad <= "0" & shiftedFracY;
   EffSubVector <= (17 downto 0 => EffSub);
   fracYpadXorOp <= fracYpad xor EffSubVector_d2;
   fracXpad <= "01" & (newX(13 downto 0)) & "00";
   cInSigAdd <= EffSub_d9 and not sticky; -- if we subtract and the sticky was one, some of the negated sticky bits would have absorbed this carry 
   fracAdder: IntAdder_18_Freq800_uid6
      port map ( clk  => clk,
                 Cin => cInSigAdd,
                 X => fracXpad,
                 Y => fracYpadXorOp,
                 R => fracAddResult);
   fracSticky<= fracAddResult & sticky_d2; 
   LZCAndShifter: Normalizer_Z_19_19_19_Freq800_uid8
      port map ( clk  => clk,
                 X => fracSticky,
                 Count => nZerosNew,
                 R => shiftedFrac);
   extendedExpInc<= ("0" & expX_d1) + '1';
   updatedExp <= ("0" &extendedExpInc_d18) - ("0000" & nZerosNew_d1);
   eqdiffsign <= '1' when nZerosNew="11111" else '0';
   expFrac<= updatedExp & shiftedFrac_d1(17 downto 3);
   stk<= shiftedFrac(2) or shiftedFrac(1) or shiftedFrac(0);
   rnd<= shiftedFrac(3);
   lsb<= shiftedFrac(4);
   needToRound<= '1' when (rnd_d1='1' and stk_d1='1') or (rnd_d1='1' and stk_d1='0' and lsb_d1='1')
  else '0';
   roundingAdder: IntAdder_24_Freq800_uid11
      port map ( clk  => clk,
                 Cin => needToRound,
                 X => expFrac,
                 Y => "000000000000000000000000",
                 R => RoundedExpFrac);
   -- possible update to exception bits
   upExc <= RoundedExpFrac(23 downto 22);
   fracR <= RoundedExpFrac(14 downto 1);
   expR <= RoundedExpFrac(21 downto 15);
   exExpExc <= upExc & excRt_d21;
   with exExpExc  select  
   excRt2<= "00" when "0000"|"0100"|"1000"|"1100"|"1001"|"1101",
      "01" when "0001",
      "10" when "0010"|"0110"|"1010"|"1110"|"0101",
      "11" when others;
   excR <= "00" when (eqdiffsign_d3='1' and EffSub_d21='1'  and not(excRt_d21="11")) else excRt2;
   signR2 <= '0' when (eqdiffsign='1' and EffSub_d18='1') else signR_d18;
   computedR <= excR & signR2_d3 & expR & fracR;
   R <= computedR;
end architecture;

