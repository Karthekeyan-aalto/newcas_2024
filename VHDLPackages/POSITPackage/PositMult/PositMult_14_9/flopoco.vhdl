--------------------------------------------------------------------------------
--                    SmallMultTableP3x3r6XuYu_comb_uid32
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin (2007-2012)
--------------------------------------------------------------------------------
library ieee; 
use ieee.std_logic_1164.all;
library work;
entity SmallMultTableP3x3r6XuYu_comb_uid32 is
   port ( X : in  std_logic_vector(5 downto 0);
          Y : out  std_logic_vector(5 downto 0)   );
end entity;

architecture arch of SmallMultTableP3x3r6XuYu_comb_uid32 is
signal TableOut :  std_logic_vector(5 downto 0);
begin
  with X select TableOut <= 
   "000000" when "000000",
   "000000" when "000001",
   "000000" when "000010",
   "000000" when "000011",
   "000000" when "000100",
   "000000" when "000101",
   "000000" when "000110",
   "000000" when "000111",
   "000000" when "001000",
   "000001" when "001001",
   "000010" when "001010",
   "000011" when "001011",
   "000100" when "001100",
   "000101" when "001101",
   "000110" when "001110",
   "000111" when "001111",
   "000000" when "010000",
   "000010" when "010001",
   "000100" when "010010",
   "000110" when "010011",
   "001000" when "010100",
   "001010" when "010101",
   "001100" when "010110",
   "001110" when "010111",
   "000000" when "011000",
   "000011" when "011001",
   "000110" when "011010",
   "001001" when "011011",
   "001100" when "011100",
   "001111" when "011101",
   "010010" when "011110",
   "010101" when "011111",
   "000000" when "100000",
   "000100" when "100001",
   "001000" when "100010",
   "001100" when "100011",
   "010000" when "100100",
   "010100" when "100101",
   "011000" when "100110",
   "011100" when "100111",
   "000000" when "101000",
   "000101" when "101001",
   "001010" when "101010",
   "001111" when "101011",
   "010100" when "101100",
   "011001" when "101101",
   "011110" when "101110",
   "100011" when "101111",
   "000000" when "110000",
   "000110" when "110001",
   "001100" when "110010",
   "010010" when "110011",
   "011000" when "110100",
   "011110" when "110101",
   "100100" when "110110",
   "101010" when "110111",
   "000000" when "111000",
   "000111" when "111001",
   "001110" when "111010",
   "010101" when "111011",
   "011100" when "111100",
   "100011" when "111101",
   "101010" when "111110",
   "110001" when "111111",
   "------" when others;
    Y <= TableOut;
end architecture;

--------------------------------------------------------------------------------
--                             LZOC_13_comb_uid6
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, Bogdan Pasca (2007)
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity LZOC_13_comb_uid6 is
   port ( I : in  std_logic_vector(12 downto 0);
          OZB : in  std_logic;
          O : out  std_logic_vector(3 downto 0)   );
end entity;

architecture arch of LZOC_13_comb_uid6 is
signal sozb :  std_logic;
signal level4 :  std_logic_vector(15 downto 0);
signal digit4 :  std_logic;
signal level3 :  std_logic_vector(7 downto 0);
signal digit3 :  std_logic;
signal level2 :  std_logic_vector(3 downto 0);
signal digit2 :  std_logic;
signal level1 :  std_logic_vector(1 downto 0);
signal digit1 :  std_logic;
begin
   sozb <= OZB;
   level4<= I& (2 downto 0 => not(sozb));
   digit4<= '1' when level4(15 downto 8) = (15 downto 8 => sozb) else '0';
   level3<= level4(7 downto 0) when digit4='1' else level4(15 downto 8);
   digit3<= '1' when level3(7 downto 4) = (7 downto 4 => sozb) else '0';
   level2<= level3(3 downto 0) when digit3='1' else level3(7 downto 4);
   digit2<= '1' when level2(3 downto 2) = (3 downto 2 => sozb) else '0';
   level1<= level2(1 downto 0) when digit2='1' else level2(3 downto 2);
   digit1<= '1' when level1(1 downto 1) = (1 downto 1 => sozb) else '0';
   O <= digit4 & digit3 & digit2 & digit1;
end architecture;

--------------------------------------------------------------------------------
--                    LeftShifter_13_by_max_13_comb_uid10
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca, Florent de Dinechin (2008-2011)
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity LeftShifter_13_by_max_13_comb_uid10 is
   port ( X : in  std_logic_vector(12 downto 0);
          S : in  std_logic_vector(3 downto 0);
          R : out  std_logic_vector(25 downto 0)   );
end entity;

architecture arch of LeftShifter_13_by_max_13_comb_uid10 is
signal level0 :  std_logic_vector(12 downto 0);
signal ps :  std_logic_vector(3 downto 0);
signal level1 :  std_logic_vector(13 downto 0);
signal level2 :  std_logic_vector(15 downto 0);
signal level3 :  std_logic_vector(19 downto 0);
signal level4 :  std_logic_vector(27 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<= level0 & (0 downto 0 => '0') when ps(0)= '1' else     (0 downto 0 => '0') & level0;
   level2<= level1 & (1 downto 0 => '0') when ps(1)= '1' else     (1 downto 0 => '0') & level1;
   level3<= level2 & (3 downto 0 => '0') when ps(2)= '1' else     (3 downto 0 => '0') & level2;
   level4<= level3 & (7 downto 0 => '0') when ps(3)= '1' else     (7 downto 0 => '0') & level3;
   R <= level4(25 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                        PositDecoder_14_9_comb_uid4
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Raul Murillo, 2019
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PositDecoder_14_9_comb_uid4 is
   port ( Input : in  std_logic_vector(13 downto 0);
          Sign : out  std_logic;
          Reg : out  std_logic_vector(4 downto 0);
          Exp : out  std_logic_vector(8 downto 0);
          Frac : out  std_logic_vector(2 downto 0);
          z : out  std_logic;
          inf : out  std_logic   );
end entity;

architecture arch of PositDecoder_14_9_comb_uid4 is
   component LZOC_13_comb_uid6 is
      port ( I : in  std_logic_vector(12 downto 0);
             OZB : in  std_logic;
             O : out  std_logic_vector(3 downto 0)   );
   end component;

   component LeftShifter_13_by_max_13_comb_uid10 is
      port ( X : in  std_logic_vector(12 downto 0);
             S : in  std_logic_vector(3 downto 0);
             R : out  std_logic_vector(25 downto 0)   );
   end component;

signal nzero :  std_logic;
signal my_sign :  std_logic;
signal rep_sign :  std_logic_vector(12 downto 0);
signal twos :  std_logic_vector(12 downto 0);
signal rc :  std_logic;
signal rep_rc :  std_logic_vector(12 downto 0);
signal inv :  std_logic_vector(12 downto 0);
signal zero_var :  std_logic;
signal zc :  std_logic_vector(3 downto 0);
signal zc_sub :  std_logic_vector(3 downto 0);
signal shifted_twos :  std_logic_vector(25 downto 0);
signal tmp :  std_logic_vector(10 downto 0);
begin
-------------------------------- Special Cases --------------------------------
   nzero <= '0' when Input(12 downto 0) = 0 else '1';
   -- 1 if Input is zero
   z <= Input(13) NOR nzero;
   -- 1 if Input is infinity
   inf <= Input(13) AND (NOT nzero);
------------------------------- Extract Sign bit -------------------------------
   my_sign <= Input(13);
   Sign <= my_sign;
--------------------------- 2's Complement of Input ---------------------------
   rep_sign <= (others => my_sign);
   twos <= (rep_sign XOR Input(12 downto 0)) + my_sign;
   rc <= twos(12);
------------------------ Count leading zeros of regime ------------------------
   rep_rc <= (others => rc);
   -- Invert 2's
   inv <= rep_rc XOR twos;
   zero_var <= '0';
   LZOC_Component: LZOC_13_comb_uid6
      port map ( I => inv,
                 O => zc,
                 OZB => zero_var);
----------------------------- Shift out the regime -----------------------------
   zc_sub <= zc - 1;
   LeftShifterComponent: LeftShifter_13_by_max_13_comb_uid10
      port map ( R => shifted_twos,
                 S => zc_sub,
                 X => twos);
   tmp <= shifted_twos(10 downto 0);
------------------------ Extract fraction and exponent ------------------------
   Frac <= nzero & tmp(1 downto 0);
   Exp <= tmp(10 downto 2);
-------------------------------- Select regime --------------------------------
   Reg <= '0' & zc_sub when rc = '1' else NOT('0' & zc) + 1;
end architecture;

--------------------------------------------------------------------------------
--                             LZOC_13_comb_uid18
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, Bogdan Pasca (2007)
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity LZOC_13_comb_uid18 is
   port ( I : in  std_logic_vector(12 downto 0);
          OZB : in  std_logic;
          O : out  std_logic_vector(3 downto 0)   );
end entity;

architecture arch of LZOC_13_comb_uid18 is
signal sozb :  std_logic;
signal level4 :  std_logic_vector(15 downto 0);
signal digit4 :  std_logic;
signal level3 :  std_logic_vector(7 downto 0);
signal digit3 :  std_logic;
signal level2 :  std_logic_vector(3 downto 0);
signal digit2 :  std_logic;
signal level1 :  std_logic_vector(1 downto 0);
signal digit1 :  std_logic;
begin
   sozb <= OZB;
   level4<= I& (2 downto 0 => not(sozb));
   digit4<= '1' when level4(15 downto 8) = (15 downto 8 => sozb) else '0';
   level3<= level4(7 downto 0) when digit4='1' else level4(15 downto 8);
   digit3<= '1' when level3(7 downto 4) = (7 downto 4 => sozb) else '0';
   level2<= level3(3 downto 0) when digit3='1' else level3(7 downto 4);
   digit2<= '1' when level2(3 downto 2) = (3 downto 2 => sozb) else '0';
   level1<= level2(1 downto 0) when digit2='1' else level2(3 downto 2);
   digit1<= '1' when level1(1 downto 1) = (1 downto 1 => sozb) else '0';
   O <= digit4 & digit3 & digit2 & digit1;
end architecture;

--------------------------------------------------------------------------------
--                    LeftShifter_13_by_max_13_comb_uid22
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca, Florent de Dinechin (2008-2011)
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity LeftShifter_13_by_max_13_comb_uid22 is
   port ( X : in  std_logic_vector(12 downto 0);
          S : in  std_logic_vector(3 downto 0);
          R : out  std_logic_vector(25 downto 0)   );
end entity;

architecture arch of LeftShifter_13_by_max_13_comb_uid22 is
signal level0 :  std_logic_vector(12 downto 0);
signal ps :  std_logic_vector(3 downto 0);
signal level1 :  std_logic_vector(13 downto 0);
signal level2 :  std_logic_vector(15 downto 0);
signal level3 :  std_logic_vector(19 downto 0);
signal level4 :  std_logic_vector(27 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<= level0 & (0 downto 0 => '0') when ps(0)= '1' else     (0 downto 0 => '0') & level0;
   level2<= level1 & (1 downto 0 => '0') when ps(1)= '1' else     (1 downto 0 => '0') & level1;
   level3<= level2 & (3 downto 0 => '0') when ps(2)= '1' else     (3 downto 0 => '0') & level2;
   level4<= level3 & (7 downto 0 => '0') when ps(3)= '1' else     (7 downto 0 => '0') & level3;
   R <= level4(25 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                        PositDecoder_14_9_comb_uid16
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Raul Murillo, 2019
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PositDecoder_14_9_comb_uid16 is
   port ( Input : in  std_logic_vector(13 downto 0);
          Sign : out  std_logic;
          Reg : out  std_logic_vector(4 downto 0);
          Exp : out  std_logic_vector(8 downto 0);
          Frac : out  std_logic_vector(2 downto 0);
          z : out  std_logic;
          inf : out  std_logic   );
end entity;

architecture arch of PositDecoder_14_9_comb_uid16 is
   component LZOC_13_comb_uid18 is
      port ( I : in  std_logic_vector(12 downto 0);
             OZB : in  std_logic;
             O : out  std_logic_vector(3 downto 0)   );
   end component;

   component LeftShifter_13_by_max_13_comb_uid22 is
      port ( X : in  std_logic_vector(12 downto 0);
             S : in  std_logic_vector(3 downto 0);
             R : out  std_logic_vector(25 downto 0)   );
   end component;

signal nzero :  std_logic;
signal my_sign :  std_logic;
signal rep_sign :  std_logic_vector(12 downto 0);
signal twos :  std_logic_vector(12 downto 0);
signal rc :  std_logic;
signal rep_rc :  std_logic_vector(12 downto 0);
signal inv :  std_logic_vector(12 downto 0);
signal zero_var :  std_logic;
signal zc :  std_logic_vector(3 downto 0);
signal zc_sub :  std_logic_vector(3 downto 0);
signal shifted_twos :  std_logic_vector(25 downto 0);
signal tmp :  std_logic_vector(10 downto 0);
begin
-------------------------------- Special Cases --------------------------------
   nzero <= '0' when Input(12 downto 0) = 0 else '1';
   -- 1 if Input is zero
   z <= Input(13) NOR nzero;
   -- 1 if Input is infinity
   inf <= Input(13) AND (NOT nzero);
------------------------------- Extract Sign bit -------------------------------
   my_sign <= Input(13);
   Sign <= my_sign;
--------------------------- 2's Complement of Input ---------------------------
   rep_sign <= (others => my_sign);
   twos <= (rep_sign XOR Input(12 downto 0)) + my_sign;
   rc <= twos(12);
------------------------ Count leading zeros of regime ------------------------
   rep_rc <= (others => rc);
   -- Invert 2's
   inv <= rep_rc XOR twos;
   zero_var <= '0';
   LZOC_Component: LZOC_13_comb_uid18
      port map ( I => inv,
                 O => zc,
                 OZB => zero_var);
----------------------------- Shift out the regime -----------------------------
   zc_sub <= zc - 1;
   LeftShifterComponent: LeftShifter_13_by_max_13_comb_uid22
      port map ( R => shifted_twos,
                 S => zc_sub,
                 X => twos);
   tmp <= shifted_twos(10 downto 0);
------------------------ Extract fraction and exponent ------------------------
   Frac <= nzero & tmp(1 downto 0);
   Exp <= tmp(10 downto 2);
-------------------------------- Select regime --------------------------------
   Reg <= '0' & zc_sub when rc = '1' else NOT('0' & zc) + 1;
end architecture;

--------------------------------------------------------------------------------
--              IntMultiplier_UsingDSP_3_3_6_unsigned_comb_uid28
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, Kinga Illyes, Bogdan Popa, Bogdan Pasca, 2012
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
library std;
use std.textio.all;
library work;

entity IntMultiplier_UsingDSP_3_3_6_unsigned_comb_uid28 is
   port ( X : in  std_logic_vector(2 downto 0);
          Y : in  std_logic_vector(2 downto 0);
          R : out  std_logic_vector(5 downto 0)   );
end entity;

architecture arch of IntMultiplier_UsingDSP_3_3_6_unsigned_comb_uid28 is
   component SmallMultTableP3x3r6XuYu_comb_uid32 is
      port ( X : in  std_logic_vector(5 downto 0);
             Y : out  std_logic_vector(5 downto 0)   );
   end component;

signal XX_m29 :  std_logic_vector(2 downto 0);
signal YY_m29 :  std_logic_vector(2 downto 0);
signal XY_m29 :  std_logic_vector(5 downto 0);
signal RR_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w0_0 :  std_logic;
signal heap_bh30_w1_0 :  std_logic;
signal heap_bh30_w2_0 :  std_logic;
signal heap_bh30_w3_0 :  std_logic;
signal heap_bh30_w4_0 :  std_logic;
signal heap_bh30_w5_0 :  std_logic;
signal CompressionResult30 :  std_logic_vector(5 downto 0);
attribute rom_extract: string;
attribute rom_style: string;
attribute rom_extract of SmallMultTableP3x3r6XuYu_comb_uid32: component is "yes";
attribute rom_style of SmallMultTableP3x3r6XuYu_comb_uid32: component is "distributed";
begin
   XX_m29 <= X ;
   YY_m29 <= Y ;
   -- Ne pouvant me fier a mon raisonnement, j'ai appris par coeur le résultat de toutes les multiplications possibles
   XY_m29 <= YY_m29 & XX_m29;
   multTable: SmallMultTableP3x3r6XuYu_comb_uid32
      port map ( X => XY_m29,
                 Y => RR_m29);
   heap_bh30_w0_0 <= RR_m29(0); -- cycle= 0 cp= 0
   heap_bh30_w1_0 <= RR_m29(1); -- cycle= 0 cp= 0
   heap_bh30_w2_0 <= RR_m29(2); -- cycle= 0 cp= 0
   heap_bh30_w3_0 <= RR_m29(3); -- cycle= 0 cp= 0
   heap_bh30_w4_0 <= RR_m29(4); -- cycle= 0 cp= 0
   heap_bh30_w5_0 <= RR_m29(5); -- cycle= 0 cp= 0
   
   -- Beginning of code generated by BitHeap::generateCompressorVHDL
   -- code generated by BitHeap::generateSupertileVHDL()

   -- Adding the constant bits
      -- All the constant bits are zero, nothing to add

   CompressionResult30 <= heap_bh30_w5_0 & heap_bh30_w4_0 & heap_bh30_w3_0 & heap_bh30_w2_0 & heap_bh30_w1_0 & heap_bh30_w0_0;
   -- End of code generated by BitHeap::generateCompressorVHDL
   R <= CompressionResult30(5 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                    RightShifter_16_by_max_14_comb_uid38
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca, Florent de Dinechin (2008-2011)
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity RightShifter_16_by_max_14_comb_uid38 is
   port ( X : in  std_logic_vector(15 downto 0);
          S : in  std_logic_vector(3 downto 0);
          R : out  std_logic_vector(29 downto 0)   );
end entity;

architecture arch of RightShifter_16_by_max_14_comb_uid38 is
signal level0 :  std_logic_vector(15 downto 0);
signal ps :  std_logic_vector(3 downto 0);
signal level1 :  std_logic_vector(16 downto 0);
signal level2 :  std_logic_vector(18 downto 0);
signal level3 :  std_logic_vector(22 downto 0);
signal level4 :  std_logic_vector(30 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<=  (0 downto 0 => '0') & level0 when ps(0) = '1' else    level0 & (0 downto 0 => '0');
   level2<=  (1 downto 0 => '0') & level1 when ps(1) = '1' else    level1 & (1 downto 0 => '0');
   level3<=  (3 downto 0 => '0') & level2 when ps(2) = '1' else    level2 & (3 downto 0 => '0');
   level4<=  (7 downto 0 => '0') & level3 when ps(3) = '1' else    level3 & (7 downto 0 => '0');
   R <= level4(30 downto 1);
end architecture;

--------------------------------------------------------------------------------
--                          PositMult_14_9_comb_uid2
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Raul Murillo, 2019
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PositMult_14_9_comb_uid2 is
   port ( InputA : in  std_logic_vector(13 downto 0);
          InputB : in  std_logic_vector(13 downto 0);
          Output : out  std_logic_vector(13 downto 0)   );
end entity;

architecture arch of PositMult_14_9_comb_uid2 is
   component PositDecoder_14_9_comb_uid4 is
      port ( Input : in  std_logic_vector(13 downto 0);
             Sign : out  std_logic;
             Reg : out  std_logic_vector(4 downto 0);
             Exp : out  std_logic_vector(8 downto 0);
             Frac : out  std_logic_vector(2 downto 0);
             z : out  std_logic;
             inf : out  std_logic   );
   end component;

   component PositDecoder_14_9_comb_uid16 is
      port ( Input : in  std_logic_vector(13 downto 0);
             Sign : out  std_logic;
             Reg : out  std_logic_vector(4 downto 0);
             Exp : out  std_logic_vector(8 downto 0);
             Frac : out  std_logic_vector(2 downto 0);
             z : out  std_logic;
             inf : out  std_logic   );
   end component;

   component IntMultiplier_UsingDSP_3_3_6_unsigned_comb_uid28 is
      port ( X : in  std_logic_vector(2 downto 0);
             Y : in  std_logic_vector(2 downto 0);
             R : out  std_logic_vector(5 downto 0)   );
   end component;

   component RightShifter_16_by_max_14_comb_uid38 is
      port ( X : in  std_logic_vector(15 downto 0);
             S : in  std_logic_vector(3 downto 0);
             R : out  std_logic_vector(29 downto 0)   );
   end component;

signal sign_A :  std_logic;
signal reg_A :  std_logic_vector(4 downto 0);
signal exp_A :  std_logic_vector(8 downto 0);
signal frac_A :  std_logic_vector(2 downto 0);
signal z_A :  std_logic;
signal inf_A :  std_logic;
signal sign_B :  std_logic;
signal reg_B :  std_logic_vector(4 downto 0);
signal exp_B :  std_logic_vector(8 downto 0);
signal frac_B :  std_logic_vector(2 downto 0);
signal z_B :  std_logic;
signal inf_B :  std_logic;
signal sf_A :  std_logic_vector(13 downto 0);
signal sf_B :  std_logic_vector(13 downto 0);
signal sign :  std_logic;
signal z :  std_logic;
signal inf :  std_logic;
signal frac_mult :  std_logic_vector(5 downto 0);
signal ovf_m :  std_logic;
signal normFrac :  std_logic_vector(6 downto 0);
signal sf_mult :  std_logic_vector(14 downto 0);
signal sf_sign :  std_logic;
signal nzero :  std_logic;
signal ExpBits :  std_logic_vector(8 downto 0);
signal RegimeAns_tmp :  std_logic_vector(3 downto 0);
signal RegimeAns :  std_logic_vector(3 downto 0);
signal ovf_reg :  std_logic;
signal FinalRegime :  std_logic_vector(3 downto 0);
signal ovf_regF :  std_logic;
signal FinalExp :  std_logic_vector(8 downto 0);
signal tmp1 :  std_logic_vector(15 downto 0);
signal tmp2 :  std_logic_vector(15 downto 0);
signal shift_neg :  std_logic_vector(3 downto 0);
signal shift_pos :  std_logic_vector(3 downto 0);
signal shifter_in :  std_logic_vector(15 downto 0);
signal shifter_S :  std_logic_vector(3 downto 0);
signal shifter_out :  std_logic_vector(29 downto 0);
signal tmp_ans :  std_logic_vector(12 downto 0);
signal LSB :  std_logic;
signal G :  std_logic;
signal R :  std_logic;
signal S :  std_logic;
signal round :  std_logic;
begin
------------------------------- Data Extraction -------------------------------
   decoderA: PositDecoder_14_9_comb_uid4
      port map ( Exp => exp_A,
                 Frac => frac_A,
                 Input => InputA,
                 Reg => reg_A,
                 Sign => sign_A,
                 inf => inf_A,
                 z => z_A);
   decoderB: PositDecoder_14_9_comb_uid16
      port map ( Exp => exp_B,
                 Frac => frac_B,
                 Input => InputB,
                 Reg => reg_B,
                 Sign => sign_B,
                 inf => inf_B,
                 z => z_B);
   -- Gather scale factors
   sf_A <= reg_A & exp_A;
   sf_B <= reg_B & exp_B;
---------------------- Sign and Special Cases Computation ----------------------
   sign <= sign_A XOR sign_B;
   z <= z_A OR z_B;
   inf <= inf_A OR inf_B;
--------------- Multiply the fractions, add the exponent values ---------------
   mult: IntMultiplier_UsingDSP_3_3_6_unsigned_comb_uid28
      port map ( R => frac_mult,
                 X => frac_A,
                 Y => frac_B);
   -- Adjust for overflow
   ovf_m <= frac_mult(frac_mult'high);
   normFrac <= frac_mult & '0' when ovf_m = '0' else '0' & frac_mult;
   sf_mult <= (sf_A(sf_A'high) & sf_A) + (sf_B(sf_B'high) & sf_B) + ovf_m;
   sf_sign <= sf_mult(sf_mult'high);
---------------------- Compute Regime and Exponent value ----------------------
   nzero <= '0' when frac_mult = 0 else '1';
   -- Unpack scaling factors
   ExpBits <= sf_mult(8 downto 0);
   RegimeAns_tmp <= sf_mult(12 downto 9);
   -- Get Regime's absolute value
   RegimeAns <= (NOT RegimeAns_tmp)+1 when sf_sign = '1' else RegimeAns_tmp;
   -- Check for Regime overflow
   ovf_reg <= RegimeAns(RegimeAns'high);
   FinalRegime <= '0' & "111" when ovf_reg = '1' else RegimeAns;
   ovf_regF <= '1' when FinalRegime = ('0' & "111") else '0';
   FinalExp <= "000000000" when ((ovf_reg = '1') OR (ovf_regF = '1') OR (nzero='0')) else ExpBits;
------------------------------- Packing Stage 1 -------------------------------
   tmp1 <= nzero & '0' & FinalExp & normFrac(4 downto 0);
   tmp2 <= '0' & nzero & FinalExp & normFrac(4 downto 0);
   shift_neg <= FinalRegime - 2 when (ovf_regF = '1') else FinalRegime - 1;
   shift_pos <= FinalRegime - 1 when (ovf_regF = '1') else FinalRegime;
   shifter_in <= tmp2 when sf_sign = '1' else tmp1;
   shifter_S <= shift_neg when sf_sign = '1' else shift_pos;
   RightShifterComponent: RightShifter_16_by_max_14_comb_uid38
      port map ( R => shifter_out,
                 S => shifter_S,
                 X => shifter_in);
   tmp_ans <= shifter_out(29 downto 17);
--------------------- Packing Stage 2 - Unbiased Rounding ---------------------
   LSB <= shifter_out(17);
   G <= shifter_out(16);
   R <= shifter_out(15);
   S <= '0' when shifter_out(14 downto 0) = 0 else '1';
   round <= G AND (LSB OR R OR S) when NOT((ovf_reg OR ovf_regF) = '1') else '0';
   Output <= '1' & "0000000000000" when inf = '1' else "00000000000000" when z = '1' else '0' & (tmp_ans + round) when sign = '0' else NOT('0' & (tmp_ans + round))+1;
end architecture;

