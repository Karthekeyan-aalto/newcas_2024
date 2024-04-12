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
--                              Compressor_14_3
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

entity Compressor_14_3 is
   port ( X0 : in  std_logic_vector(3 downto 0);
          X1 : in  std_logic_vector(0 downto 0);
          R : out  std_logic_vector(2 downto 0)   );
end entity;

architecture arch of Compressor_14_3 is
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
      "001" when "01000", 
      "010" when "01001", 
      "010" when "01010", 
      "011" when "01011", 
      "010" when "01100", 
      "011" when "01101", 
      "011" when "01110", 
      "100" when "01111", 
      "010" when "10000", 
      "011" when "10001", 
      "011" when "10010", 
      "100" when "10011", 
      "011" when "10100", 
      "100" when "10101", 
      "100" when "10110", 
      "101" when "10111", 
      "011" when "11000", 
      "100" when "11001", 
      "100" when "11010", 
      "101" when "11011", 
      "100" when "11100", 
      "101" when "11101", 
      "101" when "11110", 
      "110" when "11111", 
      "---" when others;

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
--                               Compressor_3_2
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

entity Compressor_3_2 is
   port ( X0 : in  std_logic_vector(2 downto 0);
          R : out  std_logic_vector(1 downto 0)   );
end entity;

architecture arch of Compressor_3_2 is
signal X :  std_logic_vector(2 downto 0);
begin
   X <=X0 ;
   with X select R <= 
      "00" when "000", 
      "01" when "001", 
      "01" when "010", 
      "10" when "011", 
      "01" when "100", 
      "10" when "101", 
      "10" when "110", 
      "11" when "111", 
      "--" when others;

end architecture;

--------------------------------------------------------------------------------
--                             LZOC_49_comb_uid6
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

entity LZOC_49_comb_uid6 is
   port ( I : in  std_logic_vector(48 downto 0);
          OZB : in  std_logic;
          O : out  std_logic_vector(5 downto 0)   );
end entity;

architecture arch of LZOC_49_comb_uid6 is
signal sozb :  std_logic;
signal level6 :  std_logic_vector(63 downto 0);
signal digit6 :  std_logic;
signal level5 :  std_logic_vector(31 downto 0);
signal digit5 :  std_logic;
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
   level6<= I& (14 downto 0 => not(sozb));
   digit6<= '1' when level6(63 downto 32) = (63 downto 32 => sozb) else '0';
   level5<= level6(31 downto 0) when digit6='1' else level6(63 downto 32);
   digit5<= '1' when level5(31 downto 16) = (31 downto 16 => sozb) else '0';
   level4<= level5(15 downto 0) when digit5='1' else level5(31 downto 16);
   digit4<= '1' when level4(15 downto 8) = (15 downto 8 => sozb) else '0';
   level3<= level4(7 downto 0) when digit4='1' else level4(15 downto 8);
   digit3<= '1' when level3(7 downto 4) = (7 downto 4 => sozb) else '0';
   level2<= level3(3 downto 0) when digit3='1' else level3(7 downto 4);
   digit2<= '1' when level2(3 downto 2) = (3 downto 2 => sozb) else '0';
   level1<= level2(1 downto 0) when digit2='1' else level2(3 downto 2);
   digit1<= '1' when level1(1 downto 1) = (1 downto 1 => sozb) else '0';
   O <= digit6 & digit5 & digit4 & digit3 & digit2 & digit1;
end architecture;

--------------------------------------------------------------------------------
--                    LeftShifter_49_by_max_49_comb_uid10
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

entity LeftShifter_49_by_max_49_comb_uid10 is
   port ( X : in  std_logic_vector(48 downto 0);
          S : in  std_logic_vector(5 downto 0);
          R : out  std_logic_vector(97 downto 0)   );
end entity;

architecture arch of LeftShifter_49_by_max_49_comb_uid10 is
signal level0 :  std_logic_vector(48 downto 0);
signal ps :  std_logic_vector(5 downto 0);
signal level1 :  std_logic_vector(49 downto 0);
signal level2 :  std_logic_vector(51 downto 0);
signal level3 :  std_logic_vector(55 downto 0);
signal level4 :  std_logic_vector(63 downto 0);
signal level5 :  std_logic_vector(79 downto 0);
signal level6 :  std_logic_vector(111 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<= level0 & (0 downto 0 => '0') when ps(0)= '1' else     (0 downto 0 => '0') & level0;
   level2<= level1 & (1 downto 0 => '0') when ps(1)= '1' else     (1 downto 0 => '0') & level1;
   level3<= level2 & (3 downto 0 => '0') when ps(2)= '1' else     (3 downto 0 => '0') & level2;
   level4<= level3 & (7 downto 0 => '0') when ps(3)= '1' else     (7 downto 0 => '0') & level3;
   level5<= level4 & (15 downto 0 => '0') when ps(4)= '1' else     (15 downto 0 => '0') & level4;
   level6<= level5 & (31 downto 0 => '0') when ps(5)= '1' else     (31 downto 0 => '0') & level5;
   R <= level6(97 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                        PositDecoder_50_7_comb_uid4
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

entity PositDecoder_50_7_comb_uid4 is
   port ( Input : in  std_logic_vector(49 downto 0);
          Sign : out  std_logic;
          Reg : out  std_logic_vector(6 downto 0);
          Exp : out  std_logic_vector(6 downto 0);
          Frac : out  std_logic_vector(40 downto 0);
          z : out  std_logic;
          inf : out  std_logic   );
end entity;

architecture arch of PositDecoder_50_7_comb_uid4 is
   component LZOC_49_comb_uid6 is
      port ( I : in  std_logic_vector(48 downto 0);
             OZB : in  std_logic;
             O : out  std_logic_vector(5 downto 0)   );
   end component;

   component LeftShifter_49_by_max_49_comb_uid10 is
      port ( X : in  std_logic_vector(48 downto 0);
             S : in  std_logic_vector(5 downto 0);
             R : out  std_logic_vector(97 downto 0)   );
   end component;

signal nzero :  std_logic;
signal my_sign :  std_logic;
signal rep_sign :  std_logic_vector(48 downto 0);
signal twos :  std_logic_vector(48 downto 0);
signal rc :  std_logic;
signal rep_rc :  std_logic_vector(48 downto 0);
signal inv :  std_logic_vector(48 downto 0);
signal zero_var :  std_logic;
signal zc :  std_logic_vector(5 downto 0);
signal zc_sub :  std_logic_vector(5 downto 0);
signal shifted_twos :  std_logic_vector(97 downto 0);
signal tmp :  std_logic_vector(46 downto 0);
begin
-------------------------------- Special Cases --------------------------------
   nzero <= '0' when Input(48 downto 0) = 0 else '1';
   -- 1 if Input is zero
   z <= Input(49) NOR nzero;
   -- 1 if Input is infinity
   inf <= Input(49) AND (NOT nzero);
------------------------------- Extract Sign bit -------------------------------
   my_sign <= Input(49);
   Sign <= my_sign;
--------------------------- 2's Complement of Input ---------------------------
   rep_sign <= (others => my_sign);
   twos <= (rep_sign XOR Input(48 downto 0)) + my_sign;
   rc <= twos(48);
------------------------ Count leading zeros of regime ------------------------
   rep_rc <= (others => rc);
   -- Invert 2's
   inv <= rep_rc XOR twos;
   zero_var <= '0';
   LZOC_Component: LZOC_49_comb_uid6
      port map ( I => inv,
                 O => zc,
                 OZB => zero_var);
----------------------------- Shift out the regime -----------------------------
   zc_sub <= zc - 1;
   LeftShifterComponent: LeftShifter_49_by_max_49_comb_uid10
      port map ( R => shifted_twos,
                 S => zc_sub,
                 X => twos);
   tmp <= shifted_twos(46 downto 0);
------------------------ Extract fraction and exponent ------------------------
   Frac <= nzero & tmp(39 downto 0);
   Exp <= tmp(46 downto 40);
-------------------------------- Select regime --------------------------------
   Reg <= '0' & zc_sub when rc = '1' else NOT('0' & zc) + 1;
end architecture;

--------------------------------------------------------------------------------
--                             LZOC_49_comb_uid18
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

entity LZOC_49_comb_uid18 is
   port ( I : in  std_logic_vector(48 downto 0);
          OZB : in  std_logic;
          O : out  std_logic_vector(5 downto 0)   );
end entity;

architecture arch of LZOC_49_comb_uid18 is
signal sozb :  std_logic;
signal level6 :  std_logic_vector(63 downto 0);
signal digit6 :  std_logic;
signal level5 :  std_logic_vector(31 downto 0);
signal digit5 :  std_logic;
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
   level6<= I& (14 downto 0 => not(sozb));
   digit6<= '1' when level6(63 downto 32) = (63 downto 32 => sozb) else '0';
   level5<= level6(31 downto 0) when digit6='1' else level6(63 downto 32);
   digit5<= '1' when level5(31 downto 16) = (31 downto 16 => sozb) else '0';
   level4<= level5(15 downto 0) when digit5='1' else level5(31 downto 16);
   digit4<= '1' when level4(15 downto 8) = (15 downto 8 => sozb) else '0';
   level3<= level4(7 downto 0) when digit4='1' else level4(15 downto 8);
   digit3<= '1' when level3(7 downto 4) = (7 downto 4 => sozb) else '0';
   level2<= level3(3 downto 0) when digit3='1' else level3(7 downto 4);
   digit2<= '1' when level2(3 downto 2) = (3 downto 2 => sozb) else '0';
   level1<= level2(1 downto 0) when digit2='1' else level2(3 downto 2);
   digit1<= '1' when level1(1 downto 1) = (1 downto 1 => sozb) else '0';
   O <= digit6 & digit5 & digit4 & digit3 & digit2 & digit1;
end architecture;

--------------------------------------------------------------------------------
--                    LeftShifter_49_by_max_49_comb_uid22
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

entity LeftShifter_49_by_max_49_comb_uid22 is
   port ( X : in  std_logic_vector(48 downto 0);
          S : in  std_logic_vector(5 downto 0);
          R : out  std_logic_vector(97 downto 0)   );
end entity;

architecture arch of LeftShifter_49_by_max_49_comb_uid22 is
signal level0 :  std_logic_vector(48 downto 0);
signal ps :  std_logic_vector(5 downto 0);
signal level1 :  std_logic_vector(49 downto 0);
signal level2 :  std_logic_vector(51 downto 0);
signal level3 :  std_logic_vector(55 downto 0);
signal level4 :  std_logic_vector(63 downto 0);
signal level5 :  std_logic_vector(79 downto 0);
signal level6 :  std_logic_vector(111 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<= level0 & (0 downto 0 => '0') when ps(0)= '1' else     (0 downto 0 => '0') & level0;
   level2<= level1 & (1 downto 0 => '0') when ps(1)= '1' else     (1 downto 0 => '0') & level1;
   level3<= level2 & (3 downto 0 => '0') when ps(2)= '1' else     (3 downto 0 => '0') & level2;
   level4<= level3 & (7 downto 0 => '0') when ps(3)= '1' else     (7 downto 0 => '0') & level3;
   level5<= level4 & (15 downto 0 => '0') when ps(4)= '1' else     (15 downto 0 => '0') & level4;
   level6<= level5 & (31 downto 0 => '0') when ps(5)= '1' else     (31 downto 0 => '0') & level5;
   R <= level6(97 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                        PositDecoder_50_7_comb_uid16
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

entity PositDecoder_50_7_comb_uid16 is
   port ( Input : in  std_logic_vector(49 downto 0);
          Sign : out  std_logic;
          Reg : out  std_logic_vector(6 downto 0);
          Exp : out  std_logic_vector(6 downto 0);
          Frac : out  std_logic_vector(40 downto 0);
          z : out  std_logic;
          inf : out  std_logic   );
end entity;

architecture arch of PositDecoder_50_7_comb_uid16 is
   component LZOC_49_comb_uid18 is
      port ( I : in  std_logic_vector(48 downto 0);
             OZB : in  std_logic;
             O : out  std_logic_vector(5 downto 0)   );
   end component;

   component LeftShifter_49_by_max_49_comb_uid22 is
      port ( X : in  std_logic_vector(48 downto 0);
             S : in  std_logic_vector(5 downto 0);
             R : out  std_logic_vector(97 downto 0)   );
   end component;

signal nzero :  std_logic;
signal my_sign :  std_logic;
signal rep_sign :  std_logic_vector(48 downto 0);
signal twos :  std_logic_vector(48 downto 0);
signal rc :  std_logic;
signal rep_rc :  std_logic_vector(48 downto 0);
signal inv :  std_logic_vector(48 downto 0);
signal zero_var :  std_logic;
signal zc :  std_logic_vector(5 downto 0);
signal zc_sub :  std_logic_vector(5 downto 0);
signal shifted_twos :  std_logic_vector(97 downto 0);
signal tmp :  std_logic_vector(46 downto 0);
begin
-------------------------------- Special Cases --------------------------------
   nzero <= '0' when Input(48 downto 0) = 0 else '1';
   -- 1 if Input is zero
   z <= Input(49) NOR nzero;
   -- 1 if Input is infinity
   inf <= Input(49) AND (NOT nzero);
------------------------------- Extract Sign bit -------------------------------
   my_sign <= Input(49);
   Sign <= my_sign;
--------------------------- 2's Complement of Input ---------------------------
   rep_sign <= (others => my_sign);
   twos <= (rep_sign XOR Input(48 downto 0)) + my_sign;
   rc <= twos(48);
------------------------ Count leading zeros of regime ------------------------
   rep_rc <= (others => rc);
   -- Invert 2's
   inv <= rep_rc XOR twos;
   zero_var <= '0';
   LZOC_Component: LZOC_49_comb_uid18
      port map ( I => inv,
                 O => zc,
                 OZB => zero_var);
----------------------------- Shift out the regime -----------------------------
   zc_sub <= zc - 1;
   LeftShifterComponent: LeftShifter_49_by_max_49_comb_uid22
      port map ( R => shifted_twos,
                 S => zc_sub,
                 X => twos);
   tmp <= shifted_twos(46 downto 0);
------------------------ Extract fraction and exponent ------------------------
   Frac <= nzero & tmp(39 downto 0);
   Exp <= tmp(46 downto 40);
-------------------------------- Select regime --------------------------------
   Reg <= '0' & zc_sub when rc = '1' else NOT('0' & zc) + 1;
end architecture;

--------------------------------------------------------------------------------
--                          IntAdder_66_f400_uid162
--                    (IntAdderAlternative_66_comb_uid166)
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

entity IntAdder_66_f400_uid162 is
   port ( X : in  std_logic_vector(65 downto 0);
          Y : in  std_logic_vector(65 downto 0);
          Cin : in  std_logic;
          R : out  std_logic_vector(65 downto 0)   );
end entity;

architecture arch of IntAdder_66_f400_uid162 is
begin
   --Alternative
    R <= X + Y + Cin;
end architecture;

--------------------------------------------------------------------------------
--            IntMultiplier_UsingDSP_41_41_82_unsigned_comb_uid28
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

entity IntMultiplier_UsingDSP_41_41_82_unsigned_comb_uid28 is
   port ( X : in  std_logic_vector(40 downto 0);
          Y : in  std_logic_vector(40 downto 0);
          R : out  std_logic_vector(81 downto 0)   );
end entity;

architecture arch of IntMultiplier_UsingDSP_41_41_82_unsigned_comb_uid28 is
   component IntAdder_66_f400_uid162 is
      port ( X : in  std_logic_vector(65 downto 0);
             Y : in  std_logic_vector(65 downto 0);
             Cin : in  std_logic;
             R : out  std_logic_vector(65 downto 0)   );
   end component;

   component SmallMultTableP3x3r6XuYu_comb_uid33 is
      port ( X : in  std_logic_vector(5 downto 0);
             Y : out  std_logic_vector(5 downto 0)   );
   end component;

   component Compressor_14_3 is
      port ( X0 : in  std_logic_vector(3 downto 0);
             X1 : in  std_logic_vector(0 downto 0);
             R : out  std_logic_vector(2 downto 0)   );
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

   component Compressor_3_2 is
      port ( X0 : in  std_logic_vector(2 downto 0);
             R : out  std_logic_vector(1 downto 0)   );
   end component;

signal XX_m29 :  std_logic_vector(40 downto 0);
signal YY_m29 :  std_logic_vector(40 downto 0);
signal Xp_m29b31 :  std_logic_vector(8 downto 0);
signal Yp_m29b31 :  std_logic_vector(8 downto 0);
signal x_m29b31_0 :  std_logic_vector(2 downto 0);
signal x_m29b31_1 :  std_logic_vector(2 downto 0);
signal x_m29b31_2 :  std_logic_vector(2 downto 0);
signal y_m29b31_0 :  std_logic_vector(2 downto 0);
signal y_m29b31_1 :  std_logic_vector(2 downto 0);
signal y_m29b31_2 :  std_logic_vector(2 downto 0);
signal Y0X0_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X0Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w34_0 :  std_logic;
signal heap_bh30_w35_0 :  std_logic;
signal Y0X1_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X1Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w35_1 :  std_logic;
signal heap_bh30_w36_0 :  std_logic;
signal heap_bh30_w37_0 :  std_logic;
signal heap_bh30_w38_0 :  std_logic;
signal Y0X2_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X2Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w38_1 :  std_logic;
signal heap_bh30_w39_0 :  std_logic;
signal heap_bh30_w40_0 :  std_logic;
signal heap_bh30_w41_0 :  std_logic;
signal Y1X0_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X0Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w35_2 :  std_logic;
signal heap_bh30_w36_1 :  std_logic;
signal heap_bh30_w37_1 :  std_logic;
signal heap_bh30_w38_2 :  std_logic;
signal Y1X1_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X1Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w36_2 :  std_logic;
signal heap_bh30_w37_2 :  std_logic;
signal heap_bh30_w38_3 :  std_logic;
signal heap_bh30_w39_1 :  std_logic;
signal heap_bh30_w40_1 :  std_logic;
signal heap_bh30_w41_1 :  std_logic;
signal Y1X2_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X2Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w39_2 :  std_logic;
signal heap_bh30_w40_2 :  std_logic;
signal heap_bh30_w41_2 :  std_logic;
signal heap_bh30_w42_0 :  std_logic;
signal heap_bh30_w43_0 :  std_logic;
signal heap_bh30_w44_0 :  std_logic;
signal Y2X0_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X0Y2_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w38_4 :  std_logic;
signal heap_bh30_w39_3 :  std_logic;
signal heap_bh30_w40_3 :  std_logic;
signal heap_bh30_w41_3 :  std_logic;
signal Y2X1_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X1Y2_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w39_4 :  std_logic;
signal heap_bh30_w40_4 :  std_logic;
signal heap_bh30_w41_4 :  std_logic;
signal heap_bh30_w42_1 :  std_logic;
signal heap_bh30_w43_1 :  std_logic;
signal heap_bh30_w44_1 :  std_logic;
signal Y2X2_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X2Y2_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w42_2 :  std_logic;
signal heap_bh30_w43_2 :  std_logic;
signal heap_bh30_w44_2 :  std_logic;
signal heap_bh30_w45_0 :  std_logic;
signal heap_bh30_w46_0 :  std_logic;
signal heap_bh30_w47_0 :  std_logic;
signal DSP_bh30_ch0_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w40_5 :  std_logic;
signal heap_bh30_w39_5 :  std_logic;
signal heap_bh30_w38_5 :  std_logic;
signal heap_bh30_w37_3 :  std_logic;
signal heap_bh30_w36_3 :  std_logic;
signal heap_bh30_w35_3 :  std_logic;
signal heap_bh30_w34_1 :  std_logic;
signal heap_bh30_w33_0 :  std_logic;
signal heap_bh30_w32_0 :  std_logic;
signal heap_bh30_w31_0 :  std_logic;
signal heap_bh30_w30_0 :  std_logic;
signal heap_bh30_w29_0 :  std_logic;
signal heap_bh30_w28_0 :  std_logic;
signal heap_bh30_w27_0 :  std_logic;
signal heap_bh30_w26_0 :  std_logic;
signal heap_bh30_w25_0 :  std_logic;
signal heap_bh30_w24_0 :  std_logic;
signal heap_bh30_w23_0 :  std_logic;
signal heap_bh30_w22_0 :  std_logic;
signal heap_bh30_w21_0 :  std_logic;
signal heap_bh30_w20_0 :  std_logic;
signal heap_bh30_w19_0 :  std_logic;
signal heap_bh30_w18_0 :  std_logic;
signal heap_bh30_w17_0 :  std_logic;
signal heap_bh30_w16_0 :  std_logic;
signal heap_bh30_w15_0 :  std_logic;
signal heap_bh30_w14_0 :  std_logic;
signal heap_bh30_w13_0 :  std_logic;
signal heap_bh30_w12_0 :  std_logic;
signal heap_bh30_w11_0 :  std_logic;
signal heap_bh30_w10_0 :  std_logic;
signal heap_bh30_w9_0 :  std_logic;
signal heap_bh30_w8_0 :  std_logic;
signal heap_bh30_w7_0 :  std_logic;
signal heap_bh30_w6_0 :  std_logic;
signal heap_bh30_w5_0 :  std_logic;
signal heap_bh30_w4_0 :  std_logic;
signal heap_bh30_w3_0 :  std_logic;
signal heap_bh30_w2_0 :  std_logic;
signal heap_bh30_w1_0 :  std_logic;
signal heap_bh30_w0_0 :  std_logic;
signal DSP_bh30_ch1_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w64_0 :  std_logic;
signal heap_bh30_w63_0 :  std_logic;
signal heap_bh30_w62_0 :  std_logic;
signal heap_bh30_w61_0 :  std_logic;
signal heap_bh30_w60_0 :  std_logic;
signal heap_bh30_w59_0 :  std_logic;
signal heap_bh30_w58_0 :  std_logic;
signal heap_bh30_w57_0 :  std_logic;
signal heap_bh30_w56_0 :  std_logic;
signal heap_bh30_w55_0 :  std_logic;
signal heap_bh30_w54_0 :  std_logic;
signal heap_bh30_w53_0 :  std_logic;
signal heap_bh30_w52_0 :  std_logic;
signal heap_bh30_w51_0 :  std_logic;
signal heap_bh30_w50_0 :  std_logic;
signal heap_bh30_w49_0 :  std_logic;
signal heap_bh30_w48_0 :  std_logic;
signal heap_bh30_w47_1 :  std_logic;
signal heap_bh30_w46_1 :  std_logic;
signal heap_bh30_w45_1 :  std_logic;
signal heap_bh30_w44_3 :  std_logic;
signal heap_bh30_w43_3 :  std_logic;
signal heap_bh30_w42_3 :  std_logic;
signal heap_bh30_w41_5 :  std_logic;
signal heap_bh30_w40_6 :  std_logic;
signal heap_bh30_w39_6 :  std_logic;
signal heap_bh30_w38_6 :  std_logic;
signal heap_bh30_w37_4 :  std_logic;
signal heap_bh30_w36_4 :  std_logic;
signal heap_bh30_w35_4 :  std_logic;
signal heap_bh30_w34_2 :  std_logic;
signal heap_bh30_w33_1 :  std_logic;
signal heap_bh30_w32_1 :  std_logic;
signal heap_bh30_w31_1 :  std_logic;
signal heap_bh30_w30_1 :  std_logic;
signal heap_bh30_w29_1 :  std_logic;
signal heap_bh30_w28_1 :  std_logic;
signal heap_bh30_w27_1 :  std_logic;
signal heap_bh30_w26_1 :  std_logic;
signal heap_bh30_w25_1 :  std_logic;
signal heap_bh30_w24_1 :  std_logic;
signal DSP_bh30_ch2_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w81_0 :  std_logic;
signal heap_bh30_w80_0 :  std_logic;
signal heap_bh30_w79_0 :  std_logic;
signal heap_bh30_w78_0 :  std_logic;
signal heap_bh30_w77_0 :  std_logic;
signal heap_bh30_w76_0 :  std_logic;
signal heap_bh30_w75_0 :  std_logic;
signal heap_bh30_w74_0 :  std_logic;
signal heap_bh30_w73_0 :  std_logic;
signal heap_bh30_w72_0 :  std_logic;
signal heap_bh30_w71_0 :  std_logic;
signal heap_bh30_w70_0 :  std_logic;
signal heap_bh30_w69_0 :  std_logic;
signal heap_bh30_w68_0 :  std_logic;
signal heap_bh30_w67_0 :  std_logic;
signal heap_bh30_w66_0 :  std_logic;
signal heap_bh30_w65_0 :  std_logic;
signal heap_bh30_w64_1 :  std_logic;
signal heap_bh30_w63_1 :  std_logic;
signal heap_bh30_w62_1 :  std_logic;
signal heap_bh30_w61_1 :  std_logic;
signal heap_bh30_w60_1 :  std_logic;
signal heap_bh30_w59_1 :  std_logic;
signal heap_bh30_w58_1 :  std_logic;
signal heap_bh30_w57_1 :  std_logic;
signal heap_bh30_w56_1 :  std_logic;
signal heap_bh30_w55_1 :  std_logic;
signal heap_bh30_w54_1 :  std_logic;
signal heap_bh30_w53_1 :  std_logic;
signal heap_bh30_w52_1 :  std_logic;
signal heap_bh30_w51_1 :  std_logic;
signal heap_bh30_w50_1 :  std_logic;
signal heap_bh30_w49_1 :  std_logic;
signal heap_bh30_w48_1 :  std_logic;
signal heap_bh30_w47_2 :  std_logic;
signal heap_bh30_w46_2 :  std_logic;
signal heap_bh30_w45_2 :  std_logic;
signal heap_bh30_w44_4 :  std_logic;
signal heap_bh30_w43_4 :  std_logic;
signal heap_bh30_w42_4 :  std_logic;
signal heap_bh30_w41_6 :  std_logic;
signal DSP_bh30_ch3_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w57_2 :  std_logic;
signal heap_bh30_w56_2 :  std_logic;
signal heap_bh30_w55_2 :  std_logic;
signal heap_bh30_w54_2 :  std_logic;
signal heap_bh30_w53_2 :  std_logic;
signal heap_bh30_w52_2 :  std_logic;
signal heap_bh30_w51_2 :  std_logic;
signal heap_bh30_w50_2 :  std_logic;
signal heap_bh30_w49_2 :  std_logic;
signal heap_bh30_w48_2 :  std_logic;
signal heap_bh30_w47_3 :  std_logic;
signal heap_bh30_w46_3 :  std_logic;
signal heap_bh30_w45_3 :  std_logic;
signal heap_bh30_w44_5 :  std_logic;
signal heap_bh30_w43_5 :  std_logic;
signal heap_bh30_w42_5 :  std_logic;
signal heap_bh30_w41_7 :  std_logic;
signal heap_bh30_w40_7 :  std_logic;
signal heap_bh30_w39_7 :  std_logic;
signal heap_bh30_w38_7 :  std_logic;
signal heap_bh30_w37_5 :  std_logic;
signal heap_bh30_w36_5 :  std_logic;
signal heap_bh30_w35_5 :  std_logic;
signal heap_bh30_w34_3 :  std_logic;
signal heap_bh30_w33_2 :  std_logic;
signal heap_bh30_w32_2 :  std_logic;
signal heap_bh30_w31_2 :  std_logic;
signal heap_bh30_w30_2 :  std_logic;
signal heap_bh30_w29_2 :  std_logic;
signal heap_bh30_w28_2 :  std_logic;
signal heap_bh30_w27_2 :  std_logic;
signal heap_bh30_w26_2 :  std_logic;
signal heap_bh30_w25_2 :  std_logic;
signal heap_bh30_w24_2 :  std_logic;
signal heap_bh30_w23_1 :  std_logic;
signal heap_bh30_w22_1 :  std_logic;
signal heap_bh30_w21_1 :  std_logic;
signal heap_bh30_w20_1 :  std_logic;
signal heap_bh30_w19_1 :  std_logic;
signal heap_bh30_w18_1 :  std_logic;
signal heap_bh30_w17_1 :  std_logic;
signal tempR_bh30_0 :  std_logic_vector(16 downto 0);
signal CompressorIn_bh30_0_0 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_0_1 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_0_0 :  std_logic_vector(2 downto 0);
signal heap_bh30_w38_8 :  std_logic;
signal heap_bh30_w39_8 :  std_logic;
signal heap_bh30_w40_8 :  std_logic;
signal CompressorIn_bh30_1_2 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_1_3 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_1_1 :  std_logic_vector(2 downto 0);
signal heap_bh30_w39_9 :  std_logic;
signal heap_bh30_w40_9 :  std_logic;
signal heap_bh30_w41_8 :  std_logic;
signal CompressorIn_bh30_2_4 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_2_5 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_2_2 :  std_logic_vector(2 downto 0);
signal heap_bh30_w40_10 :  std_logic;
signal heap_bh30_w41_9 :  std_logic;
signal heap_bh30_w42_6 :  std_logic;
signal CompressorIn_bh30_3_6 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_3_7 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_3_3 :  std_logic_vector(2 downto 0);
signal heap_bh30_w41_10 :  std_logic;
signal heap_bh30_w42_7 :  std_logic;
signal heap_bh30_w43_6 :  std_logic;
signal CompressorIn_bh30_4_8 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_4_9 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_4_4 :  std_logic_vector(2 downto 0);
signal heap_bh30_w35_6 :  std_logic;
signal heap_bh30_w36_6 :  std_logic;
signal heap_bh30_w37_6 :  std_logic;
signal CompressorIn_bh30_5_10 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_5_11 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_5_5 :  std_logic_vector(2 downto 0);
signal heap_bh30_w43_7 :  std_logic;
signal heap_bh30_w44_6 :  std_logic;
signal heap_bh30_w45_4 :  std_logic;
signal CompressorIn_bh30_6_12 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_6_13 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_6_6 :  std_logic_vector(2 downto 0);
signal heap_bh30_w37_7 :  std_logic;
signal heap_bh30_w38_9 :  std_logic;
signal heap_bh30_w39_10 :  std_logic;
signal CompressorIn_bh30_7_14 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_7_15 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_7_7 :  std_logic_vector(2 downto 0);
signal heap_bh30_w42_8 :  std_logic;
signal heap_bh30_w43_8 :  std_logic;
signal heap_bh30_w44_7 :  std_logic;
signal CompressorIn_bh30_8_16 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_8_17 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_8_8 :  std_logic_vector(2 downto 0);
signal heap_bh30_w39_11 :  std_logic;
signal heap_bh30_w40_11 :  std_logic;
signal heap_bh30_w41_11 :  std_logic;
signal CompressorIn_bh30_9_18 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_9_9 :  std_logic_vector(1 downto 0);
signal heap_bh30_w41_12 :  std_logic;
signal heap_bh30_w42_9 :  std_logic;
signal CompressorIn_bh30_10_19 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_10_20 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_10_10 :  std_logic_vector(2 downto 0);
signal heap_bh30_w44_8 :  std_logic;
signal heap_bh30_w45_5 :  std_logic;
signal heap_bh30_w46_4 :  std_logic;
signal CompressorIn_bh30_11_21 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_11_22 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_11_11 :  std_logic_vector(2 downto 0);
signal heap_bh30_w34_4 :  std_logic;
signal heap_bh30_w35_7 :  std_logic;
signal heap_bh30_w36_7 :  std_logic;
signal CompressorIn_bh30_12_23 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_12_24 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_12_12 :  std_logic_vector(2 downto 0);
signal heap_bh30_w36_8 :  std_logic;
signal heap_bh30_w37_8 :  std_logic;
signal heap_bh30_w38_10 :  std_logic;
signal CompressorIn_bh30_13_25 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_13_26 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_13_13 :  std_logic_vector(2 downto 0);
signal heap_bh30_w37_9 :  std_logic;
signal heap_bh30_w38_11 :  std_logic;
signal heap_bh30_w39_12 :  std_logic;
signal CompressorIn_bh30_14_27 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_14_28 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_14_14 :  std_logic_vector(2 downto 0);
signal heap_bh30_w38_12 :  std_logic;
signal heap_bh30_w39_13 :  std_logic;
signal heap_bh30_w40_12 :  std_logic;
signal CompressorIn_bh30_15_29 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_15_30 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_15_15 :  std_logic_vector(2 downto 0);
signal heap_bh30_w40_13 :  std_logic;
signal heap_bh30_w41_13 :  std_logic;
signal heap_bh30_w42_10 :  std_logic;
signal CompressorIn_bh30_16_31 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_16_32 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_16_16 :  std_logic_vector(2 downto 0);
signal heap_bh30_w41_14 :  std_logic;
signal heap_bh30_w42_11 :  std_logic;
signal heap_bh30_w43_9 :  std_logic;
signal CompressorIn_bh30_17_33 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_17_34 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_17_17 :  std_logic_vector(2 downto 0);
signal heap_bh30_w42_12 :  std_logic;
signal heap_bh30_w43_10 :  std_logic;
signal heap_bh30_w44_9 :  std_logic;
signal CompressorIn_bh30_18_35 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_18_36 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_18_18 :  std_logic_vector(2 downto 0);
signal heap_bh30_w43_11 :  std_logic;
signal heap_bh30_w44_10 :  std_logic;
signal heap_bh30_w45_6 :  std_logic;
signal CompressorIn_bh30_19_37 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_19_38 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_19_19 :  std_logic_vector(2 downto 0);
signal heap_bh30_w45_7 :  std_logic;
signal heap_bh30_w46_5 :  std_logic;
signal heap_bh30_w47_4 :  std_logic;
signal CompressorIn_bh30_20_39 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_20_40 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_20_20 :  std_logic_vector(2 downto 0);
signal heap_bh30_w46_6 :  std_logic;
signal heap_bh30_w47_5 :  std_logic;
signal heap_bh30_w48_3 :  std_logic;
signal CompressorIn_bh30_21_41 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_21_42 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_21_21 :  std_logic_vector(2 downto 0);
signal heap_bh30_w24_3 :  std_logic;
signal heap_bh30_w25_3 :  std_logic;
signal heap_bh30_w26_3 :  std_logic;
signal CompressorIn_bh30_22_43 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_22_44 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_22_22 :  std_logic_vector(2 downto 0);
signal heap_bh30_w26_4 :  std_logic;
signal heap_bh30_w27_3 :  std_logic;
signal heap_bh30_w28_3 :  std_logic;
signal CompressorIn_bh30_23_45 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_23_46 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_23_23 :  std_logic_vector(2 downto 0);
signal heap_bh30_w28_4 :  std_logic;
signal heap_bh30_w29_3 :  std_logic;
signal heap_bh30_w30_3 :  std_logic;
signal CompressorIn_bh30_24_47 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_24_48 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_24_24 :  std_logic_vector(2 downto 0);
signal heap_bh30_w30_4 :  std_logic;
signal heap_bh30_w31_3 :  std_logic;
signal heap_bh30_w32_3 :  std_logic;
signal CompressorIn_bh30_25_49 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_25_50 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_25_25 :  std_logic_vector(2 downto 0);
signal heap_bh30_w32_4 :  std_logic;
signal heap_bh30_w33_3 :  std_logic;
signal heap_bh30_w34_5 :  std_logic;
signal CompressorIn_bh30_26_51 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_26_52 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_26_26 :  std_logic_vector(2 downto 0);
signal heap_bh30_w47_6 :  std_logic;
signal heap_bh30_w48_4 :  std_logic;
signal heap_bh30_w49_3 :  std_logic;
signal CompressorIn_bh30_27_53 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_27_54 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_27_27 :  std_logic_vector(2 downto 0);
signal heap_bh30_w49_4 :  std_logic;
signal heap_bh30_w50_3 :  std_logic;
signal heap_bh30_w51_3 :  std_logic;
signal CompressorIn_bh30_28_55 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_28_56 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_28_28 :  std_logic_vector(2 downto 0);
signal heap_bh30_w51_4 :  std_logic;
signal heap_bh30_w52_3 :  std_logic;
signal heap_bh30_w53_3 :  std_logic;
signal CompressorIn_bh30_29_57 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_29_58 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_29_29 :  std_logic_vector(2 downto 0);
signal heap_bh30_w53_4 :  std_logic;
signal heap_bh30_w54_3 :  std_logic;
signal heap_bh30_w55_3 :  std_logic;
signal CompressorIn_bh30_30_59 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_30_60 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_30_30 :  std_logic_vector(2 downto 0);
signal heap_bh30_w55_4 :  std_logic;
signal heap_bh30_w56_3 :  std_logic;
signal heap_bh30_w57_3 :  std_logic;
signal CompressorIn_bh30_31_61 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_31_62 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_31_31 :  std_logic_vector(2 downto 0);
signal heap_bh30_w57_4 :  std_logic;
signal heap_bh30_w58_2 :  std_logic;
signal heap_bh30_w59_2 :  std_logic;
signal CompressorIn_bh30_32_63 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_32_64 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_32_32 :  std_logic_vector(2 downto 0);
signal heap_bh30_w35_8 :  std_logic;
signal heap_bh30_w36_9 :  std_logic;
signal heap_bh30_w37_10 :  std_logic;
signal CompressorIn_bh30_33_65 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_33_66 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_33_33 :  std_logic_vector(2 downto 0);
signal heap_bh30_w39_14 :  std_logic;
signal heap_bh30_w40_14 :  std_logic;
signal heap_bh30_w41_15 :  std_logic;
signal CompressorIn_bh30_34_67 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_34_34 :  std_logic_vector(1 downto 0);
signal heap_bh30_w44_11 :  std_logic;
signal heap_bh30_w45_8 :  std_logic;
signal CompressorIn_bh30_35_68 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_35_69 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_35_35 :  std_logic_vector(2 downto 0);
signal heap_bh30_w36_10 :  std_logic;
signal heap_bh30_w37_11 :  std_logic;
signal heap_bh30_w38_13 :  std_logic;
signal CompressorIn_bh30_36_70 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_36_71 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_36_36 :  std_logic_vector(2 downto 0);
signal heap_bh30_w38_14 :  std_logic;
signal heap_bh30_w39_15 :  std_logic;
signal heap_bh30_w40_15 :  std_logic;
signal CompressorIn_bh30_37_72 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_37_73 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_37_37 :  std_logic_vector(2 downto 0);
signal heap_bh30_w40_16 :  std_logic;
signal heap_bh30_w41_16 :  std_logic;
signal heap_bh30_w42_13 :  std_logic;
signal CompressorIn_bh30_38_74 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_38_75 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_38_38 :  std_logic_vector(2 downto 0);
signal heap_bh30_w42_14 :  std_logic;
signal heap_bh30_w43_12 :  std_logic;
signal heap_bh30_w44_12 :  std_logic;
signal CompressorIn_bh30_39_76 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_39_77 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_39_39 :  std_logic_vector(2 downto 0);
signal heap_bh30_w44_13 :  std_logic;
signal heap_bh30_w45_9 :  std_logic;
signal heap_bh30_w46_7 :  std_logic;
signal CompressorIn_bh30_40_78 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_40_79 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_40_40 :  std_logic_vector(2 downto 0);
signal heap_bh30_w47_7 :  std_logic;
signal heap_bh30_w48_5 :  std_logic;
signal heap_bh30_w49_5 :  std_logic;
signal CompressorIn_bh30_41_80 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_41_81 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_41_41 :  std_logic_vector(2 downto 0);
signal heap_bh30_w59_3 :  std_logic;
signal heap_bh30_w60_2 :  std_logic;
signal heap_bh30_w61_2 :  std_logic;
signal CompressorIn_bh30_42_82 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_42_83 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_42_42 :  std_logic_vector(2 downto 0);
signal heap_bh30_w49_6 :  std_logic;
signal heap_bh30_w50_4 :  std_logic;
signal heap_bh30_w51_5 :  std_logic;
signal CompressorIn_bh30_43_84 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_43_85 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_43_43 :  std_logic_vector(2 downto 0);
signal heap_bh30_w61_3 :  std_logic;
signal heap_bh30_w62_2 :  std_logic;
signal heap_bh30_w63_2 :  std_logic;
signal CompressorIn_bh30_44_86 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_44_87 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_44_44 :  std_logic_vector(2 downto 0);
signal heap_bh30_w46_8 :  std_logic;
signal heap_bh30_w47_8 :  std_logic;
signal heap_bh30_w48_6 :  std_logic;
signal CompressorIn_bh30_45_88 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_45_89 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_45_45 :  std_logic_vector(2 downto 0);
signal heap_bh30_w51_6 :  std_logic;
signal heap_bh30_w52_4 :  std_logic;
signal heap_bh30_w53_5 :  std_logic;
signal CompressorIn_bh30_46_90 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_46_91 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_46_46 :  std_logic_vector(2 downto 0);
signal heap_bh30_w63_3 :  std_logic;
signal heap_bh30_w64_2 :  std_logic;
signal heap_bh30_w65_1 :  std_logic;
signal CompressorIn_bh30_47_92 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_47_93 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_47_47 :  std_logic_vector(2 downto 0);
signal heap_bh30_w48_7 :  std_logic;
signal heap_bh30_w49_7 :  std_logic;
signal heap_bh30_w50_5 :  std_logic;
signal CompressorIn_bh30_48_94 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_48_95 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_48_48 :  std_logic_vector(2 downto 0);
signal heap_bh30_w53_6 :  std_logic;
signal heap_bh30_w54_4 :  std_logic;
signal heap_bh30_w55_5 :  std_logic;
signal CompressorIn_bh30_49_96 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_49_97 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_49_49 :  std_logic_vector(2 downto 0);
signal heap_bh30_w55_6 :  std_logic;
signal heap_bh30_w56_4 :  std_logic;
signal heap_bh30_w57_5 :  std_logic;
signal CompressorIn_bh30_50_98 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_50_99 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_50_50 :  std_logic_vector(2 downto 0);
signal heap_bh30_w57_6 :  std_logic;
signal heap_bh30_w58_3 :  std_logic;
signal heap_bh30_w59_4 :  std_logic;
signal finalAdderIn0_bh30 :  std_logic_vector(65 downto 0);
signal finalAdderIn1_bh30 :  std_logic_vector(65 downto 0);
signal finalAdderCin_bh30 :  std_logic;
signal finalAdderOut_bh30 :  std_logic_vector(65 downto 0);
signal CompressionResult30 :  std_logic_vector(82 downto 0);
attribute rom_extract: string;
attribute rom_style: string;
attribute rom_extract of SmallMultTableP3x3r6XuYu_comb_uid33: component is "yes";
attribute rom_style of SmallMultTableP3x3r6XuYu_comb_uid33: component is "distributed";
begin
   XX_m29 <= X ;
   YY_m29 <= Y ;
   -- code generated by IntMultiplier::buildHeapLogicOnly()
   -- buildheaplogiconly called for lsbX=17 lsbY=17 msbX=24 msbY=24
   Xp_m29b31 <= XX_m29(23 downto 17) & "00";
   Yp_m29b31 <= YY_m29(23 downto 17) & "00";
   x_m29b31_0 <= Xp_m29b31(2 downto 0);
   x_m29b31_1 <= Xp_m29b31(5 downto 3);
   x_m29b31_2 <= Xp_m29b31(8 downto 6);
   y_m29b31_0 <= Yp_m29b31(2 downto 0);
   y_m29b31_1 <= Yp_m29b31(5 downto 3);
   y_m29b31_2 <= Yp_m29b31(8 downto 6);
   -- Partial product row number 0
   Y0X0_31_m29 <= y_m29b31_0 & x_m29b31_0;
   PP_m29_31X0Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X0_31_m29,
                 Y => PP31X0Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w34_0 <= PP31X0Y0_m29(4); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w35_0 <= PP31X0Y0_m29(5); -- cycle= 0 cp= 5.4816e-10

   Y0X1_31_m29 <= y_m29b31_0 & x_m29b31_1;
   PP_m29_31X1Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X1_31_m29,
                 Y => PP31X1Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w35_1 <= PP31X1Y0_m29(2); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w36_0 <= PP31X1Y0_m29(3); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w37_0 <= PP31X1Y0_m29(4); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w38_0 <= PP31X1Y0_m29(5); -- cycle= 0 cp= 5.4816e-10

   Y0X2_31_m29 <= y_m29b31_0 & x_m29b31_2;
   PP_m29_31X2Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X2_31_m29,
                 Y => PP31X2Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w38_1 <= PP31X2Y0_m29(2); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w39_0 <= PP31X2Y0_m29(3); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w40_0 <= PP31X2Y0_m29(4); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w41_0 <= PP31X2Y0_m29(5); -- cycle= 0 cp= 5.4816e-10

   -- Partial product row number 1
   Y1X0_31_m29 <= y_m29b31_1 & x_m29b31_0;
   PP_m29_31X0Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X0_31_m29,
                 Y => PP31X0Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w35_2 <= PP31X0Y1_m29(2); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w36_1 <= PP31X0Y1_m29(3); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w37_1 <= PP31X0Y1_m29(4); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w38_2 <= PP31X0Y1_m29(5); -- cycle= 0 cp= 5.4816e-10

   Y1X1_31_m29 <= y_m29b31_1 & x_m29b31_1;
   PP_m29_31X1Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X1_31_m29,
                 Y => PP31X1Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w36_2 <= PP31X1Y1_m29(0); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w37_2 <= PP31X1Y1_m29(1); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w38_3 <= PP31X1Y1_m29(2); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w39_1 <= PP31X1Y1_m29(3); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w40_1 <= PP31X1Y1_m29(4); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w41_1 <= PP31X1Y1_m29(5); -- cycle= 0 cp= 5.4816e-10

   Y1X2_31_m29 <= y_m29b31_1 & x_m29b31_2;
   PP_m29_31X2Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X2_31_m29,
                 Y => PP31X2Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w39_2 <= PP31X2Y1_m29(0); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w40_2 <= PP31X2Y1_m29(1); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w41_2 <= PP31X2Y1_m29(2); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w42_0 <= PP31X2Y1_m29(3); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w43_0 <= PP31X2Y1_m29(4); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w44_0 <= PP31X2Y1_m29(5); -- cycle= 0 cp= 5.4816e-10

   -- Partial product row number 2
   Y2X0_31_m29 <= y_m29b31_2 & x_m29b31_0;
   PP_m29_31X0Y2_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y2X0_31_m29,
                 Y => PP31X0Y2_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w38_4 <= PP31X0Y2_m29(2); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w39_3 <= PP31X0Y2_m29(3); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w40_3 <= PP31X0Y2_m29(4); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w41_3 <= PP31X0Y2_m29(5); -- cycle= 0 cp= 5.4816e-10

   Y2X1_31_m29 <= y_m29b31_2 & x_m29b31_1;
   PP_m29_31X1Y2_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y2X1_31_m29,
                 Y => PP31X1Y2_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w39_4 <= PP31X1Y2_m29(0); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w40_4 <= PP31X1Y2_m29(1); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w41_4 <= PP31X1Y2_m29(2); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w42_1 <= PP31X1Y2_m29(3); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w43_1 <= PP31X1Y2_m29(4); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w44_1 <= PP31X1Y2_m29(5); -- cycle= 0 cp= 5.4816e-10

   Y2X2_31_m29 <= y_m29b31_2 & x_m29b31_2;
   PP_m29_31X2Y2_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y2X2_31_m29,
                 Y => PP31X2Y2_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w42_2 <= PP31X2Y2_m29(0); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w43_2 <= PP31X2Y2_m29(1); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w44_2 <= PP31X2Y2_m29(2); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w45_0 <= PP31X2Y2_m29(3); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w46_0 <= PP31X2Y2_m29(4); -- cycle= 0 cp= 5.4816e-10
   heap_bh30_w47_0 <= PP31X2Y2_m29(5); -- cycle= 0 cp= 5.4816e-10

   
   -- Beginning of code generated by BitHeap::generateCompressorVHDL
   -- code generated by BitHeap::generateSupertileVHDL()
   DSP_bh30_ch0_0 <= std_logic_vector(unsigned("" & XX_m29(23 downto 0) & "") * unsigned("" & YY_m29(16 downto 0) & ""));
   heap_bh30_w40_5 <= DSP_bh30_ch0_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w39_5 <= DSP_bh30_ch0_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w38_5 <= DSP_bh30_ch0_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w37_3 <= DSP_bh30_ch0_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w36_3 <= DSP_bh30_ch0_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w35_3 <= DSP_bh30_ch0_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w34_1 <= DSP_bh30_ch0_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w33_0 <= DSP_bh30_ch0_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w32_0 <= DSP_bh30_ch0_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w31_0 <= DSP_bh30_ch0_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w30_0 <= DSP_bh30_ch0_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w29_0 <= DSP_bh30_ch0_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w28_0 <= DSP_bh30_ch0_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w27_0 <= DSP_bh30_ch0_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w26_0 <= DSP_bh30_ch0_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w25_0 <= DSP_bh30_ch0_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w24_0 <= DSP_bh30_ch0_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w23_0 <= DSP_bh30_ch0_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w22_0 <= DSP_bh30_ch0_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w21_0 <= DSP_bh30_ch0_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w20_0 <= DSP_bh30_ch0_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w19_0 <= DSP_bh30_ch0_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w18_0 <= DSP_bh30_ch0_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w17_0 <= DSP_bh30_ch0_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w16_0 <= DSP_bh30_ch0_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w15_0 <= DSP_bh30_ch0_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w14_0 <= DSP_bh30_ch0_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w13_0 <= DSP_bh30_ch0_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w12_0 <= DSP_bh30_ch0_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w11_0 <= DSP_bh30_ch0_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w10_0 <= DSP_bh30_ch0_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w9_0 <= DSP_bh30_ch0_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w8_0 <= DSP_bh30_ch0_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w7_0 <= DSP_bh30_ch0_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w6_0 <= DSP_bh30_ch0_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w5_0 <= DSP_bh30_ch0_0(5); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w4_0 <= DSP_bh30_ch0_0(4); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w3_0 <= DSP_bh30_ch0_0(3); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w2_0 <= DSP_bh30_ch0_0(2); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w1_0 <= DSP_bh30_ch0_0(1); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w0_0 <= DSP_bh30_ch0_0(0); -- cycle= 0 cp= 2.387e-09
   DSP_bh30_ch1_0 <= std_logic_vector(unsigned("" & XX_m29(40 downto 24) & "") * unsigned("" & YY_m29(23 downto 0) & ""));
   heap_bh30_w64_0 <= DSP_bh30_ch1_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w63_0 <= DSP_bh30_ch1_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w62_0 <= DSP_bh30_ch1_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w61_0 <= DSP_bh30_ch1_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w60_0 <= DSP_bh30_ch1_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w59_0 <= DSP_bh30_ch1_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w58_0 <= DSP_bh30_ch1_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w57_0 <= DSP_bh30_ch1_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w56_0 <= DSP_bh30_ch1_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w55_0 <= DSP_bh30_ch1_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w54_0 <= DSP_bh30_ch1_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w53_0 <= DSP_bh30_ch1_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w52_0 <= DSP_bh30_ch1_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w51_0 <= DSP_bh30_ch1_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w50_0 <= DSP_bh30_ch1_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w49_0 <= DSP_bh30_ch1_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w48_0 <= DSP_bh30_ch1_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w47_1 <= DSP_bh30_ch1_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w46_1 <= DSP_bh30_ch1_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w45_1 <= DSP_bh30_ch1_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w44_3 <= DSP_bh30_ch1_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w43_3 <= DSP_bh30_ch1_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w42_3 <= DSP_bh30_ch1_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w41_5 <= DSP_bh30_ch1_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w40_6 <= DSP_bh30_ch1_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w39_6 <= DSP_bh30_ch1_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w38_6 <= DSP_bh30_ch1_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w37_4 <= DSP_bh30_ch1_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w36_4 <= DSP_bh30_ch1_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w35_4 <= DSP_bh30_ch1_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w34_2 <= DSP_bh30_ch1_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w33_1 <= DSP_bh30_ch1_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w32_1 <= DSP_bh30_ch1_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w31_1 <= DSP_bh30_ch1_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w30_1 <= DSP_bh30_ch1_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w29_1 <= DSP_bh30_ch1_0(5); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w28_1 <= DSP_bh30_ch1_0(4); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w27_1 <= DSP_bh30_ch1_0(3); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w26_1 <= DSP_bh30_ch1_0(2); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w25_1 <= DSP_bh30_ch1_0(1); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w24_1 <= DSP_bh30_ch1_0(0); -- cycle= 0 cp= 2.387e-09
   DSP_bh30_ch2_0 <= std_logic_vector(unsigned("" & XX_m29(40 downto 17) & "") * unsigned("" & YY_m29(40 downto 24) & ""));
   heap_bh30_w81_0 <= DSP_bh30_ch2_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w80_0 <= DSP_bh30_ch2_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w79_0 <= DSP_bh30_ch2_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w78_0 <= DSP_bh30_ch2_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w77_0 <= DSP_bh30_ch2_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w76_0 <= DSP_bh30_ch2_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w75_0 <= DSP_bh30_ch2_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w74_0 <= DSP_bh30_ch2_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w73_0 <= DSP_bh30_ch2_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w72_0 <= DSP_bh30_ch2_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w71_0 <= DSP_bh30_ch2_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w70_0 <= DSP_bh30_ch2_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w69_0 <= DSP_bh30_ch2_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w68_0 <= DSP_bh30_ch2_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w67_0 <= DSP_bh30_ch2_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w66_0 <= DSP_bh30_ch2_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w65_0 <= DSP_bh30_ch2_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w64_1 <= DSP_bh30_ch2_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w63_1 <= DSP_bh30_ch2_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w62_1 <= DSP_bh30_ch2_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w61_1 <= DSP_bh30_ch2_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w60_1 <= DSP_bh30_ch2_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w59_1 <= DSP_bh30_ch2_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w58_1 <= DSP_bh30_ch2_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w57_1 <= DSP_bh30_ch2_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w56_1 <= DSP_bh30_ch2_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w55_1 <= DSP_bh30_ch2_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w54_1 <= DSP_bh30_ch2_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w53_1 <= DSP_bh30_ch2_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w52_1 <= DSP_bh30_ch2_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w51_1 <= DSP_bh30_ch2_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w50_1 <= DSP_bh30_ch2_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w49_1 <= DSP_bh30_ch2_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w48_1 <= DSP_bh30_ch2_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w47_2 <= DSP_bh30_ch2_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w46_2 <= DSP_bh30_ch2_0(5); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w45_2 <= DSP_bh30_ch2_0(4); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w44_4 <= DSP_bh30_ch2_0(3); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w43_4 <= DSP_bh30_ch2_0(2); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w42_4 <= DSP_bh30_ch2_0(1); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w41_6 <= DSP_bh30_ch2_0(0); -- cycle= 0 cp= 2.387e-09
   DSP_bh30_ch3_0 <= std_logic_vector(unsigned("" & XX_m29(16 downto 0) & "") * unsigned("" & YY_m29(40 downto 17) & ""));
   heap_bh30_w57_2 <= DSP_bh30_ch3_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w56_2 <= DSP_bh30_ch3_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w55_2 <= DSP_bh30_ch3_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w54_2 <= DSP_bh30_ch3_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w53_2 <= DSP_bh30_ch3_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w52_2 <= DSP_bh30_ch3_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w51_2 <= DSP_bh30_ch3_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w50_2 <= DSP_bh30_ch3_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w49_2 <= DSP_bh30_ch3_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w48_2 <= DSP_bh30_ch3_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w47_3 <= DSP_bh30_ch3_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w46_3 <= DSP_bh30_ch3_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w45_3 <= DSP_bh30_ch3_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w44_5 <= DSP_bh30_ch3_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w43_5 <= DSP_bh30_ch3_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w42_5 <= DSP_bh30_ch3_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w41_7 <= DSP_bh30_ch3_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w40_7 <= DSP_bh30_ch3_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w39_7 <= DSP_bh30_ch3_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w38_7 <= DSP_bh30_ch3_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w37_5 <= DSP_bh30_ch3_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w36_5 <= DSP_bh30_ch3_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w35_5 <= DSP_bh30_ch3_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w34_3 <= DSP_bh30_ch3_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w33_2 <= DSP_bh30_ch3_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w32_2 <= DSP_bh30_ch3_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w31_2 <= DSP_bh30_ch3_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w30_2 <= DSP_bh30_ch3_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w29_2 <= DSP_bh30_ch3_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w28_2 <= DSP_bh30_ch3_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w27_2 <= DSP_bh30_ch3_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w26_2 <= DSP_bh30_ch3_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w25_2 <= DSP_bh30_ch3_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w24_2 <= DSP_bh30_ch3_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w23_1 <= DSP_bh30_ch3_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w22_1 <= DSP_bh30_ch3_0(5); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w21_1 <= DSP_bh30_ch3_0(4); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w20_1 <= DSP_bh30_ch3_0(3); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w19_1 <= DSP_bh30_ch3_0(2); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w18_1 <= DSP_bh30_ch3_0(1); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w17_1 <= DSP_bh30_ch3_0(0); -- cycle= 0 cp= 2.387e-09

   -- Adding the constant bits
      -- All the constant bits are zero, nothing to add

   tempR_bh30_0 <= heap_bh30_w16_0 & heap_bh30_w15_0 & heap_bh30_w14_0 & heap_bh30_w13_0 & heap_bh30_w12_0 & heap_bh30_w11_0 & heap_bh30_w10_0 & heap_bh30_w9_0 & heap_bh30_w8_0 & heap_bh30_w7_0 & heap_bh30_w6_0 & heap_bh30_w5_0 & heap_bh30_w4_0 & heap_bh30_w3_0 & heap_bh30_w2_0 & heap_bh30_w1_0 & heap_bh30_w0_0; -- already compressed

   CompressorIn_bh30_0_0 <= heap_bh30_w38_4 & heap_bh30_w38_3 & heap_bh30_w38_2 & heap_bh30_w38_1;
   CompressorIn_bh30_0_1(0) <= heap_bh30_w39_4;
      Compressor_bh30_0: Compressor_14_3
      port map ( R => CompressorOut_bh30_0_0,
                 X0 => CompressorIn_bh30_0_0,
                 X1 => CompressorIn_bh30_0_1);
   heap_bh30_w38_8 <= CompressorOut_bh30_0_0(0); -- cycle= 0 cp= 1.07888e-09
   heap_bh30_w39_8 <= CompressorOut_bh30_0_0(1); -- cycle= 0 cp= 1.07888e-09
   heap_bh30_w40_8 <= CompressorOut_bh30_0_0(2); -- cycle= 0 cp= 1.07888e-09

   CompressorIn_bh30_1_2 <= heap_bh30_w39_3 & heap_bh30_w39_2 & heap_bh30_w39_1 & heap_bh30_w39_0;
   CompressorIn_bh30_1_3(0) <= heap_bh30_w40_4;
      Compressor_bh30_1: Compressor_14_3
      port map ( R => CompressorOut_bh30_1_1,
                 X0 => CompressorIn_bh30_1_2,
                 X1 => CompressorIn_bh30_1_3);
   heap_bh30_w39_9 <= CompressorOut_bh30_1_1(0); -- cycle= 0 cp= 1.07888e-09
   heap_bh30_w40_9 <= CompressorOut_bh30_1_1(1); -- cycle= 0 cp= 1.07888e-09
   heap_bh30_w41_8 <= CompressorOut_bh30_1_1(2); -- cycle= 0 cp= 1.07888e-09

   CompressorIn_bh30_2_4 <= heap_bh30_w40_3 & heap_bh30_w40_2 & heap_bh30_w40_1 & heap_bh30_w40_0;
   CompressorIn_bh30_2_5(0) <= heap_bh30_w41_4;
      Compressor_bh30_2: Compressor_14_3
      port map ( R => CompressorOut_bh30_2_2,
                 X0 => CompressorIn_bh30_2_4,
                 X1 => CompressorIn_bh30_2_5);
   heap_bh30_w40_10 <= CompressorOut_bh30_2_2(0); -- cycle= 0 cp= 1.07888e-09
   heap_bh30_w41_9 <= CompressorOut_bh30_2_2(1); -- cycle= 0 cp= 1.07888e-09
   heap_bh30_w42_6 <= CompressorOut_bh30_2_2(2); -- cycle= 0 cp= 1.07888e-09

   CompressorIn_bh30_3_6 <= heap_bh30_w41_3 & heap_bh30_w41_2 & heap_bh30_w41_1 & heap_bh30_w41_0;
   CompressorIn_bh30_3_7(0) <= heap_bh30_w42_2;
      Compressor_bh30_3: Compressor_14_3
      port map ( R => CompressorOut_bh30_3_3,
                 X0 => CompressorIn_bh30_3_6,
                 X1 => CompressorIn_bh30_3_7);
   heap_bh30_w41_10 <= CompressorOut_bh30_3_3(0); -- cycle= 0 cp= 1.07888e-09
   heap_bh30_w42_7 <= CompressorOut_bh30_3_3(1); -- cycle= 0 cp= 1.07888e-09
   heap_bh30_w43_6 <= CompressorOut_bh30_3_3(2); -- cycle= 0 cp= 1.07888e-09

   CompressorIn_bh30_4_8 <= heap_bh30_w35_2 & heap_bh30_w35_1 & heap_bh30_w35_0;
   CompressorIn_bh30_4_9 <= heap_bh30_w36_2 & heap_bh30_w36_1;
      Compressor_bh30_4: Compressor_23_3
      port map ( R => CompressorOut_bh30_4_4,
                 X0 => CompressorIn_bh30_4_8,
                 X1 => CompressorIn_bh30_4_9);
   heap_bh30_w35_6 <= CompressorOut_bh30_4_4(0); -- cycle= 0 cp= 1.07888e-09
   heap_bh30_w36_6 <= CompressorOut_bh30_4_4(1); -- cycle= 0 cp= 1.07888e-09
   heap_bh30_w37_6 <= CompressorOut_bh30_4_4(2); -- cycle= 0 cp= 1.07888e-09

   CompressorIn_bh30_5_10 <= heap_bh30_w43_2 & heap_bh30_w43_1 & heap_bh30_w43_0;
   CompressorIn_bh30_5_11 <= heap_bh30_w44_2 & heap_bh30_w44_1;
      Compressor_bh30_5: Compressor_23_3
      port map ( R => CompressorOut_bh30_5_5,
                 X0 => CompressorIn_bh30_5_10,
                 X1 => CompressorIn_bh30_5_11);
   heap_bh30_w43_7 <= CompressorOut_bh30_5_5(0); -- cycle= 0 cp= 1.07888e-09
   heap_bh30_w44_6 <= CompressorOut_bh30_5_5(1); -- cycle= 0 cp= 1.07888e-09
   heap_bh30_w45_4 <= CompressorOut_bh30_5_5(2); -- cycle= 0 cp= 1.07888e-09

   CompressorIn_bh30_6_12 <= heap_bh30_w37_2 & heap_bh30_w37_1 & heap_bh30_w37_0;
   CompressorIn_bh30_6_13(0) <= heap_bh30_w38_0;
      Compressor_bh30_6: Compressor_13_3
      port map ( R => CompressorOut_bh30_6_6,
                 X0 => CompressorIn_bh30_6_12,
                 X1 => CompressorIn_bh30_6_13);
   heap_bh30_w37_7 <= CompressorOut_bh30_6_6(0); -- cycle= 0 cp= 1.07888e-09
   heap_bh30_w38_9 <= CompressorOut_bh30_6_6(1); -- cycle= 0 cp= 1.07888e-09
   heap_bh30_w39_10 <= CompressorOut_bh30_6_6(2); -- cycle= 0 cp= 1.07888e-09

   CompressorIn_bh30_7_14 <= heap_bh30_w42_1 & heap_bh30_w42_0 & heap_bh30_w42_7 & heap_bh30_w42_6;
   CompressorIn_bh30_7_15(0) <= heap_bh30_w43_7;
      Compressor_bh30_7: Compressor_14_3
      port map ( R => CompressorOut_bh30_7_7,
                 X0 => CompressorIn_bh30_7_14,
                 X1 => CompressorIn_bh30_7_15);
   heap_bh30_w42_8 <= CompressorOut_bh30_7_7(0); -- cycle= 0 cp= 1.6096e-09
   heap_bh30_w43_8 <= CompressorOut_bh30_7_7(1); -- cycle= 0 cp= 1.6096e-09
   heap_bh30_w44_7 <= CompressorOut_bh30_7_7(2); -- cycle= 0 cp= 1.6096e-09

   CompressorIn_bh30_8_16 <= heap_bh30_w39_10 & heap_bh30_w39_9 & heap_bh30_w39_8;
   CompressorIn_bh30_8_17 <= heap_bh30_w40_10 & heap_bh30_w40_9;
      Compressor_bh30_8: Compressor_23_3
      port map ( R => CompressorOut_bh30_8_8,
                 X0 => CompressorIn_bh30_8_16,
                 X1 => CompressorIn_bh30_8_17);
   heap_bh30_w39_11 <= CompressorOut_bh30_8_8(0); -- cycle= 0 cp= 1.6096e-09
   heap_bh30_w40_11 <= CompressorOut_bh30_8_8(1); -- cycle= 0 cp= 1.6096e-09
   heap_bh30_w41_11 <= CompressorOut_bh30_8_8(2); -- cycle= 0 cp= 1.6096e-09

   CompressorIn_bh30_9_18 <= heap_bh30_w41_10 & heap_bh30_w41_9 & heap_bh30_w41_8;
      Compressor_bh30_9: Compressor_3_2
      port map ( R => CompressorOut_bh30_9_9,
                 X0 => CompressorIn_bh30_9_18);
   heap_bh30_w41_12 <= CompressorOut_bh30_9_9(0); -- cycle= 0 cp= 1.6096e-09
   heap_bh30_w42_9 <= CompressorOut_bh30_9_9(1); -- cycle= 0 cp= 1.6096e-09

   CompressorIn_bh30_10_19 <= heap_bh30_w44_0 & heap_bh30_w44_6 & heap_bh30_w44_7;
   CompressorIn_bh30_10_20 <= heap_bh30_w45_0 & heap_bh30_w45_4;
      Compressor_bh30_10: Compressor_23_3
      port map ( R => CompressorOut_bh30_10_10,
                 X0 => CompressorIn_bh30_10_19,
                 X1 => CompressorIn_bh30_10_20);
   heap_bh30_w44_8 <= CompressorOut_bh30_10_10(0); -- cycle= 0 cp= 2.14032e-09
   heap_bh30_w45_5 <= CompressorOut_bh30_10_10(1); -- cycle= 0 cp= 2.14032e-09
   heap_bh30_w46_4 <= CompressorOut_bh30_10_10(2); -- cycle= 0 cp= 2.14032e-09

   CompressorIn_bh30_11_21 <= heap_bh30_w34_0 & heap_bh30_w34_3 & heap_bh30_w34_2 & heap_bh30_w34_1;
   CompressorIn_bh30_11_22(0) <= heap_bh30_w35_6;
      Compressor_bh30_11: Compressor_14_3
      port map ( R => CompressorOut_bh30_11_11,
                 X0 => CompressorIn_bh30_11_21,
                 X1 => CompressorIn_bh30_11_22);
   heap_bh30_w34_4 <= CompressorOut_bh30_11_11(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w35_7 <= CompressorOut_bh30_11_11(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w36_7 <= CompressorOut_bh30_11_11(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_12_23 <= heap_bh30_w36_0 & heap_bh30_w36_6 & heap_bh30_w36_5 & heap_bh30_w36_4;
   CompressorIn_bh30_12_24(0) <= heap_bh30_w37_7;
      Compressor_bh30_12: Compressor_14_3
      port map ( R => CompressorOut_bh30_12_12,
                 X0 => CompressorIn_bh30_12_23,
                 X1 => CompressorIn_bh30_12_24);
   heap_bh30_w36_8 <= CompressorOut_bh30_12_12(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w37_8 <= CompressorOut_bh30_12_12(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w38_10 <= CompressorOut_bh30_12_12(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_13_25 <= heap_bh30_w37_6 & heap_bh30_w37_5 & heap_bh30_w37_4 & heap_bh30_w37_3;
   CompressorIn_bh30_13_26(0) <= heap_bh30_w38_9;
      Compressor_bh30_13: Compressor_14_3
      port map ( R => CompressorOut_bh30_13_13,
                 X0 => CompressorIn_bh30_13_25,
                 X1 => CompressorIn_bh30_13_26);
   heap_bh30_w37_9 <= CompressorOut_bh30_13_13(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w38_11 <= CompressorOut_bh30_13_13(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w39_12 <= CompressorOut_bh30_13_13(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_14_27 <= heap_bh30_w38_8 & heap_bh30_w38_7 & heap_bh30_w38_6 & heap_bh30_w38_5;
   CompressorIn_bh30_14_28(0) <= heap_bh30_w39_11;
      Compressor_bh30_14: Compressor_14_3
      port map ( R => CompressorOut_bh30_14_14,
                 X0 => CompressorIn_bh30_14_27,
                 X1 => CompressorIn_bh30_14_28);
   heap_bh30_w38_12 <= CompressorOut_bh30_14_14(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w39_13 <= CompressorOut_bh30_14_14(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w40_12 <= CompressorOut_bh30_14_14(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_15_29 <= heap_bh30_w40_8 & heap_bh30_w40_11 & heap_bh30_w40_7 & heap_bh30_w40_6;
   CompressorIn_bh30_15_30(0) <= heap_bh30_w41_12;
      Compressor_bh30_15: Compressor_14_3
      port map ( R => CompressorOut_bh30_15_15,
                 X0 => CompressorIn_bh30_15_29,
                 X1 => CompressorIn_bh30_15_30);
   heap_bh30_w40_13 <= CompressorOut_bh30_15_15(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w41_13 <= CompressorOut_bh30_15_15(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w42_10 <= CompressorOut_bh30_15_15(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_16_31 <= heap_bh30_w41_11 & heap_bh30_w41_7 & heap_bh30_w41_6 & heap_bh30_w41_5;
   CompressorIn_bh30_16_32(0) <= heap_bh30_w42_9;
      Compressor_bh30_16: Compressor_14_3
      port map ( R => CompressorOut_bh30_16_16,
                 X0 => CompressorIn_bh30_16_31,
                 X1 => CompressorIn_bh30_16_32);
   heap_bh30_w41_14 <= CompressorOut_bh30_16_16(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w42_11 <= CompressorOut_bh30_16_16(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w43_9 <= CompressorOut_bh30_16_16(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_17_33 <= heap_bh30_w42_8 & heap_bh30_w42_5 & heap_bh30_w42_4 & heap_bh30_w42_3;
   CompressorIn_bh30_17_34(0) <= heap_bh30_w43_6;
      Compressor_bh30_17: Compressor_14_3
      port map ( R => CompressorOut_bh30_17_17,
                 X0 => CompressorIn_bh30_17_33,
                 X1 => CompressorIn_bh30_17_34);
   heap_bh30_w42_12 <= CompressorOut_bh30_17_17(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w43_10 <= CompressorOut_bh30_17_17(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w44_9 <= CompressorOut_bh30_17_17(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_18_35 <= heap_bh30_w43_8 & heap_bh30_w43_5 & heap_bh30_w43_4 & heap_bh30_w43_3;
   CompressorIn_bh30_18_36(0) <= heap_bh30_w44_8;
      Compressor_bh30_18: Compressor_14_3
      port map ( R => CompressorOut_bh30_18_18,
                 X0 => CompressorIn_bh30_18_35,
                 X1 => CompressorIn_bh30_18_36);
   heap_bh30_w43_11 <= CompressorOut_bh30_18_18(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w44_10 <= CompressorOut_bh30_18_18(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w45_6 <= CompressorOut_bh30_18_18(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_19_37 <= heap_bh30_w45_5 & heap_bh30_w45_3 & heap_bh30_w45_2 & heap_bh30_w45_1;
   CompressorIn_bh30_19_38(0) <= heap_bh30_w46_0;
      Compressor_bh30_19: Compressor_14_3
      port map ( R => CompressorOut_bh30_19_19,
                 X0 => CompressorIn_bh30_19_37,
                 X1 => CompressorIn_bh30_19_38);
   heap_bh30_w45_7 <= CompressorOut_bh30_19_19(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w46_5 <= CompressorOut_bh30_19_19(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w47_4 <= CompressorOut_bh30_19_19(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_20_39 <= heap_bh30_w46_4 & heap_bh30_w46_3 & heap_bh30_w46_2 & heap_bh30_w46_1;
   CompressorIn_bh30_20_40(0) <= heap_bh30_w47_0;
      Compressor_bh30_20: Compressor_14_3
      port map ( R => CompressorOut_bh30_20_20,
                 X0 => CompressorIn_bh30_20_39,
                 X1 => CompressorIn_bh30_20_40);
   heap_bh30_w46_6 <= CompressorOut_bh30_20_20(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w47_5 <= CompressorOut_bh30_20_20(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w48_3 <= CompressorOut_bh30_20_20(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_21_41 <= heap_bh30_w24_2 & heap_bh30_w24_1 & heap_bh30_w24_0;
   CompressorIn_bh30_21_42 <= heap_bh30_w25_2 & heap_bh30_w25_1;
      Compressor_bh30_21: Compressor_23_3
      port map ( R => CompressorOut_bh30_21_21,
                 X0 => CompressorIn_bh30_21_41,
                 X1 => CompressorIn_bh30_21_42);
   heap_bh30_w24_3 <= CompressorOut_bh30_21_21(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w25_3 <= CompressorOut_bh30_21_21(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w26_3 <= CompressorOut_bh30_21_21(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_22_43 <= heap_bh30_w26_2 & heap_bh30_w26_1 & heap_bh30_w26_0;
   CompressorIn_bh30_22_44 <= heap_bh30_w27_2 & heap_bh30_w27_1;
      Compressor_bh30_22: Compressor_23_3
      port map ( R => CompressorOut_bh30_22_22,
                 X0 => CompressorIn_bh30_22_43,
                 X1 => CompressorIn_bh30_22_44);
   heap_bh30_w26_4 <= CompressorOut_bh30_22_22(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w27_3 <= CompressorOut_bh30_22_22(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w28_3 <= CompressorOut_bh30_22_22(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_23_45 <= heap_bh30_w28_2 & heap_bh30_w28_1 & heap_bh30_w28_0;
   CompressorIn_bh30_23_46 <= heap_bh30_w29_2 & heap_bh30_w29_1;
      Compressor_bh30_23: Compressor_23_3
      port map ( R => CompressorOut_bh30_23_23,
                 X0 => CompressorIn_bh30_23_45,
                 X1 => CompressorIn_bh30_23_46);
   heap_bh30_w28_4 <= CompressorOut_bh30_23_23(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w29_3 <= CompressorOut_bh30_23_23(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w30_3 <= CompressorOut_bh30_23_23(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_24_47 <= heap_bh30_w30_2 & heap_bh30_w30_1 & heap_bh30_w30_0;
   CompressorIn_bh30_24_48 <= heap_bh30_w31_2 & heap_bh30_w31_1;
      Compressor_bh30_24: Compressor_23_3
      port map ( R => CompressorOut_bh30_24_24,
                 X0 => CompressorIn_bh30_24_47,
                 X1 => CompressorIn_bh30_24_48);
   heap_bh30_w30_4 <= CompressorOut_bh30_24_24(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w31_3 <= CompressorOut_bh30_24_24(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w32_3 <= CompressorOut_bh30_24_24(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_25_49 <= heap_bh30_w32_2 & heap_bh30_w32_1 & heap_bh30_w32_0;
   CompressorIn_bh30_25_50 <= heap_bh30_w33_2 & heap_bh30_w33_1;
      Compressor_bh30_25: Compressor_23_3
      port map ( R => CompressorOut_bh30_25_25,
                 X0 => CompressorIn_bh30_25_49,
                 X1 => CompressorIn_bh30_25_50);
   heap_bh30_w32_4 <= CompressorOut_bh30_25_25(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w33_3 <= CompressorOut_bh30_25_25(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w34_5 <= CompressorOut_bh30_25_25(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_26_51 <= heap_bh30_w47_3 & heap_bh30_w47_2 & heap_bh30_w47_1;
   CompressorIn_bh30_26_52 <= heap_bh30_w48_2 & heap_bh30_w48_1;
      Compressor_bh30_26: Compressor_23_3
      port map ( R => CompressorOut_bh30_26_26,
                 X0 => CompressorIn_bh30_26_51,
                 X1 => CompressorIn_bh30_26_52);
   heap_bh30_w47_6 <= CompressorOut_bh30_26_26(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w48_4 <= CompressorOut_bh30_26_26(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w49_3 <= CompressorOut_bh30_26_26(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_27_53 <= heap_bh30_w49_2 & heap_bh30_w49_1 & heap_bh30_w49_0;
   CompressorIn_bh30_27_54 <= heap_bh30_w50_2 & heap_bh30_w50_1;
      Compressor_bh30_27: Compressor_23_3
      port map ( R => CompressorOut_bh30_27_27,
                 X0 => CompressorIn_bh30_27_53,
                 X1 => CompressorIn_bh30_27_54);
   heap_bh30_w49_4 <= CompressorOut_bh30_27_27(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w50_3 <= CompressorOut_bh30_27_27(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w51_3 <= CompressorOut_bh30_27_27(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_28_55 <= heap_bh30_w51_2 & heap_bh30_w51_1 & heap_bh30_w51_0;
   CompressorIn_bh30_28_56 <= heap_bh30_w52_2 & heap_bh30_w52_1;
      Compressor_bh30_28: Compressor_23_3
      port map ( R => CompressorOut_bh30_28_28,
                 X0 => CompressorIn_bh30_28_55,
                 X1 => CompressorIn_bh30_28_56);
   heap_bh30_w51_4 <= CompressorOut_bh30_28_28(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w52_3 <= CompressorOut_bh30_28_28(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w53_3 <= CompressorOut_bh30_28_28(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_29_57 <= heap_bh30_w53_2 & heap_bh30_w53_1 & heap_bh30_w53_0;
   CompressorIn_bh30_29_58 <= heap_bh30_w54_2 & heap_bh30_w54_1;
      Compressor_bh30_29: Compressor_23_3
      port map ( R => CompressorOut_bh30_29_29,
                 X0 => CompressorIn_bh30_29_57,
                 X1 => CompressorIn_bh30_29_58);
   heap_bh30_w53_4 <= CompressorOut_bh30_29_29(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w54_3 <= CompressorOut_bh30_29_29(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w55_3 <= CompressorOut_bh30_29_29(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_30_59 <= heap_bh30_w55_2 & heap_bh30_w55_1 & heap_bh30_w55_0;
   CompressorIn_bh30_30_60 <= heap_bh30_w56_2 & heap_bh30_w56_1;
      Compressor_bh30_30: Compressor_23_3
      port map ( R => CompressorOut_bh30_30_30,
                 X0 => CompressorIn_bh30_30_59,
                 X1 => CompressorIn_bh30_30_60);
   heap_bh30_w55_4 <= CompressorOut_bh30_30_30(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w56_3 <= CompressorOut_bh30_30_30(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w57_3 <= CompressorOut_bh30_30_30(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_31_61 <= heap_bh30_w57_2 & heap_bh30_w57_1 & heap_bh30_w57_0;
   CompressorIn_bh30_31_62 <= heap_bh30_w58_1 & heap_bh30_w58_0;
      Compressor_bh30_31: Compressor_23_3
      port map ( R => CompressorOut_bh30_31_31,
                 X0 => CompressorIn_bh30_31_61,
                 X1 => CompressorIn_bh30_31_62);
   heap_bh30_w57_4 <= CompressorOut_bh30_31_31(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w58_2 <= CompressorOut_bh30_31_31(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w59_2 <= CompressorOut_bh30_31_31(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_32_63 <= heap_bh30_w35_5 & heap_bh30_w35_4 & heap_bh30_w35_3;
   CompressorIn_bh30_32_64(0) <= heap_bh30_w36_3;
      Compressor_bh30_32: Compressor_13_3
      port map ( R => CompressorOut_bh30_32_32,
                 X0 => CompressorIn_bh30_32_63,
                 X1 => CompressorIn_bh30_32_64);
   heap_bh30_w35_8 <= CompressorOut_bh30_32_32(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w36_9 <= CompressorOut_bh30_32_32(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w37_10 <= CompressorOut_bh30_32_32(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_33_65 <= heap_bh30_w39_7 & heap_bh30_w39_6 & heap_bh30_w39_5;
   CompressorIn_bh30_33_66(0) <= heap_bh30_w40_5;
      Compressor_bh30_33: Compressor_13_3
      port map ( R => CompressorOut_bh30_33_33,
                 X0 => CompressorIn_bh30_33_65,
                 X1 => CompressorIn_bh30_33_66);
   heap_bh30_w39_14 <= CompressorOut_bh30_33_33(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w40_14 <= CompressorOut_bh30_33_33(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w41_15 <= CompressorOut_bh30_33_33(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_34_67 <= heap_bh30_w44_5 & heap_bh30_w44_4 & heap_bh30_w44_3;
      Compressor_bh30_34: Compressor_3_2
      port map ( R => CompressorOut_bh30_34_34,
                 X0 => CompressorIn_bh30_34_67);
   heap_bh30_w44_11 <= CompressorOut_bh30_34_34(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w45_8 <= CompressorOut_bh30_34_34(1); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_35_68 <= heap_bh30_w36_9 & heap_bh30_w36_8 & heap_bh30_w36_7;
   CompressorIn_bh30_35_69 <= heap_bh30_w37_10 & heap_bh30_w37_9;
      Compressor_bh30_35: Compressor_23_3
      port map ( R => CompressorOut_bh30_35_35,
                 X0 => CompressorIn_bh30_35_68,
                 X1 => CompressorIn_bh30_35_69);
   heap_bh30_w36_10 <= CompressorOut_bh30_35_35(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w37_11 <= CompressorOut_bh30_35_35(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w38_13 <= CompressorOut_bh30_35_35(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_36_70 <= heap_bh30_w38_12 & heap_bh30_w38_11 & heap_bh30_w38_10;
   CompressorIn_bh30_36_71 <= heap_bh30_w39_14 & heap_bh30_w39_13;
      Compressor_bh30_36: Compressor_23_3
      port map ( R => CompressorOut_bh30_36_36,
                 X0 => CompressorIn_bh30_36_70,
                 X1 => CompressorIn_bh30_36_71);
   heap_bh30_w38_14 <= CompressorOut_bh30_36_36(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w39_15 <= CompressorOut_bh30_36_36(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w40_15 <= CompressorOut_bh30_36_36(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_37_72 <= heap_bh30_w40_14 & heap_bh30_w40_13 & heap_bh30_w40_12;
   CompressorIn_bh30_37_73 <= heap_bh30_w41_15 & heap_bh30_w41_14;
      Compressor_bh30_37: Compressor_23_3
      port map ( R => CompressorOut_bh30_37_37,
                 X0 => CompressorIn_bh30_37_72,
                 X1 => CompressorIn_bh30_37_73);
   heap_bh30_w40_16 <= CompressorOut_bh30_37_37(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w41_16 <= CompressorOut_bh30_37_37(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w42_13 <= CompressorOut_bh30_37_37(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_38_74 <= heap_bh30_w42_12 & heap_bh30_w42_11 & heap_bh30_w42_10;
   CompressorIn_bh30_38_75 <= heap_bh30_w43_11 & heap_bh30_w43_10;
      Compressor_bh30_38: Compressor_23_3
      port map ( R => CompressorOut_bh30_38_38,
                 X0 => CompressorIn_bh30_38_74,
                 X1 => CompressorIn_bh30_38_75);
   heap_bh30_w42_14 <= CompressorOut_bh30_38_38(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w43_12 <= CompressorOut_bh30_38_38(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w44_12 <= CompressorOut_bh30_38_38(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_39_76 <= heap_bh30_w44_11 & heap_bh30_w44_10 & heap_bh30_w44_9;
   CompressorIn_bh30_39_77 <= heap_bh30_w45_8 & heap_bh30_w45_7;
      Compressor_bh30_39: Compressor_23_3
      port map ( R => CompressorOut_bh30_39_39,
                 X0 => CompressorIn_bh30_39_76,
                 X1 => CompressorIn_bh30_39_77);
   heap_bh30_w44_13 <= CompressorOut_bh30_39_39(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w45_9 <= CompressorOut_bh30_39_39(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w46_7 <= CompressorOut_bh30_39_39(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_40_78 <= heap_bh30_w47_6 & heap_bh30_w47_5 & heap_bh30_w47_4;
   CompressorIn_bh30_40_79 <= heap_bh30_w48_0 & heap_bh30_w48_4;
      Compressor_bh30_40: Compressor_23_3
      port map ( R => CompressorOut_bh30_40_40,
                 X0 => CompressorIn_bh30_40_78,
                 X1 => CompressorIn_bh30_40_79);
   heap_bh30_w47_7 <= CompressorOut_bh30_40_40(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w48_5 <= CompressorOut_bh30_40_40(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w49_5 <= CompressorOut_bh30_40_40(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_41_80 <= heap_bh30_w59_1 & heap_bh30_w59_0 & heap_bh30_w59_2;
   CompressorIn_bh30_41_81 <= heap_bh30_w60_1 & heap_bh30_w60_0;
      Compressor_bh30_41: Compressor_23_3
      port map ( R => CompressorOut_bh30_41_41,
                 X0 => CompressorIn_bh30_41_80,
                 X1 => CompressorIn_bh30_41_81);
   heap_bh30_w59_3 <= CompressorOut_bh30_41_41(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w60_2 <= CompressorOut_bh30_41_41(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w61_2 <= CompressorOut_bh30_41_41(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_42_82 <= heap_bh30_w49_4 & heap_bh30_w49_3 & heap_bh30_w49_5;
   CompressorIn_bh30_42_83 <= heap_bh30_w50_0 & heap_bh30_w50_3;
      Compressor_bh30_42: Compressor_23_3
      port map ( R => CompressorOut_bh30_42_42,
                 X0 => CompressorIn_bh30_42_82,
                 X1 => CompressorIn_bh30_42_83);
   heap_bh30_w49_6 <= CompressorOut_bh30_42_42(0); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w50_4 <= CompressorOut_bh30_42_42(1); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w51_5 <= CompressorOut_bh30_42_42(2); -- cycle= 0 cp= 3.97916e-09

   CompressorIn_bh30_43_84 <= heap_bh30_w61_1 & heap_bh30_w61_0 & heap_bh30_w61_2;
   CompressorIn_bh30_43_85 <= heap_bh30_w62_1 & heap_bh30_w62_0;
      Compressor_bh30_43: Compressor_23_3
      port map ( R => CompressorOut_bh30_43_43,
                 X0 => CompressorIn_bh30_43_84,
                 X1 => CompressorIn_bh30_43_85);
   heap_bh30_w61_3 <= CompressorOut_bh30_43_43(0); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w62_2 <= CompressorOut_bh30_43_43(1); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w63_2 <= CompressorOut_bh30_43_43(2); -- cycle= 0 cp= 3.97916e-09

   CompressorIn_bh30_44_86 <= heap_bh30_w46_6 & heap_bh30_w46_5 & heap_bh30_w46_7;
   CompressorIn_bh30_44_87(0) <= heap_bh30_w47_7;
      Compressor_bh30_44: Compressor_13_3
      port map ( R => CompressorOut_bh30_44_44,
                 X0 => CompressorIn_bh30_44_86,
                 X1 => CompressorIn_bh30_44_87);
   heap_bh30_w46_8 <= CompressorOut_bh30_44_44(0); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w47_8 <= CompressorOut_bh30_44_44(1); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w48_6 <= CompressorOut_bh30_44_44(2); -- cycle= 0 cp= 3.97916e-09

   CompressorIn_bh30_45_88 <= heap_bh30_w51_4 & heap_bh30_w51_3 & heap_bh30_w51_5;
   CompressorIn_bh30_45_89 <= heap_bh30_w52_0 & heap_bh30_w52_3;
      Compressor_bh30_45: Compressor_23_3
      port map ( R => CompressorOut_bh30_45_45,
                 X0 => CompressorIn_bh30_45_88,
                 X1 => CompressorIn_bh30_45_89);
   heap_bh30_w51_6 <= CompressorOut_bh30_45_45(0); -- cycle= 0 cp= 4.50988e-09
   heap_bh30_w52_4 <= CompressorOut_bh30_45_45(1); -- cycle= 0 cp= 4.50988e-09
   heap_bh30_w53_5 <= CompressorOut_bh30_45_45(2); -- cycle= 0 cp= 4.50988e-09

   CompressorIn_bh30_46_90 <= heap_bh30_w63_1 & heap_bh30_w63_0 & heap_bh30_w63_2;
   CompressorIn_bh30_46_91 <= heap_bh30_w64_1 & heap_bh30_w64_0;
      Compressor_bh30_46: Compressor_23_3
      port map ( R => CompressorOut_bh30_46_46,
                 X0 => CompressorIn_bh30_46_90,
                 X1 => CompressorIn_bh30_46_91);
   heap_bh30_w63_3 <= CompressorOut_bh30_46_46(0); -- cycle= 0 cp= 4.50988e-09
   heap_bh30_w64_2 <= CompressorOut_bh30_46_46(1); -- cycle= 0 cp= 4.50988e-09
   heap_bh30_w65_1 <= CompressorOut_bh30_46_46(2); -- cycle= 0 cp= 4.50988e-09

   CompressorIn_bh30_47_92 <= heap_bh30_w48_3 & heap_bh30_w48_5 & heap_bh30_w48_6;
   CompressorIn_bh30_47_93(0) <= heap_bh30_w49_6;
      Compressor_bh30_47: Compressor_13_3
      port map ( R => CompressorOut_bh30_47_47,
                 X0 => CompressorIn_bh30_47_92,
                 X1 => CompressorIn_bh30_47_93);
   heap_bh30_w48_7 <= CompressorOut_bh30_47_47(0); -- cycle= 0 cp= 4.50988e-09
   heap_bh30_w49_7 <= CompressorOut_bh30_47_47(1); -- cycle= 0 cp= 4.50988e-09
   heap_bh30_w50_5 <= CompressorOut_bh30_47_47(2); -- cycle= 0 cp= 4.50988e-09

   CompressorIn_bh30_48_94 <= heap_bh30_w53_4 & heap_bh30_w53_3 & heap_bh30_w53_5;
   CompressorIn_bh30_48_95 <= heap_bh30_w54_0 & heap_bh30_w54_3;
      Compressor_bh30_48: Compressor_23_3
      port map ( R => CompressorOut_bh30_48_48,
                 X0 => CompressorIn_bh30_48_94,
                 X1 => CompressorIn_bh30_48_95);
   heap_bh30_w53_6 <= CompressorOut_bh30_48_48(0); -- cycle= 0 cp= 5.0406e-09
   heap_bh30_w54_4 <= CompressorOut_bh30_48_48(1); -- cycle= 0 cp= 5.0406e-09
   heap_bh30_w55_5 <= CompressorOut_bh30_48_48(2); -- cycle= 0 cp= 5.0406e-09

   CompressorIn_bh30_49_96 <= heap_bh30_w55_4 & heap_bh30_w55_3 & heap_bh30_w55_5;
   CompressorIn_bh30_49_97 <= heap_bh30_w56_0 & heap_bh30_w56_3;
      Compressor_bh30_49: Compressor_23_3
      port map ( R => CompressorOut_bh30_49_49,
                 X0 => CompressorIn_bh30_49_96,
                 X1 => CompressorIn_bh30_49_97);
   heap_bh30_w55_6 <= CompressorOut_bh30_49_49(0); -- cycle= 0 cp= 5.57132e-09
   heap_bh30_w56_4 <= CompressorOut_bh30_49_49(1); -- cycle= 0 cp= 5.57132e-09
   heap_bh30_w57_5 <= CompressorOut_bh30_49_49(2); -- cycle= 0 cp= 5.57132e-09

   CompressorIn_bh30_50_98 <= heap_bh30_w57_4 & heap_bh30_w57_3 & heap_bh30_w57_5;
   CompressorIn_bh30_50_99(0) <= heap_bh30_w58_2;
      Compressor_bh30_50: Compressor_13_3
      port map ( R => CompressorOut_bh30_50_50,
                 X0 => CompressorIn_bh30_50_98,
                 X1 => CompressorIn_bh30_50_99);
   heap_bh30_w57_6 <= CompressorOut_bh30_50_50(0); -- cycle= 0 cp= 6.10204e-09
   heap_bh30_w58_3 <= CompressorOut_bh30_50_50(1); -- cycle= 0 cp= 6.10204e-09
   heap_bh30_w59_4 <= CompressorOut_bh30_50_50(2); -- cycle= 0 cp= 6.10204e-09
   finalAdderIn0_bh30 <= "0" & heap_bh30_w81_0 & heap_bh30_w80_0 & heap_bh30_w79_0 & heap_bh30_w78_0 & heap_bh30_w77_0 & heap_bh30_w76_0 & heap_bh30_w75_0 & heap_bh30_w74_0 & heap_bh30_w73_0 & heap_bh30_w72_0 & heap_bh30_w71_0 & heap_bh30_w70_0 & heap_bh30_w69_0 & heap_bh30_w68_0 & heap_bh30_w67_0 & heap_bh30_w66_0 & heap_bh30_w65_0 & heap_bh30_w64_2 & heap_bh30_w63_3 & heap_bh30_w62_2 & heap_bh30_w61_3 & heap_bh30_w60_2 & heap_bh30_w59_3 & heap_bh30_w58_3 & heap_bh30_w57_6 & heap_bh30_w56_4 & heap_bh30_w55_6 & heap_bh30_w54_4 & heap_bh30_w53_6 & heap_bh30_w52_4 & heap_bh30_w51_6 & heap_bh30_w50_4 & heap_bh30_w49_7 & heap_bh30_w48_7 & heap_bh30_w47_8 & heap_bh30_w46_8 & heap_bh30_w45_6 & heap_bh30_w44_13 & heap_bh30_w43_9 & heap_bh30_w42_14 & heap_bh30_w41_13 & heap_bh30_w40_16 & heap_bh30_w39_12 & heap_bh30_w38_14 & heap_bh30_w37_8 & heap_bh30_w36_10 & heap_bh30_w35_8 & heap_bh30_w34_5 & heap_bh30_w33_0 & heap_bh30_w32_4 & heap_bh30_w31_0 & heap_bh30_w30_4 & heap_bh30_w29_0 & heap_bh30_w28_4 & heap_bh30_w27_0 & heap_bh30_w26_4 & heap_bh30_w25_0 & heap_bh30_w24_3 & heap_bh30_w23_1 & heap_bh30_w22_1 & heap_bh30_w21_1 & heap_bh30_w20_1 & heap_bh30_w19_1 & heap_bh30_w18_1 & heap_bh30_w17_1;
   finalAdderIn1_bh30 <= "0" & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & heap_bh30_w65_1 & '0' & '0' & '0' & '0' & '0' & heap_bh30_w59_4 & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & heap_bh30_w50_5 & '0' & '0' & '0' & '0' & heap_bh30_w45_9 & heap_bh30_w44_12 & heap_bh30_w43_12 & heap_bh30_w42_13 & heap_bh30_w41_16 & heap_bh30_w40_15 & heap_bh30_w39_15 & heap_bh30_w38_13 & heap_bh30_w37_11 & '0' & heap_bh30_w35_7 & heap_bh30_w34_4 & heap_bh30_w33_3 & heap_bh30_w32_3 & heap_bh30_w31_3 & heap_bh30_w30_3 & heap_bh30_w29_3 & heap_bh30_w28_3 & heap_bh30_w27_3 & heap_bh30_w26_3 & heap_bh30_w25_3 & '0' & heap_bh30_w23_0 & heap_bh30_w22_0 & heap_bh30_w21_0 & heap_bh30_w20_0 & heap_bh30_w19_0 & heap_bh30_w18_0 & heap_bh30_w17_0;
   finalAdderCin_bh30 <= '0';
      Adder_final30_0: IntAdder_66_f400_uid162
      port map ( Cin => finalAdderCin_bh30,
                 R => finalAdderOut_bh30,
                 X => finalAdderIn0_bh30,
                 Y => finalAdderIn1_bh30);
   -- concatenate all the compressed chunks
   CompressionResult30 <= finalAdderOut_bh30 & tempR_bh30_0;
   -- End of code generated by BitHeap::generateCompressorVHDL
   R <= CompressionResult30(81 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                   RightShifter_90_by_max_50_comb_uid172
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

entity RightShifter_90_by_max_50_comb_uid172 is
   port ( X : in  std_logic_vector(89 downto 0);
          S : in  std_logic_vector(5 downto 0);
          R : out  std_logic_vector(139 downto 0)   );
end entity;

architecture arch of RightShifter_90_by_max_50_comb_uid172 is
signal level0 :  std_logic_vector(89 downto 0);
signal ps :  std_logic_vector(5 downto 0);
signal level1 :  std_logic_vector(90 downto 0);
signal level2 :  std_logic_vector(92 downto 0);
signal level3 :  std_logic_vector(96 downto 0);
signal level4 :  std_logic_vector(104 downto 0);
signal level5 :  std_logic_vector(120 downto 0);
signal level6 :  std_logic_vector(152 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<=  (0 downto 0 => '0') & level0 when ps(0) = '1' else    level0 & (0 downto 0 => '0');
   level2<=  (1 downto 0 => '0') & level1 when ps(1) = '1' else    level1 & (1 downto 0 => '0');
   level3<=  (3 downto 0 => '0') & level2 when ps(2) = '1' else    level2 & (3 downto 0 => '0');
   level4<=  (7 downto 0 => '0') & level3 when ps(3) = '1' else    level3 & (7 downto 0 => '0');
   level5<=  (15 downto 0 => '0') & level4 when ps(4) = '1' else    level4 & (15 downto 0 => '0');
   level6<=  (31 downto 0 => '0') & level5 when ps(5) = '1' else    level5 & (31 downto 0 => '0');
   R <= level6(152 downto 13);
end architecture;

--------------------------------------------------------------------------------
--                          PositMult_50_7_comb_uid2
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

entity PositMult_50_7_comb_uid2 is
   port ( InputA : in  std_logic_vector(49 downto 0);
          InputB : in  std_logic_vector(49 downto 0);
          Output : out  std_logic_vector(49 downto 0)   );
end entity;

architecture arch of PositMult_50_7_comb_uid2 is
   component PositDecoder_50_7_comb_uid4 is
      port ( Input : in  std_logic_vector(49 downto 0);
             Sign : out  std_logic;
             Reg : out  std_logic_vector(6 downto 0);
             Exp : out  std_logic_vector(6 downto 0);
             Frac : out  std_logic_vector(40 downto 0);
             z : out  std_logic;
             inf : out  std_logic   );
   end component;

   component PositDecoder_50_7_comb_uid16 is
      port ( Input : in  std_logic_vector(49 downto 0);
             Sign : out  std_logic;
             Reg : out  std_logic_vector(6 downto 0);
             Exp : out  std_logic_vector(6 downto 0);
             Frac : out  std_logic_vector(40 downto 0);
             z : out  std_logic;
             inf : out  std_logic   );
   end component;

   component IntMultiplier_UsingDSP_41_41_82_unsigned_comb_uid28 is
      port ( X : in  std_logic_vector(40 downto 0);
             Y : in  std_logic_vector(40 downto 0);
             R : out  std_logic_vector(81 downto 0)   );
   end component;

   component RightShifter_90_by_max_50_comb_uid172 is
      port ( X : in  std_logic_vector(89 downto 0);
             S : in  std_logic_vector(5 downto 0);
             R : out  std_logic_vector(139 downto 0)   );
   end component;

signal sign_A :  std_logic;
signal reg_A :  std_logic_vector(6 downto 0);
signal exp_A :  std_logic_vector(6 downto 0);
signal frac_A :  std_logic_vector(40 downto 0);
signal z_A :  std_logic;
signal inf_A :  std_logic;
signal sign_B :  std_logic;
signal reg_B :  std_logic_vector(6 downto 0);
signal exp_B :  std_logic_vector(6 downto 0);
signal frac_B :  std_logic_vector(40 downto 0);
signal z_B :  std_logic;
signal inf_B :  std_logic;
signal sf_A :  std_logic_vector(13 downto 0);
signal sf_B :  std_logic_vector(13 downto 0);
signal sign :  std_logic;
signal z :  std_logic;
signal inf :  std_logic;
signal frac_mult :  std_logic_vector(81 downto 0);
signal ovf_m :  std_logic;
signal normFrac :  std_logic_vector(82 downto 0);
signal sf_mult :  std_logic_vector(14 downto 0);
signal sf_sign :  std_logic;
signal nzero :  std_logic;
signal ExpBits :  std_logic_vector(6 downto 0);
signal RegimeAns_tmp :  std_logic_vector(5 downto 0);
signal RegimeAns :  std_logic_vector(5 downto 0);
signal ovf_reg :  std_logic;
signal FinalRegime :  std_logic_vector(5 downto 0);
signal ovf_regF :  std_logic;
signal FinalExp :  std_logic_vector(6 downto 0);
signal tmp1 :  std_logic_vector(89 downto 0);
signal tmp2 :  std_logic_vector(89 downto 0);
signal shift_neg :  std_logic_vector(5 downto 0);
signal shift_pos :  std_logic_vector(5 downto 0);
signal shifter_in :  std_logic_vector(89 downto 0);
signal shifter_S :  std_logic_vector(5 downto 0);
signal shifter_out :  std_logic_vector(139 downto 0);
signal tmp_ans :  std_logic_vector(48 downto 0);
signal LSB :  std_logic;
signal G :  std_logic;
signal R :  std_logic;
signal S :  std_logic;
signal round :  std_logic;
begin
------------------------------- Data Extraction -------------------------------
   decoderA: PositDecoder_50_7_comb_uid4
      port map ( Exp => exp_A,
                 Frac => frac_A,
                 Input => InputA,
                 Reg => reg_A,
                 Sign => sign_A,
                 inf => inf_A,
                 z => z_A);
   decoderB: PositDecoder_50_7_comb_uid16
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
   mult: IntMultiplier_UsingDSP_41_41_82_unsigned_comb_uid28
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
   ExpBits <= sf_mult(6 downto 0);
   RegimeAns_tmp <= sf_mult(12 downto 7);
   -- Get Regime's absolute value
   RegimeAns <= (NOT RegimeAns_tmp)+1 when sf_sign = '1' else RegimeAns_tmp;
   -- Check for Regime overflow
   ovf_reg <= RegimeAns(RegimeAns'high);
   FinalRegime <= '0' & "11111" when ovf_reg = '1' else RegimeAns;
   ovf_regF <= '1' when FinalRegime = ('0' & "11111") else '0';
   FinalExp <= "0000000" when ((ovf_reg = '1') OR (ovf_regF = '1') OR (nzero='0')) else ExpBits;
------------------------------- Packing Stage 1 -------------------------------
   tmp1 <= nzero & '0' & FinalExp & normFrac(80 downto 0);
   tmp2 <= '0' & nzero & FinalExp & normFrac(80 downto 0);
   shift_neg <= FinalRegime - 2 when (ovf_regF = '1') else FinalRegime - 1;
   shift_pos <= FinalRegime - 1 when (ovf_regF = '1') else FinalRegime;
   shifter_in <= tmp2 when sf_sign = '1' else tmp1;
   shifter_S <= shift_neg when sf_sign = '1' else shift_pos;
   RightShifterComponent: RightShifter_90_by_max_50_comb_uid172
      port map ( R => shifter_out,
                 S => shifter_S,
                 X => shifter_in);
   tmp_ans <= shifter_out(139 downto 91);
--------------------- Packing Stage 2 - Unbiased Rounding ---------------------
   LSB <= shifter_out(91);
   G <= shifter_out(90);
   R <= shifter_out(89);
   S <= '0' when shifter_out(88 downto 0) = 0 else '1';
   round <= G AND (LSB OR R OR S) when NOT((ovf_reg OR ovf_regF) = '1') else '0';
   Output <= '1' & "0000000000000000000000000000000000000000000000000" when inf = '1' else "00000000000000000000000000000000000000000000000000" when z = '1' else '0' & (tmp_ans + round) when sign = '0' else NOT('0' & (tmp_ans + round))+1;
end architecture;

