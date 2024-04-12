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
--                             LZOC_29_comb_uid6
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

entity LZOC_29_comb_uid6 is
   port ( I : in  std_logic_vector(28 downto 0);
          OZB : in  std_logic;
          O : out  std_logic_vector(4 downto 0)   );
end entity;

architecture arch of LZOC_29_comb_uid6 is
signal sozb :  std_logic;
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
   level5<= I& (2 downto 0 => not(sozb));
   digit5<= '1' when level5(31 downto 16) = (31 downto 16 => sozb) else '0';
   level4<= level5(15 downto 0) when digit5='1' else level5(31 downto 16);
   digit4<= '1' when level4(15 downto 8) = (15 downto 8 => sozb) else '0';
   level3<= level4(7 downto 0) when digit4='1' else level4(15 downto 8);
   digit3<= '1' when level3(7 downto 4) = (7 downto 4 => sozb) else '0';
   level2<= level3(3 downto 0) when digit3='1' else level3(7 downto 4);
   digit2<= '1' when level2(3 downto 2) = (3 downto 2 => sozb) else '0';
   level1<= level2(1 downto 0) when digit2='1' else level2(3 downto 2);
   digit1<= '1' when level1(1 downto 1) = (1 downto 1 => sozb) else '0';
   O <= digit5 & digit4 & digit3 & digit2 & digit1;
end architecture;

--------------------------------------------------------------------------------
--                    LeftShifter_29_by_max_29_comb_uid10
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

entity LeftShifter_29_by_max_29_comb_uid10 is
   port ( X : in  std_logic_vector(28 downto 0);
          S : in  std_logic_vector(4 downto 0);
          R : out  std_logic_vector(57 downto 0)   );
end entity;

architecture arch of LeftShifter_29_by_max_29_comb_uid10 is
signal level0 :  std_logic_vector(28 downto 0);
signal ps :  std_logic_vector(4 downto 0);
signal level1 :  std_logic_vector(29 downto 0);
signal level2 :  std_logic_vector(31 downto 0);
signal level3 :  std_logic_vector(35 downto 0);
signal level4 :  std_logic_vector(43 downto 0);
signal level5 :  std_logic_vector(59 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<= level0 & (0 downto 0 => '0') when ps(0)= '1' else     (0 downto 0 => '0') & level0;
   level2<= level1 & (1 downto 0 => '0') when ps(1)= '1' else     (1 downto 0 => '0') & level1;
   level3<= level2 & (3 downto 0 => '0') when ps(2)= '1' else     (3 downto 0 => '0') & level2;
   level4<= level3 & (7 downto 0 => '0') when ps(3)= '1' else     (7 downto 0 => '0') & level3;
   level5<= level4 & (15 downto 0 => '0') when ps(4)= '1' else     (15 downto 0 => '0') & level4;
   R <= level5(57 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                        PositDecoder_30_6_comb_uid4
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

entity PositDecoder_30_6_comb_uid4 is
   port ( Input : in  std_logic_vector(29 downto 0);
          Sign : out  std_logic;
          Reg : out  std_logic_vector(5 downto 0);
          Exp : out  std_logic_vector(5 downto 0);
          Frac : out  std_logic_vector(21 downto 0);
          z : out  std_logic;
          inf : out  std_logic   );
end entity;

architecture arch of PositDecoder_30_6_comb_uid4 is
   component LZOC_29_comb_uid6 is
      port ( I : in  std_logic_vector(28 downto 0);
             OZB : in  std_logic;
             O : out  std_logic_vector(4 downto 0)   );
   end component;

   component LeftShifter_29_by_max_29_comb_uid10 is
      port ( X : in  std_logic_vector(28 downto 0);
             S : in  std_logic_vector(4 downto 0);
             R : out  std_logic_vector(57 downto 0)   );
   end component;

signal nzero :  std_logic;
signal my_sign :  std_logic;
signal rep_sign :  std_logic_vector(28 downto 0);
signal twos :  std_logic_vector(28 downto 0);
signal rc :  std_logic;
signal rep_rc :  std_logic_vector(28 downto 0);
signal inv :  std_logic_vector(28 downto 0);
signal zero_var :  std_logic;
signal zc :  std_logic_vector(4 downto 0);
signal zc_sub :  std_logic_vector(4 downto 0);
signal shifted_twos :  std_logic_vector(57 downto 0);
signal tmp :  std_logic_vector(26 downto 0);
begin
-------------------------------- Special Cases --------------------------------
   nzero <= '0' when Input(28 downto 0) = 0 else '1';
   -- 1 if Input is zero
   z <= Input(29) NOR nzero;
   -- 1 if Input is infinity
   inf <= Input(29) AND (NOT nzero);
------------------------------- Extract Sign bit -------------------------------
   my_sign <= Input(29);
   Sign <= my_sign;
--------------------------- 2's Complement of Input ---------------------------
   rep_sign <= (others => my_sign);
   twos <= (rep_sign XOR Input(28 downto 0)) + my_sign;
   rc <= twos(28);
------------------------ Count leading zeros of regime ------------------------
   rep_rc <= (others => rc);
   -- Invert 2's
   inv <= rep_rc XOR twos;
   zero_var <= '0';
   LZOC_Component: LZOC_29_comb_uid6
      port map ( I => inv,
                 O => zc,
                 OZB => zero_var);
----------------------------- Shift out the regime -----------------------------
   zc_sub <= zc - 1;
   LeftShifterComponent: LeftShifter_29_by_max_29_comb_uid10
      port map ( R => shifted_twos,
                 S => zc_sub,
                 X => twos);
   tmp <= shifted_twos(26 downto 0);
------------------------ Extract fraction and exponent ------------------------
   Frac <= nzero & tmp(20 downto 0);
   Exp <= tmp(26 downto 21);
-------------------------------- Select regime --------------------------------
   Reg <= '0' & zc_sub when rc = '1' else NOT('0' & zc) + 1;
end architecture;

--------------------------------------------------------------------------------
--                             LZOC_29_comb_uid18
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

entity LZOC_29_comb_uid18 is
   port ( I : in  std_logic_vector(28 downto 0);
          OZB : in  std_logic;
          O : out  std_logic_vector(4 downto 0)   );
end entity;

architecture arch of LZOC_29_comb_uid18 is
signal sozb :  std_logic;
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
   level5<= I& (2 downto 0 => not(sozb));
   digit5<= '1' when level5(31 downto 16) = (31 downto 16 => sozb) else '0';
   level4<= level5(15 downto 0) when digit5='1' else level5(31 downto 16);
   digit4<= '1' when level4(15 downto 8) = (15 downto 8 => sozb) else '0';
   level3<= level4(7 downto 0) when digit4='1' else level4(15 downto 8);
   digit3<= '1' when level3(7 downto 4) = (7 downto 4 => sozb) else '0';
   level2<= level3(3 downto 0) when digit3='1' else level3(7 downto 4);
   digit2<= '1' when level2(3 downto 2) = (3 downto 2 => sozb) else '0';
   level1<= level2(1 downto 0) when digit2='1' else level2(3 downto 2);
   digit1<= '1' when level1(1 downto 1) = (1 downto 1 => sozb) else '0';
   O <= digit5 & digit4 & digit3 & digit2 & digit1;
end architecture;

--------------------------------------------------------------------------------
--                    LeftShifter_29_by_max_29_comb_uid22
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

entity LeftShifter_29_by_max_29_comb_uid22 is
   port ( X : in  std_logic_vector(28 downto 0);
          S : in  std_logic_vector(4 downto 0);
          R : out  std_logic_vector(57 downto 0)   );
end entity;

architecture arch of LeftShifter_29_by_max_29_comb_uid22 is
signal level0 :  std_logic_vector(28 downto 0);
signal ps :  std_logic_vector(4 downto 0);
signal level1 :  std_logic_vector(29 downto 0);
signal level2 :  std_logic_vector(31 downto 0);
signal level3 :  std_logic_vector(35 downto 0);
signal level4 :  std_logic_vector(43 downto 0);
signal level5 :  std_logic_vector(59 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<= level0 & (0 downto 0 => '0') when ps(0)= '1' else     (0 downto 0 => '0') & level0;
   level2<= level1 & (1 downto 0 => '0') when ps(1)= '1' else     (1 downto 0 => '0') & level1;
   level3<= level2 & (3 downto 0 => '0') when ps(2)= '1' else     (3 downto 0 => '0') & level2;
   level4<= level3 & (7 downto 0 => '0') when ps(3)= '1' else     (7 downto 0 => '0') & level3;
   level5<= level4 & (15 downto 0 => '0') when ps(4)= '1' else     (15 downto 0 => '0') & level4;
   R <= level5(57 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                        PositDecoder_30_6_comb_uid16
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

entity PositDecoder_30_6_comb_uid16 is
   port ( Input : in  std_logic_vector(29 downto 0);
          Sign : out  std_logic;
          Reg : out  std_logic_vector(5 downto 0);
          Exp : out  std_logic_vector(5 downto 0);
          Frac : out  std_logic_vector(21 downto 0);
          z : out  std_logic;
          inf : out  std_logic   );
end entity;

architecture arch of PositDecoder_30_6_comb_uid16 is
   component LZOC_29_comb_uid18 is
      port ( I : in  std_logic_vector(28 downto 0);
             OZB : in  std_logic;
             O : out  std_logic_vector(4 downto 0)   );
   end component;

   component LeftShifter_29_by_max_29_comb_uid22 is
      port ( X : in  std_logic_vector(28 downto 0);
             S : in  std_logic_vector(4 downto 0);
             R : out  std_logic_vector(57 downto 0)   );
   end component;

signal nzero :  std_logic;
signal my_sign :  std_logic;
signal rep_sign :  std_logic_vector(28 downto 0);
signal twos :  std_logic_vector(28 downto 0);
signal rc :  std_logic;
signal rep_rc :  std_logic_vector(28 downto 0);
signal inv :  std_logic_vector(28 downto 0);
signal zero_var :  std_logic;
signal zc :  std_logic_vector(4 downto 0);
signal zc_sub :  std_logic_vector(4 downto 0);
signal shifted_twos :  std_logic_vector(57 downto 0);
signal tmp :  std_logic_vector(26 downto 0);
begin
-------------------------------- Special Cases --------------------------------
   nzero <= '0' when Input(28 downto 0) = 0 else '1';
   -- 1 if Input is zero
   z <= Input(29) NOR nzero;
   -- 1 if Input is infinity
   inf <= Input(29) AND (NOT nzero);
------------------------------- Extract Sign bit -------------------------------
   my_sign <= Input(29);
   Sign <= my_sign;
--------------------------- 2's Complement of Input ---------------------------
   rep_sign <= (others => my_sign);
   twos <= (rep_sign XOR Input(28 downto 0)) + my_sign;
   rc <= twos(28);
------------------------ Count leading zeros of regime ------------------------
   rep_rc <= (others => rc);
   -- Invert 2's
   inv <= rep_rc XOR twos;
   zero_var <= '0';
   LZOC_Component: LZOC_29_comb_uid18
      port map ( I => inv,
                 O => zc,
                 OZB => zero_var);
----------------------------- Shift out the regime -----------------------------
   zc_sub <= zc - 1;
   LeftShifterComponent: LeftShifter_29_by_max_29_comb_uid22
      port map ( R => shifted_twos,
                 S => zc_sub,
                 X => twos);
   tmp <= shifted_twos(26 downto 0);
------------------------ Extract fraction and exponent ------------------------
   Frac <= nzero & tmp(20 downto 0);
   Exp <= tmp(26 downto 21);
-------------------------------- Select regime --------------------------------
   Reg <= '0' & zc_sub when rc = '1' else NOT('0' & zc) + 1;
end architecture;

--------------------------------------------------------------------------------
--                          IntAdder_44_f400_uid156
--                    (IntAdderAlternative_44_comb_uid160)
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

entity IntAdder_44_f400_uid156 is
   port ( X : in  std_logic_vector(43 downto 0);
          Y : in  std_logic_vector(43 downto 0);
          Cin : in  std_logic;
          R : out  std_logic_vector(43 downto 0)   );
end entity;

architecture arch of IntAdder_44_f400_uid156 is
begin
   --Alternative
    R <= X + Y + Cin;
end architecture;

--------------------------------------------------------------------------------
--            IntMultiplier_UsingDSP_22_22_44_unsigned_comb_uid28
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

entity IntMultiplier_UsingDSP_22_22_44_unsigned_comb_uid28 is
   port ( X : in  std_logic_vector(21 downto 0);
          Y : in  std_logic_vector(21 downto 0);
          R : out  std_logic_vector(43 downto 0)   );
end entity;

architecture arch of IntMultiplier_UsingDSP_22_22_44_unsigned_comb_uid28 is
   component IntAdder_44_f400_uid156 is
      port ( X : in  std_logic_vector(43 downto 0);
             Y : in  std_logic_vector(43 downto 0);
             Cin : in  std_logic;
             R : out  std_logic_vector(43 downto 0)   );
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

signal XX_m29 :  std_logic_vector(21 downto 0);
signal YY_m29 :  std_logic_vector(21 downto 0);
signal Xp_m29b31 :  std_logic_vector(23 downto 0);
signal Yp_m29b31 :  std_logic_vector(5 downto 0);
signal x_m29b31_0 :  std_logic_vector(2 downto 0);
signal x_m29b31_1 :  std_logic_vector(2 downto 0);
signal x_m29b31_2 :  std_logic_vector(2 downto 0);
signal x_m29b31_3 :  std_logic_vector(2 downto 0);
signal x_m29b31_4 :  std_logic_vector(2 downto 0);
signal x_m29b31_5 :  std_logic_vector(2 downto 0);
signal x_m29b31_6 :  std_logic_vector(2 downto 0);
signal x_m29b31_7 :  std_logic_vector(2 downto 0);
signal y_m29b31_0 :  std_logic_vector(2 downto 0);
signal y_m29b31_1 :  std_logic_vector(2 downto 0);
signal Y0X0_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X0Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w0_0 :  std_logic;
signal heap_bh30_w1_0 :  std_logic;
signal heap_bh30_w2_0 :  std_logic;
signal Y0X1_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X1Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w1_1 :  std_logic;
signal heap_bh30_w2_1 :  std_logic;
signal heap_bh30_w3_0 :  std_logic;
signal heap_bh30_w4_0 :  std_logic;
signal heap_bh30_w5_0 :  std_logic;
signal Y0X2_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X2Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w4_1 :  std_logic;
signal heap_bh30_w5_1 :  std_logic;
signal heap_bh30_w6_0 :  std_logic;
signal heap_bh30_w7_0 :  std_logic;
signal heap_bh30_w8_0 :  std_logic;
signal Y0X3_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X3Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w7_1 :  std_logic;
signal heap_bh30_w8_1 :  std_logic;
signal heap_bh30_w9_0 :  std_logic;
signal heap_bh30_w10_0 :  std_logic;
signal heap_bh30_w11_0 :  std_logic;
signal Y0X4_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X4Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w10_1 :  std_logic;
signal heap_bh30_w11_1 :  std_logic;
signal heap_bh30_w12_0 :  std_logic;
signal heap_bh30_w13_0 :  std_logic;
signal heap_bh30_w14_0 :  std_logic;
signal Y0X5_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X5Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w13_1 :  std_logic;
signal heap_bh30_w14_1 :  std_logic;
signal heap_bh30_w15_0 :  std_logic;
signal heap_bh30_w16_0 :  std_logic;
signal heap_bh30_w17_0 :  std_logic;
signal Y0X6_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X6Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w16_1 :  std_logic;
signal heap_bh30_w17_1 :  std_logic;
signal heap_bh30_w18_0 :  std_logic;
signal heap_bh30_w19_0 :  std_logic;
signal heap_bh30_w20_0 :  std_logic;
signal Y0X7_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X7Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w19_1 :  std_logic;
signal heap_bh30_w20_1 :  std_logic;
signal heap_bh30_w21_0 :  std_logic;
signal heap_bh30_w22_0 :  std_logic;
signal heap_bh30_w23_0 :  std_logic;
signal Y1X0_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X0Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w2_2 :  std_logic;
signal heap_bh30_w3_1 :  std_logic;
signal heap_bh30_w4_2 :  std_logic;
signal heap_bh30_w5_2 :  std_logic;
signal Y1X1_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X1Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w3_2 :  std_logic;
signal heap_bh30_w4_3 :  std_logic;
signal heap_bh30_w5_3 :  std_logic;
signal heap_bh30_w6_1 :  std_logic;
signal heap_bh30_w7_2 :  std_logic;
signal heap_bh30_w8_2 :  std_logic;
signal Y1X2_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X2Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w6_2 :  std_logic;
signal heap_bh30_w7_3 :  std_logic;
signal heap_bh30_w8_3 :  std_logic;
signal heap_bh30_w9_1 :  std_logic;
signal heap_bh30_w10_2 :  std_logic;
signal heap_bh30_w11_2 :  std_logic;
signal Y1X3_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X3Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w9_2 :  std_logic;
signal heap_bh30_w10_3 :  std_logic;
signal heap_bh30_w11_3 :  std_logic;
signal heap_bh30_w12_1 :  std_logic;
signal heap_bh30_w13_2 :  std_logic;
signal heap_bh30_w14_2 :  std_logic;
signal Y1X4_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X4Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w12_2 :  std_logic;
signal heap_bh30_w13_3 :  std_logic;
signal heap_bh30_w14_3 :  std_logic;
signal heap_bh30_w15_1 :  std_logic;
signal heap_bh30_w16_2 :  std_logic;
signal heap_bh30_w17_2 :  std_logic;
signal Y1X5_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X5Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w15_2 :  std_logic;
signal heap_bh30_w16_3 :  std_logic;
signal heap_bh30_w17_3 :  std_logic;
signal heap_bh30_w18_1 :  std_logic;
signal heap_bh30_w19_2 :  std_logic;
signal heap_bh30_w20_2 :  std_logic;
signal Y1X6_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X6Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w18_2 :  std_logic;
signal heap_bh30_w19_3 :  std_logic;
signal heap_bh30_w20_3 :  std_logic;
signal heap_bh30_w21_1 :  std_logic;
signal heap_bh30_w22_1 :  std_logic;
signal heap_bh30_w23_1 :  std_logic;
signal Y1X7_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X7Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w21_2 :  std_logic;
signal heap_bh30_w22_2 :  std_logic;
signal heap_bh30_w23_2 :  std_logic;
signal heap_bh30_w24_0 :  std_logic;
signal heap_bh30_w25_0 :  std_logic;
signal heap_bh30_w26_0 :  std_logic;
signal DSP_bh30_ch0_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w43_0 :  std_logic;
signal heap_bh30_w42_0 :  std_logic;
signal heap_bh30_w41_0 :  std_logic;
signal heap_bh30_w40_0 :  std_logic;
signal heap_bh30_w39_0 :  std_logic;
signal heap_bh30_w38_0 :  std_logic;
signal heap_bh30_w37_0 :  std_logic;
signal heap_bh30_w36_0 :  std_logic;
signal heap_bh30_w35_0 :  std_logic;
signal heap_bh30_w34_0 :  std_logic;
signal heap_bh30_w33_0 :  std_logic;
signal heap_bh30_w32_0 :  std_logic;
signal heap_bh30_w31_0 :  std_logic;
signal heap_bh30_w30_0 :  std_logic;
signal heap_bh30_w29_0 :  std_logic;
signal heap_bh30_w28_0 :  std_logic;
signal heap_bh30_w27_0 :  std_logic;
signal heap_bh30_w26_1 :  std_logic;
signal heap_bh30_w25_1 :  std_logic;
signal heap_bh30_w24_1 :  std_logic;
signal heap_bh30_w23_3 :  std_logic;
signal heap_bh30_w22_3 :  std_logic;
signal heap_bh30_w21_3 :  std_logic;
signal heap_bh30_w20_4 :  std_logic;
signal heap_bh30_w19_4 :  std_logic;
signal heap_bh30_w18_3 :  std_logic;
signal heap_bh30_w17_4 :  std_logic;
signal heap_bh30_w16_4 :  std_logic;
signal heap_bh30_w15_3 :  std_logic;
signal heap_bh30_w14_4 :  std_logic;
signal heap_bh30_w13_4 :  std_logic;
signal heap_bh30_w12_3 :  std_logic;
signal heap_bh30_w11_4 :  std_logic;
signal heap_bh30_w10_4 :  std_logic;
signal heap_bh30_w9_3 :  std_logic;
signal heap_bh30_w8_4 :  std_logic;
signal heap_bh30_w7_4 :  std_logic;
signal heap_bh30_w6_3 :  std_logic;
signal heap_bh30_w5_4 :  std_logic;
signal heap_bh30_w4_4 :  std_logic;
signal heap_bh30_w3_3 :  std_logic;
signal tempR_bh30_0 :  std_logic;
signal CompressorIn_bh30_0_0 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_0_1 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_0_0 :  std_logic_vector(2 downto 0);
signal heap_bh30_w4_5 :  std_logic;
signal heap_bh30_w5_5 :  std_logic;
signal heap_bh30_w6_4 :  std_logic;
signal CompressorIn_bh30_1_2 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_1_3 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_1_1 :  std_logic_vector(2 downto 0);
signal heap_bh30_w7_5 :  std_logic;
signal heap_bh30_w8_5 :  std_logic;
signal heap_bh30_w9_4 :  std_logic;
signal CompressorIn_bh30_2_4 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_2_5 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_2_2 :  std_logic_vector(2 downto 0);
signal heap_bh30_w10_5 :  std_logic;
signal heap_bh30_w11_5 :  std_logic;
signal heap_bh30_w12_4 :  std_logic;
signal CompressorIn_bh30_3_6 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_3_7 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_3_3 :  std_logic_vector(2 downto 0);
signal heap_bh30_w13_5 :  std_logic;
signal heap_bh30_w14_5 :  std_logic;
signal heap_bh30_w15_4 :  std_logic;
signal CompressorIn_bh30_4_8 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_4_9 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_4_4 :  std_logic_vector(2 downto 0);
signal heap_bh30_w16_5 :  std_logic;
signal heap_bh30_w17_5 :  std_logic;
signal heap_bh30_w18_4 :  std_logic;
signal CompressorIn_bh30_5_10 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_5_11 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_5_5 :  std_logic_vector(2 downto 0);
signal heap_bh30_w19_5 :  std_logic;
signal heap_bh30_w20_5 :  std_logic;
signal heap_bh30_w21_4 :  std_logic;
signal CompressorIn_bh30_6_12 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_6_13 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_6_6 :  std_logic_vector(2 downto 0);
signal heap_bh30_w2_3 :  std_logic;
signal heap_bh30_w3_4 :  std_logic;
signal heap_bh30_w4_6 :  std_logic;
signal CompressorIn_bh30_7_14 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_7_15 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_7_7 :  std_logic_vector(2 downto 0);
signal heap_bh30_w5_6 :  std_logic;
signal heap_bh30_w6_5 :  std_logic;
signal heap_bh30_w7_6 :  std_logic;
signal CompressorIn_bh30_8_16 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_8_17 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_8_8 :  std_logic_vector(2 downto 0);
signal heap_bh30_w8_6 :  std_logic;
signal heap_bh30_w9_5 :  std_logic;
signal heap_bh30_w10_6 :  std_logic;
signal CompressorIn_bh30_9_18 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_9_19 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_9_9 :  std_logic_vector(2 downto 0);
signal heap_bh30_w11_6 :  std_logic;
signal heap_bh30_w12_5 :  std_logic;
signal heap_bh30_w13_6 :  std_logic;
signal CompressorIn_bh30_10_20 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_10_21 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_10_10 :  std_logic_vector(2 downto 0);
signal heap_bh30_w14_6 :  std_logic;
signal heap_bh30_w15_5 :  std_logic;
signal heap_bh30_w16_6 :  std_logic;
signal CompressorIn_bh30_11_22 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_11_23 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_11_11 :  std_logic_vector(2 downto 0);
signal heap_bh30_w17_6 :  std_logic;
signal heap_bh30_w18_5 :  std_logic;
signal heap_bh30_w19_6 :  std_logic;
signal CompressorIn_bh30_12_24 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_12_25 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_12_12 :  std_logic_vector(2 downto 0);
signal heap_bh30_w20_6 :  std_logic;
signal heap_bh30_w21_5 :  std_logic;
signal heap_bh30_w22_4 :  std_logic;
signal CompressorIn_bh30_13_26 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_13_27 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_13_13 :  std_logic_vector(2 downto 0);
signal heap_bh30_w22_5 :  std_logic;
signal heap_bh30_w23_4 :  std_logic;
signal heap_bh30_w24_2 :  std_logic;
signal CompressorIn_bh30_14_28 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_14_29 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_14_14 :  std_logic_vector(2 downto 0);
signal heap_bh30_w6_6 :  std_logic;
signal heap_bh30_w7_7 :  std_logic;
signal heap_bh30_w8_7 :  std_logic;
signal CompressorIn_bh30_15_30 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_15_31 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_15_15 :  std_logic_vector(2 downto 0);
signal heap_bh30_w9_6 :  std_logic;
signal heap_bh30_w10_7 :  std_logic;
signal heap_bh30_w11_7 :  std_logic;
signal CompressorIn_bh30_16_32 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_16_33 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_16_16 :  std_logic_vector(2 downto 0);
signal heap_bh30_w12_6 :  std_logic;
signal heap_bh30_w13_7 :  std_logic;
signal heap_bh30_w14_7 :  std_logic;
signal CompressorIn_bh30_17_34 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_17_35 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_17_17 :  std_logic_vector(2 downto 0);
signal heap_bh30_w15_6 :  std_logic;
signal heap_bh30_w16_7 :  std_logic;
signal heap_bh30_w17_7 :  std_logic;
signal CompressorIn_bh30_18_36 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_18_37 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_18_18 :  std_logic_vector(2 downto 0);
signal heap_bh30_w18_6 :  std_logic;
signal heap_bh30_w19_7 :  std_logic;
signal heap_bh30_w20_7 :  std_logic;
signal CompressorIn_bh30_19_38 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_19_39 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_19_19 :  std_logic_vector(2 downto 0);
signal heap_bh30_w21_6 :  std_logic;
signal heap_bh30_w22_6 :  std_logic;
signal heap_bh30_w23_5 :  std_logic;
signal CompressorIn_bh30_20_40 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_20_41 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_20_20 :  std_logic_vector(2 downto 0);
signal heap_bh30_w23_6 :  std_logic;
signal heap_bh30_w24_3 :  std_logic;
signal heap_bh30_w25_2 :  std_logic;
signal CompressorIn_bh30_21_42 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_21_43 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_21_21 :  std_logic_vector(2 downto 0);
signal heap_bh30_w8_8 :  std_logic;
signal heap_bh30_w9_7 :  std_logic;
signal heap_bh30_w10_8 :  std_logic;
signal CompressorIn_bh30_22_44 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_22_45 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_22_22 :  std_logic_vector(2 downto 0);
signal heap_bh30_w11_8 :  std_logic;
signal heap_bh30_w12_7 :  std_logic;
signal heap_bh30_w13_8 :  std_logic;
signal CompressorIn_bh30_23_46 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_23_47 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_23_23 :  std_logic_vector(2 downto 0);
signal heap_bh30_w14_8 :  std_logic;
signal heap_bh30_w15_7 :  std_logic;
signal heap_bh30_w16_8 :  std_logic;
signal CompressorIn_bh30_24_48 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_24_49 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_24_24 :  std_logic_vector(2 downto 0);
signal heap_bh30_w17_8 :  std_logic;
signal heap_bh30_w18_7 :  std_logic;
signal heap_bh30_w19_8 :  std_logic;
signal CompressorIn_bh30_25_50 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_25_51 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_25_25 :  std_logic_vector(2 downto 0);
signal heap_bh30_w20_8 :  std_logic;
signal heap_bh30_w21_7 :  std_logic;
signal heap_bh30_w22_7 :  std_logic;
signal CompressorIn_bh30_26_52 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_26_53 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_26_26 :  std_logic_vector(2 downto 0);
signal heap_bh30_w3_5 :  std_logic;
signal heap_bh30_w4_7 :  std_logic;
signal heap_bh30_w5_7 :  std_logic;
signal CompressorIn_bh30_27_54 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_27_55 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_27_27 :  std_logic_vector(2 downto 0);
signal heap_bh30_w5_8 :  std_logic;
signal heap_bh30_w6_7 :  std_logic;
signal heap_bh30_w7_8 :  std_logic;
signal CompressorIn_bh30_28_56 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_28_57 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_28_28 :  std_logic_vector(2 downto 0);
signal heap_bh30_w10_9 :  std_logic;
signal heap_bh30_w11_9 :  std_logic;
signal heap_bh30_w12_8 :  std_logic;
signal CompressorIn_bh30_29_58 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_29_59 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_29_29 :  std_logic_vector(2 downto 0);
signal heap_bh30_w13_9 :  std_logic;
signal heap_bh30_w14_9 :  std_logic;
signal heap_bh30_w15_8 :  std_logic;
signal CompressorIn_bh30_30_60 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_30_61 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_30_30 :  std_logic_vector(2 downto 0);
signal heap_bh30_w16_9 :  std_logic;
signal heap_bh30_w17_9 :  std_logic;
signal heap_bh30_w18_8 :  std_logic;
signal CompressorIn_bh30_31_62 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_31_63 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_31_31 :  std_logic_vector(2 downto 0);
signal heap_bh30_w19_9 :  std_logic;
signal heap_bh30_w20_9 :  std_logic;
signal heap_bh30_w21_8 :  std_logic;
signal CompressorIn_bh30_32_64 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_32_65 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_32_32 :  std_logic_vector(2 downto 0);
signal heap_bh30_w22_8 :  std_logic;
signal heap_bh30_w23_7 :  std_logic;
signal heap_bh30_w24_4 :  std_logic;
signal CompressorIn_bh30_33_66 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_33_67 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_33_33 :  std_logic_vector(2 downto 0);
signal heap_bh30_w25_3 :  std_logic;
signal heap_bh30_w26_2 :  std_logic;
signal heap_bh30_w27_1 :  std_logic;
signal CompressorIn_bh30_34_68 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_34_69 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_34_34 :  std_logic_vector(2 downto 0);
signal heap_bh30_w7_9 :  std_logic;
signal heap_bh30_w8_9 :  std_logic;
signal heap_bh30_w9_8 :  std_logic;
signal CompressorIn_bh30_35_70 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_35_71 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_35_35 :  std_logic_vector(2 downto 0);
signal heap_bh30_w12_9 :  std_logic;
signal heap_bh30_w13_10 :  std_logic;
signal heap_bh30_w14_10 :  std_logic;
signal CompressorIn_bh30_36_72 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_36_73 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_36_36 :  std_logic_vector(2 downto 0);
signal heap_bh30_w15_9 :  std_logic;
signal heap_bh30_w16_10 :  std_logic;
signal heap_bh30_w17_10 :  std_logic;
signal CompressorIn_bh30_37_74 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_37_75 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_37_37 :  std_logic_vector(2 downto 0);
signal heap_bh30_w18_9 :  std_logic;
signal heap_bh30_w19_10 :  std_logic;
signal heap_bh30_w20_10 :  std_logic;
signal CompressorIn_bh30_38_76 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_38_77 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_38_38 :  std_logic_vector(2 downto 0);
signal heap_bh30_w21_9 :  std_logic;
signal heap_bh30_w22_9 :  std_logic;
signal heap_bh30_w23_8 :  std_logic;
signal CompressorIn_bh30_39_78 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_39_79 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_39_39 :  std_logic_vector(2 downto 0);
signal heap_bh30_w24_5 :  std_logic;
signal heap_bh30_w25_4 :  std_logic;
signal heap_bh30_w26_3 :  std_logic;
signal CompressorIn_bh30_40_80 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_40_81 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_40_40 :  std_logic_vector(2 downto 0);
signal heap_bh30_w9_9 :  std_logic;
signal heap_bh30_w10_10 :  std_logic;
signal heap_bh30_w11_10 :  std_logic;
signal finalAdderIn0_bh30 :  std_logic_vector(43 downto 0);
signal finalAdderIn1_bh30 :  std_logic_vector(43 downto 0);
signal finalAdderCin_bh30 :  std_logic;
signal finalAdderOut_bh30 :  std_logic_vector(43 downto 0);
signal CompressionResult30 :  std_logic_vector(44 downto 0);
attribute rom_extract: string;
attribute rom_style: string;
attribute rom_extract of SmallMultTableP3x3r6XuYu_comb_uid33: component is "yes";
attribute rom_style of SmallMultTableP3x3r6XuYu_comb_uid33: component is "distributed";
begin
   XX_m29 <= X ;
   YY_m29 <= Y ;
   -- code generated by IntMultiplier::buildHeapLogicOnly()
   -- buildheaplogiconly called for lsbX=0 lsbY=0 msbX=22 msbY=5
   Xp_m29b31 <= XX_m29(21 downto 0) & "00";
   Yp_m29b31 <= YY_m29(4 downto 0) & "0";
   x_m29b31_0 <= Xp_m29b31(2 downto 0);
   x_m29b31_1 <= Xp_m29b31(5 downto 3);
   x_m29b31_2 <= Xp_m29b31(8 downto 6);
   x_m29b31_3 <= Xp_m29b31(11 downto 9);
   x_m29b31_4 <= Xp_m29b31(14 downto 12);
   x_m29b31_5 <= Xp_m29b31(17 downto 15);
   x_m29b31_6 <= Xp_m29b31(20 downto 18);
   x_m29b31_7 <= Xp_m29b31(23 downto 21);
   y_m29b31_0 <= Yp_m29b31(2 downto 0);
   y_m29b31_1 <= Yp_m29b31(5 downto 3);
   -- Partial product row number 0
   Y0X0_31_m29 <= y_m29b31_0 & x_m29b31_0;
   PP_m29_31X0Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X0_31_m29,
                 Y => PP31X0Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w0_0 <= PP31X0Y0_m29(3); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w1_0 <= PP31X0Y0_m29(4); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w2_0 <= PP31X0Y0_m29(5); -- cycle= 0 cp= 5.9176e-10

   Y0X1_31_m29 <= y_m29b31_0 & x_m29b31_1;
   PP_m29_31X1Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X1_31_m29,
                 Y => PP31X1Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w1_1 <= PP31X1Y0_m29(1); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w2_1 <= PP31X1Y0_m29(2); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w3_0 <= PP31X1Y0_m29(3); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w4_0 <= PP31X1Y0_m29(4); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w5_0 <= PP31X1Y0_m29(5); -- cycle= 0 cp= 5.9176e-10

   Y0X2_31_m29 <= y_m29b31_0 & x_m29b31_2;
   PP_m29_31X2Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X2_31_m29,
                 Y => PP31X2Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w4_1 <= PP31X2Y0_m29(1); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w5_1 <= PP31X2Y0_m29(2); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w6_0 <= PP31X2Y0_m29(3); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w7_0 <= PP31X2Y0_m29(4); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w8_0 <= PP31X2Y0_m29(5); -- cycle= 0 cp= 5.9176e-10

   Y0X3_31_m29 <= y_m29b31_0 & x_m29b31_3;
   PP_m29_31X3Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X3_31_m29,
                 Y => PP31X3Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w7_1 <= PP31X3Y0_m29(1); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w8_1 <= PP31X3Y0_m29(2); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w9_0 <= PP31X3Y0_m29(3); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w10_0 <= PP31X3Y0_m29(4); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w11_0 <= PP31X3Y0_m29(5); -- cycle= 0 cp= 5.9176e-10

   Y0X4_31_m29 <= y_m29b31_0 & x_m29b31_4;
   PP_m29_31X4Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X4_31_m29,
                 Y => PP31X4Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w10_1 <= PP31X4Y0_m29(1); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w11_1 <= PP31X4Y0_m29(2); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w12_0 <= PP31X4Y0_m29(3); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w13_0 <= PP31X4Y0_m29(4); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w14_0 <= PP31X4Y0_m29(5); -- cycle= 0 cp= 5.9176e-10

   Y0X5_31_m29 <= y_m29b31_0 & x_m29b31_5;
   PP_m29_31X5Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X5_31_m29,
                 Y => PP31X5Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w13_1 <= PP31X5Y0_m29(1); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w14_1 <= PP31X5Y0_m29(2); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w15_0 <= PP31X5Y0_m29(3); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w16_0 <= PP31X5Y0_m29(4); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w17_0 <= PP31X5Y0_m29(5); -- cycle= 0 cp= 5.9176e-10

   Y0X6_31_m29 <= y_m29b31_0 & x_m29b31_6;
   PP_m29_31X6Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X6_31_m29,
                 Y => PP31X6Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w16_1 <= PP31X6Y0_m29(1); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w17_1 <= PP31X6Y0_m29(2); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w18_0 <= PP31X6Y0_m29(3); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w19_0 <= PP31X6Y0_m29(4); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w20_0 <= PP31X6Y0_m29(5); -- cycle= 0 cp= 5.9176e-10

   Y0X7_31_m29 <= y_m29b31_0 & x_m29b31_7;
   PP_m29_31X7Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X7_31_m29,
                 Y => PP31X7Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w19_1 <= PP31X7Y0_m29(1); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w20_1 <= PP31X7Y0_m29(2); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w21_0 <= PP31X7Y0_m29(3); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w22_0 <= PP31X7Y0_m29(4); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w23_0 <= PP31X7Y0_m29(5); -- cycle= 0 cp= 5.9176e-10

   -- Partial product row number 1
   Y1X0_31_m29 <= y_m29b31_1 & x_m29b31_0;
   PP_m29_31X0Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X0_31_m29,
                 Y => PP31X0Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w2_2 <= PP31X0Y1_m29(2); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w3_1 <= PP31X0Y1_m29(3); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w4_2 <= PP31X0Y1_m29(4); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w5_2 <= PP31X0Y1_m29(5); -- cycle= 0 cp= 5.9176e-10

   Y1X1_31_m29 <= y_m29b31_1 & x_m29b31_1;
   PP_m29_31X1Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X1_31_m29,
                 Y => PP31X1Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w3_2 <= PP31X1Y1_m29(0); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w4_3 <= PP31X1Y1_m29(1); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w5_3 <= PP31X1Y1_m29(2); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w6_1 <= PP31X1Y1_m29(3); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w7_2 <= PP31X1Y1_m29(4); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w8_2 <= PP31X1Y1_m29(5); -- cycle= 0 cp= 5.9176e-10

   Y1X2_31_m29 <= y_m29b31_1 & x_m29b31_2;
   PP_m29_31X2Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X2_31_m29,
                 Y => PP31X2Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w6_2 <= PP31X2Y1_m29(0); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w7_3 <= PP31X2Y1_m29(1); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w8_3 <= PP31X2Y1_m29(2); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w9_1 <= PP31X2Y1_m29(3); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w10_2 <= PP31X2Y1_m29(4); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w11_2 <= PP31X2Y1_m29(5); -- cycle= 0 cp= 5.9176e-10

   Y1X3_31_m29 <= y_m29b31_1 & x_m29b31_3;
   PP_m29_31X3Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X3_31_m29,
                 Y => PP31X3Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w9_2 <= PP31X3Y1_m29(0); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w10_3 <= PP31X3Y1_m29(1); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w11_3 <= PP31X3Y1_m29(2); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w12_1 <= PP31X3Y1_m29(3); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w13_2 <= PP31X3Y1_m29(4); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w14_2 <= PP31X3Y1_m29(5); -- cycle= 0 cp= 5.9176e-10

   Y1X4_31_m29 <= y_m29b31_1 & x_m29b31_4;
   PP_m29_31X4Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X4_31_m29,
                 Y => PP31X4Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w12_2 <= PP31X4Y1_m29(0); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w13_3 <= PP31X4Y1_m29(1); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w14_3 <= PP31X4Y1_m29(2); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w15_1 <= PP31X4Y1_m29(3); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w16_2 <= PP31X4Y1_m29(4); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w17_2 <= PP31X4Y1_m29(5); -- cycle= 0 cp= 5.9176e-10

   Y1X5_31_m29 <= y_m29b31_1 & x_m29b31_5;
   PP_m29_31X5Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X5_31_m29,
                 Y => PP31X5Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w15_2 <= PP31X5Y1_m29(0); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w16_3 <= PP31X5Y1_m29(1); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w17_3 <= PP31X5Y1_m29(2); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w18_1 <= PP31X5Y1_m29(3); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w19_2 <= PP31X5Y1_m29(4); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w20_2 <= PP31X5Y1_m29(5); -- cycle= 0 cp= 5.9176e-10

   Y1X6_31_m29 <= y_m29b31_1 & x_m29b31_6;
   PP_m29_31X6Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X6_31_m29,
                 Y => PP31X6Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w18_2 <= PP31X6Y1_m29(0); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w19_3 <= PP31X6Y1_m29(1); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w20_3 <= PP31X6Y1_m29(2); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w21_1 <= PP31X6Y1_m29(3); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w22_1 <= PP31X6Y1_m29(4); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w23_1 <= PP31X6Y1_m29(5); -- cycle= 0 cp= 5.9176e-10

   Y1X7_31_m29 <= y_m29b31_1 & x_m29b31_7;
   PP_m29_31X7Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X7_31_m29,
                 Y => PP31X7Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w21_2 <= PP31X7Y1_m29(0); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w22_2 <= PP31X7Y1_m29(1); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w23_2 <= PP31X7Y1_m29(2); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w24_0 <= PP31X7Y1_m29(3); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w25_0 <= PP31X7Y1_m29(4); -- cycle= 0 cp= 5.9176e-10
   heap_bh30_w26_0 <= PP31X7Y1_m29(5); -- cycle= 0 cp= 5.9176e-10

   
   -- Beginning of code generated by BitHeap::generateCompressorVHDL
   -- code generated by BitHeap::generateSupertileVHDL()
   DSP_bh30_ch0_0 <= std_logic_vector(unsigned("" & XX_m29(21 downto 0) & "00") * unsigned("" & YY_m29(21 downto 5) & ""));
   heap_bh30_w43_0 <= DSP_bh30_ch0_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w42_0 <= DSP_bh30_ch0_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w41_0 <= DSP_bh30_ch0_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w40_0 <= DSP_bh30_ch0_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w39_0 <= DSP_bh30_ch0_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w38_0 <= DSP_bh30_ch0_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w37_0 <= DSP_bh30_ch0_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w36_0 <= DSP_bh30_ch0_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w35_0 <= DSP_bh30_ch0_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w34_0 <= DSP_bh30_ch0_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w33_0 <= DSP_bh30_ch0_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w32_0 <= DSP_bh30_ch0_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w31_0 <= DSP_bh30_ch0_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w30_0 <= DSP_bh30_ch0_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w29_0 <= DSP_bh30_ch0_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w28_0 <= DSP_bh30_ch0_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w27_0 <= DSP_bh30_ch0_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w26_1 <= DSP_bh30_ch0_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w25_1 <= DSP_bh30_ch0_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w24_1 <= DSP_bh30_ch0_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w23_3 <= DSP_bh30_ch0_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w22_3 <= DSP_bh30_ch0_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w21_3 <= DSP_bh30_ch0_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w20_4 <= DSP_bh30_ch0_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w19_4 <= DSP_bh30_ch0_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w18_3 <= DSP_bh30_ch0_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w17_4 <= DSP_bh30_ch0_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w16_4 <= DSP_bh30_ch0_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w15_3 <= DSP_bh30_ch0_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w14_4 <= DSP_bh30_ch0_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w13_4 <= DSP_bh30_ch0_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w12_3 <= DSP_bh30_ch0_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w11_4 <= DSP_bh30_ch0_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w10_4 <= DSP_bh30_ch0_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w9_3 <= DSP_bh30_ch0_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w8_4 <= DSP_bh30_ch0_0(5); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w7_4 <= DSP_bh30_ch0_0(4); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w6_3 <= DSP_bh30_ch0_0(3); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w5_4 <= DSP_bh30_ch0_0(2); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w4_4 <= DSP_bh30_ch0_0(1); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w3_3 <= DSP_bh30_ch0_0(0); -- cycle= 0 cp= 2.387e-09

   -- Adding the constant bits
      -- All the constant bits are zero, nothing to add

   tempR_bh30_0 <= heap_bh30_w0_0; -- already compressed

   CompressorIn_bh30_0_0 <= heap_bh30_w4_3 & heap_bh30_w4_2 & heap_bh30_w4_1 & heap_bh30_w4_0;
   CompressorIn_bh30_0_1(0) <= heap_bh30_w5_3;
      Compressor_bh30_0: Compressor_14_3
      port map ( R => CompressorOut_bh30_0_0,
                 X0 => CompressorIn_bh30_0_0,
                 X1 => CompressorIn_bh30_0_1);
   heap_bh30_w4_5 <= CompressorOut_bh30_0_0(0); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w5_5 <= CompressorOut_bh30_0_0(1); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w6_4 <= CompressorOut_bh30_0_0(2); -- cycle= 0 cp= 1.12248e-09

   CompressorIn_bh30_1_2 <= heap_bh30_w7_3 & heap_bh30_w7_2 & heap_bh30_w7_1 & heap_bh30_w7_0;
   CompressorIn_bh30_1_3(0) <= heap_bh30_w8_3;
      Compressor_bh30_1: Compressor_14_3
      port map ( R => CompressorOut_bh30_1_1,
                 X0 => CompressorIn_bh30_1_2,
                 X1 => CompressorIn_bh30_1_3);
   heap_bh30_w7_5 <= CompressorOut_bh30_1_1(0); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w8_5 <= CompressorOut_bh30_1_1(1); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w9_4 <= CompressorOut_bh30_1_1(2); -- cycle= 0 cp= 1.12248e-09

   CompressorIn_bh30_2_4 <= heap_bh30_w10_3 & heap_bh30_w10_2 & heap_bh30_w10_1 & heap_bh30_w10_0;
   CompressorIn_bh30_2_5(0) <= heap_bh30_w11_3;
      Compressor_bh30_2: Compressor_14_3
      port map ( R => CompressorOut_bh30_2_2,
                 X0 => CompressorIn_bh30_2_4,
                 X1 => CompressorIn_bh30_2_5);
   heap_bh30_w10_5 <= CompressorOut_bh30_2_2(0); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w11_5 <= CompressorOut_bh30_2_2(1); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w12_4 <= CompressorOut_bh30_2_2(2); -- cycle= 0 cp= 1.12248e-09

   CompressorIn_bh30_3_6 <= heap_bh30_w13_3 & heap_bh30_w13_2 & heap_bh30_w13_1 & heap_bh30_w13_0;
   CompressorIn_bh30_3_7(0) <= heap_bh30_w14_3;
      Compressor_bh30_3: Compressor_14_3
      port map ( R => CompressorOut_bh30_3_3,
                 X0 => CompressorIn_bh30_3_6,
                 X1 => CompressorIn_bh30_3_7);
   heap_bh30_w13_5 <= CompressorOut_bh30_3_3(0); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w14_5 <= CompressorOut_bh30_3_3(1); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w15_4 <= CompressorOut_bh30_3_3(2); -- cycle= 0 cp= 1.12248e-09

   CompressorIn_bh30_4_8 <= heap_bh30_w16_3 & heap_bh30_w16_2 & heap_bh30_w16_1 & heap_bh30_w16_0;
   CompressorIn_bh30_4_9(0) <= heap_bh30_w17_3;
      Compressor_bh30_4: Compressor_14_3
      port map ( R => CompressorOut_bh30_4_4,
                 X0 => CompressorIn_bh30_4_8,
                 X1 => CompressorIn_bh30_4_9);
   heap_bh30_w16_5 <= CompressorOut_bh30_4_4(0); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w17_5 <= CompressorOut_bh30_4_4(1); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w18_4 <= CompressorOut_bh30_4_4(2); -- cycle= 0 cp= 1.12248e-09

   CompressorIn_bh30_5_10 <= heap_bh30_w19_3 & heap_bh30_w19_2 & heap_bh30_w19_1 & heap_bh30_w19_0;
   CompressorIn_bh30_5_11(0) <= heap_bh30_w20_3;
      Compressor_bh30_5: Compressor_14_3
      port map ( R => CompressorOut_bh30_5_5,
                 X0 => CompressorIn_bh30_5_10,
                 X1 => CompressorIn_bh30_5_11);
   heap_bh30_w19_5 <= CompressorOut_bh30_5_5(0); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w20_5 <= CompressorOut_bh30_5_5(1); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w21_4 <= CompressorOut_bh30_5_5(2); -- cycle= 0 cp= 1.12248e-09

   CompressorIn_bh30_6_12 <= heap_bh30_w2_2 & heap_bh30_w2_1 & heap_bh30_w2_0;
   CompressorIn_bh30_6_13 <= heap_bh30_w3_2 & heap_bh30_w3_1;
      Compressor_bh30_6: Compressor_23_3
      port map ( R => CompressorOut_bh30_6_6,
                 X0 => CompressorIn_bh30_6_12,
                 X1 => CompressorIn_bh30_6_13);
   heap_bh30_w2_3 <= CompressorOut_bh30_6_6(0); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w3_4 <= CompressorOut_bh30_6_6(1); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w4_6 <= CompressorOut_bh30_6_6(2); -- cycle= 0 cp= 1.12248e-09

   CompressorIn_bh30_7_14 <= heap_bh30_w5_2 & heap_bh30_w5_1 & heap_bh30_w5_0;
   CompressorIn_bh30_7_15 <= heap_bh30_w6_2 & heap_bh30_w6_1;
      Compressor_bh30_7: Compressor_23_3
      port map ( R => CompressorOut_bh30_7_7,
                 X0 => CompressorIn_bh30_7_14,
                 X1 => CompressorIn_bh30_7_15);
   heap_bh30_w5_6 <= CompressorOut_bh30_7_7(0); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w6_5 <= CompressorOut_bh30_7_7(1); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w7_6 <= CompressorOut_bh30_7_7(2); -- cycle= 0 cp= 1.12248e-09

   CompressorIn_bh30_8_16 <= heap_bh30_w8_2 & heap_bh30_w8_1 & heap_bh30_w8_0;
   CompressorIn_bh30_8_17 <= heap_bh30_w9_2 & heap_bh30_w9_1;
      Compressor_bh30_8: Compressor_23_3
      port map ( R => CompressorOut_bh30_8_8,
                 X0 => CompressorIn_bh30_8_16,
                 X1 => CompressorIn_bh30_8_17);
   heap_bh30_w8_6 <= CompressorOut_bh30_8_8(0); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w9_5 <= CompressorOut_bh30_8_8(1); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w10_6 <= CompressorOut_bh30_8_8(2); -- cycle= 0 cp= 1.12248e-09

   CompressorIn_bh30_9_18 <= heap_bh30_w11_2 & heap_bh30_w11_1 & heap_bh30_w11_0;
   CompressorIn_bh30_9_19 <= heap_bh30_w12_2 & heap_bh30_w12_1;
      Compressor_bh30_9: Compressor_23_3
      port map ( R => CompressorOut_bh30_9_9,
                 X0 => CompressorIn_bh30_9_18,
                 X1 => CompressorIn_bh30_9_19);
   heap_bh30_w11_6 <= CompressorOut_bh30_9_9(0); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w12_5 <= CompressorOut_bh30_9_9(1); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w13_6 <= CompressorOut_bh30_9_9(2); -- cycle= 0 cp= 1.12248e-09

   CompressorIn_bh30_10_20 <= heap_bh30_w14_2 & heap_bh30_w14_1 & heap_bh30_w14_0;
   CompressorIn_bh30_10_21 <= heap_bh30_w15_2 & heap_bh30_w15_1;
      Compressor_bh30_10: Compressor_23_3
      port map ( R => CompressorOut_bh30_10_10,
                 X0 => CompressorIn_bh30_10_20,
                 X1 => CompressorIn_bh30_10_21);
   heap_bh30_w14_6 <= CompressorOut_bh30_10_10(0); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w15_5 <= CompressorOut_bh30_10_10(1); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w16_6 <= CompressorOut_bh30_10_10(2); -- cycle= 0 cp= 1.12248e-09

   CompressorIn_bh30_11_22 <= heap_bh30_w17_2 & heap_bh30_w17_1 & heap_bh30_w17_0;
   CompressorIn_bh30_11_23 <= heap_bh30_w18_2 & heap_bh30_w18_1;
      Compressor_bh30_11: Compressor_23_3
      port map ( R => CompressorOut_bh30_11_11,
                 X0 => CompressorIn_bh30_11_22,
                 X1 => CompressorIn_bh30_11_23);
   heap_bh30_w17_6 <= CompressorOut_bh30_11_11(0); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w18_5 <= CompressorOut_bh30_11_11(1); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w19_6 <= CompressorOut_bh30_11_11(2); -- cycle= 0 cp= 1.12248e-09

   CompressorIn_bh30_12_24 <= heap_bh30_w20_2 & heap_bh30_w20_1 & heap_bh30_w20_0;
   CompressorIn_bh30_12_25 <= heap_bh30_w21_2 & heap_bh30_w21_1;
      Compressor_bh30_12: Compressor_23_3
      port map ( R => CompressorOut_bh30_12_12,
                 X0 => CompressorIn_bh30_12_24,
                 X1 => CompressorIn_bh30_12_25);
   heap_bh30_w20_6 <= CompressorOut_bh30_12_12(0); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w21_5 <= CompressorOut_bh30_12_12(1); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w22_4 <= CompressorOut_bh30_12_12(2); -- cycle= 0 cp= 1.12248e-09

   CompressorIn_bh30_13_26 <= heap_bh30_w22_2 & heap_bh30_w22_1 & heap_bh30_w22_0;
   CompressorIn_bh30_13_27 <= heap_bh30_w23_2 & heap_bh30_w23_1;
      Compressor_bh30_13: Compressor_23_3
      port map ( R => CompressorOut_bh30_13_13,
                 X0 => CompressorIn_bh30_13_26,
                 X1 => CompressorIn_bh30_13_27);
   heap_bh30_w22_5 <= CompressorOut_bh30_13_13(0); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w23_4 <= CompressorOut_bh30_13_13(1); -- cycle= 0 cp= 1.12248e-09
   heap_bh30_w24_2 <= CompressorOut_bh30_13_13(2); -- cycle= 0 cp= 1.12248e-09

   CompressorIn_bh30_14_28 <= heap_bh30_w6_0 & heap_bh30_w6_5 & heap_bh30_w6_4;
   CompressorIn_bh30_14_29 <= heap_bh30_w7_6 & heap_bh30_w7_5;
      Compressor_bh30_14: Compressor_23_3
      port map ( R => CompressorOut_bh30_14_14,
                 X0 => CompressorIn_bh30_14_28,
                 X1 => CompressorIn_bh30_14_29);
   heap_bh30_w6_6 <= CompressorOut_bh30_14_14(0); -- cycle= 0 cp= 1.6532e-09
   heap_bh30_w7_7 <= CompressorOut_bh30_14_14(1); -- cycle= 0 cp= 1.6532e-09
   heap_bh30_w8_7 <= CompressorOut_bh30_14_14(2); -- cycle= 0 cp= 1.6532e-09

   CompressorIn_bh30_15_30 <= heap_bh30_w9_0 & heap_bh30_w9_5 & heap_bh30_w9_4;
   CompressorIn_bh30_15_31 <= heap_bh30_w10_6 & heap_bh30_w10_5;
      Compressor_bh30_15: Compressor_23_3
      port map ( R => CompressorOut_bh30_15_15,
                 X0 => CompressorIn_bh30_15_30,
                 X1 => CompressorIn_bh30_15_31);
   heap_bh30_w9_6 <= CompressorOut_bh30_15_15(0); -- cycle= 0 cp= 1.6532e-09
   heap_bh30_w10_7 <= CompressorOut_bh30_15_15(1); -- cycle= 0 cp= 1.6532e-09
   heap_bh30_w11_7 <= CompressorOut_bh30_15_15(2); -- cycle= 0 cp= 1.6532e-09

   CompressorIn_bh30_16_32 <= heap_bh30_w12_0 & heap_bh30_w12_5 & heap_bh30_w12_4;
   CompressorIn_bh30_16_33 <= heap_bh30_w13_6 & heap_bh30_w13_5;
      Compressor_bh30_16: Compressor_23_3
      port map ( R => CompressorOut_bh30_16_16,
                 X0 => CompressorIn_bh30_16_32,
                 X1 => CompressorIn_bh30_16_33);
   heap_bh30_w12_6 <= CompressorOut_bh30_16_16(0); -- cycle= 0 cp= 1.6532e-09
   heap_bh30_w13_7 <= CompressorOut_bh30_16_16(1); -- cycle= 0 cp= 1.6532e-09
   heap_bh30_w14_7 <= CompressorOut_bh30_16_16(2); -- cycle= 0 cp= 1.6532e-09

   CompressorIn_bh30_17_34 <= heap_bh30_w15_0 & heap_bh30_w15_5 & heap_bh30_w15_4;
   CompressorIn_bh30_17_35 <= heap_bh30_w16_6 & heap_bh30_w16_5;
      Compressor_bh30_17: Compressor_23_3
      port map ( R => CompressorOut_bh30_17_17,
                 X0 => CompressorIn_bh30_17_34,
                 X1 => CompressorIn_bh30_17_35);
   heap_bh30_w15_6 <= CompressorOut_bh30_17_17(0); -- cycle= 0 cp= 1.6532e-09
   heap_bh30_w16_7 <= CompressorOut_bh30_17_17(1); -- cycle= 0 cp= 1.6532e-09
   heap_bh30_w17_7 <= CompressorOut_bh30_17_17(2); -- cycle= 0 cp= 1.6532e-09

   CompressorIn_bh30_18_36 <= heap_bh30_w18_0 & heap_bh30_w18_5 & heap_bh30_w18_4;
   CompressorIn_bh30_18_37 <= heap_bh30_w19_6 & heap_bh30_w19_5;
      Compressor_bh30_18: Compressor_23_3
      port map ( R => CompressorOut_bh30_18_18,
                 X0 => CompressorIn_bh30_18_36,
                 X1 => CompressorIn_bh30_18_37);
   heap_bh30_w18_6 <= CompressorOut_bh30_18_18(0); -- cycle= 0 cp= 1.6532e-09
   heap_bh30_w19_7 <= CompressorOut_bh30_18_18(1); -- cycle= 0 cp= 1.6532e-09
   heap_bh30_w20_7 <= CompressorOut_bh30_18_18(2); -- cycle= 0 cp= 1.6532e-09

   CompressorIn_bh30_19_38 <= heap_bh30_w21_0 & heap_bh30_w21_5 & heap_bh30_w21_4;
   CompressorIn_bh30_19_39 <= heap_bh30_w22_5 & heap_bh30_w22_4;
      Compressor_bh30_19: Compressor_23_3
      port map ( R => CompressorOut_bh30_19_19,
                 X0 => CompressorIn_bh30_19_38,
                 X1 => CompressorIn_bh30_19_39);
   heap_bh30_w21_6 <= CompressorOut_bh30_19_19(0); -- cycle= 0 cp= 1.6532e-09
   heap_bh30_w22_6 <= CompressorOut_bh30_19_19(1); -- cycle= 0 cp= 1.6532e-09
   heap_bh30_w23_5 <= CompressorOut_bh30_19_19(2); -- cycle= 0 cp= 1.6532e-09

   CompressorIn_bh30_20_40 <= heap_bh30_w23_0 & heap_bh30_w23_4 & heap_bh30_w23_5;
   CompressorIn_bh30_20_41 <= heap_bh30_w24_0 & heap_bh30_w24_2;
      Compressor_bh30_20: Compressor_23_3
      port map ( R => CompressorOut_bh30_20_20,
                 X0 => CompressorIn_bh30_20_40,
                 X1 => CompressorIn_bh30_20_41);
   heap_bh30_w23_6 <= CompressorOut_bh30_20_20(0); -- cycle= 0 cp= 2.18392e-09
   heap_bh30_w24_3 <= CompressorOut_bh30_20_20(1); -- cycle= 0 cp= 2.18392e-09
   heap_bh30_w25_2 <= CompressorOut_bh30_20_20(2); -- cycle= 0 cp= 2.18392e-09

   CompressorIn_bh30_21_42 <= heap_bh30_w8_6 & heap_bh30_w8_5 & heap_bh30_w8_7;
   CompressorIn_bh30_21_43(0) <= heap_bh30_w9_6;
      Compressor_bh30_21: Compressor_13_3
      port map ( R => CompressorOut_bh30_21_21,
                 X0 => CompressorIn_bh30_21_42,
                 X1 => CompressorIn_bh30_21_43);
   heap_bh30_w8_8 <= CompressorOut_bh30_21_21(0); -- cycle= 0 cp= 2.18392e-09
   heap_bh30_w9_7 <= CompressorOut_bh30_21_21(1); -- cycle= 0 cp= 2.18392e-09
   heap_bh30_w10_8 <= CompressorOut_bh30_21_21(2); -- cycle= 0 cp= 2.18392e-09

   CompressorIn_bh30_22_44 <= heap_bh30_w11_6 & heap_bh30_w11_5 & heap_bh30_w11_7;
   CompressorIn_bh30_22_45(0) <= heap_bh30_w12_6;
      Compressor_bh30_22: Compressor_13_3
      port map ( R => CompressorOut_bh30_22_22,
                 X0 => CompressorIn_bh30_22_44,
                 X1 => CompressorIn_bh30_22_45);
   heap_bh30_w11_8 <= CompressorOut_bh30_22_22(0); -- cycle= 0 cp= 2.18392e-09
   heap_bh30_w12_7 <= CompressorOut_bh30_22_22(1); -- cycle= 0 cp= 2.18392e-09
   heap_bh30_w13_8 <= CompressorOut_bh30_22_22(2); -- cycle= 0 cp= 2.18392e-09

   CompressorIn_bh30_23_46 <= heap_bh30_w14_6 & heap_bh30_w14_5 & heap_bh30_w14_7;
   CompressorIn_bh30_23_47(0) <= heap_bh30_w15_6;
      Compressor_bh30_23: Compressor_13_3
      port map ( R => CompressorOut_bh30_23_23,
                 X0 => CompressorIn_bh30_23_46,
                 X1 => CompressorIn_bh30_23_47);
   heap_bh30_w14_8 <= CompressorOut_bh30_23_23(0); -- cycle= 0 cp= 2.18392e-09
   heap_bh30_w15_7 <= CompressorOut_bh30_23_23(1); -- cycle= 0 cp= 2.18392e-09
   heap_bh30_w16_8 <= CompressorOut_bh30_23_23(2); -- cycle= 0 cp= 2.18392e-09

   CompressorIn_bh30_24_48 <= heap_bh30_w17_6 & heap_bh30_w17_5 & heap_bh30_w17_7;
   CompressorIn_bh30_24_49(0) <= heap_bh30_w18_6;
      Compressor_bh30_24: Compressor_13_3
      port map ( R => CompressorOut_bh30_24_24,
                 X0 => CompressorIn_bh30_24_48,
                 X1 => CompressorIn_bh30_24_49);
   heap_bh30_w17_8 <= CompressorOut_bh30_24_24(0); -- cycle= 0 cp= 2.18392e-09
   heap_bh30_w18_7 <= CompressorOut_bh30_24_24(1); -- cycle= 0 cp= 2.18392e-09
   heap_bh30_w19_8 <= CompressorOut_bh30_24_24(2); -- cycle= 0 cp= 2.18392e-09

   CompressorIn_bh30_25_50 <= heap_bh30_w20_6 & heap_bh30_w20_5 & heap_bh30_w20_7;
   CompressorIn_bh30_25_51(0) <= heap_bh30_w21_6;
      Compressor_bh30_25: Compressor_13_3
      port map ( R => CompressorOut_bh30_25_25,
                 X0 => CompressorIn_bh30_25_50,
                 X1 => CompressorIn_bh30_25_51);
   heap_bh30_w20_8 <= CompressorOut_bh30_25_25(0); -- cycle= 0 cp= 2.18392e-09
   heap_bh30_w21_7 <= CompressorOut_bh30_25_25(1); -- cycle= 0 cp= 2.18392e-09
   heap_bh30_w22_7 <= CompressorOut_bh30_25_25(2); -- cycle= 0 cp= 2.18392e-09

   CompressorIn_bh30_26_52 <= heap_bh30_w3_0 & heap_bh30_w3_4 & heap_bh30_w3_3;
   CompressorIn_bh30_26_53 <= heap_bh30_w4_6 & heap_bh30_w4_5;
      Compressor_bh30_26: Compressor_23_3
      port map ( R => CompressorOut_bh30_26_26,
                 X0 => CompressorIn_bh30_26_52,
                 X1 => CompressorIn_bh30_26_53);
   heap_bh30_w3_5 <= CompressorOut_bh30_26_26(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w4_7 <= CompressorOut_bh30_26_26(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w5_7 <= CompressorOut_bh30_26_26(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_27_54 <= heap_bh30_w5_6 & heap_bh30_w5_5 & heap_bh30_w5_4;
   CompressorIn_bh30_27_55 <= heap_bh30_w6_6 & heap_bh30_w6_3;
      Compressor_bh30_27: Compressor_23_3
      port map ( R => CompressorOut_bh30_27_27,
                 X0 => CompressorIn_bh30_27_54,
                 X1 => CompressorIn_bh30_27_55);
   heap_bh30_w5_8 <= CompressorOut_bh30_27_27(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w6_7 <= CompressorOut_bh30_27_27(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w7_8 <= CompressorOut_bh30_27_27(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_28_56 <= heap_bh30_w10_7 & heap_bh30_w10_8 & heap_bh30_w10_4;
   CompressorIn_bh30_28_57 <= heap_bh30_w11_8 & heap_bh30_w11_4;
      Compressor_bh30_28: Compressor_23_3
      port map ( R => CompressorOut_bh30_28_28,
                 X0 => CompressorIn_bh30_28_56,
                 X1 => CompressorIn_bh30_28_57);
   heap_bh30_w10_9 <= CompressorOut_bh30_28_28(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w11_9 <= CompressorOut_bh30_28_28(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w12_8 <= CompressorOut_bh30_28_28(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_29_58 <= heap_bh30_w13_7 & heap_bh30_w13_8 & heap_bh30_w13_4;
   CompressorIn_bh30_29_59 <= heap_bh30_w14_8 & heap_bh30_w14_4;
      Compressor_bh30_29: Compressor_23_3
      port map ( R => CompressorOut_bh30_29_29,
                 X0 => CompressorIn_bh30_29_58,
                 X1 => CompressorIn_bh30_29_59);
   heap_bh30_w13_9 <= CompressorOut_bh30_29_29(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w14_9 <= CompressorOut_bh30_29_29(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w15_8 <= CompressorOut_bh30_29_29(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_30_60 <= heap_bh30_w16_7 & heap_bh30_w16_8 & heap_bh30_w16_4;
   CompressorIn_bh30_30_61 <= heap_bh30_w17_8 & heap_bh30_w17_4;
      Compressor_bh30_30: Compressor_23_3
      port map ( R => CompressorOut_bh30_30_30,
                 X0 => CompressorIn_bh30_30_60,
                 X1 => CompressorIn_bh30_30_61);
   heap_bh30_w16_9 <= CompressorOut_bh30_30_30(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w17_9 <= CompressorOut_bh30_30_30(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w18_8 <= CompressorOut_bh30_30_30(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_31_62 <= heap_bh30_w19_7 & heap_bh30_w19_8 & heap_bh30_w19_4;
   CompressorIn_bh30_31_63 <= heap_bh30_w20_8 & heap_bh30_w20_4;
      Compressor_bh30_31: Compressor_23_3
      port map ( R => CompressorOut_bh30_31_31,
                 X0 => CompressorIn_bh30_31_62,
                 X1 => CompressorIn_bh30_31_63);
   heap_bh30_w19_9 <= CompressorOut_bh30_31_31(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w20_9 <= CompressorOut_bh30_31_31(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w21_8 <= CompressorOut_bh30_31_31(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_32_64 <= heap_bh30_w22_6 & heap_bh30_w22_7 & heap_bh30_w22_3;
   CompressorIn_bh30_32_65 <= heap_bh30_w23_6 & heap_bh30_w23_3;
      Compressor_bh30_32: Compressor_23_3
      port map ( R => CompressorOut_bh30_32_32,
                 X0 => CompressorIn_bh30_32_64,
                 X1 => CompressorIn_bh30_32_65);
   heap_bh30_w22_8 <= CompressorOut_bh30_32_32(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w23_7 <= CompressorOut_bh30_32_32(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w24_4 <= CompressorOut_bh30_32_32(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_33_66 <= heap_bh30_w25_0 & heap_bh30_w25_2 & heap_bh30_w25_1;
   CompressorIn_bh30_33_67 <= heap_bh30_w26_0 & heap_bh30_w26_1;
      Compressor_bh30_33: Compressor_23_3
      port map ( R => CompressorOut_bh30_33_33,
                 X0 => CompressorIn_bh30_33_66,
                 X1 => CompressorIn_bh30_33_67);
   heap_bh30_w25_3 <= CompressorOut_bh30_33_33(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w26_2 <= CompressorOut_bh30_33_33(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w27_1 <= CompressorOut_bh30_33_33(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_34_68 <= heap_bh30_w7_7 & heap_bh30_w7_4 & heap_bh30_w7_8;
   CompressorIn_bh30_34_69 <= heap_bh30_w8_8 & heap_bh30_w8_4;
      Compressor_bh30_34: Compressor_23_3
      port map ( R => CompressorOut_bh30_34_34,
                 X0 => CompressorIn_bh30_34_68,
                 X1 => CompressorIn_bh30_34_69);
   heap_bh30_w7_9 <= CompressorOut_bh30_34_34(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w8_9 <= CompressorOut_bh30_34_34(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w9_8 <= CompressorOut_bh30_34_34(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_35_70 <= heap_bh30_w12_7 & heap_bh30_w12_3 & heap_bh30_w12_8;
   CompressorIn_bh30_35_71(0) <= heap_bh30_w13_9;
      Compressor_bh30_35: Compressor_13_3
      port map ( R => CompressorOut_bh30_35_35,
                 X0 => CompressorIn_bh30_35_70,
                 X1 => CompressorIn_bh30_35_71);
   heap_bh30_w12_9 <= CompressorOut_bh30_35_35(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w13_10 <= CompressorOut_bh30_35_35(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w14_10 <= CompressorOut_bh30_35_35(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_36_72 <= heap_bh30_w15_7 & heap_bh30_w15_3 & heap_bh30_w15_8;
   CompressorIn_bh30_36_73(0) <= heap_bh30_w16_9;
      Compressor_bh30_36: Compressor_13_3
      port map ( R => CompressorOut_bh30_36_36,
                 X0 => CompressorIn_bh30_36_72,
                 X1 => CompressorIn_bh30_36_73);
   heap_bh30_w15_9 <= CompressorOut_bh30_36_36(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w16_10 <= CompressorOut_bh30_36_36(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w17_10 <= CompressorOut_bh30_36_36(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_37_74 <= heap_bh30_w18_7 & heap_bh30_w18_3 & heap_bh30_w18_8;
   CompressorIn_bh30_37_75(0) <= heap_bh30_w19_9;
      Compressor_bh30_37: Compressor_13_3
      port map ( R => CompressorOut_bh30_37_37,
                 X0 => CompressorIn_bh30_37_74,
                 X1 => CompressorIn_bh30_37_75);
   heap_bh30_w18_9 <= CompressorOut_bh30_37_37(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w19_10 <= CompressorOut_bh30_37_37(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w20_10 <= CompressorOut_bh30_37_37(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_38_76 <= heap_bh30_w21_7 & heap_bh30_w21_3 & heap_bh30_w21_8;
   CompressorIn_bh30_38_77(0) <= heap_bh30_w22_8;
      Compressor_bh30_38: Compressor_13_3
      port map ( R => CompressorOut_bh30_38_38,
                 X0 => CompressorIn_bh30_38_76,
                 X1 => CompressorIn_bh30_38_77);
   heap_bh30_w21_9 <= CompressorOut_bh30_38_38(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w22_9 <= CompressorOut_bh30_38_38(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w23_8 <= CompressorOut_bh30_38_38(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_39_78 <= heap_bh30_w24_3 & heap_bh30_w24_1 & heap_bh30_w24_4;
   CompressorIn_bh30_39_79(0) <= heap_bh30_w25_3;
      Compressor_bh30_39: Compressor_13_3
      port map ( R => CompressorOut_bh30_39_39,
                 X0 => CompressorIn_bh30_39_78,
                 X1 => CompressorIn_bh30_39_79);
   heap_bh30_w24_5 <= CompressorOut_bh30_39_39(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w25_4 <= CompressorOut_bh30_39_39(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w26_3 <= CompressorOut_bh30_39_39(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_40_80 <= heap_bh30_w9_7 & heap_bh30_w9_3 & heap_bh30_w9_8;
   CompressorIn_bh30_40_81(0) <= heap_bh30_w10_9;
      Compressor_bh30_40: Compressor_13_3
      port map ( R => CompressorOut_bh30_40_40,
                 X0 => CompressorIn_bh30_40_80,
                 X1 => CompressorIn_bh30_40_81);
   heap_bh30_w9_9 <= CompressorOut_bh30_40_40(0); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w10_10 <= CompressorOut_bh30_40_40(1); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w11_10 <= CompressorOut_bh30_40_40(2); -- cycle= 0 cp= 3.97916e-09
   finalAdderIn0_bh30 <= "0" & heap_bh30_w43_0 & heap_bh30_w42_0 & heap_bh30_w41_0 & heap_bh30_w40_0 & heap_bh30_w39_0 & heap_bh30_w38_0 & heap_bh30_w37_0 & heap_bh30_w36_0 & heap_bh30_w35_0 & heap_bh30_w34_0 & heap_bh30_w33_0 & heap_bh30_w32_0 & heap_bh30_w31_0 & heap_bh30_w30_0 & heap_bh30_w29_0 & heap_bh30_w28_0 & heap_bh30_w27_0 & heap_bh30_w26_2 & heap_bh30_w25_4 & heap_bh30_w24_5 & heap_bh30_w23_7 & heap_bh30_w22_9 & heap_bh30_w21_9 & heap_bh30_w20_9 & heap_bh30_w19_10 & heap_bh30_w18_9 & heap_bh30_w17_9 & heap_bh30_w16_10 & heap_bh30_w15_9 & heap_bh30_w14_9 & heap_bh30_w13_10 & heap_bh30_w12_9 & heap_bh30_w11_9 & heap_bh30_w10_10 & heap_bh30_w9_9 & heap_bh30_w8_9 & heap_bh30_w7_9 & heap_bh30_w6_7 & heap_bh30_w5_8 & heap_bh30_w4_4 & heap_bh30_w3_5 & heap_bh30_w2_3 & heap_bh30_w1_1;
   finalAdderIn1_bh30 <= "0" & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & heap_bh30_w27_1 & heap_bh30_w26_3 & '0' & '0' & heap_bh30_w23_8 & '0' & '0' & heap_bh30_w20_10 & '0' & '0' & heap_bh30_w17_10 & '0' & '0' & heap_bh30_w14_10 & '0' & '0' & heap_bh30_w11_10 & '0' & '0' & '0' & '0' & '0' & heap_bh30_w5_7 & heap_bh30_w4_7 & '0' & '0' & heap_bh30_w1_0;
   finalAdderCin_bh30 <= '0';
      Adder_final30_0: IntAdder_44_f400_uid156
      port map ( Cin => finalAdderCin_bh30,
                 R => finalAdderOut_bh30,
                 X => finalAdderIn0_bh30,
                 Y => finalAdderIn1_bh30);
   -- concatenate all the compressed chunks
   CompressionResult30 <= finalAdderOut_bh30 & tempR_bh30_0;
   -- End of code generated by BitHeap::generateCompressorVHDL
   R <= CompressionResult30(43 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                   RightShifter_51_by_max_30_comb_uid166
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

entity RightShifter_51_by_max_30_comb_uid166 is
   port ( X : in  std_logic_vector(50 downto 0);
          S : in  std_logic_vector(4 downto 0);
          R : out  std_logic_vector(80 downto 0)   );
end entity;

architecture arch of RightShifter_51_by_max_30_comb_uid166 is
signal level0 :  std_logic_vector(50 downto 0);
signal ps :  std_logic_vector(4 downto 0);
signal level1 :  std_logic_vector(51 downto 0);
signal level2 :  std_logic_vector(53 downto 0);
signal level3 :  std_logic_vector(57 downto 0);
signal level4 :  std_logic_vector(65 downto 0);
signal level5 :  std_logic_vector(81 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<=  (0 downto 0 => '0') & level0 when ps(0) = '1' else    level0 & (0 downto 0 => '0');
   level2<=  (1 downto 0 => '0') & level1 when ps(1) = '1' else    level1 & (1 downto 0 => '0');
   level3<=  (3 downto 0 => '0') & level2 when ps(2) = '1' else    level2 & (3 downto 0 => '0');
   level4<=  (7 downto 0 => '0') & level3 when ps(3) = '1' else    level3 & (7 downto 0 => '0');
   level5<=  (15 downto 0 => '0') & level4 when ps(4) = '1' else    level4 & (15 downto 0 => '0');
   R <= level5(81 downto 1);
end architecture;

--------------------------------------------------------------------------------
--                          PositMult_30_6_comb_uid2
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

entity PositMult_30_6_comb_uid2 is
   port ( InputA : in  std_logic_vector(29 downto 0);
          InputB : in  std_logic_vector(29 downto 0);
          Output : out  std_logic_vector(29 downto 0)   );
end entity;

architecture arch of PositMult_30_6_comb_uid2 is
   component PositDecoder_30_6_comb_uid4 is
      port ( Input : in  std_logic_vector(29 downto 0);
             Sign : out  std_logic;
             Reg : out  std_logic_vector(5 downto 0);
             Exp : out  std_logic_vector(5 downto 0);
             Frac : out  std_logic_vector(21 downto 0);
             z : out  std_logic;
             inf : out  std_logic   );
   end component;

   component PositDecoder_30_6_comb_uid16 is
      port ( Input : in  std_logic_vector(29 downto 0);
             Sign : out  std_logic;
             Reg : out  std_logic_vector(5 downto 0);
             Exp : out  std_logic_vector(5 downto 0);
             Frac : out  std_logic_vector(21 downto 0);
             z : out  std_logic;
             inf : out  std_logic   );
   end component;

   component IntMultiplier_UsingDSP_22_22_44_unsigned_comb_uid28 is
      port ( X : in  std_logic_vector(21 downto 0);
             Y : in  std_logic_vector(21 downto 0);
             R : out  std_logic_vector(43 downto 0)   );
   end component;

   component RightShifter_51_by_max_30_comb_uid166 is
      port ( X : in  std_logic_vector(50 downto 0);
             S : in  std_logic_vector(4 downto 0);
             R : out  std_logic_vector(80 downto 0)   );
   end component;

signal sign_A :  std_logic;
signal reg_A :  std_logic_vector(5 downto 0);
signal exp_A :  std_logic_vector(5 downto 0);
signal frac_A :  std_logic_vector(21 downto 0);
signal z_A :  std_logic;
signal inf_A :  std_logic;
signal sign_B :  std_logic;
signal reg_B :  std_logic_vector(5 downto 0);
signal exp_B :  std_logic_vector(5 downto 0);
signal frac_B :  std_logic_vector(21 downto 0);
signal z_B :  std_logic;
signal inf_B :  std_logic;
signal sf_A :  std_logic_vector(11 downto 0);
signal sf_B :  std_logic_vector(11 downto 0);
signal sign :  std_logic;
signal z :  std_logic;
signal inf :  std_logic;
signal frac_mult :  std_logic_vector(43 downto 0);
signal ovf_m :  std_logic;
signal normFrac :  std_logic_vector(44 downto 0);
signal sf_mult :  std_logic_vector(12 downto 0);
signal sf_sign :  std_logic;
signal nzero :  std_logic;
signal ExpBits :  std_logic_vector(5 downto 0);
signal RegimeAns_tmp :  std_logic_vector(4 downto 0);
signal RegimeAns :  std_logic_vector(4 downto 0);
signal ovf_reg :  std_logic;
signal FinalRegime :  std_logic_vector(4 downto 0);
signal ovf_regF :  std_logic;
signal FinalExp :  std_logic_vector(5 downto 0);
signal tmp1 :  std_logic_vector(50 downto 0);
signal tmp2 :  std_logic_vector(50 downto 0);
signal shift_neg :  std_logic_vector(4 downto 0);
signal shift_pos :  std_logic_vector(4 downto 0);
signal shifter_in :  std_logic_vector(50 downto 0);
signal shifter_S :  std_logic_vector(4 downto 0);
signal shifter_out :  std_logic_vector(80 downto 0);
signal tmp_ans :  std_logic_vector(28 downto 0);
signal LSB :  std_logic;
signal G :  std_logic;
signal R :  std_logic;
signal S :  std_logic;
signal round :  std_logic;
begin
------------------------------- Data Extraction -------------------------------
   decoderA: PositDecoder_30_6_comb_uid4
      port map ( Exp => exp_A,
                 Frac => frac_A,
                 Input => InputA,
                 Reg => reg_A,
                 Sign => sign_A,
                 inf => inf_A,
                 z => z_A);
   decoderB: PositDecoder_30_6_comb_uid16
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
   mult: IntMultiplier_UsingDSP_22_22_44_unsigned_comb_uid28
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
   ExpBits <= sf_mult(5 downto 0);
   RegimeAns_tmp <= sf_mult(10 downto 6);
   -- Get Regime's absolute value
   RegimeAns <= (NOT RegimeAns_tmp)+1 when sf_sign = '1' else RegimeAns_tmp;
   -- Check for Regime overflow
   ovf_reg <= RegimeAns(RegimeAns'high);
   FinalRegime <= '0' & "1111" when ovf_reg = '1' else RegimeAns;
   ovf_regF <= '1' when FinalRegime = ('0' & "1111") else '0';
   FinalExp <= "000000" when ((ovf_reg = '1') OR (ovf_regF = '1') OR (nzero='0')) else ExpBits;
------------------------------- Packing Stage 1 -------------------------------
   tmp1 <= nzero & '0' & FinalExp & normFrac(42 downto 0);
   tmp2 <= '0' & nzero & FinalExp & normFrac(42 downto 0);
   shift_neg <= FinalRegime - 2 when (ovf_regF = '1') else FinalRegime - 1;
   shift_pos <= FinalRegime - 1 when (ovf_regF = '1') else FinalRegime;
   shifter_in <= tmp2 when sf_sign = '1' else tmp1;
   shifter_S <= shift_neg when sf_sign = '1' else shift_pos;
   RightShifterComponent: RightShifter_51_by_max_30_comb_uid166
      port map ( R => shifter_out,
                 S => shifter_S,
                 X => shifter_in);
   tmp_ans <= shifter_out(80 downto 52);
--------------------- Packing Stage 2 - Unbiased Rounding ---------------------
   LSB <= shifter_out(52);
   G <= shifter_out(51);
   R <= shifter_out(50);
   S <= '0' when shifter_out(49 downto 0) = 0 else '1';
   round <= G AND (LSB OR R OR S) when NOT((ovf_reg OR ovf_regF) = '1') else '0';
   Output <= '1' & "00000000000000000000000000000" when inf = '1' else "000000000000000000000000000000" when z = '1' else '0' & (tmp_ans + round) when sign = '0' else NOT('0' & (tmp_ans + round))+1;
end architecture;

