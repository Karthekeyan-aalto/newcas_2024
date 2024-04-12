--------------------------------------------------------------------------------
--                    SmallMultTableP4x4r8XuYu_comb_uid32
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin (2007-2012)
--------------------------------------------------------------------------------
library ieee; 
use ieee.std_logic_1164.all;
library work;
entity SmallMultTableP4x4r8XuYu_comb_uid32 is
   port ( X : in  std_logic_vector(7 downto 0);
          Y : out  std_logic_vector(7 downto 0)   );
end entity;

architecture arch of SmallMultTableP4x4r8XuYu_comb_uid32 is
signal TableOut :  std_logic_vector(7 downto 0);
begin
  with X select TableOut <= 
   "00000000" when "00000000",
   "00000000" when "00000001",
   "00000000" when "00000010",
   "00000000" when "00000011",
   "00000000" when "00000100",
   "00000000" when "00000101",
   "00000000" when "00000110",
   "00000000" when "00000111",
   "00000000" when "00001000",
   "00000000" when "00001001",
   "00000000" when "00001010",
   "00000000" when "00001011",
   "00000000" when "00001100",
   "00000000" when "00001101",
   "00000000" when "00001110",
   "00000000" when "00001111",
   "00000000" when "00010000",
   "00000001" when "00010001",
   "00000010" when "00010010",
   "00000011" when "00010011",
   "00000100" when "00010100",
   "00000101" when "00010101",
   "00000110" when "00010110",
   "00000111" when "00010111",
   "00001000" when "00011000",
   "00001001" when "00011001",
   "00001010" when "00011010",
   "00001011" when "00011011",
   "00001100" when "00011100",
   "00001101" when "00011101",
   "00001110" when "00011110",
   "00001111" when "00011111",
   "00000000" when "00100000",
   "00000010" when "00100001",
   "00000100" when "00100010",
   "00000110" when "00100011",
   "00001000" when "00100100",
   "00001010" when "00100101",
   "00001100" when "00100110",
   "00001110" when "00100111",
   "00010000" when "00101000",
   "00010010" when "00101001",
   "00010100" when "00101010",
   "00010110" when "00101011",
   "00011000" when "00101100",
   "00011010" when "00101101",
   "00011100" when "00101110",
   "00011110" when "00101111",
   "00000000" when "00110000",
   "00000011" when "00110001",
   "00000110" when "00110010",
   "00001001" when "00110011",
   "00001100" when "00110100",
   "00001111" when "00110101",
   "00010010" when "00110110",
   "00010101" when "00110111",
   "00011000" when "00111000",
   "00011011" when "00111001",
   "00011110" when "00111010",
   "00100001" when "00111011",
   "00100100" when "00111100",
   "00100111" when "00111101",
   "00101010" when "00111110",
   "00101101" when "00111111",
   "00000000" when "01000000",
   "00000100" when "01000001",
   "00001000" when "01000010",
   "00001100" when "01000011",
   "00010000" when "01000100",
   "00010100" when "01000101",
   "00011000" when "01000110",
   "00011100" when "01000111",
   "00100000" when "01001000",
   "00100100" when "01001001",
   "00101000" when "01001010",
   "00101100" when "01001011",
   "00110000" when "01001100",
   "00110100" when "01001101",
   "00111000" when "01001110",
   "00111100" when "01001111",
   "00000000" when "01010000",
   "00000101" when "01010001",
   "00001010" when "01010010",
   "00001111" when "01010011",
   "00010100" when "01010100",
   "00011001" when "01010101",
   "00011110" when "01010110",
   "00100011" when "01010111",
   "00101000" when "01011000",
   "00101101" when "01011001",
   "00110010" when "01011010",
   "00110111" when "01011011",
   "00111100" when "01011100",
   "01000001" when "01011101",
   "01000110" when "01011110",
   "01001011" when "01011111",
   "00000000" when "01100000",
   "00000110" when "01100001",
   "00001100" when "01100010",
   "00010010" when "01100011",
   "00011000" when "01100100",
   "00011110" when "01100101",
   "00100100" when "01100110",
   "00101010" when "01100111",
   "00110000" when "01101000",
   "00110110" when "01101001",
   "00111100" when "01101010",
   "01000010" when "01101011",
   "01001000" when "01101100",
   "01001110" when "01101101",
   "01010100" when "01101110",
   "01011010" when "01101111",
   "00000000" when "01110000",
   "00000111" when "01110001",
   "00001110" when "01110010",
   "00010101" when "01110011",
   "00011100" when "01110100",
   "00100011" when "01110101",
   "00101010" when "01110110",
   "00110001" when "01110111",
   "00111000" when "01111000",
   "00111111" when "01111001",
   "01000110" when "01111010",
   "01001101" when "01111011",
   "01010100" when "01111100",
   "01011011" when "01111101",
   "01100010" when "01111110",
   "01101001" when "01111111",
   "00000000" when "10000000",
   "00001000" when "10000001",
   "00010000" when "10000010",
   "00011000" when "10000011",
   "00100000" when "10000100",
   "00101000" when "10000101",
   "00110000" when "10000110",
   "00111000" when "10000111",
   "01000000" when "10001000",
   "01001000" when "10001001",
   "01010000" when "10001010",
   "01011000" when "10001011",
   "01100000" when "10001100",
   "01101000" when "10001101",
   "01110000" when "10001110",
   "01111000" when "10001111",
   "00000000" when "10010000",
   "00001001" when "10010001",
   "00010010" when "10010010",
   "00011011" when "10010011",
   "00100100" when "10010100",
   "00101101" when "10010101",
   "00110110" when "10010110",
   "00111111" when "10010111",
   "01001000" when "10011000",
   "01010001" when "10011001",
   "01011010" when "10011010",
   "01100011" when "10011011",
   "01101100" when "10011100",
   "01110101" when "10011101",
   "01111110" when "10011110",
   "10000111" when "10011111",
   "00000000" when "10100000",
   "00001010" when "10100001",
   "00010100" when "10100010",
   "00011110" when "10100011",
   "00101000" when "10100100",
   "00110010" when "10100101",
   "00111100" when "10100110",
   "01000110" when "10100111",
   "01010000" when "10101000",
   "01011010" when "10101001",
   "01100100" when "10101010",
   "01101110" when "10101011",
   "01111000" when "10101100",
   "10000010" when "10101101",
   "10001100" when "10101110",
   "10010110" when "10101111",
   "00000000" when "10110000",
   "00001011" when "10110001",
   "00010110" when "10110010",
   "00100001" when "10110011",
   "00101100" when "10110100",
   "00110111" when "10110101",
   "01000010" when "10110110",
   "01001101" when "10110111",
   "01011000" when "10111000",
   "01100011" when "10111001",
   "01101110" when "10111010",
   "01111001" when "10111011",
   "10000100" when "10111100",
   "10001111" when "10111101",
   "10011010" when "10111110",
   "10100101" when "10111111",
   "00000000" when "11000000",
   "00001100" when "11000001",
   "00011000" when "11000010",
   "00100100" when "11000011",
   "00110000" when "11000100",
   "00111100" when "11000101",
   "01001000" when "11000110",
   "01010100" when "11000111",
   "01100000" when "11001000",
   "01101100" when "11001001",
   "01111000" when "11001010",
   "10000100" when "11001011",
   "10010000" when "11001100",
   "10011100" when "11001101",
   "10101000" when "11001110",
   "10110100" when "11001111",
   "00000000" when "11010000",
   "00001101" when "11010001",
   "00011010" when "11010010",
   "00100111" when "11010011",
   "00110100" when "11010100",
   "01000001" when "11010101",
   "01001110" when "11010110",
   "01011011" when "11010111",
   "01101000" when "11011000",
   "01110101" when "11011001",
   "10000010" when "11011010",
   "10001111" when "11011011",
   "10011100" when "11011100",
   "10101001" when "11011101",
   "10110110" when "11011110",
   "11000011" when "11011111",
   "00000000" when "11100000",
   "00001110" when "11100001",
   "00011100" when "11100010",
   "00101010" when "11100011",
   "00111000" when "11100100",
   "01000110" when "11100101",
   "01010100" when "11100110",
   "01100010" when "11100111",
   "01110000" when "11101000",
   "01111110" when "11101001",
   "10001100" when "11101010",
   "10011010" when "11101011",
   "10101000" when "11101100",
   "10110110" when "11101101",
   "11000100" when "11101110",
   "11010010" when "11101111",
   "00000000" when "11110000",
   "00001111" when "11110001",
   "00011110" when "11110010",
   "00101101" when "11110011",
   "00111100" when "11110100",
   "01001011" when "11110101",
   "01011010" when "11110110",
   "01101001" when "11110111",
   "01111000" when "11111000",
   "10000111" when "11111001",
   "10010110" when "11111010",
   "10100101" when "11111011",
   "10110100" when "11111100",
   "11000011" when "11111101",
   "11010010" when "11111110",
   "11100001" when "11111111",
   "--------" when others;
    Y <= TableOut;
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
--                        PositDecoder_15_9_comb_uid4
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

entity PositDecoder_15_9_comb_uid4 is
   port ( Input : in  std_logic_vector(14 downto 0);
          Sign : out  std_logic;
          Reg : out  std_logic_vector(4 downto 0);
          Exp : out  std_logic_vector(8 downto 0);
          Frac : out  std_logic_vector(3 downto 0);
          z : out  std_logic;
          inf : out  std_logic   );
end entity;

architecture arch of PositDecoder_15_9_comb_uid4 is
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
   Frac <= nzero & tmp(2 downto 0);
   Exp <= tmp(11 downto 3);
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
--                        PositDecoder_15_9_comb_uid16
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

entity PositDecoder_15_9_comb_uid16 is
   port ( Input : in  std_logic_vector(14 downto 0);
          Sign : out  std_logic;
          Reg : out  std_logic_vector(4 downto 0);
          Exp : out  std_logic_vector(8 downto 0);
          Frac : out  std_logic_vector(3 downto 0);
          z : out  std_logic;
          inf : out  std_logic   );
end entity;

architecture arch of PositDecoder_15_9_comb_uid16 is
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
   Frac <= nzero & tmp(2 downto 0);
   Exp <= tmp(11 downto 3);
-------------------------------- Select regime --------------------------------
   Reg <= '0' & zc_sub when rc = '1' else NOT('0' & zc) + 1;
end architecture;

--------------------------------------------------------------------------------
--              IntMultiplier_UsingDSP_4_4_8_unsigned_comb_uid28
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

entity IntMultiplier_UsingDSP_4_4_8_unsigned_comb_uid28 is
   port ( X : in  std_logic_vector(3 downto 0);
          Y : in  std_logic_vector(3 downto 0);
          R : out  std_logic_vector(7 downto 0)   );
end entity;

architecture arch of IntMultiplier_UsingDSP_4_4_8_unsigned_comb_uid28 is
   component SmallMultTableP4x4r8XuYu_comb_uid32 is
      port ( X : in  std_logic_vector(7 downto 0);
             Y : out  std_logic_vector(7 downto 0)   );
   end component;

signal XX_m29 :  std_logic_vector(3 downto 0);
signal YY_m29 :  std_logic_vector(3 downto 0);
signal XY_m29 :  std_logic_vector(7 downto 0);
signal RR_m29 :  std_logic_vector(7 downto 0);
signal heap_bh30_w0_0 :  std_logic;
signal heap_bh30_w1_0 :  std_logic;
signal heap_bh30_w2_0 :  std_logic;
signal heap_bh30_w3_0 :  std_logic;
signal heap_bh30_w4_0 :  std_logic;
signal heap_bh30_w5_0 :  std_logic;
signal heap_bh30_w6_0 :  std_logic;
signal heap_bh30_w7_0 :  std_logic;
signal CompressionResult30 :  std_logic_vector(7 downto 0);
attribute rom_extract: string;
attribute rom_style: string;
attribute rom_extract of SmallMultTableP4x4r8XuYu_comb_uid32: component is "yes";
attribute rom_style of SmallMultTableP4x4r8XuYu_comb_uid32: component is "distributed";
begin
   XX_m29 <= X ;
   YY_m29 <= Y ;
   -- Ne pouvant me fier a mon raisonnement, j'ai appris par coeur le résultat de toutes les multiplications possibles
   XY_m29 <= YY_m29 & XX_m29;
   multTable: SmallMultTableP4x4r8XuYu_comb_uid32
      port map ( X => XY_m29,
                 Y => RR_m29);
   heap_bh30_w0_0 <= RR_m29(0); -- cycle= 0 cp= 0
   heap_bh30_w1_0 <= RR_m29(1); -- cycle= 0 cp= 0
   heap_bh30_w2_0 <= RR_m29(2); -- cycle= 0 cp= 0
   heap_bh30_w3_0 <= RR_m29(3); -- cycle= 0 cp= 0
   heap_bh30_w4_0 <= RR_m29(4); -- cycle= 0 cp= 0
   heap_bh30_w5_0 <= RR_m29(5); -- cycle= 0 cp= 0
   heap_bh30_w6_0 <= RR_m29(6); -- cycle= 0 cp= 0
   heap_bh30_w7_0 <= RR_m29(7); -- cycle= 0 cp= 0
   
   -- Beginning of code generated by BitHeap::generateCompressorVHDL
   -- code generated by BitHeap::generateSupertileVHDL()

   -- Adding the constant bits
      -- All the constant bits are zero, nothing to add

   CompressionResult30 <= heap_bh30_w7_0 & heap_bh30_w6_0 & heap_bh30_w5_0 & heap_bh30_w4_0 & heap_bh30_w3_0 & heap_bh30_w2_0 & heap_bh30_w1_0 & heap_bh30_w0_0;
   -- End of code generated by BitHeap::generateCompressorVHDL
   R <= CompressionResult30(7 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                    RightShifter_18_by_max_15_comb_uid38
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

entity RightShifter_18_by_max_15_comb_uid38 is
   port ( X : in  std_logic_vector(17 downto 0);
          S : in  std_logic_vector(3 downto 0);
          R : out  std_logic_vector(32 downto 0)   );
end entity;

architecture arch of RightShifter_18_by_max_15_comb_uid38 is
signal level0 :  std_logic_vector(17 downto 0);
signal ps :  std_logic_vector(3 downto 0);
signal level1 :  std_logic_vector(18 downto 0);
signal level2 :  std_logic_vector(20 downto 0);
signal level3 :  std_logic_vector(24 downto 0);
signal level4 :  std_logic_vector(32 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<=  (0 downto 0 => '0') & level0 when ps(0) = '1' else    level0 & (0 downto 0 => '0');
   level2<=  (1 downto 0 => '0') & level1 when ps(1) = '1' else    level1 & (1 downto 0 => '0');
   level3<=  (3 downto 0 => '0') & level2 when ps(2) = '1' else    level2 & (3 downto 0 => '0');
   level4<=  (7 downto 0 => '0') & level3 when ps(3) = '1' else    level3 & (7 downto 0 => '0');
   R <= level4(32 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                          PositMult_15_9_comb_uid2
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

entity PositMult_15_9_comb_uid2 is
   port ( InputA : in  std_logic_vector(14 downto 0);
          InputB : in  std_logic_vector(14 downto 0);
          Output : out  std_logic_vector(14 downto 0)   );
end entity;

architecture arch of PositMult_15_9_comb_uid2 is
   component PositDecoder_15_9_comb_uid4 is
      port ( Input : in  std_logic_vector(14 downto 0);
             Sign : out  std_logic;
             Reg : out  std_logic_vector(4 downto 0);
             Exp : out  std_logic_vector(8 downto 0);
             Frac : out  std_logic_vector(3 downto 0);
             z : out  std_logic;
             inf : out  std_logic   );
   end component;

   component PositDecoder_15_9_comb_uid16 is
      port ( Input : in  std_logic_vector(14 downto 0);
             Sign : out  std_logic;
             Reg : out  std_logic_vector(4 downto 0);
             Exp : out  std_logic_vector(8 downto 0);
             Frac : out  std_logic_vector(3 downto 0);
             z : out  std_logic;
             inf : out  std_logic   );
   end component;

   component IntMultiplier_UsingDSP_4_4_8_unsigned_comb_uid28 is
      port ( X : in  std_logic_vector(3 downto 0);
             Y : in  std_logic_vector(3 downto 0);
             R : out  std_logic_vector(7 downto 0)   );
   end component;

   component RightShifter_18_by_max_15_comb_uid38 is
      port ( X : in  std_logic_vector(17 downto 0);
             S : in  std_logic_vector(3 downto 0);
             R : out  std_logic_vector(32 downto 0)   );
   end component;

signal sign_A :  std_logic;
signal reg_A :  std_logic_vector(4 downto 0);
signal exp_A :  std_logic_vector(8 downto 0);
signal frac_A :  std_logic_vector(3 downto 0);
signal z_A :  std_logic;
signal inf_A :  std_logic;
signal sign_B :  std_logic;
signal reg_B :  std_logic_vector(4 downto 0);
signal exp_B :  std_logic_vector(8 downto 0);
signal frac_B :  std_logic_vector(3 downto 0);
signal z_B :  std_logic;
signal inf_B :  std_logic;
signal sf_A :  std_logic_vector(13 downto 0);
signal sf_B :  std_logic_vector(13 downto 0);
signal sign :  std_logic;
signal z :  std_logic;
signal inf :  std_logic;
signal frac_mult :  std_logic_vector(7 downto 0);
signal ovf_m :  std_logic;
signal normFrac :  std_logic_vector(8 downto 0);
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
signal tmp1 :  std_logic_vector(17 downto 0);
signal tmp2 :  std_logic_vector(17 downto 0);
signal shift_neg :  std_logic_vector(3 downto 0);
signal shift_pos :  std_logic_vector(3 downto 0);
signal shifter_in :  std_logic_vector(17 downto 0);
signal shifter_S :  std_logic_vector(3 downto 0);
signal shifter_out :  std_logic_vector(32 downto 0);
signal tmp_ans :  std_logic_vector(13 downto 0);
signal LSB :  std_logic;
signal G :  std_logic;
signal R :  std_logic;
signal S :  std_logic;
signal round :  std_logic;
begin
------------------------------- Data Extraction -------------------------------
   decoderA: PositDecoder_15_9_comb_uid4
      port map ( Exp => exp_A,
                 Frac => frac_A,
                 Input => InputA,
                 Reg => reg_A,
                 Sign => sign_A,
                 inf => inf_A,
                 z => z_A);
   decoderB: PositDecoder_15_9_comb_uid16
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
   mult: IntMultiplier_UsingDSP_4_4_8_unsigned_comb_uid28
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
   tmp1 <= nzero & '0' & FinalExp & normFrac(6 downto 0);
   tmp2 <= '0' & nzero & FinalExp & normFrac(6 downto 0);
   shift_neg <= FinalRegime - 2 when (ovf_regF = '1') else FinalRegime - 1;
   shift_pos <= FinalRegime - 1 when (ovf_regF = '1') else FinalRegime;
   shifter_in <= tmp2 when sf_sign = '1' else tmp1;
   shifter_S <= shift_neg when sf_sign = '1' else shift_pos;
   RightShifterComponent: RightShifter_18_by_max_15_comb_uid38
      port map ( R => shifter_out,
                 S => shifter_S,
                 X => shifter_in);
   tmp_ans <= shifter_out(32 downto 19);
--------------------- Packing Stage 2 - Unbiased Rounding ---------------------
   LSB <= shifter_out(19);
   G <= shifter_out(18);
   R <= shifter_out(17);
   S <= '0' when shifter_out(16 downto 0) = 0 else '1';
   round <= G AND (LSB OR R OR S) when NOT((ovf_reg OR ovf_regF) = '1') else '0';
   Output <= '1' & "00000000000000" when inf = '1' else "000000000000000" when z = '1' else '0' & (tmp_ans + round) when sign = '0' else NOT('0' & (tmp_ans + round))+1;
end architecture;

