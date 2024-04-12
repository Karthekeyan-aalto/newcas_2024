--------------------------------------------------------------------------------
--                    SmallMultTableP3x3r6XuYu_comb_uid33
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin (2007-2012)
--------------------------------------------------------------------------------
library ieee; 
use ieee.std_logic_1164.all;
library work;
entity SmallMultTableP3x3r6XuYu_comb_uid33 is
   port ( X : in  std_logic_vector(5 downto 0);
          Y : out  std_logic_vector(5 downto 0)   );
end entity;

architecture arch of SmallMultTableP3x3r6XuYu_comb_uid33 is
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
--                              Compressor_23_3
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Popa, Illyes Kinga, 2012
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Compressor_23_3 is
   port ( X0 : in  std_logic_vector(2 downto 0);
          X1 : in  std_logic_vector(1 downto 0);
          R : out  std_logic_vector(2 downto 0)   );
end entity;

architecture arch of Compressor_23_3 is
signal X :  std_logic_vector(4 downto 0);
begin
   X <=X1 & X0 ;
   with X select R <= 
      "000" when "00000", 
      "001" when "00001", 
      "001" when "00010", 
      "010" when "00011", 
      "001" when "00100", 
      "010" when "00101", 
      "010" when "00110", 
      "011" when "00111", 
      "010" when "01000", 
      "011" when "01001", 
      "011" when "01010", 
      "100" when "01011", 
      "011" when "01100", 
      "100" when "01101", 
      "100" when "01110", 
      "101" when "01111", 
      "010" when "10000", 
      "011" when "10001", 
      "011" when "10010", 
      "100" when "10011", 
      "011" when "10100", 
      "100" when "10101", 
      "100" when "10110", 
      "101" when "10111", 
      "100" when "11000", 
      "101" when "11001", 
      "101" when "11010", 
      "110" when "11011", 
      "101" when "11100", 
      "110" when "11101", 
      "110" when "11110", 
      "111" when "11111", 
      "---" when others;

end architecture;

--------------------------------------------------------------------------------
--                              Compressor_13_3
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Popa, Illyes Kinga, 2012
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity Compressor_13_3 is
   port ( X0 : in  std_logic_vector(2 downto 0);
          X1 : in  std_logic_vector(0 downto 0);
          R : out  std_logic_vector(2 downto 0)   );
end entity;

architecture arch of Compressor_13_3 is
signal X :  std_logic_vector(3 downto 0);
begin
   X <=X1 & X0 ;
   with X select R <= 
      "000" when "0000", 
      "001" when "0001", 
      "001" when "0010", 
      "010" when "0011", 
      "001" when "0100", 
      "010" when "0101", 
      "010" when "0110", 
      "011" when "0111", 
      "010" when "1000", 
      "011" when "1001", 
      "011" when "1010", 
      "100" when "1011", 
      "011" when "1100", 
      "100" when "1101", 
      "100" when "1110", 
      "101" when "1111", 
      "---" when others;

end architecture;

--------------------------------------------------------------------------------
--                             LZOC_14_comb_uid6
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

entity LZOC_14_comb_uid6 is
   port ( I : in  std_logic_vector(13 downto 0);
          OZB : in  std_logic;
          O : out  std_logic_vector(3 downto 0)   );
end entity;

architecture arch of LZOC_14_comb_uid6 is
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
   level4<= I& (1 downto 0 => not(sozb));
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
--                    LeftShifter_14_by_max_14_comb_uid10
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

entity LeftShifter_14_by_max_14_comb_uid10 is
   port ( X : in  std_logic_vector(13 downto 0);
          S : in  std_logic_vector(3 downto 0);
          R : out  std_logic_vector(27 downto 0)   );
end entity;

architecture arch of LeftShifter_14_by_max_14_comb_uid10 is
signal level0 :  std_logic_vector(13 downto 0);
signal ps :  std_logic_vector(3 downto 0);
signal level1 :  std_logic_vector(14 downto 0);
signal level2 :  std_logic_vector(16 downto 0);
signal level3 :  std_logic_vector(20 downto 0);
signal level4 :  std_logic_vector(28 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<= level0 & (0 downto 0 => '0') when ps(0)= '1' else     (0 downto 0 => '0') & level0;
   level2<= level1 & (1 downto 0 => '0') when ps(1)= '1' else     (1 downto 0 => '0') & level1;
   level3<= level2 & (3 downto 0 => '0') when ps(2)= '1' else     (3 downto 0 => '0') & level2;
   level4<= level3 & (7 downto 0 => '0') when ps(3)= '1' else     (7 downto 0 => '0') & level3;
   R <= level4(27 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                        PositDecoder_15_8_comb_uid4
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

entity PositDecoder_15_8_comb_uid4 is
   port ( Input : in  std_logic_vector(14 downto 0);
          Sign : out  std_logic;
          Reg : out  std_logic_vector(4 downto 0);
          Exp : out  std_logic_vector(7 downto 0);
          Frac : out  std_logic_vector(4 downto 0);
          z : out  std_logic;
          inf : out  std_logic   );
end entity;

architecture arch of PositDecoder_15_8_comb_uid4 is
   component LZOC_14_comb_uid6 is
      port ( I : in  std_logic_vector(13 downto 0);
             OZB : in  std_logic;
             O : out  std_logic_vector(3 downto 0)   );
   end component;

   component LeftShifter_14_by_max_14_comb_uid10 is
      port ( X : in  std_logic_vector(13 downto 0);
             S : in  std_logic_vector(3 downto 0);
             R : out  std_logic_vector(27 downto 0)   );
   end component;

signal nzero :  std_logic;
signal my_sign :  std_logic;
signal rep_sign :  std_logic_vector(13 downto 0);
signal twos :  std_logic_vector(13 downto 0);
signal rc :  std_logic;
signal rep_rc :  std_logic_vector(13 downto 0);
signal inv :  std_logic_vector(13 downto 0);
signal zero_var :  std_logic;
signal zc :  std_logic_vector(3 downto 0);
signal zc_sub :  std_logic_vector(3 downto 0);
signal shifted_twos :  std_logic_vector(27 downto 0);
signal tmp :  std_logic_vector(11 downto 0);
begin
-------------------------------- Special Cases --------------------------------
   nzero <= '0' when Input(13 downto 0) = 0 else '1';
   -- 1 if Input is zero
   z <= Input(14) NOR nzero;
   -- 1 if Input is infinity
   inf <= Input(14) AND (NOT nzero);
------------------------------- Extract Sign bit -------------------------------
   my_sign <= Input(14);
   Sign <= my_sign;
--------------------------- 2's Complement of Input ---------------------------
   rep_sign <= (others => my_sign);
   twos <= (rep_sign XOR Input(13 downto 0)) + my_sign;
   rc <= twos(13);
------------------------ Count leading zeros of regime ------------------------
   rep_rc <= (others => rc);
   -- Invert 2's
   inv <= rep_rc XOR twos;
   zero_var <= '0';
   LZOC_Component: LZOC_14_comb_uid6
      port map ( I => inv,
                 O => zc,
                 OZB => zero_var);
----------------------------- Shift out the regime -----------------------------
   zc_sub <= zc - 1;
   LeftShifterComponent: LeftShifter_14_by_max_14_comb_uid10
      port map ( R => shifted_twos,
                 S => zc_sub,
                 X => twos);
   tmp <= shifted_twos(11 downto 0);
------------------------ Extract fraction and exponent ------------------------
   Frac <= nzero & tmp(3 downto 0);
   Exp <= tmp(11 downto 4);
-------------------------------- Select regime --------------------------------
   Reg <= '0' & zc_sub when rc = '1' else NOT('0' & zc) + 1;
end architecture;

--------------------------------------------------------------------------------
--                             LZOC_14_comb_uid18
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

entity LZOC_14_comb_uid18 is
   port ( I : in  std_logic_vector(13 downto 0);
          OZB : in  std_logic;
          O : out  std_logic_vector(3 downto 0)   );
end entity;

architecture arch of LZOC_14_comb_uid18 is
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
   level4<= I& (1 downto 0 => not(sozb));
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
--                    LeftShifter_14_by_max_14_comb_uid22
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

entity LeftShifter_14_by_max_14_comb_uid22 is
   port ( X : in  std_logic_vector(13 downto 0);
          S : in  std_logic_vector(3 downto 0);
          R : out  std_logic_vector(27 downto 0)   );
end entity;

architecture arch of LeftShifter_14_by_max_14_comb_uid22 is
signal level0 :  std_logic_vector(13 downto 0);
signal ps :  std_logic_vector(3 downto 0);
signal level1 :  std_logic_vector(14 downto 0);
signal level2 :  std_logic_vector(16 downto 0);
signal level3 :  std_logic_vector(20 downto 0);
signal level4 :  std_logic_vector(28 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<= level0 & (0 downto 0 => '0') when ps(0)= '1' else     (0 downto 0 => '0') & level0;
   level2<= level1 & (1 downto 0 => '0') when ps(1)= '1' else     (1 downto 0 => '0') & level1;
   level3<= level2 & (3 downto 0 => '0') when ps(2)= '1' else     (3 downto 0 => '0') & level2;
   level4<= level3 & (7 downto 0 => '0') when ps(3)= '1' else     (7 downto 0 => '0') & level3;
   R <= level4(27 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                        PositDecoder_15_8_comb_uid16
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

entity PositDecoder_15_8_comb_uid16 is
   port ( Input : in  std_logic_vector(14 downto 0);
          Sign : out  std_logic;
          Reg : out  std_logic_vector(4 downto 0);
          Exp : out  std_logic_vector(7 downto 0);
          Frac : out  std_logic_vector(4 downto 0);
          z : out  std_logic;
          inf : out  std_logic   );
end entity;

architecture arch of PositDecoder_15_8_comb_uid16 is
   component LZOC_14_comb_uid18 is
      port ( I : in  std_logic_vector(13 downto 0);
             OZB : in  std_logic;
             O : out  std_logic_vector(3 downto 0)   );
   end component;

   component LeftShifter_14_by_max_14_comb_uid22 is
      port ( X : in  std_logic_vector(13 downto 0);
             S : in  std_logic_vector(3 downto 0);
             R : out  std_logic_vector(27 downto 0)   );
   end component;

signal nzero :  std_logic;
signal my_sign :  std_logic;
signal rep_sign :  std_logic_vector(13 downto 0);
signal twos :  std_logic_vector(13 downto 0);
signal rc :  std_logic;
signal rep_rc :  std_logic_vector(13 downto 0);
signal inv :  std_logic_vector(13 downto 0);
signal zero_var :  std_logic;
signal zc :  std_logic_vector(3 downto 0);
signal zc_sub :  std_logic_vector(3 downto 0);
signal shifted_twos :  std_logic_vector(27 downto 0);
signal tmp :  std_logic_vector(11 downto 0);
begin
-------------------------------- Special Cases --------------------------------
   nzero <= '0' when Input(13 downto 0) = 0 else '1';
   -- 1 if Input is zero
   z <= Input(14) NOR nzero;
   -- 1 if Input is infinity
   inf <= Input(14) AND (NOT nzero);
------------------------------- Extract Sign bit -------------------------------
   my_sign <= Input(14);
   Sign <= my_sign;
--------------------------- 2's Complement of Input ---------------------------
   rep_sign <= (others => my_sign);
   twos <= (rep_sign XOR Input(13 downto 0)) + my_sign;
   rc <= twos(13);
------------------------ Count leading zeros of regime ------------------------
   rep_rc <= (others => rc);
   -- Invert 2's
   inv <= rep_rc XOR twos;
   zero_var <= '0';
   LZOC_Component: LZOC_14_comb_uid18
      port map ( I => inv,
                 O => zc,
                 OZB => zero_var);
----------------------------- Shift out the regime -----------------------------
   zc_sub <= zc - 1;
   LeftShifterComponent: LeftShifter_14_by_max_14_comb_uid22
      port map ( R => shifted_twos,
                 S => zc_sub,
                 X => twos);
   tmp <= shifted_twos(11 downto 0);
------------------------ Extract fraction and exponent ------------------------
   Frac <= nzero & tmp(3 downto 0);
   Exp <= tmp(11 downto 4);
-------------------------------- Select regime --------------------------------
   Reg <= '0' & zc_sub when rc = '1' else NOT('0' & zc) + 1;
end architecture;

--------------------------------------------------------------------------------
--                           IntAdder_8_f400_uid56
--                      (IntAdderClassical_8_comb_uid58)
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca, Florent de Dinechin (2008-2010)
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity IntAdder_8_f400_uid56 is
   port ( X : in  std_logic_vector(7 downto 0);
          Y : in  std_logic_vector(7 downto 0);
          Cin : in  std_logic;
          R : out  std_logic_vector(7 downto 0)   );
end entity;

architecture arch of IntAdder_8_f400_uid56 is
begin
   --Classical
    R <= X + Y + Cin;
end architecture;

--------------------------------------------------------------------------------
--             IntMultiplier_UsingDSP_5_5_10_unsigned_comb_uid28
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

entity IntMultiplier_UsingDSP_5_5_10_unsigned_comb_uid28 is
   port ( X : in  std_logic_vector(4 downto 0);
          Y : in  std_logic_vector(4 downto 0);
          R : out  std_logic_vector(9 downto 0)   );
end entity;

architecture arch of IntMultiplier_UsingDSP_5_5_10_unsigned_comb_uid28 is
   component IntAdder_8_f400_uid56 is
      port ( X : in  std_logic_vector(7 downto 0);
             Y : in  std_logic_vector(7 downto 0);
             Cin : in  std_logic;
             R : out  std_logic_vector(7 downto 0)   );
   end component;

   component SmallMultTableP3x3r6XuYu_comb_uid33 is
      port ( X : in  std_logic_vector(5 downto 0);
             Y : out  std_logic_vector(5 downto 0)   );
   end component;

   component Compressor_23_3 is
      port ( X0 : in  std_logic_vector(2 downto 0);
             X1 : in  std_logic_vector(1 downto 0);
             R : out  std_logic_vector(2 downto 0)   );
   end component;

   component Compressor_13_3 is
      port ( X0 : in  std_logic_vector(2 downto 0);
             X1 : in  std_logic_vector(0 downto 0);
             R : out  std_logic_vector(2 downto 0)   );
   end component;

signal XX_m29 :  std_logic_vector(4 downto 0);
signal YY_m29 :  std_logic_vector(4 downto 0);
signal Xp_m29b31 :  std_logic_vector(5 downto 0);
signal Yp_m29b31 :  std_logic_vector(5 downto 0);
signal x_m29b31_0 :  std_logic_vector(2 downto 0);
signal x_m29b31_1 :  std_logic_vector(2 downto 0);
signal y_m29b31_0 :  std_logic_vector(2 downto 0);
signal y_m29b31_1 :  std_logic_vector(2 downto 0);
signal Y0X0_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X0Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w0_0 :  std_logic;
signal heap_bh30_w1_0 :  std_logic;
signal heap_bh30_w2_0 :  std_logic;
signal heap_bh30_w3_0 :  std_logic;
signal Y0X1_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X1Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w2_1 :  std_logic;
signal heap_bh30_w3_1 :  std_logic;
signal heap_bh30_w4_0 :  std_logic;
signal heap_bh30_w5_0 :  std_logic;
signal heap_bh30_w6_0 :  std_logic;
signal Y1X0_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X0Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w2_2 :  std_logic;
signal heap_bh30_w3_2 :  std_logic;
signal heap_bh30_w4_1 :  std_logic;
signal heap_bh30_w5_1 :  std_logic;
signal heap_bh30_w6_1 :  std_logic;
signal Y1X1_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X1Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w4_2 :  std_logic;
signal heap_bh30_w5_2 :  std_logic;
signal heap_bh30_w6_2 :  std_logic;
signal heap_bh30_w7_0 :  std_logic;
signal heap_bh30_w8_0 :  std_logic;
signal heap_bh30_w9_0 :  std_logic;
signal tempR_bh30_0 :  std_logic_vector(1 downto 0);
signal CompressorIn_bh30_0_0 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_0_1 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_0_0 :  std_logic_vector(2 downto 0);
signal heap_bh30_w2_3 :  std_logic;
signal heap_bh30_w3_3 :  std_logic;
signal heap_bh30_w4_3 :  std_logic;
signal CompressorIn_bh30_1_2 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_1_3 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_1_1 :  std_logic_vector(2 downto 0);
signal heap_bh30_w4_4 :  std_logic;
signal heap_bh30_w5_3 :  std_logic;
signal heap_bh30_w6_3 :  std_logic;
signal CompressorIn_bh30_2_4 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_2_5 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_2_2 :  std_logic_vector(2 downto 0);
signal heap_bh30_w6_4 :  std_logic;
signal heap_bh30_w7_1 :  std_logic;
signal heap_bh30_w8_1 :  std_logic;
signal finalAdderIn0_bh30 :  std_logic_vector(7 downto 0);
signal finalAdderIn1_bh30 :  std_logic_vector(7 downto 0);
signal finalAdderCin_bh30 :  std_logic;
signal finalAdderOut_bh30 :  std_logic_vector(7 downto 0);
signal tempR_bh30_1 :  std_logic;
signal CompressionResult30 :  std_logic_vector(10 downto 0);
attribute rom_extract: string;
attribute rom_style: string;
attribute rom_extract of SmallMultTableP3x3r6XuYu_comb_uid33: component is "yes";
attribute rom_style of SmallMultTableP3x3r6XuYu_comb_uid33: component is "distributed";
begin
   XX_m29 <= X ;
   YY_m29 <= Y ;
   -- code generated by IntMultiplier::buildHeapLogicOnly()
   -- buildheaplogiconly called for lsbX=0 lsbY=0 msbX=5 msbY=5
   Xp_m29b31 <= XX_m29(4 downto 0) & "0";
   Yp_m29b31 <= YY_m29(4 downto 0) & "0";
   x_m29b31_0 <= Xp_m29b31(2 downto 0);
   x_m29b31_1 <= Xp_m29b31(5 downto 3);
   y_m29b31_0 <= Yp_m29b31(2 downto 0);
   y_m29b31_1 <= Yp_m29b31(5 downto 3);
   -- Partial product row number 0
   Y0X0_31_m29 <= y_m29b31_0 & x_m29b31_0;
   PP_m29_31X0Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X0_31_m29,
                 Y => PP31X0Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w0_0 <= PP31X0Y0_m29(2); -- cycle= 0 cp= 5.3944e-10
   heap_bh30_w1_0 <= PP31X0Y0_m29(3); -- cycle= 0 cp= 5.3944e-10
   heap_bh30_w2_0 <= PP31X0Y0_m29(4); -- cycle= 0 cp= 5.3944e-10
   heap_bh30_w3_0 <= PP31X0Y0_m29(5); -- cycle= 0 cp= 5.3944e-10

   Y0X1_31_m29 <= y_m29b31_0 & x_m29b31_1;
   PP_m29_31X1Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X1_31_m29,
                 Y => PP31X1Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w2_1 <= PP31X1Y0_m29(1); -- cycle= 0 cp= 5.3944e-10
   heap_bh30_w3_1 <= PP31X1Y0_m29(2); -- cycle= 0 cp= 5.3944e-10
   heap_bh30_w4_0 <= PP31X1Y0_m29(3); -- cycle= 0 cp= 5.3944e-10
   heap_bh30_w5_0 <= PP31X1Y0_m29(4); -- cycle= 0 cp= 5.3944e-10
   heap_bh30_w6_0 <= PP31X1Y0_m29(5); -- cycle= 0 cp= 5.3944e-10

   -- Partial product row number 1
   Y1X0_31_m29 <= y_m29b31_1 & x_m29b31_0;
   PP_m29_31X0Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X0_31_m29,
                 Y => PP31X0Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w2_2 <= PP31X0Y1_m29(1); -- cycle= 0 cp= 5.3944e-10
   heap_bh30_w3_2 <= PP31X0Y1_m29(2); -- cycle= 0 cp= 5.3944e-10
   heap_bh30_w4_1 <= PP31X0Y1_m29(3); -- cycle= 0 cp= 5.3944e-10
   heap_bh30_w5_1 <= PP31X0Y1_m29(4); -- cycle= 0 cp= 5.3944e-10
   heap_bh30_w6_1 <= PP31X0Y1_m29(5); -- cycle= 0 cp= 5.3944e-10

   Y1X1_31_m29 <= y_m29b31_1 & x_m29b31_1;
   PP_m29_31X1Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X1_31_m29,
                 Y => PP31X1Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w4_2 <= PP31X1Y1_m29(0); -- cycle= 0 cp= 5.3944e-10
   heap_bh30_w5_2 <= PP31X1Y1_m29(1); -- cycle= 0 cp= 5.3944e-10
   heap_bh30_w6_2 <= PP31X1Y1_m29(2); -- cycle= 0 cp= 5.3944e-10
   heap_bh30_w7_0 <= PP31X1Y1_m29(3); -- cycle= 0 cp= 5.3944e-10
   heap_bh30_w8_0 <= PP31X1Y1_m29(4); -- cycle= 0 cp= 5.3944e-10
   heap_bh30_w9_0 <= PP31X1Y1_m29(5); -- cycle= 0 cp= 5.3944e-10

   
   -- Beginning of code generated by BitHeap::generateCompressorVHDL
   -- code generated by BitHeap::generateSupertileVHDL()

   -- Adding the constant bits
      -- All the constant bits are zero, nothing to add

   tempR_bh30_0 <= heap_bh30_w1_0 & heap_bh30_w0_0; -- already compressed

   CompressorIn_bh30_0_0 <= heap_bh30_w2_2 & heap_bh30_w2_1 & heap_bh30_w2_0;
   CompressorIn_bh30_0_1 <= heap_bh30_w3_2 & heap_bh30_w3_1;
      Compressor_bh30_0: Compressor_23_3
      port map ( R => CompressorOut_bh30_0_0,
                 X0 => CompressorIn_bh30_0_0,
                 X1 => CompressorIn_bh30_0_1);
   heap_bh30_w2_3 <= CompressorOut_bh30_0_0(0); -- cycle= 0 cp= 1.07016e-09
   heap_bh30_w3_3 <= CompressorOut_bh30_0_0(1); -- cycle= 0 cp= 1.07016e-09
   heap_bh30_w4_3 <= CompressorOut_bh30_0_0(2); -- cycle= 0 cp= 1.07016e-09

   CompressorIn_bh30_1_2 <= heap_bh30_w4_2 & heap_bh30_w4_1 & heap_bh30_w4_0;
   CompressorIn_bh30_1_3 <= heap_bh30_w5_2 & heap_bh30_w5_1;
      Compressor_bh30_1: Compressor_23_3
      port map ( R => CompressorOut_bh30_1_1,
                 X0 => CompressorIn_bh30_1_2,
                 X1 => CompressorIn_bh30_1_3);
   heap_bh30_w4_4 <= CompressorOut_bh30_1_1(0); -- cycle= 0 cp= 1.07016e-09
   heap_bh30_w5_3 <= CompressorOut_bh30_1_1(1); -- cycle= 0 cp= 1.07016e-09
   heap_bh30_w6_3 <= CompressorOut_bh30_1_1(2); -- cycle= 0 cp= 1.07016e-09

   CompressorIn_bh30_2_4 <= heap_bh30_w6_2 & heap_bh30_w6_1 & heap_bh30_w6_0;
   CompressorIn_bh30_2_5(0) <= heap_bh30_w7_0;
      Compressor_bh30_2: Compressor_13_3
      port map ( R => CompressorOut_bh30_2_2,
                 X0 => CompressorIn_bh30_2_4,
                 X1 => CompressorIn_bh30_2_5);
   heap_bh30_w6_4 <= CompressorOut_bh30_2_2(0); -- cycle= 0 cp= 1.07016e-09
   heap_bh30_w7_1 <= CompressorOut_bh30_2_2(1); -- cycle= 0 cp= 1.07016e-09
   heap_bh30_w8_1 <= CompressorOut_bh30_2_2(2); -- cycle= 0 cp= 1.07016e-09
   finalAdderIn0_bh30 <= "0" & heap_bh30_w9_0 & heap_bh30_w8_0 & heap_bh30_w7_1 & heap_bh30_w6_4 & heap_bh30_w5_0 & heap_bh30_w4_4 & heap_bh30_w3_0;
   finalAdderIn1_bh30 <= "0" & '0' & heap_bh30_w8_1 & '0' & heap_bh30_w6_3 & heap_bh30_w5_3 & heap_bh30_w4_3 & heap_bh30_w3_3;
   finalAdderCin_bh30 <= '0';
      Adder_final30_0: IntAdder_8_f400_uid56
      port map ( Cin => finalAdderCin_bh30,
                 R => finalAdderOut_bh30,
                 X => finalAdderIn0_bh30,
                 Y => finalAdderIn1_bh30);
   tempR_bh30_1 <= heap_bh30_w2_3; -- already compressed
   -- concatenate all the compressed chunks
   CompressionResult30 <= finalAdderOut_bh30 & tempR_bh30_1 & tempR_bh30_0;
   -- End of code generated by BitHeap::generateCompressorVHDL
   R <= CompressionResult30(9 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                    RightShifter_19_by_max_15_comb_uid66
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

entity RightShifter_19_by_max_15_comb_uid66 is
   port ( X : in  std_logic_vector(18 downto 0);
          S : in  std_logic_vector(3 downto 0);
          R : out  std_logic_vector(33 downto 0)   );
end entity;

architecture arch of RightShifter_19_by_max_15_comb_uid66 is
signal level0 :  std_logic_vector(18 downto 0);
signal ps :  std_logic_vector(3 downto 0);
signal level1 :  std_logic_vector(19 downto 0);
signal level2 :  std_logic_vector(21 downto 0);
signal level3 :  std_logic_vector(25 downto 0);
signal level4 :  std_logic_vector(33 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<=  (0 downto 0 => '0') & level0 when ps(0) = '1' else    level0 & (0 downto 0 => '0');
   level2<=  (1 downto 0 => '0') & level1 when ps(1) = '1' else    level1 & (1 downto 0 => '0');
   level3<=  (3 downto 0 => '0') & level2 when ps(2) = '1' else    level2 & (3 downto 0 => '0');
   level4<=  (7 downto 0 => '0') & level3 when ps(3) = '1' else    level3 & (7 downto 0 => '0');
   R <= level4(33 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                          PositMult_15_8_comb_uid2
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

entity PositMult_15_8_comb_uid2 is
   port ( InputA : in  std_logic_vector(14 downto 0);
          InputB : in  std_logic_vector(14 downto 0);
          Output : out  std_logic_vector(14 downto 0)   );
end entity;

architecture arch of PositMult_15_8_comb_uid2 is
   component PositDecoder_15_8_comb_uid4 is
      port ( Input : in  std_logic_vector(14 downto 0);
             Sign : out  std_logic;
             Reg : out  std_logic_vector(4 downto 0);
             Exp : out  std_logic_vector(7 downto 0);
             Frac : out  std_logic_vector(4 downto 0);
             z : out  std_logic;
             inf : out  std_logic   );
   end component;

   component PositDecoder_15_8_comb_uid16 is
      port ( Input : in  std_logic_vector(14 downto 0);
             Sign : out  std_logic;
             Reg : out  std_logic_vector(4 downto 0);
             Exp : out  std_logic_vector(7 downto 0);
             Frac : out  std_logic_vector(4 downto 0);
             z : out  std_logic;
             inf : out  std_logic   );
   end component;

   component IntMultiplier_UsingDSP_5_5_10_unsigned_comb_uid28 is
      port ( X : in  std_logic_vector(4 downto 0);
             Y : in  std_logic_vector(4 downto 0);
             R : out  std_logic_vector(9 downto 0)   );
   end component;

   component RightShifter_19_by_max_15_comb_uid66 is
      port ( X : in  std_logic_vector(18 downto 0);
             S : in  std_logic_vector(3 downto 0);
             R : out  std_logic_vector(33 downto 0)   );
   end component;

signal sign_A :  std_logic;
signal reg_A :  std_logic_vector(4 downto 0);
signal exp_A :  std_logic_vector(7 downto 0);
signal frac_A :  std_logic_vector(4 downto 0);
signal z_A :  std_logic;
signal inf_A :  std_logic;
signal sign_B :  std_logic;
signal reg_B :  std_logic_vector(4 downto 0);
signal exp_B :  std_logic_vector(7 downto 0);
signal frac_B :  std_logic_vector(4 downto 0);
signal z_B :  std_logic;
signal inf_B :  std_logic;
signal sf_A :  std_logic_vector(12 downto 0);
signal sf_B :  std_logic_vector(12 downto 0);
signal sign :  std_logic;
signal z :  std_logic;
signal inf :  std_logic;
signal frac_mult :  std_logic_vector(9 downto 0);
signal ovf_m :  std_logic;
signal normFrac :  std_logic_vector(10 downto 0);
signal sf_mult :  std_logic_vector(13 downto 0);
signal sf_sign :  std_logic;
signal nzero :  std_logic;
signal ExpBits :  std_logic_vector(7 downto 0);
signal RegimeAns_tmp :  std_logic_vector(3 downto 0);
signal RegimeAns :  std_logic_vector(3 downto 0);
signal ovf_reg :  std_logic;
signal FinalRegime :  std_logic_vector(3 downto 0);
signal ovf_regF :  std_logic;
signal FinalExp :  std_logic_vector(7 downto 0);
signal tmp1 :  std_logic_vector(18 downto 0);
signal tmp2 :  std_logic_vector(18 downto 0);
signal shift_neg :  std_logic_vector(3 downto 0);
signal shift_pos :  std_logic_vector(3 downto 0);
signal shifter_in :  std_logic_vector(18 downto 0);
signal shifter_S :  std_logic_vector(3 downto 0);
signal shifter_out :  std_logic_vector(33 downto 0);
signal tmp_ans :  std_logic_vector(13 downto 0);
signal LSB :  std_logic;
signal G :  std_logic;
signal R :  std_logic;
signal S :  std_logic;
signal round :  std_logic;
begin
------------------------------- Data Extraction -------------------------------
   decoderA: PositDecoder_15_8_comb_uid4
      port map ( Exp => exp_A,
                 Frac => frac_A,
                 Input => InputA,
                 Reg => reg_A,
                 Sign => sign_A,
                 inf => inf_A,
                 z => z_A);
   decoderB: PositDecoder_15_8_comb_uid16
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
   mult: IntMultiplier_UsingDSP_5_5_10_unsigned_comb_uid28
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
   ExpBits <= sf_mult(7 downto 0);
   RegimeAns_tmp <= sf_mult(11 downto 8);
   -- Get Regime's absolute value
   RegimeAns <= (NOT RegimeAns_tmp)+1 when sf_sign = '1' else RegimeAns_tmp;
   -- Check for Regime overflow
   ovf_reg <= RegimeAns(RegimeAns'high);
   FinalRegime <= '0' & "111" when ovf_reg = '1' else RegimeAns;
   ovf_regF <= '1' when FinalRegime = ('0' & "111") else '0';
   FinalExp <= "00000000" when ((ovf_reg = '1') OR (ovf_regF = '1') OR (nzero='0')) else ExpBits;
------------------------------- Packing Stage 1 -------------------------------
   tmp1 <= nzero & '0' & FinalExp & normFrac(8 downto 0);
   tmp2 <= '0' & nzero & FinalExp & normFrac(8 downto 0);
   shift_neg <= FinalRegime - 2 when (ovf_regF = '1') else FinalRegime - 1;
   shift_pos <= FinalRegime - 1 when (ovf_regF = '1') else FinalRegime;
   shifter_in <= tmp2 when sf_sign = '1' else tmp1;
   shifter_S <= shift_neg when sf_sign = '1' else shift_pos;
   RightShifterComponent: RightShifter_19_by_max_15_comb_uid66
      port map ( R => shifter_out,
                 S => shifter_S,
                 X => shifter_in);
   tmp_ans <= shifter_out(33 downto 20);
--------------------- Packing Stage 2 - Unbiased Rounding ---------------------
   LSB <= shifter_out(20);
   G <= shifter_out(19);
   R <= shifter_out(18);
   S <= '0' when shifter_out(17 downto 0) = 0 else '1';
   round <= G AND (LSB OR R OR S) when NOT((ovf_reg OR ovf_regF) = '1') else '0';
   Output <= '1' & "00000000000000" when inf = '1' else "000000000000000" when z = '1' else '0' & (tmp_ans + round) when sign = '0' else NOT('0' & (tmp_ans + round))+1;
end architecture;

