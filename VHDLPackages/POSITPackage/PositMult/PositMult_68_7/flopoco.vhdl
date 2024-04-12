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
--                               Compressor_6_3
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

entity Compressor_6_3 is
   port ( X0 : in  std_logic_vector(5 downto 0);
          R : out  std_logic_vector(2 downto 0)   );
end entity;

architecture arch of Compressor_6_3 is
signal X :  std_logic_vector(5 downto 0);
begin
   X <=X0 ;
   with X select R <= 
      "000" when "000000", 
      "001" when "000001", 
      "001" when "000010", 
      "010" when "000011", 
      "001" when "000100", 
      "010" when "000101", 
      "010" when "000110", 
      "011" when "000111", 
      "001" when "001000", 
      "010" when "001001", 
      "010" when "001010", 
      "011" when "001011", 
      "010" when "001100", 
      "011" when "001101", 
      "011" when "001110", 
      "100" when "001111", 
      "001" when "010000", 
      "010" when "010001", 
      "010" when "010010", 
      "011" when "010011", 
      "010" when "010100", 
      "011" when "010101", 
      "011" when "010110", 
      "100" when "010111", 
      "010" when "011000", 
      "011" when "011001", 
      "011" when "011010", 
      "100" when "011011", 
      "011" when "011100", 
      "100" when "011101", 
      "100" when "011110", 
      "101" when "011111", 
      "001" when "100000", 
      "010" when "100001", 
      "010" when "100010", 
      "011" when "100011", 
      "010" when "100100", 
      "011" when "100101", 
      "011" when "100110", 
      "100" when "100111", 
      "010" when "101000", 
      "011" when "101001", 
      "011" when "101010", 
      "100" when "101011", 
      "011" when "101100", 
      "100" when "101101", 
      "100" when "101110", 
      "101" when "101111", 
      "010" when "110000", 
      "011" when "110001", 
      "011" when "110010", 
      "100" when "110011", 
      "011" when "110100", 
      "100" when "110101", 
      "100" when "110110", 
      "101" when "110111", 
      "011" when "111000", 
      "100" when "111001", 
      "100" when "111010", 
      "101" when "111011", 
      "100" when "111100", 
      "101" when "111101", 
      "101" when "111110", 
      "110" when "111111", 
      "---" when others;

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
--                               Compressor_4_3
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

entity Compressor_4_3 is
   port ( X0 : in  std_logic_vector(3 downto 0);
          R : out  std_logic_vector(2 downto 0)   );
end entity;

architecture arch of Compressor_4_3 is
signal X :  std_logic_vector(3 downto 0);
begin
   X <=X0 ;
   with X select R <= 
      "000" when "0000", 
      "001" when "0001", 
      "001" when "0010", 
      "010" when "0011", 
      "001" when "0100", 
      "010" when "0101", 
      "010" when "0110", 
      "011" when "0111", 
      "001" when "1000", 
      "010" when "1001", 
      "010" when "1010", 
      "011" when "1011", 
      "010" when "1100", 
      "011" when "1101", 
      "011" when "1110", 
      "100" when "1111", 
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
--                             LZOC_67_comb_uid6
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

entity LZOC_67_comb_uid6 is
   port ( I : in  std_logic_vector(66 downto 0);
          OZB : in  std_logic;
          O : out  std_logic_vector(6 downto 0)   );
end entity;

architecture arch of LZOC_67_comb_uid6 is
signal sozb :  std_logic;
signal level7 :  std_logic_vector(127 downto 0);
signal digit7 :  std_logic;
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
   level7<= I& (60 downto 0 => not(sozb));
   digit7<= '1' when level7(127 downto 64) = (127 downto 64 => sozb) else '0';
   level6<= level7(63 downto 0) when digit7='1' else level7(127 downto 64);
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
   O <= digit7 & digit6 & digit5 & digit4 & digit3 & digit2 & digit1;
end architecture;

--------------------------------------------------------------------------------
--                    LeftShifter_67_by_max_67_comb_uid10
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

entity LeftShifter_67_by_max_67_comb_uid10 is
   port ( X : in  std_logic_vector(66 downto 0);
          S : in  std_logic_vector(6 downto 0);
          R : out  std_logic_vector(133 downto 0)   );
end entity;

architecture arch of LeftShifter_67_by_max_67_comb_uid10 is
signal level0 :  std_logic_vector(66 downto 0);
signal ps :  std_logic_vector(6 downto 0);
signal level1 :  std_logic_vector(67 downto 0);
signal level2 :  std_logic_vector(69 downto 0);
signal level3 :  std_logic_vector(73 downto 0);
signal level4 :  std_logic_vector(81 downto 0);
signal level5 :  std_logic_vector(97 downto 0);
signal level6 :  std_logic_vector(129 downto 0);
signal level7 :  std_logic_vector(193 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<= level0 & (0 downto 0 => '0') when ps(0)= '1' else     (0 downto 0 => '0') & level0;
   level2<= level1 & (1 downto 0 => '0') when ps(1)= '1' else     (1 downto 0 => '0') & level1;
   level3<= level2 & (3 downto 0 => '0') when ps(2)= '1' else     (3 downto 0 => '0') & level2;
   level4<= level3 & (7 downto 0 => '0') when ps(3)= '1' else     (7 downto 0 => '0') & level3;
   level5<= level4 & (15 downto 0 => '0') when ps(4)= '1' else     (15 downto 0 => '0') & level4;
   level6<= level5 & (31 downto 0 => '0') when ps(5)= '1' else     (31 downto 0 => '0') & level5;
   level7<= level6 & (63 downto 0 => '0') when ps(6)= '1' else     (63 downto 0 => '0') & level6;
   R <= level7(133 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                        PositDecoder_68_7_comb_uid4
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

entity PositDecoder_68_7_comb_uid4 is
   port ( Input : in  std_logic_vector(67 downto 0);
          Sign : out  std_logic;
          Reg : out  std_logic_vector(7 downto 0);
          Exp : out  std_logic_vector(6 downto 0);
          Frac : out  std_logic_vector(58 downto 0);
          z : out  std_logic;
          inf : out  std_logic   );
end entity;

architecture arch of PositDecoder_68_7_comb_uid4 is
   component LZOC_67_comb_uid6 is
      port ( I : in  std_logic_vector(66 downto 0);
             OZB : in  std_logic;
             O : out  std_logic_vector(6 downto 0)   );
   end component;

   component LeftShifter_67_by_max_67_comb_uid10 is
      port ( X : in  std_logic_vector(66 downto 0);
             S : in  std_logic_vector(6 downto 0);
             R : out  std_logic_vector(133 downto 0)   );
   end component;

signal nzero :  std_logic;
signal my_sign :  std_logic;
signal rep_sign :  std_logic_vector(66 downto 0);
signal twos :  std_logic_vector(66 downto 0);
signal rc :  std_logic;
signal rep_rc :  std_logic_vector(66 downto 0);
signal inv :  std_logic_vector(66 downto 0);
signal zero_var :  std_logic;
signal zc :  std_logic_vector(6 downto 0);
signal zc_sub :  std_logic_vector(6 downto 0);
signal shifted_twos :  std_logic_vector(133 downto 0);
signal tmp :  std_logic_vector(64 downto 0);
begin
-------------------------------- Special Cases --------------------------------
   nzero <= '0' when Input(66 downto 0) = 0 else '1';
   -- 1 if Input is zero
   z <= Input(67) NOR nzero;
   -- 1 if Input is infinity
   inf <= Input(67) AND (NOT nzero);
------------------------------- Extract Sign bit -------------------------------
   my_sign <= Input(67);
   Sign <= my_sign;
--------------------------- 2's Complement of Input ---------------------------
   rep_sign <= (others => my_sign);
   twos <= (rep_sign XOR Input(66 downto 0)) + my_sign;
   rc <= twos(66);
------------------------ Count leading zeros of regime ------------------------
   rep_rc <= (others => rc);
   -- Invert 2's
   inv <= rep_rc XOR twos;
   zero_var <= '0';
   LZOC_Component: LZOC_67_comb_uid6
      port map ( I => inv,
                 O => zc,
                 OZB => zero_var);
----------------------------- Shift out the regime -----------------------------
   zc_sub <= zc - 1;
   LeftShifterComponent: LeftShifter_67_by_max_67_comb_uid10
      port map ( R => shifted_twos,
                 S => zc_sub,
                 X => twos);
   tmp <= shifted_twos(64 downto 0);
------------------------ Extract fraction and exponent ------------------------
   Frac <= nzero & tmp(57 downto 0);
   Exp <= tmp(64 downto 58);
-------------------------------- Select regime --------------------------------
   Reg <= '0' & zc_sub when rc = '1' else NOT('0' & zc) + 1;
end architecture;

--------------------------------------------------------------------------------
--                             LZOC_67_comb_uid18
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

entity LZOC_67_comb_uid18 is
   port ( I : in  std_logic_vector(66 downto 0);
          OZB : in  std_logic;
          O : out  std_logic_vector(6 downto 0)   );
end entity;

architecture arch of LZOC_67_comb_uid18 is
signal sozb :  std_logic;
signal level7 :  std_logic_vector(127 downto 0);
signal digit7 :  std_logic;
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
   level7<= I& (60 downto 0 => not(sozb));
   digit7<= '1' when level7(127 downto 64) = (127 downto 64 => sozb) else '0';
   level6<= level7(63 downto 0) when digit7='1' else level7(127 downto 64);
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
   O <= digit7 & digit6 & digit5 & digit4 & digit3 & digit2 & digit1;
end architecture;

--------------------------------------------------------------------------------
--                    LeftShifter_67_by_max_67_comb_uid22
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

entity LeftShifter_67_by_max_67_comb_uid22 is
   port ( X : in  std_logic_vector(66 downto 0);
          S : in  std_logic_vector(6 downto 0);
          R : out  std_logic_vector(133 downto 0)   );
end entity;

architecture arch of LeftShifter_67_by_max_67_comb_uid22 is
signal level0 :  std_logic_vector(66 downto 0);
signal ps :  std_logic_vector(6 downto 0);
signal level1 :  std_logic_vector(67 downto 0);
signal level2 :  std_logic_vector(69 downto 0);
signal level3 :  std_logic_vector(73 downto 0);
signal level4 :  std_logic_vector(81 downto 0);
signal level5 :  std_logic_vector(97 downto 0);
signal level6 :  std_logic_vector(129 downto 0);
signal level7 :  std_logic_vector(193 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<= level0 & (0 downto 0 => '0') when ps(0)= '1' else     (0 downto 0 => '0') & level0;
   level2<= level1 & (1 downto 0 => '0') when ps(1)= '1' else     (1 downto 0 => '0') & level1;
   level3<= level2 & (3 downto 0 => '0') when ps(2)= '1' else     (3 downto 0 => '0') & level2;
   level4<= level3 & (7 downto 0 => '0') when ps(3)= '1' else     (7 downto 0 => '0') & level3;
   level5<= level4 & (15 downto 0 => '0') when ps(4)= '1' else     (15 downto 0 => '0') & level4;
   level6<= level5 & (31 downto 0 => '0') when ps(5)= '1' else     (31 downto 0 => '0') & level5;
   level7<= level6 & (63 downto 0 => '0') when ps(6)= '1' else     (63 downto 0 => '0') & level6;
   R <= level7(133 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                        PositDecoder_68_7_comb_uid16
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

entity PositDecoder_68_7_comb_uid16 is
   port ( Input : in  std_logic_vector(67 downto 0);
          Sign : out  std_logic;
          Reg : out  std_logic_vector(7 downto 0);
          Exp : out  std_logic_vector(6 downto 0);
          Frac : out  std_logic_vector(58 downto 0);
          z : out  std_logic;
          inf : out  std_logic   );
end entity;

architecture arch of PositDecoder_68_7_comb_uid16 is
   component LZOC_67_comb_uid18 is
      port ( I : in  std_logic_vector(66 downto 0);
             OZB : in  std_logic;
             O : out  std_logic_vector(6 downto 0)   );
   end component;

   component LeftShifter_67_by_max_67_comb_uid22 is
      port ( X : in  std_logic_vector(66 downto 0);
             S : in  std_logic_vector(6 downto 0);
             R : out  std_logic_vector(133 downto 0)   );
   end component;

signal nzero :  std_logic;
signal my_sign :  std_logic;
signal rep_sign :  std_logic_vector(66 downto 0);
signal twos :  std_logic_vector(66 downto 0);
signal rc :  std_logic;
signal rep_rc :  std_logic_vector(66 downto 0);
signal inv :  std_logic_vector(66 downto 0);
signal zero_var :  std_logic;
signal zc :  std_logic_vector(6 downto 0);
signal zc_sub :  std_logic_vector(6 downto 0);
signal shifted_twos :  std_logic_vector(133 downto 0);
signal tmp :  std_logic_vector(64 downto 0);
begin
-------------------------------- Special Cases --------------------------------
   nzero <= '0' when Input(66 downto 0) = 0 else '1';
   -- 1 if Input is zero
   z <= Input(67) NOR nzero;
   -- 1 if Input is infinity
   inf <= Input(67) AND (NOT nzero);
------------------------------- Extract Sign bit -------------------------------
   my_sign <= Input(67);
   Sign <= my_sign;
--------------------------- 2's Complement of Input ---------------------------
   rep_sign <= (others => my_sign);
   twos <= (rep_sign XOR Input(66 downto 0)) + my_sign;
   rc <= twos(66);
------------------------ Count leading zeros of regime ------------------------
   rep_rc <= (others => rc);
   -- Invert 2's
   inv <= rep_rc XOR twos;
   zero_var <= '0';
   LZOC_Component: LZOC_67_comb_uid18
      port map ( I => inv,
                 O => zc,
                 OZB => zero_var);
----------------------------- Shift out the regime -----------------------------
   zc_sub <= zc - 1;
   LeftShifterComponent: LeftShifter_67_by_max_67_comb_uid22
      port map ( R => shifted_twos,
                 S => zc_sub,
                 X => twos);
   tmp <= shifted_twos(64 downto 0);
------------------------ Extract fraction and exponent ------------------------
   Frac <= nzero & tmp(57 downto 0);
   Exp <= tmp(64 downto 58);
-------------------------------- Select regime --------------------------------
   Reg <= '0' & zc_sub when rc = '1' else NOT('0' & zc) + 1;
end architecture;

--------------------------------------------------------------------------------
--                          IntAdder_119_f400_uid376
--                   (IntAdderAlternative_119_comb_uid380)
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

entity IntAdder_119_f400_uid376 is
   port ( X : in  std_logic_vector(118 downto 0);
          Y : in  std_logic_vector(118 downto 0);
          Cin : in  std_logic;
          R : out  std_logic_vector(118 downto 0)   );
end entity;

architecture arch of IntAdder_119_f400_uid376 is
begin
   --Alternative
    R <= X + Y + Cin;
end architecture;

--------------------------------------------------------------------------------
--            IntMultiplier_UsingDSP_59_59_118_unsigned_comb_uid28
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

entity IntMultiplier_UsingDSP_59_59_118_unsigned_comb_uid28 is
   port ( X : in  std_logic_vector(58 downto 0);
          Y : in  std_logic_vector(58 downto 0);
          R : out  std_logic_vector(117 downto 0)   );
end entity;

architecture arch of IntMultiplier_UsingDSP_59_59_118_unsigned_comb_uid28 is
   component IntAdder_119_f400_uid376 is
      port ( X : in  std_logic_vector(118 downto 0);
             Y : in  std_logic_vector(118 downto 0);
             Cin : in  std_logic;
             R : out  std_logic_vector(118 downto 0)   );
   end component;

   component SmallMultTableP3x3r6XuYu_comb_uid33 is
      port ( X : in  std_logic_vector(5 downto 0);
             Y : out  std_logic_vector(5 downto 0)   );
   end component;

   component Compressor_6_3 is
      port ( X0 : in  std_logic_vector(5 downto 0);
             R : out  std_logic_vector(2 downto 0)   );
   end component;

   component Compressor_14_3 is
      port ( X0 : in  std_logic_vector(3 downto 0);
             X1 : in  std_logic_vector(0 downto 0);
             R : out  std_logic_vector(2 downto 0)   );
   end component;

   component Compressor_4_3 is
      port ( X0 : in  std_logic_vector(3 downto 0);
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

signal XX_m29 :  std_logic_vector(58 downto 0);
signal YY_m29 :  std_logic_vector(58 downto 0);
signal Xp_m29b31 :  std_logic_vector(11 downto 0);
signal Yp_m29b31 :  std_logic_vector(8 downto 0);
signal x_m29b31_0 :  std_logic_vector(2 downto 0);
signal x_m29b31_1 :  std_logic_vector(2 downto 0);
signal x_m29b31_2 :  std_logic_vector(2 downto 0);
signal x_m29b31_3 :  std_logic_vector(2 downto 0);
signal y_m29b31_0 :  std_logic_vector(2 downto 0);
signal y_m29b31_1 :  std_logic_vector(2 downto 0);
signal y_m29b31_2 :  std_logic_vector(2 downto 0);
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
signal Y0X2_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X2Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w5_1 :  std_logic;
signal heap_bh30_w6_1 :  std_logic;
signal heap_bh30_w7_0 :  std_logic;
signal heap_bh30_w8_0 :  std_logic;
signal heap_bh30_w9_0 :  std_logic;
signal Y0X3_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X3Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w8_1 :  std_logic;
signal heap_bh30_w9_1 :  std_logic;
signal heap_bh30_w10_0 :  std_logic;
signal heap_bh30_w11_0 :  std_logic;
signal heap_bh30_w12_0 :  std_logic;
signal Y1X0_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X0Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w2_2 :  std_logic;
signal heap_bh30_w3_2 :  std_logic;
signal heap_bh30_w4_1 :  std_logic;
signal heap_bh30_w5_2 :  std_logic;
signal heap_bh30_w6_2 :  std_logic;
signal Y1X1_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X1Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w4_2 :  std_logic;
signal heap_bh30_w5_3 :  std_logic;
signal heap_bh30_w6_3 :  std_logic;
signal heap_bh30_w7_1 :  std_logic;
signal heap_bh30_w8_2 :  std_logic;
signal heap_bh30_w9_2 :  std_logic;
signal Y1X2_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X2Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w7_2 :  std_logic;
signal heap_bh30_w8_3 :  std_logic;
signal heap_bh30_w9_3 :  std_logic;
signal heap_bh30_w10_1 :  std_logic;
signal heap_bh30_w11_1 :  std_logic;
signal heap_bh30_w12_1 :  std_logic;
signal Y1X3_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X3Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w10_2 :  std_logic;
signal heap_bh30_w11_2 :  std_logic;
signal heap_bh30_w12_2 :  std_logic;
signal heap_bh30_w13_0 :  std_logic;
signal heap_bh30_w14_0 :  std_logic;
signal heap_bh30_w15_0 :  std_logic;
signal Y2X0_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X0Y2_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w5_4 :  std_logic;
signal heap_bh30_w6_4 :  std_logic;
signal heap_bh30_w7_3 :  std_logic;
signal heap_bh30_w8_4 :  std_logic;
signal heap_bh30_w9_4 :  std_logic;
signal Y2X1_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X1Y2_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w7_4 :  std_logic;
signal heap_bh30_w8_5 :  std_logic;
signal heap_bh30_w9_5 :  std_logic;
signal heap_bh30_w10_3 :  std_logic;
signal heap_bh30_w11_3 :  std_logic;
signal heap_bh30_w12_3 :  std_logic;
signal Y2X2_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X2Y2_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w10_4 :  std_logic;
signal heap_bh30_w11_4 :  std_logic;
signal heap_bh30_w12_4 :  std_logic;
signal heap_bh30_w13_1 :  std_logic;
signal heap_bh30_w14_1 :  std_logic;
signal heap_bh30_w15_1 :  std_logic;
signal Y2X3_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X3Y2_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w13_2 :  std_logic;
signal heap_bh30_w14_2 :  std_logic;
signal heap_bh30_w15_2 :  std_logic;
signal heap_bh30_w16_0 :  std_logic;
signal heap_bh30_w17_0 :  std_logic;
signal heap_bh30_w18_0 :  std_logic;
signal DSP_bh30_ch0_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w117_0 :  std_logic;
signal heap_bh30_w116_0 :  std_logic;
signal heap_bh30_w115_0 :  std_logic;
signal heap_bh30_w114_0 :  std_logic;
signal heap_bh30_w113_0 :  std_logic;
signal heap_bh30_w112_0 :  std_logic;
signal heap_bh30_w111_0 :  std_logic;
signal heap_bh30_w110_0 :  std_logic;
signal heap_bh30_w109_0 :  std_logic;
signal heap_bh30_w108_0 :  std_logic;
signal heap_bh30_w107_0 :  std_logic;
signal heap_bh30_w106_0 :  std_logic;
signal heap_bh30_w105_0 :  std_logic;
signal heap_bh30_w104_0 :  std_logic;
signal heap_bh30_w103_0 :  std_logic;
signal heap_bh30_w102_0 :  std_logic;
signal heap_bh30_w101_0 :  std_logic;
signal heap_bh30_w100_0 :  std_logic;
signal heap_bh30_w99_0 :  std_logic;
signal heap_bh30_w98_0 :  std_logic;
signal heap_bh30_w97_0 :  std_logic;
signal heap_bh30_w96_0 :  std_logic;
signal heap_bh30_w95_0 :  std_logic;
signal heap_bh30_w94_0 :  std_logic;
signal heap_bh30_w93_0 :  std_logic;
signal heap_bh30_w92_0 :  std_logic;
signal heap_bh30_w91_0 :  std_logic;
signal heap_bh30_w90_0 :  std_logic;
signal heap_bh30_w89_0 :  std_logic;
signal heap_bh30_w88_0 :  std_logic;
signal heap_bh30_w87_0 :  std_logic;
signal heap_bh30_w86_0 :  std_logic;
signal heap_bh30_w85_0 :  std_logic;
signal heap_bh30_w84_0 :  std_logic;
signal heap_bh30_w83_0 :  std_logic;
signal heap_bh30_w82_0 :  std_logic;
signal heap_bh30_w81_0 :  std_logic;
signal heap_bh30_w80_0 :  std_logic;
signal heap_bh30_w79_0 :  std_logic;
signal heap_bh30_w78_0 :  std_logic;
signal heap_bh30_w77_0 :  std_logic;
signal DSP_bh30_ch1_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w93_1 :  std_logic;
signal heap_bh30_w92_1 :  std_logic;
signal heap_bh30_w91_1 :  std_logic;
signal heap_bh30_w90_1 :  std_logic;
signal heap_bh30_w89_1 :  std_logic;
signal heap_bh30_w88_1 :  std_logic;
signal heap_bh30_w87_1 :  std_logic;
signal heap_bh30_w86_1 :  std_logic;
signal heap_bh30_w85_1 :  std_logic;
signal heap_bh30_w84_1 :  std_logic;
signal heap_bh30_w83_1 :  std_logic;
signal heap_bh30_w82_1 :  std_logic;
signal heap_bh30_w81_1 :  std_logic;
signal heap_bh30_w80_1 :  std_logic;
signal heap_bh30_w79_1 :  std_logic;
signal heap_bh30_w78_1 :  std_logic;
signal heap_bh30_w77_1 :  std_logic;
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
signal DSP_bh30_ch2_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w69_1 :  std_logic;
signal heap_bh30_w68_1 :  std_logic;
signal heap_bh30_w67_1 :  std_logic;
signal heap_bh30_w66_1 :  std_logic;
signal heap_bh30_w65_1 :  std_logic;
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
signal heap_bh30_w52_0 :  std_logic;
signal heap_bh30_w51_0 :  std_logic;
signal heap_bh30_w50_0 :  std_logic;
signal heap_bh30_w49_0 :  std_logic;
signal heap_bh30_w48_0 :  std_logic;
signal heap_bh30_w47_0 :  std_logic;
signal heap_bh30_w46_0 :  std_logic;
signal heap_bh30_w45_0 :  std_logic;
signal heap_bh30_w44_0 :  std_logic;
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
signal DSP_bh30_ch3_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w100_1 :  std_logic;
signal heap_bh30_w99_1 :  std_logic;
signal heap_bh30_w98_1 :  std_logic;
signal heap_bh30_w97_1 :  std_logic;
signal heap_bh30_w96_1 :  std_logic;
signal heap_bh30_w95_1 :  std_logic;
signal heap_bh30_w94_1 :  std_logic;
signal heap_bh30_w93_2 :  std_logic;
signal heap_bh30_w92_2 :  std_logic;
signal heap_bh30_w91_2 :  std_logic;
signal heap_bh30_w90_2 :  std_logic;
signal heap_bh30_w89_2 :  std_logic;
signal heap_bh30_w88_2 :  std_logic;
signal heap_bh30_w87_2 :  std_logic;
signal heap_bh30_w86_2 :  std_logic;
signal heap_bh30_w85_2 :  std_logic;
signal heap_bh30_w84_2 :  std_logic;
signal heap_bh30_w83_2 :  std_logic;
signal heap_bh30_w82_2 :  std_logic;
signal heap_bh30_w81_2 :  std_logic;
signal heap_bh30_w80_2 :  std_logic;
signal heap_bh30_w79_2 :  std_logic;
signal heap_bh30_w78_2 :  std_logic;
signal heap_bh30_w77_2 :  std_logic;
signal heap_bh30_w76_1 :  std_logic;
signal heap_bh30_w75_1 :  std_logic;
signal heap_bh30_w74_1 :  std_logic;
signal heap_bh30_w73_1 :  std_logic;
signal heap_bh30_w72_1 :  std_logic;
signal heap_bh30_w71_1 :  std_logic;
signal heap_bh30_w70_1 :  std_logic;
signal heap_bh30_w69_2 :  std_logic;
signal heap_bh30_w68_2 :  std_logic;
signal heap_bh30_w67_2 :  std_logic;
signal heap_bh30_w66_2 :  std_logic;
signal heap_bh30_w65_2 :  std_logic;
signal heap_bh30_w64_2 :  std_logic;
signal heap_bh30_w63_2 :  std_logic;
signal heap_bh30_w62_2 :  std_logic;
signal heap_bh30_w61_2 :  std_logic;
signal heap_bh30_w60_2 :  std_logic;
signal DSP_bh30_ch4_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w76_2 :  std_logic;
signal heap_bh30_w75_2 :  std_logic;
signal heap_bh30_w74_2 :  std_logic;
signal heap_bh30_w73_2 :  std_logic;
signal heap_bh30_w72_2 :  std_logic;
signal heap_bh30_w71_2 :  std_logic;
signal heap_bh30_w70_2 :  std_logic;
signal heap_bh30_w69_3 :  std_logic;
signal heap_bh30_w68_3 :  std_logic;
signal heap_bh30_w67_3 :  std_logic;
signal heap_bh30_w66_3 :  std_logic;
signal heap_bh30_w65_3 :  std_logic;
signal heap_bh30_w64_3 :  std_logic;
signal heap_bh30_w63_3 :  std_logic;
signal heap_bh30_w62_3 :  std_logic;
signal heap_bh30_w61_3 :  std_logic;
signal heap_bh30_w60_3 :  std_logic;
signal heap_bh30_w59_2 :  std_logic;
signal heap_bh30_w58_2 :  std_logic;
signal heap_bh30_w57_2 :  std_logic;
signal heap_bh30_w56_2 :  std_logic;
signal heap_bh30_w55_2 :  std_logic;
signal heap_bh30_w54_2 :  std_logic;
signal heap_bh30_w53_2 :  std_logic;
signal heap_bh30_w52_1 :  std_logic;
signal heap_bh30_w51_1 :  std_logic;
signal heap_bh30_w50_1 :  std_logic;
signal heap_bh30_w49_1 :  std_logic;
signal heap_bh30_w48_1 :  std_logic;
signal heap_bh30_w47_1 :  std_logic;
signal heap_bh30_w46_1 :  std_logic;
signal heap_bh30_w45_1 :  std_logic;
signal heap_bh30_w44_1 :  std_logic;
signal heap_bh30_w43_1 :  std_logic;
signal heap_bh30_w42_1 :  std_logic;
signal heap_bh30_w41_1 :  std_logic;
signal heap_bh30_w40_1 :  std_logic;
signal heap_bh30_w39_1 :  std_logic;
signal heap_bh30_w38_1 :  std_logic;
signal heap_bh30_w37_1 :  std_logic;
signal heap_bh30_w36_1 :  std_logic;
signal DSP_bh30_ch5_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w52_2 :  std_logic;
signal heap_bh30_w51_2 :  std_logic;
signal heap_bh30_w50_2 :  std_logic;
signal heap_bh30_w49_2 :  std_logic;
signal heap_bh30_w48_2 :  std_logic;
signal heap_bh30_w47_2 :  std_logic;
signal heap_bh30_w46_2 :  std_logic;
signal heap_bh30_w45_2 :  std_logic;
signal heap_bh30_w44_2 :  std_logic;
signal heap_bh30_w43_2 :  std_logic;
signal heap_bh30_w42_2 :  std_logic;
signal heap_bh30_w41_2 :  std_logic;
signal heap_bh30_w40_2 :  std_logic;
signal heap_bh30_w39_2 :  std_logic;
signal heap_bh30_w38_2 :  std_logic;
signal heap_bh30_w37_2 :  std_logic;
signal heap_bh30_w36_2 :  std_logic;
signal heap_bh30_w35_1 :  std_logic;
signal heap_bh30_w34_1 :  std_logic;
signal heap_bh30_w33_1 :  std_logic;
signal heap_bh30_w32_1 :  std_logic;
signal heap_bh30_w31_1 :  std_logic;
signal heap_bh30_w30_1 :  std_logic;
signal heap_bh30_w29_1 :  std_logic;
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
signal heap_bh30_w18_1 :  std_logic;
signal heap_bh30_w17_1 :  std_logic;
signal heap_bh30_w16_1 :  std_logic;
signal heap_bh30_w15_3 :  std_logic;
signal heap_bh30_w14_3 :  std_logic;
signal heap_bh30_w13_3 :  std_logic;
signal heap_bh30_w12_5 :  std_logic;
signal DSP_bh30_ch6_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w83_3 :  std_logic;
signal heap_bh30_w82_3 :  std_logic;
signal heap_bh30_w81_3 :  std_logic;
signal heap_bh30_w80_3 :  std_logic;
signal heap_bh30_w79_3 :  std_logic;
signal heap_bh30_w78_3 :  std_logic;
signal heap_bh30_w77_3 :  std_logic;
signal heap_bh30_w76_3 :  std_logic;
signal heap_bh30_w75_3 :  std_logic;
signal heap_bh30_w74_3 :  std_logic;
signal heap_bh30_w73_3 :  std_logic;
signal heap_bh30_w72_3 :  std_logic;
signal heap_bh30_w71_3 :  std_logic;
signal heap_bh30_w70_3 :  std_logic;
signal heap_bh30_w69_4 :  std_logic;
signal heap_bh30_w68_4 :  std_logic;
signal heap_bh30_w67_4 :  std_logic;
signal heap_bh30_w66_4 :  std_logic;
signal heap_bh30_w65_4 :  std_logic;
signal heap_bh30_w64_4 :  std_logic;
signal heap_bh30_w63_4 :  std_logic;
signal heap_bh30_w62_4 :  std_logic;
signal heap_bh30_w61_4 :  std_logic;
signal heap_bh30_w60_4 :  std_logic;
signal heap_bh30_w59_3 :  std_logic;
signal heap_bh30_w58_3 :  std_logic;
signal heap_bh30_w57_3 :  std_logic;
signal heap_bh30_w56_3 :  std_logic;
signal heap_bh30_w55_3 :  std_logic;
signal heap_bh30_w54_3 :  std_logic;
signal heap_bh30_w53_3 :  std_logic;
signal heap_bh30_w52_3 :  std_logic;
signal heap_bh30_w51_3 :  std_logic;
signal heap_bh30_w50_3 :  std_logic;
signal heap_bh30_w49_3 :  std_logic;
signal heap_bh30_w48_3 :  std_logic;
signal heap_bh30_w47_3 :  std_logic;
signal heap_bh30_w46_3 :  std_logic;
signal heap_bh30_w45_3 :  std_logic;
signal heap_bh30_w44_3 :  std_logic;
signal heap_bh30_w43_3 :  std_logic;
signal DSP_bh30_ch7_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w59_4 :  std_logic;
signal heap_bh30_w58_4 :  std_logic;
signal heap_bh30_w57_4 :  std_logic;
signal heap_bh30_w56_4 :  std_logic;
signal heap_bh30_w55_4 :  std_logic;
signal heap_bh30_w54_4 :  std_logic;
signal heap_bh30_w53_4 :  std_logic;
signal heap_bh30_w52_4 :  std_logic;
signal heap_bh30_w51_4 :  std_logic;
signal heap_bh30_w50_4 :  std_logic;
signal heap_bh30_w49_4 :  std_logic;
signal heap_bh30_w48_4 :  std_logic;
signal heap_bh30_w47_4 :  std_logic;
signal heap_bh30_w46_4 :  std_logic;
signal heap_bh30_w45_4 :  std_logic;
signal heap_bh30_w44_4 :  std_logic;
signal heap_bh30_w43_4 :  std_logic;
signal heap_bh30_w42_3 :  std_logic;
signal heap_bh30_w41_3 :  std_logic;
signal heap_bh30_w40_3 :  std_logic;
signal heap_bh30_w39_3 :  std_logic;
signal heap_bh30_w38_3 :  std_logic;
signal heap_bh30_w37_3 :  std_logic;
signal heap_bh30_w36_3 :  std_logic;
signal heap_bh30_w35_2 :  std_logic;
signal heap_bh30_w34_2 :  std_logic;
signal heap_bh30_w33_2 :  std_logic;
signal heap_bh30_w32_2 :  std_logic;
signal heap_bh30_w31_2 :  std_logic;
signal heap_bh30_w30_2 :  std_logic;
signal heap_bh30_w29_2 :  std_logic;
signal heap_bh30_w28_1 :  std_logic;
signal heap_bh30_w27_1 :  std_logic;
signal heap_bh30_w26_1 :  std_logic;
signal heap_bh30_w25_1 :  std_logic;
signal heap_bh30_w24_1 :  std_logic;
signal heap_bh30_w23_1 :  std_logic;
signal heap_bh30_w22_1 :  std_logic;
signal heap_bh30_w21_1 :  std_logic;
signal heap_bh30_w20_1 :  std_logic;
signal heap_bh30_w19_1 :  std_logic;
signal DSP_bh30_ch8_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w35_3 :  std_logic;
signal heap_bh30_w34_3 :  std_logic;
signal heap_bh30_w33_3 :  std_logic;
signal heap_bh30_w32_3 :  std_logic;
signal heap_bh30_w31_3 :  std_logic;
signal heap_bh30_w30_3 :  std_logic;
signal heap_bh30_w29_3 :  std_logic;
signal heap_bh30_w28_2 :  std_logic;
signal heap_bh30_w27_2 :  std_logic;
signal heap_bh30_w26_2 :  std_logic;
signal heap_bh30_w25_2 :  std_logic;
signal heap_bh30_w24_2 :  std_logic;
signal heap_bh30_w23_2 :  std_logic;
signal heap_bh30_w22_2 :  std_logic;
signal heap_bh30_w21_2 :  std_logic;
signal heap_bh30_w20_2 :  std_logic;
signal heap_bh30_w19_2 :  std_logic;
signal heap_bh30_w18_2 :  std_logic;
signal heap_bh30_w17_2 :  std_logic;
signal heap_bh30_w16_2 :  std_logic;
signal heap_bh30_w15_4 :  std_logic;
signal heap_bh30_w14_4 :  std_logic;
signal heap_bh30_w13_4 :  std_logic;
signal heap_bh30_w12_6 :  std_logic;
signal heap_bh30_w11_5 :  std_logic;
signal heap_bh30_w10_5 :  std_logic;
signal heap_bh30_w9_6 :  std_logic;
signal heap_bh30_w8_6 :  std_logic;
signal heap_bh30_w7_5 :  std_logic;
signal heap_bh30_w6_5 :  std_logic;
signal heap_bh30_w5_5 :  std_logic;
signal heap_bh30_w4_3 :  std_logic;
signal heap_bh30_w3_3 :  std_logic;
signal heap_bh30_w2_3 :  std_logic;
signal heap_bh30_w1_1 :  std_logic;
signal heap_bh30_w0_1 :  std_logic;
signal DSP_bh30_ch9_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w66_5 :  std_logic;
signal heap_bh30_w65_5 :  std_logic;
signal heap_bh30_w64_5 :  std_logic;
signal heap_bh30_w63_5 :  std_logic;
signal heap_bh30_w62_5 :  std_logic;
signal heap_bh30_w61_5 :  std_logic;
signal heap_bh30_w60_5 :  std_logic;
signal heap_bh30_w59_5 :  std_logic;
signal heap_bh30_w58_5 :  std_logic;
signal heap_bh30_w57_5 :  std_logic;
signal heap_bh30_w56_5 :  std_logic;
signal heap_bh30_w55_5 :  std_logic;
signal heap_bh30_w54_5 :  std_logic;
signal heap_bh30_w53_5 :  std_logic;
signal heap_bh30_w52_5 :  std_logic;
signal heap_bh30_w51_5 :  std_logic;
signal heap_bh30_w50_5 :  std_logic;
signal heap_bh30_w49_5 :  std_logic;
signal heap_bh30_w48_5 :  std_logic;
signal heap_bh30_w47_5 :  std_logic;
signal heap_bh30_w46_5 :  std_logic;
signal heap_bh30_w45_5 :  std_logic;
signal heap_bh30_w44_5 :  std_logic;
signal heap_bh30_w43_5 :  std_logic;
signal heap_bh30_w42_4 :  std_logic;
signal heap_bh30_w41_4 :  std_logic;
signal heap_bh30_w40_4 :  std_logic;
signal heap_bh30_w39_4 :  std_logic;
signal heap_bh30_w38_4 :  std_logic;
signal heap_bh30_w37_4 :  std_logic;
signal heap_bh30_w36_4 :  std_logic;
signal heap_bh30_w35_4 :  std_logic;
signal heap_bh30_w34_4 :  std_logic;
signal heap_bh30_w33_4 :  std_logic;
signal heap_bh30_w32_4 :  std_logic;
signal heap_bh30_w31_4 :  std_logic;
signal heap_bh30_w30_4 :  std_logic;
signal heap_bh30_w29_4 :  std_logic;
signal heap_bh30_w28_3 :  std_logic;
signal heap_bh30_w27_3 :  std_logic;
signal heap_bh30_w26_3 :  std_logic;
signal DSP_bh30_ch10_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w42_5 :  std_logic;
signal heap_bh30_w41_5 :  std_logic;
signal heap_bh30_w40_5 :  std_logic;
signal heap_bh30_w39_5 :  std_logic;
signal heap_bh30_w38_5 :  std_logic;
signal heap_bh30_w37_5 :  std_logic;
signal heap_bh30_w36_5 :  std_logic;
signal heap_bh30_w35_5 :  std_logic;
signal heap_bh30_w34_5 :  std_logic;
signal heap_bh30_w33_5 :  std_logic;
signal heap_bh30_w32_5 :  std_logic;
signal heap_bh30_w31_5 :  std_logic;
signal heap_bh30_w30_5 :  std_logic;
signal heap_bh30_w29_5 :  std_logic;
signal heap_bh30_w28_4 :  std_logic;
signal heap_bh30_w27_4 :  std_logic;
signal heap_bh30_w26_4 :  std_logic;
signal heap_bh30_w25_3 :  std_logic;
signal heap_bh30_w24_3 :  std_logic;
signal heap_bh30_w23_3 :  std_logic;
signal heap_bh30_w22_3 :  std_logic;
signal heap_bh30_w21_3 :  std_logic;
signal heap_bh30_w20_3 :  std_logic;
signal heap_bh30_w19_3 :  std_logic;
signal heap_bh30_w18_3 :  std_logic;
signal heap_bh30_w17_3 :  std_logic;
signal heap_bh30_w16_3 :  std_logic;
signal heap_bh30_w15_5 :  std_logic;
signal heap_bh30_w14_5 :  std_logic;
signal heap_bh30_w13_5 :  std_logic;
signal heap_bh30_w12_7 :  std_logic;
signal heap_bh30_w11_6 :  std_logic;
signal heap_bh30_w10_6 :  std_logic;
signal heap_bh30_w9_7 :  std_logic;
signal heap_bh30_w8_7 :  std_logic;
signal heap_bh30_w7_6 :  std_logic;
signal heap_bh30_w6_6 :  std_logic;
signal heap_bh30_w5_6 :  std_logic;
signal heap_bh30_w4_4 :  std_logic;
signal heap_bh30_w3_4 :  std_logic;
signal heap_bh30_w2_4 :  std_logic;
signal CompressorIn_bh30_0_0 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_0_0 :  std_logic_vector(2 downto 0);
signal heap_bh30_w8_8 :  std_logic;
signal heap_bh30_w9_8 :  std_logic;
signal heap_bh30_w10_7 :  std_logic;
signal CompressorIn_bh30_1_1 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_1_1 :  std_logic_vector(2 downto 0);
signal heap_bh30_w9_9 :  std_logic;
signal heap_bh30_w10_8 :  std_logic;
signal heap_bh30_w11_7 :  std_logic;
signal CompressorIn_bh30_2_2 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_2_3 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_2_2 :  std_logic_vector(2 downto 0);
signal heap_bh30_w5_7 :  std_logic;
signal heap_bh30_w6_7 :  std_logic;
signal heap_bh30_w7_7 :  std_logic;
signal CompressorIn_bh30_3_4 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_3_5 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_3_3 :  std_logic_vector(2 downto 0);
signal heap_bh30_w6_8 :  std_logic;
signal heap_bh30_w7_8 :  std_logic;
signal heap_bh30_w8_9 :  std_logic;
signal CompressorIn_bh30_4_6 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_4_7 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_4_4 :  std_logic_vector(2 downto 0);
signal heap_bh30_w10_9 :  std_logic;
signal heap_bh30_w11_8 :  std_logic;
signal heap_bh30_w12_8 :  std_logic;
signal CompressorIn_bh30_5_8 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_5_9 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_5_5 :  std_logic_vector(2 downto 0);
signal heap_bh30_w11_9 :  std_logic;
signal heap_bh30_w12_9 :  std_logic;
signal heap_bh30_w13_6 :  std_logic;
signal CompressorIn_bh30_6_10 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_6_11 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_6_6 :  std_logic_vector(2 downto 0);
signal heap_bh30_w12_10 :  std_logic;
signal heap_bh30_w13_7 :  std_logic;
signal heap_bh30_w14_6 :  std_logic;
signal CompressorIn_bh30_7_12 :  std_logic_vector(3 downto 0);
signal CompressorOut_bh30_7_7 :  std_logic_vector(2 downto 0);
signal heap_bh30_w7_9 :  std_logic;
signal heap_bh30_w8_10 :  std_logic;
signal heap_bh30_w9_10 :  std_logic;
signal CompressorIn_bh30_8_13 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_8_14 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_8_8 :  std_logic_vector(2 downto 0);
signal heap_bh30_w2_5 :  std_logic;
signal heap_bh30_w3_5 :  std_logic;
signal heap_bh30_w4_5 :  std_logic;
signal CompressorIn_bh30_9_15 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_9_16 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_9_9 :  std_logic_vector(2 downto 0);
signal heap_bh30_w14_7 :  std_logic;
signal heap_bh30_w15_6 :  std_logic;
signal heap_bh30_w16_4 :  std_logic;
signal CompressorIn_bh30_10_17 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_10_18 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_10_10 :  std_logic_vector(2 downto 0);
signal heap_bh30_w4_6 :  std_logic;
signal heap_bh30_w5_8 :  std_logic;
signal heap_bh30_w6_9 :  std_logic;
signal CompressorIn_bh30_11_19 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_11_20 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_11_11 :  std_logic_vector(2 downto 0);
signal heap_bh30_w10_10 :  std_logic;
signal heap_bh30_w11_10 :  std_logic;
signal heap_bh30_w12_11 :  std_logic;
signal CompressorIn_bh30_12_21 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_12_22 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_12_12 :  std_logic_vector(2 downto 0);
signal heap_bh30_w13_8 :  std_logic;
signal heap_bh30_w14_8 :  std_logic;
signal heap_bh30_w15_7 :  std_logic;
signal CompressorIn_bh30_13_23 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_13_24 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_13_13 :  std_logic_vector(2 downto 0);
signal heap_bh30_w6_10 :  std_logic;
signal heap_bh30_w7_10 :  std_logic;
signal heap_bh30_w8_11 :  std_logic;
signal CompressorIn_bh30_14_25 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_14_26 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_14_14 :  std_logic_vector(2 downto 0);
signal heap_bh30_w8_12 :  std_logic;
signal heap_bh30_w9_11 :  std_logic;
signal heap_bh30_w10_11 :  std_logic;
signal CompressorIn_bh30_15_27 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_15_15 :  std_logic_vector(1 downto 0);
signal heap_bh30_w12_12 :  std_logic;
signal heap_bh30_w13_9 :  std_logic;
signal CompressorIn_bh30_16_28 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_16_29 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_16_16 :  std_logic_vector(2 downto 0);
signal heap_bh30_w11_11 :  std_logic;
signal heap_bh30_w12_13 :  std_logic;
signal heap_bh30_w13_10 :  std_logic;
signal CompressorIn_bh30_17_30 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_17_31 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_17_17 :  std_logic_vector(2 downto 0);
signal heap_bh30_w15_8 :  std_logic;
signal heap_bh30_w16_5 :  std_logic;
signal heap_bh30_w17_4 :  std_logic;
signal CompressorIn_bh30_18_32 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_18_18 :  std_logic_vector(2 downto 0);
signal heap_bh30_w13_11 :  std_logic;
signal heap_bh30_w14_9 :  std_logic;
signal heap_bh30_w15_9 :  std_logic;
signal CompressorIn_bh30_19_33 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_19_19 :  std_logic_vector(2 downto 0);
signal heap_bh30_w29_6 :  std_logic;
signal heap_bh30_w30_6 :  std_logic;
signal heap_bh30_w31_6 :  std_logic;
signal CompressorIn_bh30_20_34 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_20_20 :  std_logic_vector(2 downto 0);
signal heap_bh30_w30_7 :  std_logic;
signal heap_bh30_w31_7 :  std_logic;
signal heap_bh30_w32_6 :  std_logic;
signal CompressorIn_bh30_21_35 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_21_21 :  std_logic_vector(2 downto 0);
signal heap_bh30_w31_8 :  std_logic;
signal heap_bh30_w32_7 :  std_logic;
signal heap_bh30_w33_6 :  std_logic;
signal CompressorIn_bh30_22_36 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_22_22 :  std_logic_vector(2 downto 0);
signal heap_bh30_w32_8 :  std_logic;
signal heap_bh30_w33_7 :  std_logic;
signal heap_bh30_w34_6 :  std_logic;
signal CompressorIn_bh30_23_37 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_23_23 :  std_logic_vector(2 downto 0);
signal heap_bh30_w33_8 :  std_logic;
signal heap_bh30_w34_7 :  std_logic;
signal heap_bh30_w35_6 :  std_logic;
signal CompressorIn_bh30_24_38 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_24_24 :  std_logic_vector(2 downto 0);
signal heap_bh30_w34_8 :  std_logic;
signal heap_bh30_w35_7 :  std_logic;
signal heap_bh30_w36_6 :  std_logic;
signal CompressorIn_bh30_25_39 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_25_25 :  std_logic_vector(2 downto 0);
signal heap_bh30_w35_8 :  std_logic;
signal heap_bh30_w36_7 :  std_logic;
signal heap_bh30_w37_6 :  std_logic;
signal CompressorIn_bh30_26_40 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_26_26 :  std_logic_vector(2 downto 0);
signal heap_bh30_w36_8 :  std_logic;
signal heap_bh30_w37_7 :  std_logic;
signal heap_bh30_w38_6 :  std_logic;
signal CompressorIn_bh30_27_41 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_27_27 :  std_logic_vector(2 downto 0);
signal heap_bh30_w37_8 :  std_logic;
signal heap_bh30_w38_7 :  std_logic;
signal heap_bh30_w39_6 :  std_logic;
signal CompressorIn_bh30_28_42 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_28_28 :  std_logic_vector(2 downto 0);
signal heap_bh30_w38_8 :  std_logic;
signal heap_bh30_w39_7 :  std_logic;
signal heap_bh30_w40_6 :  std_logic;
signal CompressorIn_bh30_29_43 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_29_29 :  std_logic_vector(2 downto 0);
signal heap_bh30_w39_8 :  std_logic;
signal heap_bh30_w40_7 :  std_logic;
signal heap_bh30_w41_6 :  std_logic;
signal CompressorIn_bh30_30_44 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_30_30 :  std_logic_vector(2 downto 0);
signal heap_bh30_w40_8 :  std_logic;
signal heap_bh30_w41_7 :  std_logic;
signal heap_bh30_w42_6 :  std_logic;
signal CompressorIn_bh30_31_45 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_31_31 :  std_logic_vector(2 downto 0);
signal heap_bh30_w41_8 :  std_logic;
signal heap_bh30_w42_7 :  std_logic;
signal heap_bh30_w43_6 :  std_logic;
signal CompressorIn_bh30_32_46 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_32_32 :  std_logic_vector(2 downto 0);
signal heap_bh30_w42_8 :  std_logic;
signal heap_bh30_w43_7 :  std_logic;
signal heap_bh30_w44_6 :  std_logic;
signal CompressorIn_bh30_33_47 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_33_33 :  std_logic_vector(2 downto 0);
signal heap_bh30_w43_8 :  std_logic;
signal heap_bh30_w44_7 :  std_logic;
signal heap_bh30_w45_6 :  std_logic;
signal CompressorIn_bh30_34_48 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_34_34 :  std_logic_vector(2 downto 0);
signal heap_bh30_w44_8 :  std_logic;
signal heap_bh30_w45_7 :  std_logic;
signal heap_bh30_w46_6 :  std_logic;
signal CompressorIn_bh30_35_49 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_35_35 :  std_logic_vector(2 downto 0);
signal heap_bh30_w45_8 :  std_logic;
signal heap_bh30_w46_7 :  std_logic;
signal heap_bh30_w47_6 :  std_logic;
signal CompressorIn_bh30_36_50 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_36_36 :  std_logic_vector(2 downto 0);
signal heap_bh30_w46_8 :  std_logic;
signal heap_bh30_w47_7 :  std_logic;
signal heap_bh30_w48_6 :  std_logic;
signal CompressorIn_bh30_37_51 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_37_37 :  std_logic_vector(2 downto 0);
signal heap_bh30_w47_8 :  std_logic;
signal heap_bh30_w48_7 :  std_logic;
signal heap_bh30_w49_6 :  std_logic;
signal CompressorIn_bh30_38_52 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_38_38 :  std_logic_vector(2 downto 0);
signal heap_bh30_w48_8 :  std_logic;
signal heap_bh30_w49_7 :  std_logic;
signal heap_bh30_w50_6 :  std_logic;
signal CompressorIn_bh30_39_53 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_39_39 :  std_logic_vector(2 downto 0);
signal heap_bh30_w49_8 :  std_logic;
signal heap_bh30_w50_7 :  std_logic;
signal heap_bh30_w51_6 :  std_logic;
signal CompressorIn_bh30_40_54 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_40_40 :  std_logic_vector(2 downto 0);
signal heap_bh30_w50_8 :  std_logic;
signal heap_bh30_w51_7 :  std_logic;
signal heap_bh30_w52_6 :  std_logic;
signal CompressorIn_bh30_41_55 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_41_41 :  std_logic_vector(2 downto 0);
signal heap_bh30_w51_8 :  std_logic;
signal heap_bh30_w52_7 :  std_logic;
signal heap_bh30_w53_6 :  std_logic;
signal CompressorIn_bh30_42_56 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_42_42 :  std_logic_vector(2 downto 0);
signal heap_bh30_w52_8 :  std_logic;
signal heap_bh30_w53_7 :  std_logic;
signal heap_bh30_w54_6 :  std_logic;
signal CompressorIn_bh30_43_57 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_43_43 :  std_logic_vector(2 downto 0);
signal heap_bh30_w53_8 :  std_logic;
signal heap_bh30_w54_7 :  std_logic;
signal heap_bh30_w55_6 :  std_logic;
signal CompressorIn_bh30_44_58 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_44_44 :  std_logic_vector(2 downto 0);
signal heap_bh30_w54_8 :  std_logic;
signal heap_bh30_w55_7 :  std_logic;
signal heap_bh30_w56_6 :  std_logic;
signal CompressorIn_bh30_45_59 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_45_45 :  std_logic_vector(2 downto 0);
signal heap_bh30_w55_8 :  std_logic;
signal heap_bh30_w56_7 :  std_logic;
signal heap_bh30_w57_6 :  std_logic;
signal CompressorIn_bh30_46_60 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_46_46 :  std_logic_vector(2 downto 0);
signal heap_bh30_w56_8 :  std_logic;
signal heap_bh30_w57_7 :  std_logic;
signal heap_bh30_w58_6 :  std_logic;
signal CompressorIn_bh30_47_61 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_47_47 :  std_logic_vector(2 downto 0);
signal heap_bh30_w57_8 :  std_logic;
signal heap_bh30_w58_7 :  std_logic;
signal heap_bh30_w59_6 :  std_logic;
signal CompressorIn_bh30_48_62 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_48_48 :  std_logic_vector(2 downto 0);
signal heap_bh30_w58_8 :  std_logic;
signal heap_bh30_w59_7 :  std_logic;
signal heap_bh30_w60_6 :  std_logic;
signal CompressorIn_bh30_49_63 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_49_49 :  std_logic_vector(2 downto 0);
signal heap_bh30_w59_8 :  std_logic;
signal heap_bh30_w60_7 :  std_logic;
signal heap_bh30_w61_6 :  std_logic;
signal CompressorIn_bh30_50_64 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_50_50 :  std_logic_vector(2 downto 0);
signal heap_bh30_w60_8 :  std_logic;
signal heap_bh30_w61_7 :  std_logic;
signal heap_bh30_w62_6 :  std_logic;
signal CompressorIn_bh30_51_65 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_51_51 :  std_logic_vector(2 downto 0);
signal heap_bh30_w61_8 :  std_logic;
signal heap_bh30_w62_7 :  std_logic;
signal heap_bh30_w63_6 :  std_logic;
signal CompressorIn_bh30_52_66 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_52_52 :  std_logic_vector(2 downto 0);
signal heap_bh30_w62_8 :  std_logic;
signal heap_bh30_w63_7 :  std_logic;
signal heap_bh30_w64_6 :  std_logic;
signal CompressorIn_bh30_53_67 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_53_53 :  std_logic_vector(2 downto 0);
signal heap_bh30_w63_8 :  std_logic;
signal heap_bh30_w64_7 :  std_logic;
signal heap_bh30_w65_6 :  std_logic;
signal CompressorIn_bh30_54_68 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_54_54 :  std_logic_vector(2 downto 0);
signal heap_bh30_w64_8 :  std_logic;
signal heap_bh30_w65_7 :  std_logic;
signal heap_bh30_w66_6 :  std_logic;
signal CompressorIn_bh30_55_69 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_55_55 :  std_logic_vector(2 downto 0);
signal heap_bh30_w65_8 :  std_logic;
signal heap_bh30_w66_7 :  std_logic;
signal heap_bh30_w67_5 :  std_logic;
signal CompressorIn_bh30_56_70 :  std_logic_vector(5 downto 0);
signal CompressorOut_bh30_56_56 :  std_logic_vector(2 downto 0);
signal heap_bh30_w66_8 :  std_logic;
signal heap_bh30_w67_6 :  std_logic;
signal heap_bh30_w68_5 :  std_logic;
signal CompressorIn_bh30_57_71 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_57_72 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_57_57 :  std_logic_vector(2 downto 0);
signal heap_bh30_w3_6 :  std_logic;
signal heap_bh30_w4_7 :  std_logic;
signal heap_bh30_w5_9 :  std_logic;
signal CompressorIn_bh30_58_73 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_58_74 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_58_58 :  std_logic_vector(2 downto 0);
signal heap_bh30_w5_10 :  std_logic;
signal heap_bh30_w6_11 :  std_logic;
signal heap_bh30_w7_11 :  std_logic;
signal CompressorIn_bh30_59_75 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_59_76 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_59_59 :  std_logic_vector(2 downto 0);
signal heap_bh30_w7_12 :  std_logic;
signal heap_bh30_w8_13 :  std_logic;
signal heap_bh30_w9_12 :  std_logic;
signal CompressorIn_bh30_60_77 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_60_78 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_60_60 :  std_logic_vector(2 downto 0);
signal heap_bh30_w9_13 :  std_logic;
signal heap_bh30_w10_12 :  std_logic;
signal heap_bh30_w11_12 :  std_logic;
signal CompressorIn_bh30_61_79 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_61_80 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_61_61 :  std_logic_vector(2 downto 0);
signal heap_bh30_w14_10 :  std_logic;
signal heap_bh30_w15_10 :  std_logic;
signal heap_bh30_w16_6 :  std_logic;
signal CompressorIn_bh30_62_81 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_62_82 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_62_62 :  std_logic_vector(2 downto 0);
signal heap_bh30_w16_7 :  std_logic;
signal heap_bh30_w17_5 :  std_logic;
signal heap_bh30_w18_4 :  std_logic;
signal CompressorIn_bh30_63_83 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_63_84 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_63_63 :  std_logic_vector(2 downto 0);
signal heap_bh30_w17_6 :  std_logic;
signal heap_bh30_w18_5 :  std_logic;
signal heap_bh30_w19_4 :  std_logic;
signal CompressorIn_bh30_64_85 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_64_86 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_64_64 :  std_logic_vector(2 downto 0);
signal heap_bh30_w19_5 :  std_logic;
signal heap_bh30_w20_4 :  std_logic;
signal heap_bh30_w21_4 :  std_logic;
signal CompressorIn_bh30_65_87 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_65_88 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_65_65 :  std_logic_vector(2 downto 0);
signal heap_bh30_w21_5 :  std_logic;
signal heap_bh30_w22_4 :  std_logic;
signal heap_bh30_w23_4 :  std_logic;
signal CompressorIn_bh30_66_89 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_66_90 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_66_66 :  std_logic_vector(2 downto 0);
signal heap_bh30_w23_5 :  std_logic;
signal heap_bh30_w24_4 :  std_logic;
signal heap_bh30_w25_4 :  std_logic;
signal CompressorIn_bh30_67_91 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_67_92 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_67_67 :  std_logic_vector(2 downto 0);
signal heap_bh30_w25_5 :  std_logic;
signal heap_bh30_w26_5 :  std_logic;
signal heap_bh30_w27_5 :  std_logic;
signal CompressorIn_bh30_68_93 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_68_94 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_68_68 :  std_logic_vector(2 downto 0);
signal heap_bh30_w26_6 :  std_logic;
signal heap_bh30_w27_6 :  std_logic;
signal heap_bh30_w28_5 :  std_logic;
signal CompressorIn_bh30_69_95 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_69_96 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_69_69 :  std_logic_vector(2 downto 0);
signal heap_bh30_w27_7 :  std_logic;
signal heap_bh30_w28_6 :  std_logic;
signal heap_bh30_w29_7 :  std_logic;
signal CompressorIn_bh30_70_97 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_70_98 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_70_70 :  std_logic_vector(2 downto 0);
signal heap_bh30_w67_7 :  std_logic;
signal heap_bh30_w68_6 :  std_logic;
signal heap_bh30_w69_5 :  std_logic;
signal CompressorIn_bh30_71_99 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_71_100 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_71_71 :  std_logic_vector(2 downto 0);
signal heap_bh30_w68_7 :  std_logic;
signal heap_bh30_w69_6 :  std_logic;
signal heap_bh30_w70_4 :  std_logic;
signal CompressorIn_bh30_72_101 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_72_102 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_72_72 :  std_logic_vector(2 downto 0);
signal heap_bh30_w69_7 :  std_logic;
signal heap_bh30_w70_5 :  std_logic;
signal heap_bh30_w71_4 :  std_logic;
signal CompressorIn_bh30_73_103 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_73_104 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_73_73 :  std_logic_vector(2 downto 0);
signal heap_bh30_w71_5 :  std_logic;
signal heap_bh30_w72_4 :  std_logic;
signal heap_bh30_w73_4 :  std_logic;
signal CompressorIn_bh30_74_105 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_74_106 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_74_74 :  std_logic_vector(2 downto 0);
signal heap_bh30_w73_5 :  std_logic;
signal heap_bh30_w74_4 :  std_logic;
signal heap_bh30_w75_4 :  std_logic;
signal CompressorIn_bh30_75_107 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_75_108 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_75_75 :  std_logic_vector(2 downto 0);
signal heap_bh30_w75_5 :  std_logic;
signal heap_bh30_w76_4 :  std_logic;
signal heap_bh30_w77_4 :  std_logic;
signal CompressorIn_bh30_76_109 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_76_110 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_76_76 :  std_logic_vector(2 downto 0);
signal heap_bh30_w77_5 :  std_logic;
signal heap_bh30_w78_4 :  std_logic;
signal heap_bh30_w79_4 :  std_logic;
signal CompressorIn_bh30_77_111 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_77_112 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_77_77 :  std_logic_vector(2 downto 0);
signal heap_bh30_w79_5 :  std_logic;
signal heap_bh30_w80_4 :  std_logic;
signal heap_bh30_w81_4 :  std_logic;
signal CompressorIn_bh30_78_113 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_78_114 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_78_78 :  std_logic_vector(2 downto 0);
signal heap_bh30_w81_5 :  std_logic;
signal heap_bh30_w82_4 :  std_logic;
signal heap_bh30_w83_4 :  std_logic;
signal CompressorIn_bh30_79_115 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_79_116 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_79_79 :  std_logic_vector(2 downto 0);
signal heap_bh30_w83_5 :  std_logic;
signal heap_bh30_w84_3 :  std_logic;
signal heap_bh30_w85_3 :  std_logic;
signal CompressorIn_bh30_80_117 :  std_logic_vector(3 downto 0);
signal CompressorOut_bh30_80_80 :  std_logic_vector(2 downto 0);
signal heap_bh30_w12_14 :  std_logic;
signal heap_bh30_w13_12 :  std_logic;
signal heap_bh30_w14_11 :  std_logic;
signal CompressorIn_bh30_81_118 :  std_logic_vector(3 downto 0);
signal CompressorOut_bh30_81_81 :  std_logic_vector(2 downto 0);
signal heap_bh30_w28_7 :  std_logic;
signal heap_bh30_w29_8 :  std_logic;
signal heap_bh30_w30_8 :  std_logic;
signal CompressorIn_bh30_82_119 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_82_120 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_82_82 :  std_logic_vector(2 downto 0);
signal heap_bh30_w10_13 :  std_logic;
signal heap_bh30_w11_13 :  std_logic;
signal heap_bh30_w12_15 :  std_logic;
signal CompressorIn_bh30_83_121 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_83_122 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_83_83 :  std_logic_vector(2 downto 0);
signal heap_bh30_w85_4 :  std_logic;
signal heap_bh30_w86_3 :  std_logic;
signal heap_bh30_w87_3 :  std_logic;
signal CompressorIn_bh30_84_123 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_84_124 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_84_84 :  std_logic_vector(2 downto 0);
signal heap_bh30_w87_4 :  std_logic;
signal heap_bh30_w88_3 :  std_logic;
signal heap_bh30_w89_3 :  std_logic;
signal CompressorIn_bh30_85_125 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_85_126 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_85_85 :  std_logic_vector(2 downto 0);
signal heap_bh30_w89_4 :  std_logic;
signal heap_bh30_w90_3 :  std_logic;
signal heap_bh30_w91_3 :  std_logic;
signal CompressorIn_bh30_86_127 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_86_128 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_86_86 :  std_logic_vector(2 downto 0);
signal heap_bh30_w91_4 :  std_logic;
signal heap_bh30_w92_3 :  std_logic;
signal heap_bh30_w93_3 :  std_logic;
signal CompressorIn_bh30_87_129 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_87_130 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_87_87 :  std_logic_vector(2 downto 0);
signal heap_bh30_w93_4 :  std_logic;
signal heap_bh30_w94_2 :  std_logic;
signal heap_bh30_w95_2 :  std_logic;
signal CompressorIn_bh30_88_131 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_88_88 :  std_logic_vector(1 downto 0);
signal heap_bh30_w2_6 :  std_logic;
signal heap_bh30_w3_7 :  std_logic;
signal CompressorIn_bh30_89_132 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_89_89 :  std_logic_vector(1 downto 0);
signal heap_bh30_w4_8 :  std_logic;
signal heap_bh30_w5_11 :  std_logic;
signal CompressorIn_bh30_90_133 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_90_90 :  std_logic_vector(1 downto 0);
signal heap_bh30_w8_14 :  std_logic;
signal heap_bh30_w9_14 :  std_logic;
signal CompressorIn_bh30_91_134 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_91_91 :  std_logic_vector(1 downto 0);
signal heap_bh30_w15_11 :  std_logic;
signal heap_bh30_w16_8 :  std_logic;
signal CompressorIn_bh30_92_135 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_92_92 :  std_logic_vector(1 downto 0);
signal heap_bh30_w18_6 :  std_logic;
signal heap_bh30_w19_6 :  std_logic;
signal CompressorIn_bh30_93_136 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_93_93 :  std_logic_vector(1 downto 0);
signal heap_bh30_w20_5 :  std_logic;
signal heap_bh30_w21_6 :  std_logic;
signal CompressorIn_bh30_94_137 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_94_94 :  std_logic_vector(1 downto 0);
signal heap_bh30_w22_5 :  std_logic;
signal heap_bh30_w23_6 :  std_logic;
signal CompressorIn_bh30_95_138 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_95_95 :  std_logic_vector(1 downto 0);
signal heap_bh30_w24_5 :  std_logic;
signal heap_bh30_w25_6 :  std_logic;
signal CompressorIn_bh30_96_139 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_96_96 :  std_logic_vector(1 downto 0);
signal heap_bh30_w70_6 :  std_logic;
signal heap_bh30_w71_6 :  std_logic;
signal CompressorIn_bh30_97_140 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_97_97 :  std_logic_vector(1 downto 0);
signal heap_bh30_w72_5 :  std_logic;
signal heap_bh30_w73_6 :  std_logic;
signal CompressorIn_bh30_98_141 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_98_98 :  std_logic_vector(1 downto 0);
signal heap_bh30_w74_5 :  std_logic;
signal heap_bh30_w75_6 :  std_logic;
signal CompressorIn_bh30_99_142 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_99_99 :  std_logic_vector(1 downto 0);
signal heap_bh30_w76_5 :  std_logic;
signal heap_bh30_w77_6 :  std_logic;
signal CompressorIn_bh30_100_143 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_100_100 :  std_logic_vector(1 downto 0);
signal heap_bh30_w78_5 :  std_logic;
signal heap_bh30_w79_6 :  std_logic;
signal CompressorIn_bh30_101_144 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_101_101 :  std_logic_vector(1 downto 0);
signal heap_bh30_w80_5 :  std_logic;
signal heap_bh30_w81_6 :  std_logic;
signal CompressorIn_bh30_102_145 :  std_logic_vector(2 downto 0);
signal CompressorOut_bh30_102_102 :  std_logic_vector(1 downto 0);
signal heap_bh30_w82_5 :  std_logic;
signal heap_bh30_w83_6 :  std_logic;
signal CompressorIn_bh30_103_146 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_103_147 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_103_103 :  std_logic_vector(2 downto 0);
signal heap_bh30_w14_12 :  std_logic;
signal heap_bh30_w15_12 :  std_logic;
signal heap_bh30_w16_9 :  std_logic;
signal CompressorIn_bh30_104_148 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_104_149 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_104_104 :  std_logic_vector(2 downto 0);
signal heap_bh30_w67_8 :  std_logic;
signal heap_bh30_w68_8 :  std_logic;
signal heap_bh30_w69_8 :  std_logic;
signal CompressorIn_bh30_105_150 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_105_151 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_105_105 :  std_logic_vector(2 downto 0);
signal heap_bh30_w5_12 :  std_logic;
signal heap_bh30_w6_12 :  std_logic;
signal heap_bh30_w7_13 :  std_logic;
signal CompressorIn_bh30_106_152 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_106_153 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_106_106 :  std_logic_vector(2 downto 0);
signal heap_bh30_w9_15 :  std_logic;
signal heap_bh30_w10_14 :  std_logic;
signal heap_bh30_w11_14 :  std_logic;
signal CompressorIn_bh30_107_154 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_107_155 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_107_107 :  std_logic_vector(2 downto 0);
signal heap_bh30_w11_15 :  std_logic;
signal heap_bh30_w12_16 :  std_logic;
signal heap_bh30_w13_13 :  std_logic;
signal CompressorIn_bh30_108_156 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_108_157 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_108_108 :  std_logic_vector(2 downto 0);
signal heap_bh30_w16_10 :  std_logic;
signal heap_bh30_w17_7 :  std_logic;
signal heap_bh30_w18_7 :  std_logic;
signal CompressorIn_bh30_109_158 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_109_159 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_109_109 :  std_logic_vector(2 downto 0);
signal heap_bh30_w18_8 :  std_logic;
signal heap_bh30_w19_7 :  std_logic;
signal heap_bh30_w20_6 :  std_logic;
signal CompressorIn_bh30_110_160 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_110_161 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_110_110 :  std_logic_vector(2 downto 0);
signal heap_bh30_w21_7 :  std_logic;
signal heap_bh30_w22_6 :  std_logic;
signal heap_bh30_w23_7 :  std_logic;
signal CompressorIn_bh30_111_162 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_111_163 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_111_111 :  std_logic_vector(2 downto 0);
signal heap_bh30_w23_8 :  std_logic;
signal heap_bh30_w24_6 :  std_logic;
signal heap_bh30_w25_7 :  std_logic;
signal CompressorIn_bh30_112_164 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_112_165 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_112_112 :  std_logic_vector(2 downto 0);
signal heap_bh30_w25_8 :  std_logic;
signal heap_bh30_w26_7 :  std_logic;
signal heap_bh30_w27_8 :  std_logic;
signal CompressorIn_bh30_113_166 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_113_167 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_113_113 :  std_logic_vector(2 downto 0);
signal heap_bh30_w27_9 :  std_logic;
signal heap_bh30_w28_8 :  std_logic;
signal heap_bh30_w29_9 :  std_logic;
signal CompressorIn_bh30_114_168 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_114_169 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_114_114 :  std_logic_vector(2 downto 0);
signal heap_bh30_w29_10 :  std_logic;
signal heap_bh30_w30_9 :  std_logic;
signal heap_bh30_w31_9 :  std_logic;
signal CompressorIn_bh30_115_170 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_115_171 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_115_115 :  std_logic_vector(2 downto 0);
signal heap_bh30_w31_10 :  std_logic;
signal heap_bh30_w32_9 :  std_logic;
signal heap_bh30_w33_9 :  std_logic;
signal CompressorIn_bh30_116_172 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_116_173 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_116_116 :  std_logic_vector(2 downto 0);
signal heap_bh30_w33_10 :  std_logic;
signal heap_bh30_w34_9 :  std_logic;
signal heap_bh30_w35_9 :  std_logic;
signal CompressorIn_bh30_117_174 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_117_175 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_117_117 :  std_logic_vector(2 downto 0);
signal heap_bh30_w35_10 :  std_logic;
signal heap_bh30_w36_9 :  std_logic;
signal heap_bh30_w37_9 :  std_logic;
signal CompressorIn_bh30_118_176 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_118_177 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_118_118 :  std_logic_vector(2 downto 0);
signal heap_bh30_w37_10 :  std_logic;
signal heap_bh30_w38_9 :  std_logic;
signal heap_bh30_w39_9 :  std_logic;
signal CompressorIn_bh30_119_178 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_119_179 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_119_119 :  std_logic_vector(2 downto 0);
signal heap_bh30_w39_10 :  std_logic;
signal heap_bh30_w40_9 :  std_logic;
signal heap_bh30_w41_9 :  std_logic;
signal CompressorIn_bh30_120_180 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_120_181 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_120_120 :  std_logic_vector(2 downto 0);
signal heap_bh30_w41_10 :  std_logic;
signal heap_bh30_w42_9 :  std_logic;
signal heap_bh30_w43_9 :  std_logic;
signal CompressorIn_bh30_121_182 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_121_183 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_121_121 :  std_logic_vector(2 downto 0);
signal heap_bh30_w43_10 :  std_logic;
signal heap_bh30_w44_9 :  std_logic;
signal heap_bh30_w45_9 :  std_logic;
signal CompressorIn_bh30_122_184 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_122_185 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_122_122 :  std_logic_vector(2 downto 0);
signal heap_bh30_w45_10 :  std_logic;
signal heap_bh30_w46_9 :  std_logic;
signal heap_bh30_w47_9 :  std_logic;
signal CompressorIn_bh30_123_186 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_123_187 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_123_123 :  std_logic_vector(2 downto 0);
signal heap_bh30_w47_10 :  std_logic;
signal heap_bh30_w48_9 :  std_logic;
signal heap_bh30_w49_9 :  std_logic;
signal CompressorIn_bh30_124_188 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_124_189 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_124_124 :  std_logic_vector(2 downto 0);
signal heap_bh30_w49_10 :  std_logic;
signal heap_bh30_w50_9 :  std_logic;
signal heap_bh30_w51_9 :  std_logic;
signal CompressorIn_bh30_125_190 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_125_191 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_125_125 :  std_logic_vector(2 downto 0);
signal heap_bh30_w51_10 :  std_logic;
signal heap_bh30_w52_9 :  std_logic;
signal heap_bh30_w53_9 :  std_logic;
signal CompressorIn_bh30_126_192 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_126_193 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_126_126 :  std_logic_vector(2 downto 0);
signal heap_bh30_w53_10 :  std_logic;
signal heap_bh30_w54_9 :  std_logic;
signal heap_bh30_w55_9 :  std_logic;
signal CompressorIn_bh30_127_194 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_127_195 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_127_127 :  std_logic_vector(2 downto 0);
signal heap_bh30_w55_10 :  std_logic;
signal heap_bh30_w56_9 :  std_logic;
signal heap_bh30_w57_9 :  std_logic;
signal CompressorIn_bh30_128_196 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_128_197 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_128_128 :  std_logic_vector(2 downto 0);
signal heap_bh30_w57_10 :  std_logic;
signal heap_bh30_w58_9 :  std_logic;
signal heap_bh30_w59_9 :  std_logic;
signal CompressorIn_bh30_129_198 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_129_199 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_129_129 :  std_logic_vector(2 downto 0);
signal heap_bh30_w59_10 :  std_logic;
signal heap_bh30_w60_9 :  std_logic;
signal heap_bh30_w61_9 :  std_logic;
signal CompressorIn_bh30_130_200 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_130_201 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_130_130 :  std_logic_vector(2 downto 0);
signal heap_bh30_w61_10 :  std_logic;
signal heap_bh30_w62_9 :  std_logic;
signal heap_bh30_w63_9 :  std_logic;
signal CompressorIn_bh30_131_202 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_131_203 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_131_131 :  std_logic_vector(2 downto 0);
signal heap_bh30_w63_10 :  std_logic;
signal heap_bh30_w64_9 :  std_logic;
signal heap_bh30_w65_9 :  std_logic;
signal CompressorIn_bh30_132_204 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_132_205 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_132_132 :  std_logic_vector(2 downto 0);
signal heap_bh30_w65_10 :  std_logic;
signal heap_bh30_w66_9 :  std_logic;
signal heap_bh30_w67_9 :  std_logic;
signal CompressorIn_bh30_133_206 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_133_207 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_133_133 :  std_logic_vector(2 downto 0);
signal heap_bh30_w69_9 :  std_logic;
signal heap_bh30_w70_7 :  std_logic;
signal heap_bh30_w71_7 :  std_logic;
signal CompressorIn_bh30_134_208 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_134_209 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_134_134 :  std_logic_vector(2 downto 0);
signal heap_bh30_w71_8 :  std_logic;
signal heap_bh30_w72_6 :  std_logic;
signal heap_bh30_w73_7 :  std_logic;
signal CompressorIn_bh30_135_210 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_135_211 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_135_135 :  std_logic_vector(2 downto 0);
signal heap_bh30_w73_8 :  std_logic;
signal heap_bh30_w74_6 :  std_logic;
signal heap_bh30_w75_7 :  std_logic;
signal CompressorIn_bh30_136_212 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_136_213 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_136_136 :  std_logic_vector(2 downto 0);
signal heap_bh30_w75_8 :  std_logic;
signal heap_bh30_w76_6 :  std_logic;
signal heap_bh30_w77_7 :  std_logic;
signal CompressorIn_bh30_137_214 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_137_215 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_137_137 :  std_logic_vector(2 downto 0);
signal heap_bh30_w77_8 :  std_logic;
signal heap_bh30_w78_6 :  std_logic;
signal heap_bh30_w79_7 :  std_logic;
signal CompressorIn_bh30_138_216 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_138_217 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_138_138 :  std_logic_vector(2 downto 0);
signal heap_bh30_w79_8 :  std_logic;
signal heap_bh30_w80_6 :  std_logic;
signal heap_bh30_w81_7 :  std_logic;
signal CompressorIn_bh30_139_218 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_139_219 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_139_139 :  std_logic_vector(2 downto 0);
signal heap_bh30_w81_8 :  std_logic;
signal heap_bh30_w82_6 :  std_logic;
signal heap_bh30_w83_7 :  std_logic;
signal CompressorIn_bh30_140_220 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_140_221 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_140_140 :  std_logic_vector(2 downto 0);
signal heap_bh30_w83_8 :  std_logic;
signal heap_bh30_w84_4 :  std_logic;
signal heap_bh30_w85_5 :  std_logic;
signal CompressorIn_bh30_141_222 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_141_223 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_141_141 :  std_logic_vector(2 downto 0);
signal heap_bh30_w95_3 :  std_logic;
signal heap_bh30_w96_2 :  std_logic;
signal heap_bh30_w97_2 :  std_logic;
signal CompressorIn_bh30_142_224 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_142_225 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_142_142 :  std_logic_vector(2 downto 0);
signal heap_bh30_w7_14 :  std_logic;
signal heap_bh30_w8_15 :  std_logic;
signal heap_bh30_w9_16 :  std_logic;
signal CompressorIn_bh30_143_226 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_143_227 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_143_143 :  std_logic_vector(2 downto 0);
signal heap_bh30_w15_13 :  std_logic;
signal heap_bh30_w16_11 :  std_logic;
signal heap_bh30_w17_8 :  std_logic;
signal CompressorIn_bh30_144_228 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_144_229 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_144_144 :  std_logic_vector(2 downto 0);
signal heap_bh30_w68_9 :  std_logic;
signal heap_bh30_w69_10 :  std_logic;
signal heap_bh30_w70_8 :  std_logic;
signal CompressorIn_bh30_145_230 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_145_231 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_145_145 :  std_logic_vector(2 downto 0);
signal heap_bh30_w85_6 :  std_logic;
signal heap_bh30_w86_4 :  std_logic;
signal heap_bh30_w87_5 :  std_logic;
signal CompressorIn_bh30_146_232 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_146_233 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_146_146 :  std_logic_vector(2 downto 0);
signal heap_bh30_w97_3 :  std_logic;
signal heap_bh30_w98_2 :  std_logic;
signal heap_bh30_w99_2 :  std_logic;
signal CompressorIn_bh30_147_234 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_147_235 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_147_147 :  std_logic_vector(2 downto 0);
signal heap_bh30_w13_14 :  std_logic;
signal heap_bh30_w14_13 :  std_logic;
signal heap_bh30_w15_14 :  std_logic;
signal CompressorIn_bh30_148_236 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_148_237 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_148_148 :  std_logic_vector(2 downto 0);
signal heap_bh30_w20_7 :  std_logic;
signal heap_bh30_w21_8 :  std_logic;
signal heap_bh30_w22_7 :  std_logic;
signal CompressorIn_bh30_149_238 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_149_239 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_149_149 :  std_logic_vector(2 downto 0);
signal heap_bh30_w70_9 :  std_logic;
signal heap_bh30_w71_9 :  std_logic;
signal heap_bh30_w72_7 :  std_logic;
signal CompressorIn_bh30_150_240 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_150_241 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_150_150 :  std_logic_vector(2 downto 0);
signal heap_bh30_w87_6 :  std_logic;
signal heap_bh30_w88_4 :  std_logic;
signal heap_bh30_w89_5 :  std_logic;
signal CompressorIn_bh30_151_242 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_151_243 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_151_151 :  std_logic_vector(2 downto 0);
signal heap_bh30_w99_3 :  std_logic;
signal heap_bh30_w100_2 :  std_logic;
signal heap_bh30_w101_1 :  std_logic;
signal CompressorIn_bh30_152_244 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_152_245 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_152_152 :  std_logic_vector(2 downto 0);
signal heap_bh30_w89_6 :  std_logic;
signal heap_bh30_w90_4 :  std_logic;
signal heap_bh30_w91_5 :  std_logic;
signal CompressorIn_bh30_153_246 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_153_247 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_153_153 :  std_logic_vector(2 downto 0);
signal heap_bh30_w91_6 :  std_logic;
signal heap_bh30_w92_4 :  std_logic;
signal heap_bh30_w93_5 :  std_logic;
signal CompressorIn_bh30_154_248 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_154_249 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_154_154 :  std_logic_vector(2 downto 0);
signal heap_bh30_w93_6 :  std_logic;
signal heap_bh30_w94_3 :  std_logic;
signal heap_bh30_w95_4 :  std_logic;
signal finalAdderIn0_bh30 :  std_logic_vector(118 downto 0);
signal finalAdderIn1_bh30 :  std_logic_vector(118 downto 0);
signal finalAdderCin_bh30 :  std_logic;
signal finalAdderOut_bh30 :  std_logic_vector(118 downto 0);
signal CompressionResult30 :  std_logic_vector(118 downto 0);
attribute rom_extract: string;
attribute rom_style: string;
attribute rom_extract of SmallMultTableP3x3r6XuYu_comb_uid33: component is "yes";
attribute rom_style of SmallMultTableP3x3r6XuYu_comb_uid33: component is "distributed";
begin
   XX_m29 <= X ;
   YY_m29 <= Y ;
   -- code generated by IntMultiplier::buildHeapLogicOnly()
   -- buildheaplogiconly called for lsbX=0 lsbY=0 msbX=11 msbY=8
   Xp_m29b31 <= XX_m29(10 downto 0) & "0";
   Yp_m29b31 <= YY_m29(7 downto 0) & "0";
   x_m29b31_0 <= Xp_m29b31(2 downto 0);
   x_m29b31_1 <= Xp_m29b31(5 downto 3);
   x_m29b31_2 <= Xp_m29b31(8 downto 6);
   x_m29b31_3 <= Xp_m29b31(11 downto 9);
   y_m29b31_0 <= Yp_m29b31(2 downto 0);
   y_m29b31_1 <= Yp_m29b31(5 downto 3);
   y_m29b31_2 <= Yp_m29b31(8 downto 6);
   -- Partial product row number 0
   Y0X0_31_m29 <= y_m29b31_0 & x_m29b31_0;
   PP_m29_31X0Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X0_31_m29,
                 Y => PP31X0Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w0_0 <= PP31X0Y0_m29(2); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w1_0 <= PP31X0Y0_m29(3); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w2_0 <= PP31X0Y0_m29(4); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w3_0 <= PP31X0Y0_m29(5); -- cycle= 0 cp= 5.5688e-10

   Y0X1_31_m29 <= y_m29b31_0 & x_m29b31_1;
   PP_m29_31X1Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X1_31_m29,
                 Y => PP31X1Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w2_1 <= PP31X1Y0_m29(1); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w3_1 <= PP31X1Y0_m29(2); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w4_0 <= PP31X1Y0_m29(3); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w5_0 <= PP31X1Y0_m29(4); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w6_0 <= PP31X1Y0_m29(5); -- cycle= 0 cp= 5.5688e-10

   Y0X2_31_m29 <= y_m29b31_0 & x_m29b31_2;
   PP_m29_31X2Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X2_31_m29,
                 Y => PP31X2Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w5_1 <= PP31X2Y0_m29(1); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w6_1 <= PP31X2Y0_m29(2); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w7_0 <= PP31X2Y0_m29(3); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w8_0 <= PP31X2Y0_m29(4); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w9_0 <= PP31X2Y0_m29(5); -- cycle= 0 cp= 5.5688e-10

   Y0X3_31_m29 <= y_m29b31_0 & x_m29b31_3;
   PP_m29_31X3Y0_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y0X3_31_m29,
                 Y => PP31X3Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w8_1 <= PP31X3Y0_m29(1); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w9_1 <= PP31X3Y0_m29(2); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w10_0 <= PP31X3Y0_m29(3); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w11_0 <= PP31X3Y0_m29(4); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w12_0 <= PP31X3Y0_m29(5); -- cycle= 0 cp= 5.5688e-10

   -- Partial product row number 1
   Y1X0_31_m29 <= y_m29b31_1 & x_m29b31_0;
   PP_m29_31X0Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X0_31_m29,
                 Y => PP31X0Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w2_2 <= PP31X0Y1_m29(1); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w3_2 <= PP31X0Y1_m29(2); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w4_1 <= PP31X0Y1_m29(3); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w5_2 <= PP31X0Y1_m29(4); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w6_2 <= PP31X0Y1_m29(5); -- cycle= 0 cp= 5.5688e-10

   Y1X1_31_m29 <= y_m29b31_1 & x_m29b31_1;
   PP_m29_31X1Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X1_31_m29,
                 Y => PP31X1Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w4_2 <= PP31X1Y1_m29(0); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w5_3 <= PP31X1Y1_m29(1); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w6_3 <= PP31X1Y1_m29(2); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w7_1 <= PP31X1Y1_m29(3); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w8_2 <= PP31X1Y1_m29(4); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w9_2 <= PP31X1Y1_m29(5); -- cycle= 0 cp= 5.5688e-10

   Y1X2_31_m29 <= y_m29b31_1 & x_m29b31_2;
   PP_m29_31X2Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X2_31_m29,
                 Y => PP31X2Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w7_2 <= PP31X2Y1_m29(0); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w8_3 <= PP31X2Y1_m29(1); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w9_3 <= PP31X2Y1_m29(2); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w10_1 <= PP31X2Y1_m29(3); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w11_1 <= PP31X2Y1_m29(4); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w12_1 <= PP31X2Y1_m29(5); -- cycle= 0 cp= 5.5688e-10

   Y1X3_31_m29 <= y_m29b31_1 & x_m29b31_3;
   PP_m29_31X3Y1_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y1X3_31_m29,
                 Y => PP31X3Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w10_2 <= PP31X3Y1_m29(0); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w11_2 <= PP31X3Y1_m29(1); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w12_2 <= PP31X3Y1_m29(2); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w13_0 <= PP31X3Y1_m29(3); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w14_0 <= PP31X3Y1_m29(4); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w15_0 <= PP31X3Y1_m29(5); -- cycle= 0 cp= 5.5688e-10

   -- Partial product row number 2
   Y2X0_31_m29 <= y_m29b31_2 & x_m29b31_0;
   PP_m29_31X0Y2_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y2X0_31_m29,
                 Y => PP31X0Y2_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w5_4 <= PP31X0Y2_m29(1); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w6_4 <= PP31X0Y2_m29(2); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w7_3 <= PP31X0Y2_m29(3); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w8_4 <= PP31X0Y2_m29(4); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w9_4 <= PP31X0Y2_m29(5); -- cycle= 0 cp= 5.5688e-10

   Y2X1_31_m29 <= y_m29b31_2 & x_m29b31_1;
   PP_m29_31X1Y2_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y2X1_31_m29,
                 Y => PP31X1Y2_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w7_4 <= PP31X1Y2_m29(0); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w8_5 <= PP31X1Y2_m29(1); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w9_5 <= PP31X1Y2_m29(2); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w10_3 <= PP31X1Y2_m29(3); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w11_3 <= PP31X1Y2_m29(4); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w12_3 <= PP31X1Y2_m29(5); -- cycle= 0 cp= 5.5688e-10

   Y2X2_31_m29 <= y_m29b31_2 & x_m29b31_2;
   PP_m29_31X2Y2_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y2X2_31_m29,
                 Y => PP31X2Y2_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w10_4 <= PP31X2Y2_m29(0); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w11_4 <= PP31X2Y2_m29(1); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w12_4 <= PP31X2Y2_m29(2); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w13_1 <= PP31X2Y2_m29(3); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w14_1 <= PP31X2Y2_m29(4); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w15_1 <= PP31X2Y2_m29(5); -- cycle= 0 cp= 5.5688e-10

   Y2X3_31_m29 <= y_m29b31_2 & x_m29b31_3;
   PP_m29_31X3Y2_Tbl: SmallMultTableP3x3r6XuYu_comb_uid33
      port map ( X => Y2X3_31_m29,
                 Y => PP31X3Y2_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w13_2 <= PP31X3Y2_m29(0); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w14_2 <= PP31X3Y2_m29(1); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w15_2 <= PP31X3Y2_m29(2); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w16_0 <= PP31X3Y2_m29(3); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w17_0 <= PP31X3Y2_m29(4); -- cycle= 0 cp= 5.5688e-10
   heap_bh30_w18_0 <= PP31X3Y2_m29(5); -- cycle= 0 cp= 5.5688e-10

   
   -- Beginning of code generated by BitHeap::generateCompressorVHDL
   -- code generated by BitHeap::generateSupertileVHDL()
   DSP_bh30_ch0_0 <= std_logic_vector(unsigned("" & XX_m29(58 downto 35) & "") * unsigned("" & YY_m29(58 downto 42) & ""));
   heap_bh30_w117_0 <= DSP_bh30_ch0_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w116_0 <= DSP_bh30_ch0_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w115_0 <= DSP_bh30_ch0_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w114_0 <= DSP_bh30_ch0_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w113_0 <= DSP_bh30_ch0_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w112_0 <= DSP_bh30_ch0_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w111_0 <= DSP_bh30_ch0_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w110_0 <= DSP_bh30_ch0_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w109_0 <= DSP_bh30_ch0_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w108_0 <= DSP_bh30_ch0_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w107_0 <= DSP_bh30_ch0_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w106_0 <= DSP_bh30_ch0_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w105_0 <= DSP_bh30_ch0_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w104_0 <= DSP_bh30_ch0_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w103_0 <= DSP_bh30_ch0_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w102_0 <= DSP_bh30_ch0_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w101_0 <= DSP_bh30_ch0_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w100_0 <= DSP_bh30_ch0_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w99_0 <= DSP_bh30_ch0_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w98_0 <= DSP_bh30_ch0_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w97_0 <= DSP_bh30_ch0_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w96_0 <= DSP_bh30_ch0_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w95_0 <= DSP_bh30_ch0_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w94_0 <= DSP_bh30_ch0_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w93_0 <= DSP_bh30_ch0_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w92_0 <= DSP_bh30_ch0_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w91_0 <= DSP_bh30_ch0_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w90_0 <= DSP_bh30_ch0_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w89_0 <= DSP_bh30_ch0_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w88_0 <= DSP_bh30_ch0_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w87_0 <= DSP_bh30_ch0_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w86_0 <= DSP_bh30_ch0_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w85_0 <= DSP_bh30_ch0_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w84_0 <= DSP_bh30_ch0_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w83_0 <= DSP_bh30_ch0_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w82_0 <= DSP_bh30_ch0_0(5); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w81_0 <= DSP_bh30_ch0_0(4); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w80_0 <= DSP_bh30_ch0_0(3); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w79_0 <= DSP_bh30_ch0_0(2); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w78_0 <= DSP_bh30_ch0_0(1); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w77_0 <= DSP_bh30_ch0_0(0); -- cycle= 0 cp= 2.387e-09
   DSP_bh30_ch1_0 <= std_logic_vector(unsigned("" & XX_m29(34 downto 11) & "") * unsigned("" & YY_m29(58 downto 42) & ""));
   heap_bh30_w93_1 <= DSP_bh30_ch1_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w92_1 <= DSP_bh30_ch1_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w91_1 <= DSP_bh30_ch1_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w90_1 <= DSP_bh30_ch1_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w89_1 <= DSP_bh30_ch1_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w88_1 <= DSP_bh30_ch1_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w87_1 <= DSP_bh30_ch1_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w86_1 <= DSP_bh30_ch1_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w85_1 <= DSP_bh30_ch1_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w84_1 <= DSP_bh30_ch1_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w83_1 <= DSP_bh30_ch1_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w82_1 <= DSP_bh30_ch1_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w81_1 <= DSP_bh30_ch1_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w80_1 <= DSP_bh30_ch1_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w79_1 <= DSP_bh30_ch1_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w78_1 <= DSP_bh30_ch1_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w77_1 <= DSP_bh30_ch1_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w76_0 <= DSP_bh30_ch1_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w75_0 <= DSP_bh30_ch1_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w74_0 <= DSP_bh30_ch1_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w73_0 <= DSP_bh30_ch1_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w72_0 <= DSP_bh30_ch1_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w71_0 <= DSP_bh30_ch1_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w70_0 <= DSP_bh30_ch1_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w69_0 <= DSP_bh30_ch1_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w68_0 <= DSP_bh30_ch1_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w67_0 <= DSP_bh30_ch1_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w66_0 <= DSP_bh30_ch1_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w65_0 <= DSP_bh30_ch1_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w64_0 <= DSP_bh30_ch1_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w63_0 <= DSP_bh30_ch1_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w62_0 <= DSP_bh30_ch1_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w61_0 <= DSP_bh30_ch1_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w60_0 <= DSP_bh30_ch1_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w59_0 <= DSP_bh30_ch1_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w58_0 <= DSP_bh30_ch1_0(5); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w57_0 <= DSP_bh30_ch1_0(4); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w56_0 <= DSP_bh30_ch1_0(3); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w55_0 <= DSP_bh30_ch1_0(2); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w54_0 <= DSP_bh30_ch1_0(1); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w53_0 <= DSP_bh30_ch1_0(0); -- cycle= 0 cp= 2.387e-09
   DSP_bh30_ch2_0 <= std_logic_vector(unsigned("" & XX_m29(10 downto 0) & "0000000000000") * unsigned("" & YY_m29(58 downto 42) & ""));
   heap_bh30_w69_1 <= DSP_bh30_ch2_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w68_1 <= DSP_bh30_ch2_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w67_1 <= DSP_bh30_ch2_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w66_1 <= DSP_bh30_ch2_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w65_1 <= DSP_bh30_ch2_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w64_1 <= DSP_bh30_ch2_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w63_1 <= DSP_bh30_ch2_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w62_1 <= DSP_bh30_ch2_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w61_1 <= DSP_bh30_ch2_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w60_1 <= DSP_bh30_ch2_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w59_1 <= DSP_bh30_ch2_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w58_1 <= DSP_bh30_ch2_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w57_1 <= DSP_bh30_ch2_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w56_1 <= DSP_bh30_ch2_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w55_1 <= DSP_bh30_ch2_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w54_1 <= DSP_bh30_ch2_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w53_1 <= DSP_bh30_ch2_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w52_0 <= DSP_bh30_ch2_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w51_0 <= DSP_bh30_ch2_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w50_0 <= DSP_bh30_ch2_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w49_0 <= DSP_bh30_ch2_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w48_0 <= DSP_bh30_ch2_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w47_0 <= DSP_bh30_ch2_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w46_0 <= DSP_bh30_ch2_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w45_0 <= DSP_bh30_ch2_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w44_0 <= DSP_bh30_ch2_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w43_0 <= DSP_bh30_ch2_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w42_0 <= DSP_bh30_ch2_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w41_0 <= DSP_bh30_ch2_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w40_0 <= DSP_bh30_ch2_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w39_0 <= DSP_bh30_ch2_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w38_0 <= DSP_bh30_ch2_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w37_0 <= DSP_bh30_ch2_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w36_0 <= DSP_bh30_ch2_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w35_0 <= DSP_bh30_ch2_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w34_0 <= DSP_bh30_ch2_0(5); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w33_0 <= DSP_bh30_ch2_0(4); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w32_0 <= DSP_bh30_ch2_0(3); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w31_0 <= DSP_bh30_ch2_0(2); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w30_0 <= DSP_bh30_ch2_0(1); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w29_0 <= DSP_bh30_ch2_0(0); -- cycle= 0 cp= 2.387e-09
   DSP_bh30_ch3_0 <= std_logic_vector(unsigned("" & XX_m29(58 downto 35) & "") * unsigned("" & YY_m29(41 downto 25) & ""));
   heap_bh30_w100_1 <= DSP_bh30_ch3_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w99_1 <= DSP_bh30_ch3_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w98_1 <= DSP_bh30_ch3_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w97_1 <= DSP_bh30_ch3_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w96_1 <= DSP_bh30_ch3_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w95_1 <= DSP_bh30_ch3_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w94_1 <= DSP_bh30_ch3_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w93_2 <= DSP_bh30_ch3_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w92_2 <= DSP_bh30_ch3_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w91_2 <= DSP_bh30_ch3_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w90_2 <= DSP_bh30_ch3_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w89_2 <= DSP_bh30_ch3_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w88_2 <= DSP_bh30_ch3_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w87_2 <= DSP_bh30_ch3_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w86_2 <= DSP_bh30_ch3_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w85_2 <= DSP_bh30_ch3_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w84_2 <= DSP_bh30_ch3_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w83_2 <= DSP_bh30_ch3_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w82_2 <= DSP_bh30_ch3_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w81_2 <= DSP_bh30_ch3_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w80_2 <= DSP_bh30_ch3_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w79_2 <= DSP_bh30_ch3_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w78_2 <= DSP_bh30_ch3_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w77_2 <= DSP_bh30_ch3_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w76_1 <= DSP_bh30_ch3_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w75_1 <= DSP_bh30_ch3_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w74_1 <= DSP_bh30_ch3_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w73_1 <= DSP_bh30_ch3_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w72_1 <= DSP_bh30_ch3_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w71_1 <= DSP_bh30_ch3_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w70_1 <= DSP_bh30_ch3_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w69_2 <= DSP_bh30_ch3_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w68_2 <= DSP_bh30_ch3_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w67_2 <= DSP_bh30_ch3_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w66_2 <= DSP_bh30_ch3_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w65_2 <= DSP_bh30_ch3_0(5); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w64_2 <= DSP_bh30_ch3_0(4); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w63_2 <= DSP_bh30_ch3_0(3); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w62_2 <= DSP_bh30_ch3_0(2); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w61_2 <= DSP_bh30_ch3_0(1); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w60_2 <= DSP_bh30_ch3_0(0); -- cycle= 0 cp= 2.387e-09
   DSP_bh30_ch4_0 <= std_logic_vector(unsigned("" & XX_m29(34 downto 11) & "") * unsigned("" & YY_m29(41 downto 25) & ""));
   heap_bh30_w76_2 <= DSP_bh30_ch4_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w75_2 <= DSP_bh30_ch4_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w74_2 <= DSP_bh30_ch4_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w73_2 <= DSP_bh30_ch4_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w72_2 <= DSP_bh30_ch4_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w71_2 <= DSP_bh30_ch4_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w70_2 <= DSP_bh30_ch4_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w69_3 <= DSP_bh30_ch4_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w68_3 <= DSP_bh30_ch4_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w67_3 <= DSP_bh30_ch4_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w66_3 <= DSP_bh30_ch4_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w65_3 <= DSP_bh30_ch4_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w64_3 <= DSP_bh30_ch4_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w63_3 <= DSP_bh30_ch4_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w62_3 <= DSP_bh30_ch4_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w61_3 <= DSP_bh30_ch4_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w60_3 <= DSP_bh30_ch4_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w59_2 <= DSP_bh30_ch4_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w58_2 <= DSP_bh30_ch4_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w57_2 <= DSP_bh30_ch4_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w56_2 <= DSP_bh30_ch4_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w55_2 <= DSP_bh30_ch4_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w54_2 <= DSP_bh30_ch4_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w53_2 <= DSP_bh30_ch4_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w52_1 <= DSP_bh30_ch4_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w51_1 <= DSP_bh30_ch4_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w50_1 <= DSP_bh30_ch4_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w49_1 <= DSP_bh30_ch4_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w48_1 <= DSP_bh30_ch4_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w47_1 <= DSP_bh30_ch4_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w46_1 <= DSP_bh30_ch4_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w45_1 <= DSP_bh30_ch4_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w44_1 <= DSP_bh30_ch4_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w43_1 <= DSP_bh30_ch4_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w42_1 <= DSP_bh30_ch4_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w41_1 <= DSP_bh30_ch4_0(5); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w40_1 <= DSP_bh30_ch4_0(4); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w39_1 <= DSP_bh30_ch4_0(3); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w38_1 <= DSP_bh30_ch4_0(2); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w37_1 <= DSP_bh30_ch4_0(1); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w36_1 <= DSP_bh30_ch4_0(0); -- cycle= 0 cp= 2.387e-09
   DSP_bh30_ch5_0 <= std_logic_vector(unsigned("" & XX_m29(10 downto 0) & "0000000000000") * unsigned("" & YY_m29(41 downto 25) & ""));
   heap_bh30_w52_2 <= DSP_bh30_ch5_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w51_2 <= DSP_bh30_ch5_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w50_2 <= DSP_bh30_ch5_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w49_2 <= DSP_bh30_ch5_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w48_2 <= DSP_bh30_ch5_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w47_2 <= DSP_bh30_ch5_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w46_2 <= DSP_bh30_ch5_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w45_2 <= DSP_bh30_ch5_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w44_2 <= DSP_bh30_ch5_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w43_2 <= DSP_bh30_ch5_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w42_2 <= DSP_bh30_ch5_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w41_2 <= DSP_bh30_ch5_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w40_2 <= DSP_bh30_ch5_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w39_2 <= DSP_bh30_ch5_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w38_2 <= DSP_bh30_ch5_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w37_2 <= DSP_bh30_ch5_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w36_2 <= DSP_bh30_ch5_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w35_1 <= DSP_bh30_ch5_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w34_1 <= DSP_bh30_ch5_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w33_1 <= DSP_bh30_ch5_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w32_1 <= DSP_bh30_ch5_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w31_1 <= DSP_bh30_ch5_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w30_1 <= DSP_bh30_ch5_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w29_1 <= DSP_bh30_ch5_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w28_0 <= DSP_bh30_ch5_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w27_0 <= DSP_bh30_ch5_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w26_0 <= DSP_bh30_ch5_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w25_0 <= DSP_bh30_ch5_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w24_0 <= DSP_bh30_ch5_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w23_0 <= DSP_bh30_ch5_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w22_0 <= DSP_bh30_ch5_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w21_0 <= DSP_bh30_ch5_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w20_0 <= DSP_bh30_ch5_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w19_0 <= DSP_bh30_ch5_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w18_1 <= DSP_bh30_ch5_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w17_1 <= DSP_bh30_ch5_0(5); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w16_1 <= DSP_bh30_ch5_0(4); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w15_3 <= DSP_bh30_ch5_0(3); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w14_3 <= DSP_bh30_ch5_0(2); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w13_3 <= DSP_bh30_ch5_0(1); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w12_5 <= DSP_bh30_ch5_0(0); -- cycle= 0 cp= 2.387e-09
   DSP_bh30_ch6_0 <= std_logic_vector(unsigned("" & XX_m29(58 downto 35) & "") * unsigned("" & YY_m29(24 downto 8) & ""));
   heap_bh30_w83_3 <= DSP_bh30_ch6_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w82_3 <= DSP_bh30_ch6_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w81_3 <= DSP_bh30_ch6_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w80_3 <= DSP_bh30_ch6_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w79_3 <= DSP_bh30_ch6_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w78_3 <= DSP_bh30_ch6_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w77_3 <= DSP_bh30_ch6_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w76_3 <= DSP_bh30_ch6_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w75_3 <= DSP_bh30_ch6_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w74_3 <= DSP_bh30_ch6_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w73_3 <= DSP_bh30_ch6_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w72_3 <= DSP_bh30_ch6_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w71_3 <= DSP_bh30_ch6_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w70_3 <= DSP_bh30_ch6_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w69_4 <= DSP_bh30_ch6_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w68_4 <= DSP_bh30_ch6_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w67_4 <= DSP_bh30_ch6_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w66_4 <= DSP_bh30_ch6_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w65_4 <= DSP_bh30_ch6_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w64_4 <= DSP_bh30_ch6_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w63_4 <= DSP_bh30_ch6_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w62_4 <= DSP_bh30_ch6_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w61_4 <= DSP_bh30_ch6_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w60_4 <= DSP_bh30_ch6_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w59_3 <= DSP_bh30_ch6_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w58_3 <= DSP_bh30_ch6_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w57_3 <= DSP_bh30_ch6_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w56_3 <= DSP_bh30_ch6_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w55_3 <= DSP_bh30_ch6_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w54_3 <= DSP_bh30_ch6_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w53_3 <= DSP_bh30_ch6_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w52_3 <= DSP_bh30_ch6_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w51_3 <= DSP_bh30_ch6_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w50_3 <= DSP_bh30_ch6_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w49_3 <= DSP_bh30_ch6_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w48_3 <= DSP_bh30_ch6_0(5); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w47_3 <= DSP_bh30_ch6_0(4); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w46_3 <= DSP_bh30_ch6_0(3); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w45_3 <= DSP_bh30_ch6_0(2); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w44_3 <= DSP_bh30_ch6_0(1); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w43_3 <= DSP_bh30_ch6_0(0); -- cycle= 0 cp= 2.387e-09
   DSP_bh30_ch7_0 <= std_logic_vector(unsigned("" & XX_m29(34 downto 11) & "") * unsigned("" & YY_m29(24 downto 8) & ""));
   heap_bh30_w59_4 <= DSP_bh30_ch7_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w58_4 <= DSP_bh30_ch7_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w57_4 <= DSP_bh30_ch7_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w56_4 <= DSP_bh30_ch7_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w55_4 <= DSP_bh30_ch7_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w54_4 <= DSP_bh30_ch7_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w53_4 <= DSP_bh30_ch7_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w52_4 <= DSP_bh30_ch7_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w51_4 <= DSP_bh30_ch7_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w50_4 <= DSP_bh30_ch7_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w49_4 <= DSP_bh30_ch7_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w48_4 <= DSP_bh30_ch7_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w47_4 <= DSP_bh30_ch7_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w46_4 <= DSP_bh30_ch7_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w45_4 <= DSP_bh30_ch7_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w44_4 <= DSP_bh30_ch7_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w43_4 <= DSP_bh30_ch7_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w42_3 <= DSP_bh30_ch7_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w41_3 <= DSP_bh30_ch7_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w40_3 <= DSP_bh30_ch7_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w39_3 <= DSP_bh30_ch7_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w38_3 <= DSP_bh30_ch7_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w37_3 <= DSP_bh30_ch7_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w36_3 <= DSP_bh30_ch7_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w35_2 <= DSP_bh30_ch7_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w34_2 <= DSP_bh30_ch7_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w33_2 <= DSP_bh30_ch7_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w32_2 <= DSP_bh30_ch7_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w31_2 <= DSP_bh30_ch7_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w30_2 <= DSP_bh30_ch7_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w29_2 <= DSP_bh30_ch7_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w28_1 <= DSP_bh30_ch7_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w27_1 <= DSP_bh30_ch7_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w26_1 <= DSP_bh30_ch7_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w25_1 <= DSP_bh30_ch7_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w24_1 <= DSP_bh30_ch7_0(5); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w23_1 <= DSP_bh30_ch7_0(4); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w22_1 <= DSP_bh30_ch7_0(3); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w21_1 <= DSP_bh30_ch7_0(2); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w20_1 <= DSP_bh30_ch7_0(1); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w19_1 <= DSP_bh30_ch7_0(0); -- cycle= 0 cp= 2.387e-09
   DSP_bh30_ch8_0 <= std_logic_vector(unsigned("" & XX_m29(10 downto 0) & "0000000000000") * unsigned("" & YY_m29(24 downto 8) & ""));
   heap_bh30_w35_3 <= DSP_bh30_ch8_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w34_3 <= DSP_bh30_ch8_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w33_3 <= DSP_bh30_ch8_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w32_3 <= DSP_bh30_ch8_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w31_3 <= DSP_bh30_ch8_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w30_3 <= DSP_bh30_ch8_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w29_3 <= DSP_bh30_ch8_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w28_2 <= DSP_bh30_ch8_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w27_2 <= DSP_bh30_ch8_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w26_2 <= DSP_bh30_ch8_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w25_2 <= DSP_bh30_ch8_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w24_2 <= DSP_bh30_ch8_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w23_2 <= DSP_bh30_ch8_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w22_2 <= DSP_bh30_ch8_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w21_2 <= DSP_bh30_ch8_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w20_2 <= DSP_bh30_ch8_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w19_2 <= DSP_bh30_ch8_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w18_2 <= DSP_bh30_ch8_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w17_2 <= DSP_bh30_ch8_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w16_2 <= DSP_bh30_ch8_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w15_4 <= DSP_bh30_ch8_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w14_4 <= DSP_bh30_ch8_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w13_4 <= DSP_bh30_ch8_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w12_6 <= DSP_bh30_ch8_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w11_5 <= DSP_bh30_ch8_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w10_5 <= DSP_bh30_ch8_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w9_6 <= DSP_bh30_ch8_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w8_6 <= DSP_bh30_ch8_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w7_5 <= DSP_bh30_ch8_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w6_5 <= DSP_bh30_ch8_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w5_5 <= DSP_bh30_ch8_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w4_3 <= DSP_bh30_ch8_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w3_3 <= DSP_bh30_ch8_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w2_3 <= DSP_bh30_ch8_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w1_1 <= DSP_bh30_ch8_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w0_1 <= DSP_bh30_ch8_0(5); -- cycle= 0 cp= 2.387e-09
   DSP_bh30_ch9_0 <= std_logic_vector(unsigned("" & XX_m29(58 downto 35) & "") * unsigned("" & YY_m29(7 downto 0) & "000000000"));
   heap_bh30_w66_5 <= DSP_bh30_ch9_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w65_5 <= DSP_bh30_ch9_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w64_5 <= DSP_bh30_ch9_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w63_5 <= DSP_bh30_ch9_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w62_5 <= DSP_bh30_ch9_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w61_5 <= DSP_bh30_ch9_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w60_5 <= DSP_bh30_ch9_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w59_5 <= DSP_bh30_ch9_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w58_5 <= DSP_bh30_ch9_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w57_5 <= DSP_bh30_ch9_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w56_5 <= DSP_bh30_ch9_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w55_5 <= DSP_bh30_ch9_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w54_5 <= DSP_bh30_ch9_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w53_5 <= DSP_bh30_ch9_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w52_5 <= DSP_bh30_ch9_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w51_5 <= DSP_bh30_ch9_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w50_5 <= DSP_bh30_ch9_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w49_5 <= DSP_bh30_ch9_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w48_5 <= DSP_bh30_ch9_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w47_5 <= DSP_bh30_ch9_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w46_5 <= DSP_bh30_ch9_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w45_5 <= DSP_bh30_ch9_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w44_5 <= DSP_bh30_ch9_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w43_5 <= DSP_bh30_ch9_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w42_4 <= DSP_bh30_ch9_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w41_4 <= DSP_bh30_ch9_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w40_4 <= DSP_bh30_ch9_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w39_4 <= DSP_bh30_ch9_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w38_4 <= DSP_bh30_ch9_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w37_4 <= DSP_bh30_ch9_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w36_4 <= DSP_bh30_ch9_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w35_4 <= DSP_bh30_ch9_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w34_4 <= DSP_bh30_ch9_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w33_4 <= DSP_bh30_ch9_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w32_4 <= DSP_bh30_ch9_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w31_4 <= DSP_bh30_ch9_0(5); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w30_4 <= DSP_bh30_ch9_0(4); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w29_4 <= DSP_bh30_ch9_0(3); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w28_3 <= DSP_bh30_ch9_0(2); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w27_3 <= DSP_bh30_ch9_0(1); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w26_3 <= DSP_bh30_ch9_0(0); -- cycle= 0 cp= 2.387e-09
   DSP_bh30_ch10_0 <= std_logic_vector(unsigned("" & XX_m29(34 downto 11) & "") * unsigned("" & YY_m29(7 downto 0) & "000000000"));
   heap_bh30_w42_5 <= DSP_bh30_ch10_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w41_5 <= DSP_bh30_ch10_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w40_5 <= DSP_bh30_ch10_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w39_5 <= DSP_bh30_ch10_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w38_5 <= DSP_bh30_ch10_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w37_5 <= DSP_bh30_ch10_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w36_5 <= DSP_bh30_ch10_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w35_5 <= DSP_bh30_ch10_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w34_5 <= DSP_bh30_ch10_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w33_5 <= DSP_bh30_ch10_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w32_5 <= DSP_bh30_ch10_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w31_5 <= DSP_bh30_ch10_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w30_5 <= DSP_bh30_ch10_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w29_5 <= DSP_bh30_ch10_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w28_4 <= DSP_bh30_ch10_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w27_4 <= DSP_bh30_ch10_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w26_4 <= DSP_bh30_ch10_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w25_3 <= DSP_bh30_ch10_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w24_3 <= DSP_bh30_ch10_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w23_3 <= DSP_bh30_ch10_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w22_3 <= DSP_bh30_ch10_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w21_3 <= DSP_bh30_ch10_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w20_3 <= DSP_bh30_ch10_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w19_3 <= DSP_bh30_ch10_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w18_3 <= DSP_bh30_ch10_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w17_3 <= DSP_bh30_ch10_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w16_3 <= DSP_bh30_ch10_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w15_5 <= DSP_bh30_ch10_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w14_5 <= DSP_bh30_ch10_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w13_5 <= DSP_bh30_ch10_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w12_7 <= DSP_bh30_ch10_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w11_6 <= DSP_bh30_ch10_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w10_6 <= DSP_bh30_ch10_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w9_7 <= DSP_bh30_ch10_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w8_7 <= DSP_bh30_ch10_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w7_6 <= DSP_bh30_ch10_0(5); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w6_6 <= DSP_bh30_ch10_0(4); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w5_6 <= DSP_bh30_ch10_0(3); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w4_4 <= DSP_bh30_ch10_0(2); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w3_4 <= DSP_bh30_ch10_0(1); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w2_4 <= DSP_bh30_ch10_0(0); -- cycle= 0 cp= 2.387e-09

   -- Adding the constant bits
      -- All the constant bits are zero, nothing to add


   CompressorIn_bh30_0_0 <= heap_bh30_w8_5 & heap_bh30_w8_4 & heap_bh30_w8_3 & heap_bh30_w8_2 & heap_bh30_w8_1 & heap_bh30_w8_0;
      Compressor_bh30_0: Compressor_6_3
      port map ( R => CompressorOut_bh30_0_0,
                 X0 => CompressorIn_bh30_0_0);
   heap_bh30_w8_8 <= CompressorOut_bh30_0_0(0); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w9_8 <= CompressorOut_bh30_0_0(1); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w10_7 <= CompressorOut_bh30_0_0(2); -- cycle= 0 cp= 1.0876e-09

   CompressorIn_bh30_1_1 <= heap_bh30_w9_5 & heap_bh30_w9_4 & heap_bh30_w9_3 & heap_bh30_w9_2 & heap_bh30_w9_1 & heap_bh30_w9_0;
      Compressor_bh30_1: Compressor_6_3
      port map ( R => CompressorOut_bh30_1_1,
                 X0 => CompressorIn_bh30_1_1);
   heap_bh30_w9_9 <= CompressorOut_bh30_1_1(0); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w10_8 <= CompressorOut_bh30_1_1(1); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w11_7 <= CompressorOut_bh30_1_1(2); -- cycle= 0 cp= 1.0876e-09

   CompressorIn_bh30_2_2 <= heap_bh30_w5_4 & heap_bh30_w5_3 & heap_bh30_w5_2 & heap_bh30_w5_1;
   CompressorIn_bh30_2_3(0) <= heap_bh30_w6_4;
      Compressor_bh30_2: Compressor_14_3
      port map ( R => CompressorOut_bh30_2_2,
                 X0 => CompressorIn_bh30_2_2,
                 X1 => CompressorIn_bh30_2_3);
   heap_bh30_w5_7 <= CompressorOut_bh30_2_2(0); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w6_7 <= CompressorOut_bh30_2_2(1); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w7_7 <= CompressorOut_bh30_2_2(2); -- cycle= 0 cp= 1.0876e-09

   CompressorIn_bh30_3_4 <= heap_bh30_w6_3 & heap_bh30_w6_2 & heap_bh30_w6_1 & heap_bh30_w6_0;
   CompressorIn_bh30_3_5(0) <= heap_bh30_w7_4;
      Compressor_bh30_3: Compressor_14_3
      port map ( R => CompressorOut_bh30_3_3,
                 X0 => CompressorIn_bh30_3_4,
                 X1 => CompressorIn_bh30_3_5);
   heap_bh30_w6_8 <= CompressorOut_bh30_3_3(0); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w7_8 <= CompressorOut_bh30_3_3(1); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w8_9 <= CompressorOut_bh30_3_3(2); -- cycle= 0 cp= 1.0876e-09

   CompressorIn_bh30_4_6 <= heap_bh30_w10_4 & heap_bh30_w10_3 & heap_bh30_w10_2 & heap_bh30_w10_1;
   CompressorIn_bh30_4_7(0) <= heap_bh30_w11_4;
      Compressor_bh30_4: Compressor_14_3
      port map ( R => CompressorOut_bh30_4_4,
                 X0 => CompressorIn_bh30_4_6,
                 X1 => CompressorIn_bh30_4_7);
   heap_bh30_w10_9 <= CompressorOut_bh30_4_4(0); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w11_8 <= CompressorOut_bh30_4_4(1); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w12_8 <= CompressorOut_bh30_4_4(2); -- cycle= 0 cp= 1.0876e-09

   CompressorIn_bh30_5_8 <= heap_bh30_w11_3 & heap_bh30_w11_2 & heap_bh30_w11_1 & heap_bh30_w11_0;
   CompressorIn_bh30_5_9(0) <= heap_bh30_w12_4;
      Compressor_bh30_5: Compressor_14_3
      port map ( R => CompressorOut_bh30_5_5,
                 X0 => CompressorIn_bh30_5_8,
                 X1 => CompressorIn_bh30_5_9);
   heap_bh30_w11_9 <= CompressorOut_bh30_5_5(0); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w12_9 <= CompressorOut_bh30_5_5(1); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w13_6 <= CompressorOut_bh30_5_5(2); -- cycle= 0 cp= 1.0876e-09

   CompressorIn_bh30_6_10 <= heap_bh30_w12_3 & heap_bh30_w12_2 & heap_bh30_w12_1 & heap_bh30_w12_0;
   CompressorIn_bh30_6_11(0) <= heap_bh30_w13_2;
      Compressor_bh30_6: Compressor_14_3
      port map ( R => CompressorOut_bh30_6_6,
                 X0 => CompressorIn_bh30_6_10,
                 X1 => CompressorIn_bh30_6_11);
   heap_bh30_w12_10 <= CompressorOut_bh30_6_6(0); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w13_7 <= CompressorOut_bh30_6_6(1); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w14_6 <= CompressorOut_bh30_6_6(2); -- cycle= 0 cp= 1.0876e-09

   CompressorIn_bh30_7_12 <= heap_bh30_w7_3 & heap_bh30_w7_2 & heap_bh30_w7_1 & heap_bh30_w7_0;
      Compressor_bh30_7: Compressor_4_3
      port map ( R => CompressorOut_bh30_7_7,
                 X0 => CompressorIn_bh30_7_12);
   heap_bh30_w7_9 <= CompressorOut_bh30_7_7(0); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w8_10 <= CompressorOut_bh30_7_7(1); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w9_10 <= CompressorOut_bh30_7_7(2); -- cycle= 0 cp= 1.0876e-09

   CompressorIn_bh30_8_13 <= heap_bh30_w2_2 & heap_bh30_w2_1 & heap_bh30_w2_0;
   CompressorIn_bh30_8_14 <= heap_bh30_w3_2 & heap_bh30_w3_1;
      Compressor_bh30_8: Compressor_23_3
      port map ( R => CompressorOut_bh30_8_8,
                 X0 => CompressorIn_bh30_8_13,
                 X1 => CompressorIn_bh30_8_14);
   heap_bh30_w2_5 <= CompressorOut_bh30_8_8(0); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w3_5 <= CompressorOut_bh30_8_8(1); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w4_5 <= CompressorOut_bh30_8_8(2); -- cycle= 0 cp= 1.0876e-09

   CompressorIn_bh30_9_15 <= heap_bh30_w14_2 & heap_bh30_w14_1 & heap_bh30_w14_0;
   CompressorIn_bh30_9_16 <= heap_bh30_w15_2 & heap_bh30_w15_1;
      Compressor_bh30_9: Compressor_23_3
      port map ( R => CompressorOut_bh30_9_9,
                 X0 => CompressorIn_bh30_9_15,
                 X1 => CompressorIn_bh30_9_16);
   heap_bh30_w14_7 <= CompressorOut_bh30_9_9(0); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w15_6 <= CompressorOut_bh30_9_9(1); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w16_4 <= CompressorOut_bh30_9_9(2); -- cycle= 0 cp= 1.0876e-09

   CompressorIn_bh30_10_17 <= heap_bh30_w4_2 & heap_bh30_w4_1 & heap_bh30_w4_0;
   CompressorIn_bh30_10_18(0) <= heap_bh30_w5_0;
      Compressor_bh30_10: Compressor_13_3
      port map ( R => CompressorOut_bh30_10_10,
                 X0 => CompressorIn_bh30_10_17,
                 X1 => CompressorIn_bh30_10_18);
   heap_bh30_w4_6 <= CompressorOut_bh30_10_10(0); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w5_8 <= CompressorOut_bh30_10_10(1); -- cycle= 0 cp= 1.0876e-09
   heap_bh30_w6_9 <= CompressorOut_bh30_10_10(2); -- cycle= 0 cp= 1.0876e-09

   CompressorIn_bh30_11_19 <= heap_bh30_w10_0 & heap_bh30_w10_9 & heap_bh30_w10_8 & heap_bh30_w10_7;
   CompressorIn_bh30_11_20(0) <= heap_bh30_w11_9;
      Compressor_bh30_11: Compressor_14_3
      port map ( R => CompressorOut_bh30_11_11,
                 X0 => CompressorIn_bh30_11_19,
                 X1 => CompressorIn_bh30_11_20);
   heap_bh30_w10_10 <= CompressorOut_bh30_11_11(0); -- cycle= 0 cp= 1.61832e-09
   heap_bh30_w11_10 <= CompressorOut_bh30_11_11(1); -- cycle= 0 cp= 1.61832e-09
   heap_bh30_w12_11 <= CompressorOut_bh30_11_11(2); -- cycle= 0 cp= 1.61832e-09

   CompressorIn_bh30_12_21 <= heap_bh30_w13_1 & heap_bh30_w13_0 & heap_bh30_w13_7 & heap_bh30_w13_6;
   CompressorIn_bh30_12_22(0) <= heap_bh30_w14_7;
      Compressor_bh30_12: Compressor_14_3
      port map ( R => CompressorOut_bh30_12_12,
                 X0 => CompressorIn_bh30_12_21,
                 X1 => CompressorIn_bh30_12_22);
   heap_bh30_w13_8 <= CompressorOut_bh30_12_12(0); -- cycle= 0 cp= 1.61832e-09
   heap_bh30_w14_8 <= CompressorOut_bh30_12_12(1); -- cycle= 0 cp= 1.61832e-09
   heap_bh30_w15_7 <= CompressorOut_bh30_12_12(2); -- cycle= 0 cp= 1.61832e-09

   CompressorIn_bh30_13_23 <= heap_bh30_w6_9 & heap_bh30_w6_8 & heap_bh30_w6_7;
   CompressorIn_bh30_13_24 <= heap_bh30_w7_9 & heap_bh30_w7_8;
      Compressor_bh30_13: Compressor_23_3
      port map ( R => CompressorOut_bh30_13_13,
                 X0 => CompressorIn_bh30_13_23,
                 X1 => CompressorIn_bh30_13_24);
   heap_bh30_w6_10 <= CompressorOut_bh30_13_13(0); -- cycle= 0 cp= 1.61832e-09
   heap_bh30_w7_10 <= CompressorOut_bh30_13_13(1); -- cycle= 0 cp= 1.61832e-09
   heap_bh30_w8_11 <= CompressorOut_bh30_13_13(2); -- cycle= 0 cp= 1.61832e-09

   CompressorIn_bh30_14_25 <= heap_bh30_w8_10 & heap_bh30_w8_9 & heap_bh30_w8_8;
   CompressorIn_bh30_14_26 <= heap_bh30_w9_10 & heap_bh30_w9_9;
      Compressor_bh30_14: Compressor_23_3
      port map ( R => CompressorOut_bh30_14_14,
                 X0 => CompressorIn_bh30_14_25,
                 X1 => CompressorIn_bh30_14_26);
   heap_bh30_w8_12 <= CompressorOut_bh30_14_14(0); -- cycle= 0 cp= 1.61832e-09
   heap_bh30_w9_11 <= CompressorOut_bh30_14_14(1); -- cycle= 0 cp= 1.61832e-09
   heap_bh30_w10_11 <= CompressorOut_bh30_14_14(2); -- cycle= 0 cp= 1.61832e-09

   CompressorIn_bh30_15_27 <= heap_bh30_w12_10 & heap_bh30_w12_9 & heap_bh30_w12_8;
      Compressor_bh30_15: Compressor_3_2
      port map ( R => CompressorOut_bh30_15_15,
                 X0 => CompressorIn_bh30_15_27);
   heap_bh30_w12_12 <= CompressorOut_bh30_15_15(0); -- cycle= 0 cp= 1.61832e-09
   heap_bh30_w13_9 <= CompressorOut_bh30_15_15(1); -- cycle= 0 cp= 1.61832e-09

   CompressorIn_bh30_16_28 <= heap_bh30_w11_8 & heap_bh30_w11_7 & heap_bh30_w11_10;
   CompressorIn_bh30_16_29 <= heap_bh30_w12_12 & heap_bh30_w12_11;
      Compressor_bh30_16: Compressor_23_3
      port map ( R => CompressorOut_bh30_16_16,
                 X0 => CompressorIn_bh30_16_28,
                 X1 => CompressorIn_bh30_16_29);
   heap_bh30_w11_11 <= CompressorOut_bh30_16_16(0); -- cycle= 0 cp= 2.14904e-09
   heap_bh30_w12_13 <= CompressorOut_bh30_16_16(1); -- cycle= 0 cp= 2.14904e-09
   heap_bh30_w13_10 <= CompressorOut_bh30_16_16(2); -- cycle= 0 cp= 2.14904e-09

   CompressorIn_bh30_17_30 <= heap_bh30_w15_0 & heap_bh30_w15_6 & heap_bh30_w15_7;
   CompressorIn_bh30_17_31 <= heap_bh30_w16_0 & heap_bh30_w16_4;
      Compressor_bh30_17: Compressor_23_3
      port map ( R => CompressorOut_bh30_17_17,
                 X0 => CompressorIn_bh30_17_30,
                 X1 => CompressorIn_bh30_17_31);
   heap_bh30_w15_8 <= CompressorOut_bh30_17_17(0); -- cycle= 0 cp= 2.14904e-09
   heap_bh30_w16_5 <= CompressorOut_bh30_17_17(1); -- cycle= 0 cp= 2.14904e-09
   heap_bh30_w17_4 <= CompressorOut_bh30_17_17(2); -- cycle= 0 cp= 2.14904e-09

   CompressorIn_bh30_18_32 <= heap_bh30_w13_9 & heap_bh30_w13_8 & heap_bh30_w13_10 & heap_bh30_w13_5 & heap_bh30_w13_4 & heap_bh30_w13_3;
      Compressor_bh30_18: Compressor_6_3
      port map ( R => CompressorOut_bh30_18_18,
                 X0 => CompressorIn_bh30_18_32);
   heap_bh30_w13_11 <= CompressorOut_bh30_18_18(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w14_9 <= CompressorOut_bh30_18_18(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w15_9 <= CompressorOut_bh30_18_18(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_19_33 <= heap_bh30_w29_5 & heap_bh30_w29_4 & heap_bh30_w29_3 & heap_bh30_w29_2 & heap_bh30_w29_1 & heap_bh30_w29_0;
      Compressor_bh30_19: Compressor_6_3
      port map ( R => CompressorOut_bh30_19_19,
                 X0 => CompressorIn_bh30_19_33);
   heap_bh30_w29_6 <= CompressorOut_bh30_19_19(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w30_6 <= CompressorOut_bh30_19_19(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w31_6 <= CompressorOut_bh30_19_19(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_20_34 <= heap_bh30_w30_5 & heap_bh30_w30_4 & heap_bh30_w30_3 & heap_bh30_w30_2 & heap_bh30_w30_1 & heap_bh30_w30_0;
      Compressor_bh30_20: Compressor_6_3
      port map ( R => CompressorOut_bh30_20_20,
                 X0 => CompressorIn_bh30_20_34);
   heap_bh30_w30_7 <= CompressorOut_bh30_20_20(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w31_7 <= CompressorOut_bh30_20_20(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w32_6 <= CompressorOut_bh30_20_20(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_21_35 <= heap_bh30_w31_5 & heap_bh30_w31_4 & heap_bh30_w31_3 & heap_bh30_w31_2 & heap_bh30_w31_1 & heap_bh30_w31_0;
      Compressor_bh30_21: Compressor_6_3
      port map ( R => CompressorOut_bh30_21_21,
                 X0 => CompressorIn_bh30_21_35);
   heap_bh30_w31_8 <= CompressorOut_bh30_21_21(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w32_7 <= CompressorOut_bh30_21_21(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w33_6 <= CompressorOut_bh30_21_21(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_22_36 <= heap_bh30_w32_5 & heap_bh30_w32_4 & heap_bh30_w32_3 & heap_bh30_w32_2 & heap_bh30_w32_1 & heap_bh30_w32_0;
      Compressor_bh30_22: Compressor_6_3
      port map ( R => CompressorOut_bh30_22_22,
                 X0 => CompressorIn_bh30_22_36);
   heap_bh30_w32_8 <= CompressorOut_bh30_22_22(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w33_7 <= CompressorOut_bh30_22_22(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w34_6 <= CompressorOut_bh30_22_22(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_23_37 <= heap_bh30_w33_5 & heap_bh30_w33_4 & heap_bh30_w33_3 & heap_bh30_w33_2 & heap_bh30_w33_1 & heap_bh30_w33_0;
      Compressor_bh30_23: Compressor_6_3
      port map ( R => CompressorOut_bh30_23_23,
                 X0 => CompressorIn_bh30_23_37);
   heap_bh30_w33_8 <= CompressorOut_bh30_23_23(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w34_7 <= CompressorOut_bh30_23_23(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w35_6 <= CompressorOut_bh30_23_23(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_24_38 <= heap_bh30_w34_5 & heap_bh30_w34_4 & heap_bh30_w34_3 & heap_bh30_w34_2 & heap_bh30_w34_1 & heap_bh30_w34_0;
      Compressor_bh30_24: Compressor_6_3
      port map ( R => CompressorOut_bh30_24_24,
                 X0 => CompressorIn_bh30_24_38);
   heap_bh30_w34_8 <= CompressorOut_bh30_24_24(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w35_7 <= CompressorOut_bh30_24_24(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w36_6 <= CompressorOut_bh30_24_24(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_25_39 <= heap_bh30_w35_5 & heap_bh30_w35_4 & heap_bh30_w35_3 & heap_bh30_w35_2 & heap_bh30_w35_1 & heap_bh30_w35_0;
      Compressor_bh30_25: Compressor_6_3
      port map ( R => CompressorOut_bh30_25_25,
                 X0 => CompressorIn_bh30_25_39);
   heap_bh30_w35_8 <= CompressorOut_bh30_25_25(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w36_7 <= CompressorOut_bh30_25_25(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w37_6 <= CompressorOut_bh30_25_25(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_26_40 <= heap_bh30_w36_5 & heap_bh30_w36_4 & heap_bh30_w36_3 & heap_bh30_w36_2 & heap_bh30_w36_1 & heap_bh30_w36_0;
      Compressor_bh30_26: Compressor_6_3
      port map ( R => CompressorOut_bh30_26_26,
                 X0 => CompressorIn_bh30_26_40);
   heap_bh30_w36_8 <= CompressorOut_bh30_26_26(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w37_7 <= CompressorOut_bh30_26_26(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w38_6 <= CompressorOut_bh30_26_26(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_27_41 <= heap_bh30_w37_5 & heap_bh30_w37_4 & heap_bh30_w37_3 & heap_bh30_w37_2 & heap_bh30_w37_1 & heap_bh30_w37_0;
      Compressor_bh30_27: Compressor_6_3
      port map ( R => CompressorOut_bh30_27_27,
                 X0 => CompressorIn_bh30_27_41);
   heap_bh30_w37_8 <= CompressorOut_bh30_27_27(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w38_7 <= CompressorOut_bh30_27_27(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w39_6 <= CompressorOut_bh30_27_27(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_28_42 <= heap_bh30_w38_5 & heap_bh30_w38_4 & heap_bh30_w38_3 & heap_bh30_w38_2 & heap_bh30_w38_1 & heap_bh30_w38_0;
      Compressor_bh30_28: Compressor_6_3
      port map ( R => CompressorOut_bh30_28_28,
                 X0 => CompressorIn_bh30_28_42);
   heap_bh30_w38_8 <= CompressorOut_bh30_28_28(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w39_7 <= CompressorOut_bh30_28_28(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w40_6 <= CompressorOut_bh30_28_28(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_29_43 <= heap_bh30_w39_5 & heap_bh30_w39_4 & heap_bh30_w39_3 & heap_bh30_w39_2 & heap_bh30_w39_1 & heap_bh30_w39_0;
      Compressor_bh30_29: Compressor_6_3
      port map ( R => CompressorOut_bh30_29_29,
                 X0 => CompressorIn_bh30_29_43);
   heap_bh30_w39_8 <= CompressorOut_bh30_29_29(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w40_7 <= CompressorOut_bh30_29_29(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w41_6 <= CompressorOut_bh30_29_29(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_30_44 <= heap_bh30_w40_5 & heap_bh30_w40_4 & heap_bh30_w40_3 & heap_bh30_w40_2 & heap_bh30_w40_1 & heap_bh30_w40_0;
      Compressor_bh30_30: Compressor_6_3
      port map ( R => CompressorOut_bh30_30_30,
                 X0 => CompressorIn_bh30_30_44);
   heap_bh30_w40_8 <= CompressorOut_bh30_30_30(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w41_7 <= CompressorOut_bh30_30_30(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w42_6 <= CompressorOut_bh30_30_30(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_31_45 <= heap_bh30_w41_5 & heap_bh30_w41_4 & heap_bh30_w41_3 & heap_bh30_w41_2 & heap_bh30_w41_1 & heap_bh30_w41_0;
      Compressor_bh30_31: Compressor_6_3
      port map ( R => CompressorOut_bh30_31_31,
                 X0 => CompressorIn_bh30_31_45);
   heap_bh30_w41_8 <= CompressorOut_bh30_31_31(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w42_7 <= CompressorOut_bh30_31_31(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w43_6 <= CompressorOut_bh30_31_31(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_32_46 <= heap_bh30_w42_5 & heap_bh30_w42_4 & heap_bh30_w42_3 & heap_bh30_w42_2 & heap_bh30_w42_1 & heap_bh30_w42_0;
      Compressor_bh30_32: Compressor_6_3
      port map ( R => CompressorOut_bh30_32_32,
                 X0 => CompressorIn_bh30_32_46);
   heap_bh30_w42_8 <= CompressorOut_bh30_32_32(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w43_7 <= CompressorOut_bh30_32_32(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w44_6 <= CompressorOut_bh30_32_32(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_33_47 <= heap_bh30_w43_5 & heap_bh30_w43_4 & heap_bh30_w43_3 & heap_bh30_w43_2 & heap_bh30_w43_1 & heap_bh30_w43_0;
      Compressor_bh30_33: Compressor_6_3
      port map ( R => CompressorOut_bh30_33_33,
                 X0 => CompressorIn_bh30_33_47);
   heap_bh30_w43_8 <= CompressorOut_bh30_33_33(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w44_7 <= CompressorOut_bh30_33_33(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w45_6 <= CompressorOut_bh30_33_33(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_34_48 <= heap_bh30_w44_5 & heap_bh30_w44_4 & heap_bh30_w44_3 & heap_bh30_w44_2 & heap_bh30_w44_1 & heap_bh30_w44_0;
      Compressor_bh30_34: Compressor_6_3
      port map ( R => CompressorOut_bh30_34_34,
                 X0 => CompressorIn_bh30_34_48);
   heap_bh30_w44_8 <= CompressorOut_bh30_34_34(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w45_7 <= CompressorOut_bh30_34_34(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w46_6 <= CompressorOut_bh30_34_34(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_35_49 <= heap_bh30_w45_5 & heap_bh30_w45_4 & heap_bh30_w45_3 & heap_bh30_w45_2 & heap_bh30_w45_1 & heap_bh30_w45_0;
      Compressor_bh30_35: Compressor_6_3
      port map ( R => CompressorOut_bh30_35_35,
                 X0 => CompressorIn_bh30_35_49);
   heap_bh30_w45_8 <= CompressorOut_bh30_35_35(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w46_7 <= CompressorOut_bh30_35_35(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w47_6 <= CompressorOut_bh30_35_35(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_36_50 <= heap_bh30_w46_5 & heap_bh30_w46_4 & heap_bh30_w46_3 & heap_bh30_w46_2 & heap_bh30_w46_1 & heap_bh30_w46_0;
      Compressor_bh30_36: Compressor_6_3
      port map ( R => CompressorOut_bh30_36_36,
                 X0 => CompressorIn_bh30_36_50);
   heap_bh30_w46_8 <= CompressorOut_bh30_36_36(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w47_7 <= CompressorOut_bh30_36_36(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w48_6 <= CompressorOut_bh30_36_36(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_37_51 <= heap_bh30_w47_5 & heap_bh30_w47_4 & heap_bh30_w47_3 & heap_bh30_w47_2 & heap_bh30_w47_1 & heap_bh30_w47_0;
      Compressor_bh30_37: Compressor_6_3
      port map ( R => CompressorOut_bh30_37_37,
                 X0 => CompressorIn_bh30_37_51);
   heap_bh30_w47_8 <= CompressorOut_bh30_37_37(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w48_7 <= CompressorOut_bh30_37_37(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w49_6 <= CompressorOut_bh30_37_37(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_38_52 <= heap_bh30_w48_5 & heap_bh30_w48_4 & heap_bh30_w48_3 & heap_bh30_w48_2 & heap_bh30_w48_1 & heap_bh30_w48_0;
      Compressor_bh30_38: Compressor_6_3
      port map ( R => CompressorOut_bh30_38_38,
                 X0 => CompressorIn_bh30_38_52);
   heap_bh30_w48_8 <= CompressorOut_bh30_38_38(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w49_7 <= CompressorOut_bh30_38_38(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w50_6 <= CompressorOut_bh30_38_38(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_39_53 <= heap_bh30_w49_5 & heap_bh30_w49_4 & heap_bh30_w49_3 & heap_bh30_w49_2 & heap_bh30_w49_1 & heap_bh30_w49_0;
      Compressor_bh30_39: Compressor_6_3
      port map ( R => CompressorOut_bh30_39_39,
                 X0 => CompressorIn_bh30_39_53);
   heap_bh30_w49_8 <= CompressorOut_bh30_39_39(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w50_7 <= CompressorOut_bh30_39_39(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w51_6 <= CompressorOut_bh30_39_39(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_40_54 <= heap_bh30_w50_5 & heap_bh30_w50_4 & heap_bh30_w50_3 & heap_bh30_w50_2 & heap_bh30_w50_1 & heap_bh30_w50_0;
      Compressor_bh30_40: Compressor_6_3
      port map ( R => CompressorOut_bh30_40_40,
                 X0 => CompressorIn_bh30_40_54);
   heap_bh30_w50_8 <= CompressorOut_bh30_40_40(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w51_7 <= CompressorOut_bh30_40_40(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w52_6 <= CompressorOut_bh30_40_40(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_41_55 <= heap_bh30_w51_5 & heap_bh30_w51_4 & heap_bh30_w51_3 & heap_bh30_w51_2 & heap_bh30_w51_1 & heap_bh30_w51_0;
      Compressor_bh30_41: Compressor_6_3
      port map ( R => CompressorOut_bh30_41_41,
                 X0 => CompressorIn_bh30_41_55);
   heap_bh30_w51_8 <= CompressorOut_bh30_41_41(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w52_7 <= CompressorOut_bh30_41_41(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w53_6 <= CompressorOut_bh30_41_41(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_42_56 <= heap_bh30_w52_5 & heap_bh30_w52_4 & heap_bh30_w52_3 & heap_bh30_w52_2 & heap_bh30_w52_1 & heap_bh30_w52_0;
      Compressor_bh30_42: Compressor_6_3
      port map ( R => CompressorOut_bh30_42_42,
                 X0 => CompressorIn_bh30_42_56);
   heap_bh30_w52_8 <= CompressorOut_bh30_42_42(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w53_7 <= CompressorOut_bh30_42_42(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w54_6 <= CompressorOut_bh30_42_42(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_43_57 <= heap_bh30_w53_5 & heap_bh30_w53_4 & heap_bh30_w53_3 & heap_bh30_w53_2 & heap_bh30_w53_1 & heap_bh30_w53_0;
      Compressor_bh30_43: Compressor_6_3
      port map ( R => CompressorOut_bh30_43_43,
                 X0 => CompressorIn_bh30_43_57);
   heap_bh30_w53_8 <= CompressorOut_bh30_43_43(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w54_7 <= CompressorOut_bh30_43_43(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w55_6 <= CompressorOut_bh30_43_43(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_44_58 <= heap_bh30_w54_5 & heap_bh30_w54_4 & heap_bh30_w54_3 & heap_bh30_w54_2 & heap_bh30_w54_1 & heap_bh30_w54_0;
      Compressor_bh30_44: Compressor_6_3
      port map ( R => CompressorOut_bh30_44_44,
                 X0 => CompressorIn_bh30_44_58);
   heap_bh30_w54_8 <= CompressorOut_bh30_44_44(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w55_7 <= CompressorOut_bh30_44_44(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w56_6 <= CompressorOut_bh30_44_44(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_45_59 <= heap_bh30_w55_5 & heap_bh30_w55_4 & heap_bh30_w55_3 & heap_bh30_w55_2 & heap_bh30_w55_1 & heap_bh30_w55_0;
      Compressor_bh30_45: Compressor_6_3
      port map ( R => CompressorOut_bh30_45_45,
                 X0 => CompressorIn_bh30_45_59);
   heap_bh30_w55_8 <= CompressorOut_bh30_45_45(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w56_7 <= CompressorOut_bh30_45_45(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w57_6 <= CompressorOut_bh30_45_45(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_46_60 <= heap_bh30_w56_5 & heap_bh30_w56_4 & heap_bh30_w56_3 & heap_bh30_w56_2 & heap_bh30_w56_1 & heap_bh30_w56_0;
      Compressor_bh30_46: Compressor_6_3
      port map ( R => CompressorOut_bh30_46_46,
                 X0 => CompressorIn_bh30_46_60);
   heap_bh30_w56_8 <= CompressorOut_bh30_46_46(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w57_7 <= CompressorOut_bh30_46_46(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w58_6 <= CompressorOut_bh30_46_46(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_47_61 <= heap_bh30_w57_5 & heap_bh30_w57_4 & heap_bh30_w57_3 & heap_bh30_w57_2 & heap_bh30_w57_1 & heap_bh30_w57_0;
      Compressor_bh30_47: Compressor_6_3
      port map ( R => CompressorOut_bh30_47_47,
                 X0 => CompressorIn_bh30_47_61);
   heap_bh30_w57_8 <= CompressorOut_bh30_47_47(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w58_7 <= CompressorOut_bh30_47_47(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w59_6 <= CompressorOut_bh30_47_47(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_48_62 <= heap_bh30_w58_5 & heap_bh30_w58_4 & heap_bh30_w58_3 & heap_bh30_w58_2 & heap_bh30_w58_1 & heap_bh30_w58_0;
      Compressor_bh30_48: Compressor_6_3
      port map ( R => CompressorOut_bh30_48_48,
                 X0 => CompressorIn_bh30_48_62);
   heap_bh30_w58_8 <= CompressorOut_bh30_48_48(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w59_7 <= CompressorOut_bh30_48_48(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w60_6 <= CompressorOut_bh30_48_48(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_49_63 <= heap_bh30_w59_5 & heap_bh30_w59_4 & heap_bh30_w59_3 & heap_bh30_w59_2 & heap_bh30_w59_1 & heap_bh30_w59_0;
      Compressor_bh30_49: Compressor_6_3
      port map ( R => CompressorOut_bh30_49_49,
                 X0 => CompressorIn_bh30_49_63);
   heap_bh30_w59_8 <= CompressorOut_bh30_49_49(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w60_7 <= CompressorOut_bh30_49_49(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w61_6 <= CompressorOut_bh30_49_49(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_50_64 <= heap_bh30_w60_5 & heap_bh30_w60_4 & heap_bh30_w60_3 & heap_bh30_w60_2 & heap_bh30_w60_1 & heap_bh30_w60_0;
      Compressor_bh30_50: Compressor_6_3
      port map ( R => CompressorOut_bh30_50_50,
                 X0 => CompressorIn_bh30_50_64);
   heap_bh30_w60_8 <= CompressorOut_bh30_50_50(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w61_7 <= CompressorOut_bh30_50_50(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w62_6 <= CompressorOut_bh30_50_50(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_51_65 <= heap_bh30_w61_5 & heap_bh30_w61_4 & heap_bh30_w61_3 & heap_bh30_w61_2 & heap_bh30_w61_1 & heap_bh30_w61_0;
      Compressor_bh30_51: Compressor_6_3
      port map ( R => CompressorOut_bh30_51_51,
                 X0 => CompressorIn_bh30_51_65);
   heap_bh30_w61_8 <= CompressorOut_bh30_51_51(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w62_7 <= CompressorOut_bh30_51_51(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w63_6 <= CompressorOut_bh30_51_51(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_52_66 <= heap_bh30_w62_5 & heap_bh30_w62_4 & heap_bh30_w62_3 & heap_bh30_w62_2 & heap_bh30_w62_1 & heap_bh30_w62_0;
      Compressor_bh30_52: Compressor_6_3
      port map ( R => CompressorOut_bh30_52_52,
                 X0 => CompressorIn_bh30_52_66);
   heap_bh30_w62_8 <= CompressorOut_bh30_52_52(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w63_7 <= CompressorOut_bh30_52_52(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w64_6 <= CompressorOut_bh30_52_52(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_53_67 <= heap_bh30_w63_5 & heap_bh30_w63_4 & heap_bh30_w63_3 & heap_bh30_w63_2 & heap_bh30_w63_1 & heap_bh30_w63_0;
      Compressor_bh30_53: Compressor_6_3
      port map ( R => CompressorOut_bh30_53_53,
                 X0 => CompressorIn_bh30_53_67);
   heap_bh30_w63_8 <= CompressorOut_bh30_53_53(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w64_7 <= CompressorOut_bh30_53_53(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w65_6 <= CompressorOut_bh30_53_53(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_54_68 <= heap_bh30_w64_5 & heap_bh30_w64_4 & heap_bh30_w64_3 & heap_bh30_w64_2 & heap_bh30_w64_1 & heap_bh30_w64_0;
      Compressor_bh30_54: Compressor_6_3
      port map ( R => CompressorOut_bh30_54_54,
                 X0 => CompressorIn_bh30_54_68);
   heap_bh30_w64_8 <= CompressorOut_bh30_54_54(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w65_7 <= CompressorOut_bh30_54_54(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w66_6 <= CompressorOut_bh30_54_54(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_55_69 <= heap_bh30_w65_5 & heap_bh30_w65_4 & heap_bh30_w65_3 & heap_bh30_w65_2 & heap_bh30_w65_1 & heap_bh30_w65_0;
      Compressor_bh30_55: Compressor_6_3
      port map ( R => CompressorOut_bh30_55_55,
                 X0 => CompressorIn_bh30_55_69);
   heap_bh30_w65_8 <= CompressorOut_bh30_55_55(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w66_7 <= CompressorOut_bh30_55_55(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w67_5 <= CompressorOut_bh30_55_55(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_56_70 <= heap_bh30_w66_5 & heap_bh30_w66_4 & heap_bh30_w66_3 & heap_bh30_w66_2 & heap_bh30_w66_1 & heap_bh30_w66_0;
      Compressor_bh30_56: Compressor_6_3
      port map ( R => CompressorOut_bh30_56_56,
                 X0 => CompressorIn_bh30_56_70);
   heap_bh30_w66_8 <= CompressorOut_bh30_56_56(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w67_6 <= CompressorOut_bh30_56_56(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w68_5 <= CompressorOut_bh30_56_56(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_57_71 <= heap_bh30_w3_0 & heap_bh30_w3_5 & heap_bh30_w3_4 & heap_bh30_w3_3;
   CompressorIn_bh30_57_72(0) <= heap_bh30_w4_6;
      Compressor_bh30_57: Compressor_14_3
      port map ( R => CompressorOut_bh30_57_57,
                 X0 => CompressorIn_bh30_57_71,
                 X1 => CompressorIn_bh30_57_72);
   heap_bh30_w3_6 <= CompressorOut_bh30_57_57(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w4_7 <= CompressorOut_bh30_57_57(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w5_9 <= CompressorOut_bh30_57_57(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_58_73 <= heap_bh30_w5_8 & heap_bh30_w5_7 & heap_bh30_w5_6 & heap_bh30_w5_5;
   CompressorIn_bh30_58_74(0) <= heap_bh30_w6_10;
      Compressor_bh30_58: Compressor_14_3
      port map ( R => CompressorOut_bh30_58_58,
                 X0 => CompressorIn_bh30_58_73,
                 X1 => CompressorIn_bh30_58_74);
   heap_bh30_w5_10 <= CompressorOut_bh30_58_58(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w6_11 <= CompressorOut_bh30_58_58(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w7_11 <= CompressorOut_bh30_58_58(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_59_75 <= heap_bh30_w7_7 & heap_bh30_w7_10 & heap_bh30_w7_6 & heap_bh30_w7_5;
   CompressorIn_bh30_59_76(0) <= heap_bh30_w8_12;
      Compressor_bh30_59: Compressor_14_3
      port map ( R => CompressorOut_bh30_59_59,
                 X0 => CompressorIn_bh30_59_75,
                 X1 => CompressorIn_bh30_59_76);
   heap_bh30_w7_12 <= CompressorOut_bh30_59_59(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w8_13 <= CompressorOut_bh30_59_59(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w9_12 <= CompressorOut_bh30_59_59(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_60_77 <= heap_bh30_w9_8 & heap_bh30_w9_11 & heap_bh30_w9_7 & heap_bh30_w9_6;
   CompressorIn_bh30_60_78(0) <= heap_bh30_w10_11;
      Compressor_bh30_60: Compressor_14_3
      port map ( R => CompressorOut_bh30_60_60,
                 X0 => CompressorIn_bh30_60_77,
                 X1 => CompressorIn_bh30_60_78);
   heap_bh30_w9_13 <= CompressorOut_bh30_60_60(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w10_12 <= CompressorOut_bh30_60_60(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w11_12 <= CompressorOut_bh30_60_60(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_61_79 <= heap_bh30_w14_6 & heap_bh30_w14_8 & heap_bh30_w14_5 & heap_bh30_w14_4;
   CompressorIn_bh30_61_80(0) <= heap_bh30_w15_8;
      Compressor_bh30_61: Compressor_14_3
      port map ( R => CompressorOut_bh30_61_61,
                 X0 => CompressorIn_bh30_61_79,
                 X1 => CompressorIn_bh30_61_80);
   heap_bh30_w14_10 <= CompressorOut_bh30_61_61(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w15_10 <= CompressorOut_bh30_61_61(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w16_6 <= CompressorOut_bh30_61_61(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_62_81 <= heap_bh30_w16_5 & heap_bh30_w16_3 & heap_bh30_w16_2 & heap_bh30_w16_1;
   CompressorIn_bh30_62_82(0) <= heap_bh30_w17_0;
      Compressor_bh30_62: Compressor_14_3
      port map ( R => CompressorOut_bh30_62_62,
                 X0 => CompressorIn_bh30_62_81,
                 X1 => CompressorIn_bh30_62_82);
   heap_bh30_w16_7 <= CompressorOut_bh30_62_62(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w17_5 <= CompressorOut_bh30_62_62(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w18_4 <= CompressorOut_bh30_62_62(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_63_83 <= heap_bh30_w17_4 & heap_bh30_w17_3 & heap_bh30_w17_2 & heap_bh30_w17_1;
   CompressorIn_bh30_63_84(0) <= heap_bh30_w18_0;
      Compressor_bh30_63: Compressor_14_3
      port map ( R => CompressorOut_bh30_63_63,
                 X0 => CompressorIn_bh30_63_83,
                 X1 => CompressorIn_bh30_63_84);
   heap_bh30_w17_6 <= CompressorOut_bh30_63_63(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w18_5 <= CompressorOut_bh30_63_63(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w19_4 <= CompressorOut_bh30_63_63(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_64_85 <= heap_bh30_w19_3 & heap_bh30_w19_2 & heap_bh30_w19_1 & heap_bh30_w19_0;
   CompressorIn_bh30_64_86(0) <= heap_bh30_w20_3;
      Compressor_bh30_64: Compressor_14_3
      port map ( R => CompressorOut_bh30_64_64,
                 X0 => CompressorIn_bh30_64_85,
                 X1 => CompressorIn_bh30_64_86);
   heap_bh30_w19_5 <= CompressorOut_bh30_64_64(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w20_4 <= CompressorOut_bh30_64_64(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w21_4 <= CompressorOut_bh30_64_64(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_65_87 <= heap_bh30_w21_3 & heap_bh30_w21_2 & heap_bh30_w21_1 & heap_bh30_w21_0;
   CompressorIn_bh30_65_88(0) <= heap_bh30_w22_3;
      Compressor_bh30_65: Compressor_14_3
      port map ( R => CompressorOut_bh30_65_65,
                 X0 => CompressorIn_bh30_65_87,
                 X1 => CompressorIn_bh30_65_88);
   heap_bh30_w21_5 <= CompressorOut_bh30_65_65(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w22_4 <= CompressorOut_bh30_65_65(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w23_4 <= CompressorOut_bh30_65_65(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_66_89 <= heap_bh30_w23_3 & heap_bh30_w23_2 & heap_bh30_w23_1 & heap_bh30_w23_0;
   CompressorIn_bh30_66_90(0) <= heap_bh30_w24_3;
      Compressor_bh30_66: Compressor_14_3
      port map ( R => CompressorOut_bh30_66_66,
                 X0 => CompressorIn_bh30_66_89,
                 X1 => CompressorIn_bh30_66_90);
   heap_bh30_w23_5 <= CompressorOut_bh30_66_66(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w24_4 <= CompressorOut_bh30_66_66(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w25_4 <= CompressorOut_bh30_66_66(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_67_91 <= heap_bh30_w25_3 & heap_bh30_w25_2 & heap_bh30_w25_1 & heap_bh30_w25_0;
   CompressorIn_bh30_67_92(0) <= heap_bh30_w26_4;
      Compressor_bh30_67: Compressor_14_3
      port map ( R => CompressorOut_bh30_67_67,
                 X0 => CompressorIn_bh30_67_91,
                 X1 => CompressorIn_bh30_67_92);
   heap_bh30_w25_5 <= CompressorOut_bh30_67_67(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w26_5 <= CompressorOut_bh30_67_67(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w27_5 <= CompressorOut_bh30_67_67(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_68_93 <= heap_bh30_w26_3 & heap_bh30_w26_2 & heap_bh30_w26_1 & heap_bh30_w26_0;
   CompressorIn_bh30_68_94(0) <= heap_bh30_w27_4;
      Compressor_bh30_68: Compressor_14_3
      port map ( R => CompressorOut_bh30_68_68,
                 X0 => CompressorIn_bh30_68_93,
                 X1 => CompressorIn_bh30_68_94);
   heap_bh30_w26_6 <= CompressorOut_bh30_68_68(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w27_6 <= CompressorOut_bh30_68_68(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w28_5 <= CompressorOut_bh30_68_68(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_69_95 <= heap_bh30_w27_3 & heap_bh30_w27_2 & heap_bh30_w27_1 & heap_bh30_w27_0;
   CompressorIn_bh30_69_96(0) <= heap_bh30_w28_4;
      Compressor_bh30_69: Compressor_14_3
      port map ( R => CompressorOut_bh30_69_69,
                 X0 => CompressorIn_bh30_69_95,
                 X1 => CompressorIn_bh30_69_96);
   heap_bh30_w27_7 <= CompressorOut_bh30_69_69(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w28_6 <= CompressorOut_bh30_69_69(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w29_7 <= CompressorOut_bh30_69_69(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_70_97 <= heap_bh30_w67_4 & heap_bh30_w67_3 & heap_bh30_w67_2 & heap_bh30_w67_1;
   CompressorIn_bh30_70_98(0) <= heap_bh30_w68_4;
      Compressor_bh30_70: Compressor_14_3
      port map ( R => CompressorOut_bh30_70_70,
                 X0 => CompressorIn_bh30_70_97,
                 X1 => CompressorIn_bh30_70_98);
   heap_bh30_w67_7 <= CompressorOut_bh30_70_70(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w68_6 <= CompressorOut_bh30_70_70(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w69_5 <= CompressorOut_bh30_70_70(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_71_99 <= heap_bh30_w68_3 & heap_bh30_w68_2 & heap_bh30_w68_1 & heap_bh30_w68_0;
   CompressorIn_bh30_71_100(0) <= heap_bh30_w69_4;
      Compressor_bh30_71: Compressor_14_3
      port map ( R => CompressorOut_bh30_71_71,
                 X0 => CompressorIn_bh30_71_99,
                 X1 => CompressorIn_bh30_71_100);
   heap_bh30_w68_7 <= CompressorOut_bh30_71_71(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w69_6 <= CompressorOut_bh30_71_71(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w70_4 <= CompressorOut_bh30_71_71(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_72_101 <= heap_bh30_w69_3 & heap_bh30_w69_2 & heap_bh30_w69_1 & heap_bh30_w69_0;
   CompressorIn_bh30_72_102(0) <= heap_bh30_w70_3;
      Compressor_bh30_72: Compressor_14_3
      port map ( R => CompressorOut_bh30_72_72,
                 X0 => CompressorIn_bh30_72_101,
                 X1 => CompressorIn_bh30_72_102);
   heap_bh30_w69_7 <= CompressorOut_bh30_72_72(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w70_5 <= CompressorOut_bh30_72_72(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w71_4 <= CompressorOut_bh30_72_72(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_73_103 <= heap_bh30_w71_3 & heap_bh30_w71_2 & heap_bh30_w71_1 & heap_bh30_w71_0;
   CompressorIn_bh30_73_104(0) <= heap_bh30_w72_3;
      Compressor_bh30_73: Compressor_14_3
      port map ( R => CompressorOut_bh30_73_73,
                 X0 => CompressorIn_bh30_73_103,
                 X1 => CompressorIn_bh30_73_104);
   heap_bh30_w71_5 <= CompressorOut_bh30_73_73(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w72_4 <= CompressorOut_bh30_73_73(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w73_4 <= CompressorOut_bh30_73_73(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_74_105 <= heap_bh30_w73_3 & heap_bh30_w73_2 & heap_bh30_w73_1 & heap_bh30_w73_0;
   CompressorIn_bh30_74_106(0) <= heap_bh30_w74_3;
      Compressor_bh30_74: Compressor_14_3
      port map ( R => CompressorOut_bh30_74_74,
                 X0 => CompressorIn_bh30_74_105,
                 X1 => CompressorIn_bh30_74_106);
   heap_bh30_w73_5 <= CompressorOut_bh30_74_74(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w74_4 <= CompressorOut_bh30_74_74(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w75_4 <= CompressorOut_bh30_74_74(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_75_107 <= heap_bh30_w75_3 & heap_bh30_w75_2 & heap_bh30_w75_1 & heap_bh30_w75_0;
   CompressorIn_bh30_75_108(0) <= heap_bh30_w76_3;
      Compressor_bh30_75: Compressor_14_3
      port map ( R => CompressorOut_bh30_75_75,
                 X0 => CompressorIn_bh30_75_107,
                 X1 => CompressorIn_bh30_75_108);
   heap_bh30_w75_5 <= CompressorOut_bh30_75_75(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w76_4 <= CompressorOut_bh30_75_75(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w77_4 <= CompressorOut_bh30_75_75(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_76_109 <= heap_bh30_w77_3 & heap_bh30_w77_2 & heap_bh30_w77_1 & heap_bh30_w77_0;
   CompressorIn_bh30_76_110(0) <= heap_bh30_w78_3;
      Compressor_bh30_76: Compressor_14_3
      port map ( R => CompressorOut_bh30_76_76,
                 X0 => CompressorIn_bh30_76_109,
                 X1 => CompressorIn_bh30_76_110);
   heap_bh30_w77_5 <= CompressorOut_bh30_76_76(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w78_4 <= CompressorOut_bh30_76_76(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w79_4 <= CompressorOut_bh30_76_76(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_77_111 <= heap_bh30_w79_3 & heap_bh30_w79_2 & heap_bh30_w79_1 & heap_bh30_w79_0;
   CompressorIn_bh30_77_112(0) <= heap_bh30_w80_3;
      Compressor_bh30_77: Compressor_14_3
      port map ( R => CompressorOut_bh30_77_77,
                 X0 => CompressorIn_bh30_77_111,
                 X1 => CompressorIn_bh30_77_112);
   heap_bh30_w79_5 <= CompressorOut_bh30_77_77(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w80_4 <= CompressorOut_bh30_77_77(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w81_4 <= CompressorOut_bh30_77_77(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_78_113 <= heap_bh30_w81_3 & heap_bh30_w81_2 & heap_bh30_w81_1 & heap_bh30_w81_0;
   CompressorIn_bh30_78_114(0) <= heap_bh30_w82_3;
      Compressor_bh30_78: Compressor_14_3
      port map ( R => CompressorOut_bh30_78_78,
                 X0 => CompressorIn_bh30_78_113,
                 X1 => CompressorIn_bh30_78_114);
   heap_bh30_w81_5 <= CompressorOut_bh30_78_78(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w82_4 <= CompressorOut_bh30_78_78(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w83_4 <= CompressorOut_bh30_78_78(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_79_115 <= heap_bh30_w83_3 & heap_bh30_w83_2 & heap_bh30_w83_1 & heap_bh30_w83_0;
   CompressorIn_bh30_79_116(0) <= heap_bh30_w84_2;
      Compressor_bh30_79: Compressor_14_3
      port map ( R => CompressorOut_bh30_79_79,
                 X0 => CompressorIn_bh30_79_115,
                 X1 => CompressorIn_bh30_79_116);
   heap_bh30_w83_5 <= CompressorOut_bh30_79_79(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w84_3 <= CompressorOut_bh30_79_79(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w85_3 <= CompressorOut_bh30_79_79(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_80_117 <= heap_bh30_w12_13 & heap_bh30_w12_7 & heap_bh30_w12_6 & heap_bh30_w12_5;
      Compressor_bh30_80: Compressor_4_3
      port map ( R => CompressorOut_bh30_80_80,
                 X0 => CompressorIn_bh30_80_117);
   heap_bh30_w12_14 <= CompressorOut_bh30_80_80(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w13_12 <= CompressorOut_bh30_80_80(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w14_11 <= CompressorOut_bh30_80_80(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_81_118 <= heap_bh30_w28_3 & heap_bh30_w28_2 & heap_bh30_w28_1 & heap_bh30_w28_0;
      Compressor_bh30_81: Compressor_4_3
      port map ( R => CompressorOut_bh30_81_81,
                 X0 => CompressorIn_bh30_81_118);
   heap_bh30_w28_7 <= CompressorOut_bh30_81_81(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w29_8 <= CompressorOut_bh30_81_81(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w30_8 <= CompressorOut_bh30_81_81(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_82_119 <= heap_bh30_w10_10 & heap_bh30_w10_6 & heap_bh30_w10_5;
   CompressorIn_bh30_82_120 <= heap_bh30_w11_11 & heap_bh30_w11_6;
      Compressor_bh30_82: Compressor_23_3
      port map ( R => CompressorOut_bh30_82_82,
                 X0 => CompressorIn_bh30_82_119,
                 X1 => CompressorIn_bh30_82_120);
   heap_bh30_w10_13 <= CompressorOut_bh30_82_82(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w11_13 <= CompressorOut_bh30_82_82(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w12_15 <= CompressorOut_bh30_82_82(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_83_121 <= heap_bh30_w85_2 & heap_bh30_w85_1 & heap_bh30_w85_0;
   CompressorIn_bh30_83_122 <= heap_bh30_w86_2 & heap_bh30_w86_1;
      Compressor_bh30_83: Compressor_23_3
      port map ( R => CompressorOut_bh30_83_83,
                 X0 => CompressorIn_bh30_83_121,
                 X1 => CompressorIn_bh30_83_122);
   heap_bh30_w85_4 <= CompressorOut_bh30_83_83(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w86_3 <= CompressorOut_bh30_83_83(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w87_3 <= CompressorOut_bh30_83_83(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_84_123 <= heap_bh30_w87_2 & heap_bh30_w87_1 & heap_bh30_w87_0;
   CompressorIn_bh30_84_124 <= heap_bh30_w88_2 & heap_bh30_w88_1;
      Compressor_bh30_84: Compressor_23_3
      port map ( R => CompressorOut_bh30_84_84,
                 X0 => CompressorIn_bh30_84_123,
                 X1 => CompressorIn_bh30_84_124);
   heap_bh30_w87_4 <= CompressorOut_bh30_84_84(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w88_3 <= CompressorOut_bh30_84_84(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w89_3 <= CompressorOut_bh30_84_84(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_85_125 <= heap_bh30_w89_2 & heap_bh30_w89_1 & heap_bh30_w89_0;
   CompressorIn_bh30_85_126 <= heap_bh30_w90_2 & heap_bh30_w90_1;
      Compressor_bh30_85: Compressor_23_3
      port map ( R => CompressorOut_bh30_85_85,
                 X0 => CompressorIn_bh30_85_125,
                 X1 => CompressorIn_bh30_85_126);
   heap_bh30_w89_4 <= CompressorOut_bh30_85_85(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w90_3 <= CompressorOut_bh30_85_85(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w91_3 <= CompressorOut_bh30_85_85(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_86_127 <= heap_bh30_w91_2 & heap_bh30_w91_1 & heap_bh30_w91_0;
   CompressorIn_bh30_86_128 <= heap_bh30_w92_2 & heap_bh30_w92_1;
      Compressor_bh30_86: Compressor_23_3
      port map ( R => CompressorOut_bh30_86_86,
                 X0 => CompressorIn_bh30_86_127,
                 X1 => CompressorIn_bh30_86_128);
   heap_bh30_w91_4 <= CompressorOut_bh30_86_86(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w92_3 <= CompressorOut_bh30_86_86(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w93_3 <= CompressorOut_bh30_86_86(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_87_129 <= heap_bh30_w93_2 & heap_bh30_w93_1 & heap_bh30_w93_0;
   CompressorIn_bh30_87_130 <= heap_bh30_w94_1 & heap_bh30_w94_0;
      Compressor_bh30_87: Compressor_23_3
      port map ( R => CompressorOut_bh30_87_87,
                 X0 => CompressorIn_bh30_87_129,
                 X1 => CompressorIn_bh30_87_130);
   heap_bh30_w93_4 <= CompressorOut_bh30_87_87(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w94_2 <= CompressorOut_bh30_87_87(1); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w95_2 <= CompressorOut_bh30_87_87(2); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_88_131 <= heap_bh30_w2_5 & heap_bh30_w2_4 & heap_bh30_w2_3;
      Compressor_bh30_88: Compressor_3_2
      port map ( R => CompressorOut_bh30_88_88,
                 X0 => CompressorIn_bh30_88_131);
   heap_bh30_w2_6 <= CompressorOut_bh30_88_88(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w3_7 <= CompressorOut_bh30_88_88(1); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_89_132 <= heap_bh30_w4_5 & heap_bh30_w4_4 & heap_bh30_w4_3;
      Compressor_bh30_89: Compressor_3_2
      port map ( R => CompressorOut_bh30_89_89,
                 X0 => CompressorIn_bh30_89_132);
   heap_bh30_w4_8 <= CompressorOut_bh30_89_89(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w5_11 <= CompressorOut_bh30_89_89(1); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_90_133 <= heap_bh30_w8_11 & heap_bh30_w8_7 & heap_bh30_w8_6;
      Compressor_bh30_90: Compressor_3_2
      port map ( R => CompressorOut_bh30_90_90,
                 X0 => CompressorIn_bh30_90_133);
   heap_bh30_w8_14 <= CompressorOut_bh30_90_90(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w9_14 <= CompressorOut_bh30_90_90(1); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_91_134 <= heap_bh30_w15_5 & heap_bh30_w15_4 & heap_bh30_w15_3;
      Compressor_bh30_91: Compressor_3_2
      port map ( R => CompressorOut_bh30_91_91,
                 X0 => CompressorIn_bh30_91_134);
   heap_bh30_w15_11 <= CompressorOut_bh30_91_91(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w16_8 <= CompressorOut_bh30_91_91(1); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_92_135 <= heap_bh30_w18_3 & heap_bh30_w18_2 & heap_bh30_w18_1;
      Compressor_bh30_92: Compressor_3_2
      port map ( R => CompressorOut_bh30_92_92,
                 X0 => CompressorIn_bh30_92_135);
   heap_bh30_w18_6 <= CompressorOut_bh30_92_92(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w19_6 <= CompressorOut_bh30_92_92(1); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_93_136 <= heap_bh30_w20_2 & heap_bh30_w20_1 & heap_bh30_w20_0;
      Compressor_bh30_93: Compressor_3_2
      port map ( R => CompressorOut_bh30_93_93,
                 X0 => CompressorIn_bh30_93_136);
   heap_bh30_w20_5 <= CompressorOut_bh30_93_93(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w21_6 <= CompressorOut_bh30_93_93(1); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_94_137 <= heap_bh30_w22_2 & heap_bh30_w22_1 & heap_bh30_w22_0;
      Compressor_bh30_94: Compressor_3_2
      port map ( R => CompressorOut_bh30_94_94,
                 X0 => CompressorIn_bh30_94_137);
   heap_bh30_w22_5 <= CompressorOut_bh30_94_94(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w23_6 <= CompressorOut_bh30_94_94(1); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_95_138 <= heap_bh30_w24_2 & heap_bh30_w24_1 & heap_bh30_w24_0;
      Compressor_bh30_95: Compressor_3_2
      port map ( R => CompressorOut_bh30_95_95,
                 X0 => CompressorIn_bh30_95_138);
   heap_bh30_w24_5 <= CompressorOut_bh30_95_95(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w25_6 <= CompressorOut_bh30_95_95(1); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_96_139 <= heap_bh30_w70_2 & heap_bh30_w70_1 & heap_bh30_w70_0;
      Compressor_bh30_96: Compressor_3_2
      port map ( R => CompressorOut_bh30_96_96,
                 X0 => CompressorIn_bh30_96_139);
   heap_bh30_w70_6 <= CompressorOut_bh30_96_96(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w71_6 <= CompressorOut_bh30_96_96(1); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_97_140 <= heap_bh30_w72_2 & heap_bh30_w72_1 & heap_bh30_w72_0;
      Compressor_bh30_97: Compressor_3_2
      port map ( R => CompressorOut_bh30_97_97,
                 X0 => CompressorIn_bh30_97_140);
   heap_bh30_w72_5 <= CompressorOut_bh30_97_97(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w73_6 <= CompressorOut_bh30_97_97(1); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_98_141 <= heap_bh30_w74_2 & heap_bh30_w74_1 & heap_bh30_w74_0;
      Compressor_bh30_98: Compressor_3_2
      port map ( R => CompressorOut_bh30_98_98,
                 X0 => CompressorIn_bh30_98_141);
   heap_bh30_w74_5 <= CompressorOut_bh30_98_98(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w75_6 <= CompressorOut_bh30_98_98(1); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_99_142 <= heap_bh30_w76_2 & heap_bh30_w76_1 & heap_bh30_w76_0;
      Compressor_bh30_99: Compressor_3_2
      port map ( R => CompressorOut_bh30_99_99,
                 X0 => CompressorIn_bh30_99_142);
   heap_bh30_w76_5 <= CompressorOut_bh30_99_99(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w77_6 <= CompressorOut_bh30_99_99(1); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_100_143 <= heap_bh30_w78_2 & heap_bh30_w78_1 & heap_bh30_w78_0;
      Compressor_bh30_100: Compressor_3_2
      port map ( R => CompressorOut_bh30_100_100,
                 X0 => CompressorIn_bh30_100_143);
   heap_bh30_w78_5 <= CompressorOut_bh30_100_100(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w79_6 <= CompressorOut_bh30_100_100(1); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_101_144 <= heap_bh30_w80_2 & heap_bh30_w80_1 & heap_bh30_w80_0;
      Compressor_bh30_101: Compressor_3_2
      port map ( R => CompressorOut_bh30_101_101,
                 X0 => CompressorIn_bh30_101_144);
   heap_bh30_w80_5 <= CompressorOut_bh30_101_101(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w81_6 <= CompressorOut_bh30_101_101(1); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_102_145 <= heap_bh30_w82_2 & heap_bh30_w82_1 & heap_bh30_w82_0;
      Compressor_bh30_102: Compressor_3_2
      port map ( R => CompressorOut_bh30_102_102,
                 X0 => CompressorIn_bh30_102_145);
   heap_bh30_w82_5 <= CompressorOut_bh30_102_102(0); -- cycle= 0 cp= 2.91772e-09
   heap_bh30_w83_6 <= CompressorOut_bh30_102_102(1); -- cycle= 0 cp= 2.91772e-09

   CompressorIn_bh30_103_146 <= heap_bh30_w14_3 & heap_bh30_w14_11 & heap_bh30_w14_10 & heap_bh30_w14_9;
   CompressorIn_bh30_103_147(0) <= heap_bh30_w15_11;
      Compressor_bh30_103: Compressor_14_3
      port map ( R => CompressorOut_bh30_103_103,
                 X0 => CompressorIn_bh30_103_146,
                 X1 => CompressorIn_bh30_103_147);
   heap_bh30_w14_12 <= CompressorOut_bh30_103_103(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w15_12 <= CompressorOut_bh30_103_103(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w16_9 <= CompressorOut_bh30_103_103(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_104_148 <= heap_bh30_w67_0 & heap_bh30_w67_7 & heap_bh30_w67_6 & heap_bh30_w67_5;
   CompressorIn_bh30_104_149(0) <= heap_bh30_w68_7;
      Compressor_bh30_104: Compressor_14_3
      port map ( R => CompressorOut_bh30_104_104,
                 X0 => CompressorIn_bh30_104_148,
                 X1 => CompressorIn_bh30_104_149);
   heap_bh30_w67_8 <= CompressorOut_bh30_104_104(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w68_8 <= CompressorOut_bh30_104_104(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w69_8 <= CompressorOut_bh30_104_104(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_105_150 <= heap_bh30_w5_11 & heap_bh30_w5_10 & heap_bh30_w5_9;
   CompressorIn_bh30_105_151 <= heap_bh30_w6_6 & heap_bh30_w6_5;
      Compressor_bh30_105: Compressor_23_3
      port map ( R => CompressorOut_bh30_105_105,
                 X0 => CompressorIn_bh30_105_150,
                 X1 => CompressorIn_bh30_105_151);
   heap_bh30_w5_12 <= CompressorOut_bh30_105_105(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w6_12 <= CompressorOut_bh30_105_105(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w7_13 <= CompressorOut_bh30_105_105(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_106_152 <= heap_bh30_w9_14 & heap_bh30_w9_13 & heap_bh30_w9_12;
   CompressorIn_bh30_106_153 <= heap_bh30_w10_13 & heap_bh30_w10_12;
      Compressor_bh30_106: Compressor_23_3
      port map ( R => CompressorOut_bh30_106_106,
                 X0 => CompressorIn_bh30_106_152,
                 X1 => CompressorIn_bh30_106_153);
   heap_bh30_w9_15 <= CompressorOut_bh30_106_106(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w10_14 <= CompressorOut_bh30_106_106(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w11_14 <= CompressorOut_bh30_106_106(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_107_154 <= heap_bh30_w11_5 & heap_bh30_w11_13 & heap_bh30_w11_12;
   CompressorIn_bh30_107_155 <= heap_bh30_w12_15 & heap_bh30_w12_14;
      Compressor_bh30_107: Compressor_23_3
      port map ( R => CompressorOut_bh30_107_107,
                 X0 => CompressorIn_bh30_107_154,
                 X1 => CompressorIn_bh30_107_155);
   heap_bh30_w11_15 <= CompressorOut_bh30_107_107(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w12_16 <= CompressorOut_bh30_107_107(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w13_13 <= CompressorOut_bh30_107_107(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_108_156 <= heap_bh30_w16_8 & heap_bh30_w16_7 & heap_bh30_w16_6;
   CompressorIn_bh30_108_157 <= heap_bh30_w17_6 & heap_bh30_w17_5;
      Compressor_bh30_108: Compressor_23_3
      port map ( R => CompressorOut_bh30_108_108,
                 X0 => CompressorIn_bh30_108_156,
                 X1 => CompressorIn_bh30_108_157);
   heap_bh30_w16_10 <= CompressorOut_bh30_108_108(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w17_7 <= CompressorOut_bh30_108_108(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w18_7 <= CompressorOut_bh30_108_108(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_109_158 <= heap_bh30_w18_6 & heap_bh30_w18_5 & heap_bh30_w18_4;
   CompressorIn_bh30_109_159 <= heap_bh30_w19_6 & heap_bh30_w19_5;
      Compressor_bh30_109: Compressor_23_3
      port map ( R => CompressorOut_bh30_109_109,
                 X0 => CompressorIn_bh30_109_158,
                 X1 => CompressorIn_bh30_109_159);
   heap_bh30_w18_8 <= CompressorOut_bh30_109_109(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w19_7 <= CompressorOut_bh30_109_109(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w20_6 <= CompressorOut_bh30_109_109(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_110_160 <= heap_bh30_w21_6 & heap_bh30_w21_5 & heap_bh30_w21_4;
   CompressorIn_bh30_110_161 <= heap_bh30_w22_5 & heap_bh30_w22_4;
      Compressor_bh30_110: Compressor_23_3
      port map ( R => CompressorOut_bh30_110_110,
                 X0 => CompressorIn_bh30_110_160,
                 X1 => CompressorIn_bh30_110_161);
   heap_bh30_w21_7 <= CompressorOut_bh30_110_110(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w22_6 <= CompressorOut_bh30_110_110(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w23_7 <= CompressorOut_bh30_110_110(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_111_162 <= heap_bh30_w23_6 & heap_bh30_w23_5 & heap_bh30_w23_4;
   CompressorIn_bh30_111_163 <= heap_bh30_w24_5 & heap_bh30_w24_4;
      Compressor_bh30_111: Compressor_23_3
      port map ( R => CompressorOut_bh30_111_111,
                 X0 => CompressorIn_bh30_111_162,
                 X1 => CompressorIn_bh30_111_163);
   heap_bh30_w23_8 <= CompressorOut_bh30_111_111(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w24_6 <= CompressorOut_bh30_111_111(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w25_7 <= CompressorOut_bh30_111_111(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_112_164 <= heap_bh30_w25_6 & heap_bh30_w25_5 & heap_bh30_w25_4;
   CompressorIn_bh30_112_165 <= heap_bh30_w26_6 & heap_bh30_w26_5;
      Compressor_bh30_112: Compressor_23_3
      port map ( R => CompressorOut_bh30_112_112,
                 X0 => CompressorIn_bh30_112_164,
                 X1 => CompressorIn_bh30_112_165);
   heap_bh30_w25_8 <= CompressorOut_bh30_112_112(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w26_7 <= CompressorOut_bh30_112_112(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w27_8 <= CompressorOut_bh30_112_112(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_113_166 <= heap_bh30_w27_7 & heap_bh30_w27_6 & heap_bh30_w27_5;
   CompressorIn_bh30_113_167 <= heap_bh30_w28_7 & heap_bh30_w28_6;
      Compressor_bh30_113: Compressor_23_3
      port map ( R => CompressorOut_bh30_113_113,
                 X0 => CompressorIn_bh30_113_166,
                 X1 => CompressorIn_bh30_113_167);
   heap_bh30_w27_9 <= CompressorOut_bh30_113_113(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w28_8 <= CompressorOut_bh30_113_113(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w29_9 <= CompressorOut_bh30_113_113(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_114_168 <= heap_bh30_w29_8 & heap_bh30_w29_7 & heap_bh30_w29_6;
   CompressorIn_bh30_114_169 <= heap_bh30_w30_8 & heap_bh30_w30_7;
      Compressor_bh30_114: Compressor_23_3
      port map ( R => CompressorOut_bh30_114_114,
                 X0 => CompressorIn_bh30_114_168,
                 X1 => CompressorIn_bh30_114_169);
   heap_bh30_w29_10 <= CompressorOut_bh30_114_114(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w30_9 <= CompressorOut_bh30_114_114(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w31_9 <= CompressorOut_bh30_114_114(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_115_170 <= heap_bh30_w31_8 & heap_bh30_w31_7 & heap_bh30_w31_6;
   CompressorIn_bh30_115_171 <= heap_bh30_w32_8 & heap_bh30_w32_7;
      Compressor_bh30_115: Compressor_23_3
      port map ( R => CompressorOut_bh30_115_115,
                 X0 => CompressorIn_bh30_115_170,
                 X1 => CompressorIn_bh30_115_171);
   heap_bh30_w31_10 <= CompressorOut_bh30_115_115(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w32_9 <= CompressorOut_bh30_115_115(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w33_9 <= CompressorOut_bh30_115_115(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_116_172 <= heap_bh30_w33_8 & heap_bh30_w33_7 & heap_bh30_w33_6;
   CompressorIn_bh30_116_173 <= heap_bh30_w34_8 & heap_bh30_w34_7;
      Compressor_bh30_116: Compressor_23_3
      port map ( R => CompressorOut_bh30_116_116,
                 X0 => CompressorIn_bh30_116_172,
                 X1 => CompressorIn_bh30_116_173);
   heap_bh30_w33_10 <= CompressorOut_bh30_116_116(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w34_9 <= CompressorOut_bh30_116_116(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w35_9 <= CompressorOut_bh30_116_116(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_117_174 <= heap_bh30_w35_8 & heap_bh30_w35_7 & heap_bh30_w35_6;
   CompressorIn_bh30_117_175 <= heap_bh30_w36_8 & heap_bh30_w36_7;
      Compressor_bh30_117: Compressor_23_3
      port map ( R => CompressorOut_bh30_117_117,
                 X0 => CompressorIn_bh30_117_174,
                 X1 => CompressorIn_bh30_117_175);
   heap_bh30_w35_10 <= CompressorOut_bh30_117_117(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w36_9 <= CompressorOut_bh30_117_117(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w37_9 <= CompressorOut_bh30_117_117(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_118_176 <= heap_bh30_w37_8 & heap_bh30_w37_7 & heap_bh30_w37_6;
   CompressorIn_bh30_118_177 <= heap_bh30_w38_8 & heap_bh30_w38_7;
      Compressor_bh30_118: Compressor_23_3
      port map ( R => CompressorOut_bh30_118_118,
                 X0 => CompressorIn_bh30_118_176,
                 X1 => CompressorIn_bh30_118_177);
   heap_bh30_w37_10 <= CompressorOut_bh30_118_118(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w38_9 <= CompressorOut_bh30_118_118(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w39_9 <= CompressorOut_bh30_118_118(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_119_178 <= heap_bh30_w39_8 & heap_bh30_w39_7 & heap_bh30_w39_6;
   CompressorIn_bh30_119_179 <= heap_bh30_w40_8 & heap_bh30_w40_7;
      Compressor_bh30_119: Compressor_23_3
      port map ( R => CompressorOut_bh30_119_119,
                 X0 => CompressorIn_bh30_119_178,
                 X1 => CompressorIn_bh30_119_179);
   heap_bh30_w39_10 <= CompressorOut_bh30_119_119(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w40_9 <= CompressorOut_bh30_119_119(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w41_9 <= CompressorOut_bh30_119_119(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_120_180 <= heap_bh30_w41_8 & heap_bh30_w41_7 & heap_bh30_w41_6;
   CompressorIn_bh30_120_181 <= heap_bh30_w42_8 & heap_bh30_w42_7;
      Compressor_bh30_120: Compressor_23_3
      port map ( R => CompressorOut_bh30_120_120,
                 X0 => CompressorIn_bh30_120_180,
                 X1 => CompressorIn_bh30_120_181);
   heap_bh30_w41_10 <= CompressorOut_bh30_120_120(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w42_9 <= CompressorOut_bh30_120_120(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w43_9 <= CompressorOut_bh30_120_120(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_121_182 <= heap_bh30_w43_8 & heap_bh30_w43_7 & heap_bh30_w43_6;
   CompressorIn_bh30_121_183 <= heap_bh30_w44_8 & heap_bh30_w44_7;
      Compressor_bh30_121: Compressor_23_3
      port map ( R => CompressorOut_bh30_121_121,
                 X0 => CompressorIn_bh30_121_182,
                 X1 => CompressorIn_bh30_121_183);
   heap_bh30_w43_10 <= CompressorOut_bh30_121_121(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w44_9 <= CompressorOut_bh30_121_121(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w45_9 <= CompressorOut_bh30_121_121(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_122_184 <= heap_bh30_w45_8 & heap_bh30_w45_7 & heap_bh30_w45_6;
   CompressorIn_bh30_122_185 <= heap_bh30_w46_8 & heap_bh30_w46_7;
      Compressor_bh30_122: Compressor_23_3
      port map ( R => CompressorOut_bh30_122_122,
                 X0 => CompressorIn_bh30_122_184,
                 X1 => CompressorIn_bh30_122_185);
   heap_bh30_w45_10 <= CompressorOut_bh30_122_122(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w46_9 <= CompressorOut_bh30_122_122(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w47_9 <= CompressorOut_bh30_122_122(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_123_186 <= heap_bh30_w47_8 & heap_bh30_w47_7 & heap_bh30_w47_6;
   CompressorIn_bh30_123_187 <= heap_bh30_w48_8 & heap_bh30_w48_7;
      Compressor_bh30_123: Compressor_23_3
      port map ( R => CompressorOut_bh30_123_123,
                 X0 => CompressorIn_bh30_123_186,
                 X1 => CompressorIn_bh30_123_187);
   heap_bh30_w47_10 <= CompressorOut_bh30_123_123(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w48_9 <= CompressorOut_bh30_123_123(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w49_9 <= CompressorOut_bh30_123_123(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_124_188 <= heap_bh30_w49_8 & heap_bh30_w49_7 & heap_bh30_w49_6;
   CompressorIn_bh30_124_189 <= heap_bh30_w50_8 & heap_bh30_w50_7;
      Compressor_bh30_124: Compressor_23_3
      port map ( R => CompressorOut_bh30_124_124,
                 X0 => CompressorIn_bh30_124_188,
                 X1 => CompressorIn_bh30_124_189);
   heap_bh30_w49_10 <= CompressorOut_bh30_124_124(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w50_9 <= CompressorOut_bh30_124_124(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w51_9 <= CompressorOut_bh30_124_124(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_125_190 <= heap_bh30_w51_8 & heap_bh30_w51_7 & heap_bh30_w51_6;
   CompressorIn_bh30_125_191 <= heap_bh30_w52_8 & heap_bh30_w52_7;
      Compressor_bh30_125: Compressor_23_3
      port map ( R => CompressorOut_bh30_125_125,
                 X0 => CompressorIn_bh30_125_190,
                 X1 => CompressorIn_bh30_125_191);
   heap_bh30_w51_10 <= CompressorOut_bh30_125_125(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w52_9 <= CompressorOut_bh30_125_125(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w53_9 <= CompressorOut_bh30_125_125(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_126_192 <= heap_bh30_w53_8 & heap_bh30_w53_7 & heap_bh30_w53_6;
   CompressorIn_bh30_126_193 <= heap_bh30_w54_8 & heap_bh30_w54_7;
      Compressor_bh30_126: Compressor_23_3
      port map ( R => CompressorOut_bh30_126_126,
                 X0 => CompressorIn_bh30_126_192,
                 X1 => CompressorIn_bh30_126_193);
   heap_bh30_w53_10 <= CompressorOut_bh30_126_126(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w54_9 <= CompressorOut_bh30_126_126(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w55_9 <= CompressorOut_bh30_126_126(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_127_194 <= heap_bh30_w55_8 & heap_bh30_w55_7 & heap_bh30_w55_6;
   CompressorIn_bh30_127_195 <= heap_bh30_w56_8 & heap_bh30_w56_7;
      Compressor_bh30_127: Compressor_23_3
      port map ( R => CompressorOut_bh30_127_127,
                 X0 => CompressorIn_bh30_127_194,
                 X1 => CompressorIn_bh30_127_195);
   heap_bh30_w55_10 <= CompressorOut_bh30_127_127(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w56_9 <= CompressorOut_bh30_127_127(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w57_9 <= CompressorOut_bh30_127_127(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_128_196 <= heap_bh30_w57_8 & heap_bh30_w57_7 & heap_bh30_w57_6;
   CompressorIn_bh30_128_197 <= heap_bh30_w58_8 & heap_bh30_w58_7;
      Compressor_bh30_128: Compressor_23_3
      port map ( R => CompressorOut_bh30_128_128,
                 X0 => CompressorIn_bh30_128_196,
                 X1 => CompressorIn_bh30_128_197);
   heap_bh30_w57_10 <= CompressorOut_bh30_128_128(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w58_9 <= CompressorOut_bh30_128_128(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w59_9 <= CompressorOut_bh30_128_128(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_129_198 <= heap_bh30_w59_8 & heap_bh30_w59_7 & heap_bh30_w59_6;
   CompressorIn_bh30_129_199 <= heap_bh30_w60_8 & heap_bh30_w60_7;
      Compressor_bh30_129: Compressor_23_3
      port map ( R => CompressorOut_bh30_129_129,
                 X0 => CompressorIn_bh30_129_198,
                 X1 => CompressorIn_bh30_129_199);
   heap_bh30_w59_10 <= CompressorOut_bh30_129_129(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w60_9 <= CompressorOut_bh30_129_129(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w61_9 <= CompressorOut_bh30_129_129(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_130_200 <= heap_bh30_w61_8 & heap_bh30_w61_7 & heap_bh30_w61_6;
   CompressorIn_bh30_130_201 <= heap_bh30_w62_8 & heap_bh30_w62_7;
      Compressor_bh30_130: Compressor_23_3
      port map ( R => CompressorOut_bh30_130_130,
                 X0 => CompressorIn_bh30_130_200,
                 X1 => CompressorIn_bh30_130_201);
   heap_bh30_w61_10 <= CompressorOut_bh30_130_130(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w62_9 <= CompressorOut_bh30_130_130(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w63_9 <= CompressorOut_bh30_130_130(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_131_202 <= heap_bh30_w63_8 & heap_bh30_w63_7 & heap_bh30_w63_6;
   CompressorIn_bh30_131_203 <= heap_bh30_w64_8 & heap_bh30_w64_7;
      Compressor_bh30_131: Compressor_23_3
      port map ( R => CompressorOut_bh30_131_131,
                 X0 => CompressorIn_bh30_131_202,
                 X1 => CompressorIn_bh30_131_203);
   heap_bh30_w63_10 <= CompressorOut_bh30_131_131(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w64_9 <= CompressorOut_bh30_131_131(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w65_9 <= CompressorOut_bh30_131_131(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_132_204 <= heap_bh30_w65_8 & heap_bh30_w65_7 & heap_bh30_w65_6;
   CompressorIn_bh30_132_205 <= heap_bh30_w66_8 & heap_bh30_w66_7;
      Compressor_bh30_132: Compressor_23_3
      port map ( R => CompressorOut_bh30_132_132,
                 X0 => CompressorIn_bh30_132_204,
                 X1 => CompressorIn_bh30_132_205);
   heap_bh30_w65_10 <= CompressorOut_bh30_132_132(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w66_9 <= CompressorOut_bh30_132_132(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w67_9 <= CompressorOut_bh30_132_132(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_133_206 <= heap_bh30_w69_7 & heap_bh30_w69_6 & heap_bh30_w69_5;
   CompressorIn_bh30_133_207 <= heap_bh30_w70_6 & heap_bh30_w70_5;
      Compressor_bh30_133: Compressor_23_3
      port map ( R => CompressorOut_bh30_133_133,
                 X0 => CompressorIn_bh30_133_206,
                 X1 => CompressorIn_bh30_133_207);
   heap_bh30_w69_9 <= CompressorOut_bh30_133_133(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w70_7 <= CompressorOut_bh30_133_133(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w71_7 <= CompressorOut_bh30_133_133(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_134_208 <= heap_bh30_w71_6 & heap_bh30_w71_5 & heap_bh30_w71_4;
   CompressorIn_bh30_134_209 <= heap_bh30_w72_5 & heap_bh30_w72_4;
      Compressor_bh30_134: Compressor_23_3
      port map ( R => CompressorOut_bh30_134_134,
                 X0 => CompressorIn_bh30_134_208,
                 X1 => CompressorIn_bh30_134_209);
   heap_bh30_w71_8 <= CompressorOut_bh30_134_134(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w72_6 <= CompressorOut_bh30_134_134(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w73_7 <= CompressorOut_bh30_134_134(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_135_210 <= heap_bh30_w73_6 & heap_bh30_w73_5 & heap_bh30_w73_4;
   CompressorIn_bh30_135_211 <= heap_bh30_w74_5 & heap_bh30_w74_4;
      Compressor_bh30_135: Compressor_23_3
      port map ( R => CompressorOut_bh30_135_135,
                 X0 => CompressorIn_bh30_135_210,
                 X1 => CompressorIn_bh30_135_211);
   heap_bh30_w73_8 <= CompressorOut_bh30_135_135(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w74_6 <= CompressorOut_bh30_135_135(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w75_7 <= CompressorOut_bh30_135_135(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_136_212 <= heap_bh30_w75_6 & heap_bh30_w75_5 & heap_bh30_w75_4;
   CompressorIn_bh30_136_213 <= heap_bh30_w76_5 & heap_bh30_w76_4;
      Compressor_bh30_136: Compressor_23_3
      port map ( R => CompressorOut_bh30_136_136,
                 X0 => CompressorIn_bh30_136_212,
                 X1 => CompressorIn_bh30_136_213);
   heap_bh30_w75_8 <= CompressorOut_bh30_136_136(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w76_6 <= CompressorOut_bh30_136_136(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w77_7 <= CompressorOut_bh30_136_136(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_137_214 <= heap_bh30_w77_6 & heap_bh30_w77_5 & heap_bh30_w77_4;
   CompressorIn_bh30_137_215 <= heap_bh30_w78_5 & heap_bh30_w78_4;
      Compressor_bh30_137: Compressor_23_3
      port map ( R => CompressorOut_bh30_137_137,
                 X0 => CompressorIn_bh30_137_214,
                 X1 => CompressorIn_bh30_137_215);
   heap_bh30_w77_8 <= CompressorOut_bh30_137_137(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w78_6 <= CompressorOut_bh30_137_137(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w79_7 <= CompressorOut_bh30_137_137(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_138_216 <= heap_bh30_w79_6 & heap_bh30_w79_5 & heap_bh30_w79_4;
   CompressorIn_bh30_138_217 <= heap_bh30_w80_5 & heap_bh30_w80_4;
      Compressor_bh30_138: Compressor_23_3
      port map ( R => CompressorOut_bh30_138_138,
                 X0 => CompressorIn_bh30_138_216,
                 X1 => CompressorIn_bh30_138_217);
   heap_bh30_w79_8 <= CompressorOut_bh30_138_138(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w80_6 <= CompressorOut_bh30_138_138(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w81_7 <= CompressorOut_bh30_138_138(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_139_218 <= heap_bh30_w81_6 & heap_bh30_w81_5 & heap_bh30_w81_4;
   CompressorIn_bh30_139_219 <= heap_bh30_w82_5 & heap_bh30_w82_4;
      Compressor_bh30_139: Compressor_23_3
      port map ( R => CompressorOut_bh30_139_139,
                 X0 => CompressorIn_bh30_139_218,
                 X1 => CompressorIn_bh30_139_219);
   heap_bh30_w81_8 <= CompressorOut_bh30_139_139(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w82_6 <= CompressorOut_bh30_139_139(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w83_7 <= CompressorOut_bh30_139_139(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_140_220 <= heap_bh30_w83_6 & heap_bh30_w83_5 & heap_bh30_w83_4;
   CompressorIn_bh30_140_221 <= heap_bh30_w84_1 & heap_bh30_w84_0;
      Compressor_bh30_140: Compressor_23_3
      port map ( R => CompressorOut_bh30_140_140,
                 X0 => CompressorIn_bh30_140_220,
                 X1 => CompressorIn_bh30_140_221);
   heap_bh30_w83_8 <= CompressorOut_bh30_140_140(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w84_4 <= CompressorOut_bh30_140_140(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w85_5 <= CompressorOut_bh30_140_140(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_141_222 <= heap_bh30_w95_1 & heap_bh30_w95_0 & heap_bh30_w95_2;
   CompressorIn_bh30_141_223 <= heap_bh30_w96_1 & heap_bh30_w96_0;
      Compressor_bh30_141: Compressor_23_3
      port map ( R => CompressorOut_bh30_141_141,
                 X0 => CompressorIn_bh30_141_222,
                 X1 => CompressorIn_bh30_141_223);
   heap_bh30_w95_3 <= CompressorOut_bh30_141_141(0); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w96_2 <= CompressorOut_bh30_141_141(1); -- cycle= 0 cp= 3.44844e-09
   heap_bh30_w97_2 <= CompressorOut_bh30_141_141(2); -- cycle= 0 cp= 3.44844e-09

   CompressorIn_bh30_142_224 <= heap_bh30_w7_12 & heap_bh30_w7_11 & heap_bh30_w7_13;
   CompressorIn_bh30_142_225 <= heap_bh30_w8_14 & heap_bh30_w8_13;
      Compressor_bh30_142: Compressor_23_3
      port map ( R => CompressorOut_bh30_142_142,
                 X0 => CompressorIn_bh30_142_224,
                 X1 => CompressorIn_bh30_142_225);
   heap_bh30_w7_14 <= CompressorOut_bh30_142_142(0); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w8_15 <= CompressorOut_bh30_142_142(1); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w9_16 <= CompressorOut_bh30_142_142(2); -- cycle= 0 cp= 3.97916e-09

   CompressorIn_bh30_143_226 <= heap_bh30_w15_10 & heap_bh30_w15_9 & heap_bh30_w15_12;
   CompressorIn_bh30_143_227 <= heap_bh30_w16_10 & heap_bh30_w16_9;
      Compressor_bh30_143: Compressor_23_3
      port map ( R => CompressorOut_bh30_143_143,
                 X0 => CompressorIn_bh30_143_226,
                 X1 => CompressorIn_bh30_143_227);
   heap_bh30_w15_13 <= CompressorOut_bh30_143_143(0); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w16_11 <= CompressorOut_bh30_143_143(1); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w17_8 <= CompressorOut_bh30_143_143(2); -- cycle= 0 cp= 3.97916e-09

   CompressorIn_bh30_144_228 <= heap_bh30_w68_6 & heap_bh30_w68_5 & heap_bh30_w68_8;
   CompressorIn_bh30_144_229 <= heap_bh30_w69_9 & heap_bh30_w69_8;
      Compressor_bh30_144: Compressor_23_3
      port map ( R => CompressorOut_bh30_144_144,
                 X0 => CompressorIn_bh30_144_228,
                 X1 => CompressorIn_bh30_144_229);
   heap_bh30_w68_9 <= CompressorOut_bh30_144_144(0); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w69_10 <= CompressorOut_bh30_144_144(1); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w70_8 <= CompressorOut_bh30_144_144(2); -- cycle= 0 cp= 3.97916e-09

   CompressorIn_bh30_145_230 <= heap_bh30_w85_4 & heap_bh30_w85_3 & heap_bh30_w85_5;
   CompressorIn_bh30_145_231 <= heap_bh30_w86_0 & heap_bh30_w86_3;
      Compressor_bh30_145: Compressor_23_3
      port map ( R => CompressorOut_bh30_145_145,
                 X0 => CompressorIn_bh30_145_230,
                 X1 => CompressorIn_bh30_145_231);
   heap_bh30_w85_6 <= CompressorOut_bh30_145_145(0); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w86_4 <= CompressorOut_bh30_145_145(1); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w87_5 <= CompressorOut_bh30_145_145(2); -- cycle= 0 cp= 3.97916e-09

   CompressorIn_bh30_146_232 <= heap_bh30_w97_1 & heap_bh30_w97_0 & heap_bh30_w97_2;
   CompressorIn_bh30_146_233 <= heap_bh30_w98_1 & heap_bh30_w98_0;
      Compressor_bh30_146: Compressor_23_3
      port map ( R => CompressorOut_bh30_146_146,
                 X0 => CompressorIn_bh30_146_232,
                 X1 => CompressorIn_bh30_146_233);
   heap_bh30_w97_3 <= CompressorOut_bh30_146_146(0); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w98_2 <= CompressorOut_bh30_146_146(1); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w99_2 <= CompressorOut_bh30_146_146(2); -- cycle= 0 cp= 3.97916e-09

   CompressorIn_bh30_147_234 <= heap_bh30_w13_12 & heap_bh30_w13_11 & heap_bh30_w13_13;
   CompressorIn_bh30_147_235(0) <= heap_bh30_w14_12;
      Compressor_bh30_147: Compressor_13_3
      port map ( R => CompressorOut_bh30_147_147,
                 X0 => CompressorIn_bh30_147_234,
                 X1 => CompressorIn_bh30_147_235);
   heap_bh30_w13_14 <= CompressorOut_bh30_147_147(0); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w14_13 <= CompressorOut_bh30_147_147(1); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w15_14 <= CompressorOut_bh30_147_147(2); -- cycle= 0 cp= 3.97916e-09

   CompressorIn_bh30_148_236 <= heap_bh30_w20_5 & heap_bh30_w20_4 & heap_bh30_w20_6;
   CompressorIn_bh30_148_237(0) <= heap_bh30_w21_7;
      Compressor_bh30_148: Compressor_13_3
      port map ( R => CompressorOut_bh30_148_148,
                 X0 => CompressorIn_bh30_148_236,
                 X1 => CompressorIn_bh30_148_237);
   heap_bh30_w20_7 <= CompressorOut_bh30_148_148(0); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w21_8 <= CompressorOut_bh30_148_148(1); -- cycle= 0 cp= 3.97916e-09
   heap_bh30_w22_7 <= CompressorOut_bh30_148_148(2); -- cycle= 0 cp= 3.97916e-09

   CompressorIn_bh30_149_238 <= heap_bh30_w70_4 & heap_bh30_w70_7 & heap_bh30_w70_8;
   CompressorIn_bh30_149_239 <= heap_bh30_w71_8 & heap_bh30_w71_7;
      Compressor_bh30_149: Compressor_23_3
      port map ( R => CompressorOut_bh30_149_149,
                 X0 => CompressorIn_bh30_149_238,
                 X1 => CompressorIn_bh30_149_239);
   heap_bh30_w70_9 <= CompressorOut_bh30_149_149(0); -- cycle= 0 cp= 4.50988e-09
   heap_bh30_w71_9 <= CompressorOut_bh30_149_149(1); -- cycle= 0 cp= 4.50988e-09
   heap_bh30_w72_7 <= CompressorOut_bh30_149_149(2); -- cycle= 0 cp= 4.50988e-09

   CompressorIn_bh30_150_240 <= heap_bh30_w87_4 & heap_bh30_w87_3 & heap_bh30_w87_5;
   CompressorIn_bh30_150_241 <= heap_bh30_w88_0 & heap_bh30_w88_3;
      Compressor_bh30_150: Compressor_23_3
      port map ( R => CompressorOut_bh30_150_150,
                 X0 => CompressorIn_bh30_150_240,
                 X1 => CompressorIn_bh30_150_241);
   heap_bh30_w87_6 <= CompressorOut_bh30_150_150(0); -- cycle= 0 cp= 4.50988e-09
   heap_bh30_w88_4 <= CompressorOut_bh30_150_150(1); -- cycle= 0 cp= 4.50988e-09
   heap_bh30_w89_5 <= CompressorOut_bh30_150_150(2); -- cycle= 0 cp= 4.50988e-09

   CompressorIn_bh30_151_242 <= heap_bh30_w99_1 & heap_bh30_w99_0 & heap_bh30_w99_2;
   CompressorIn_bh30_151_243 <= heap_bh30_w100_1 & heap_bh30_w100_0;
      Compressor_bh30_151: Compressor_23_3
      port map ( R => CompressorOut_bh30_151_151,
                 X0 => CompressorIn_bh30_151_242,
                 X1 => CompressorIn_bh30_151_243);
   heap_bh30_w99_3 <= CompressorOut_bh30_151_151(0); -- cycle= 0 cp= 4.50988e-09
   heap_bh30_w100_2 <= CompressorOut_bh30_151_151(1); -- cycle= 0 cp= 4.50988e-09
   heap_bh30_w101_1 <= CompressorOut_bh30_151_151(2); -- cycle= 0 cp= 4.50988e-09

   CompressorIn_bh30_152_244 <= heap_bh30_w89_4 & heap_bh30_w89_3 & heap_bh30_w89_5;
   CompressorIn_bh30_152_245 <= heap_bh30_w90_0 & heap_bh30_w90_3;
      Compressor_bh30_152: Compressor_23_3
      port map ( R => CompressorOut_bh30_152_152,
                 X0 => CompressorIn_bh30_152_244,
                 X1 => CompressorIn_bh30_152_245);
   heap_bh30_w89_6 <= CompressorOut_bh30_152_152(0); -- cycle= 0 cp= 5.0406e-09
   heap_bh30_w90_4 <= CompressorOut_bh30_152_152(1); -- cycle= 0 cp= 5.0406e-09
   heap_bh30_w91_5 <= CompressorOut_bh30_152_152(2); -- cycle= 0 cp= 5.0406e-09

   CompressorIn_bh30_153_246 <= heap_bh30_w91_4 & heap_bh30_w91_3 & heap_bh30_w91_5;
   CompressorIn_bh30_153_247 <= heap_bh30_w92_0 & heap_bh30_w92_3;
      Compressor_bh30_153: Compressor_23_3
      port map ( R => CompressorOut_bh30_153_153,
                 X0 => CompressorIn_bh30_153_246,
                 X1 => CompressorIn_bh30_153_247);
   heap_bh30_w91_6 <= CompressorOut_bh30_153_153(0); -- cycle= 0 cp= 5.57132e-09
   heap_bh30_w92_4 <= CompressorOut_bh30_153_153(1); -- cycle= 0 cp= 5.57132e-09
   heap_bh30_w93_5 <= CompressorOut_bh30_153_153(2); -- cycle= 0 cp= 5.57132e-09

   CompressorIn_bh30_154_248 <= heap_bh30_w93_4 & heap_bh30_w93_3 & heap_bh30_w93_5;
   CompressorIn_bh30_154_249(0) <= heap_bh30_w94_2;
      Compressor_bh30_154: Compressor_13_3
      port map ( R => CompressorOut_bh30_154_154,
                 X0 => CompressorIn_bh30_154_248,
                 X1 => CompressorIn_bh30_154_249);
   heap_bh30_w93_6 <= CompressorOut_bh30_154_154(0); -- cycle= 0 cp= 6.10204e-09
   heap_bh30_w94_3 <= CompressorOut_bh30_154_154(1); -- cycle= 0 cp= 6.10204e-09
   heap_bh30_w95_4 <= CompressorOut_bh30_154_154(2); -- cycle= 0 cp= 6.10204e-09
   finalAdderIn0_bh30 <= "0" & heap_bh30_w117_0 & heap_bh30_w116_0 & heap_bh30_w115_0 & heap_bh30_w114_0 & heap_bh30_w113_0 & heap_bh30_w112_0 & heap_bh30_w111_0 & heap_bh30_w110_0 & heap_bh30_w109_0 & heap_bh30_w108_0 & heap_bh30_w107_0 & heap_bh30_w106_0 & heap_bh30_w105_0 & heap_bh30_w104_0 & heap_bh30_w103_0 & heap_bh30_w102_0 & heap_bh30_w101_0 & heap_bh30_w100_2 & heap_bh30_w99_3 & heap_bh30_w98_2 & heap_bh30_w97_3 & heap_bh30_w96_2 & heap_bh30_w95_3 & heap_bh30_w94_3 & heap_bh30_w93_6 & heap_bh30_w92_4 & heap_bh30_w91_6 & heap_bh30_w90_4 & heap_bh30_w89_6 & heap_bh30_w88_4 & heap_bh30_w87_6 & heap_bh30_w86_4 & heap_bh30_w85_6 & heap_bh30_w84_3 & heap_bh30_w83_8 & heap_bh30_w82_6 & heap_bh30_w81_8 & heap_bh30_w80_6 & heap_bh30_w79_8 & heap_bh30_w78_6 & heap_bh30_w77_8 & heap_bh30_w76_6 & heap_bh30_w75_8 & heap_bh30_w74_6 & heap_bh30_w73_8 & heap_bh30_w72_6 & heap_bh30_w71_9 & heap_bh30_w70_9 & heap_bh30_w69_10 & heap_bh30_w68_9 & heap_bh30_w67_9 & heap_bh30_w66_6 & heap_bh30_w65_10 & heap_bh30_w64_6 & heap_bh30_w63_10 & heap_bh30_w62_6 & heap_bh30_w61_10 & heap_bh30_w60_6 & heap_bh30_w59_10 & heap_bh30_w58_6 & heap_bh30_w57_10 & heap_bh30_w56_6 & heap_bh30_w55_10 & heap_bh30_w54_6 & heap_bh30_w53_10 & heap_bh30_w52_6 & heap_bh30_w51_10 & heap_bh30_w50_6 & heap_bh30_w49_10 & heap_bh30_w48_6 & heap_bh30_w47_10 & heap_bh30_w46_6 & heap_bh30_w45_10 & heap_bh30_w44_6 & heap_bh30_w43_10 & heap_bh30_w42_6 & heap_bh30_w41_10 & heap_bh30_w40_6 & heap_bh30_w39_10 & heap_bh30_w38_6 & heap_bh30_w37_10 & heap_bh30_w36_6 & heap_bh30_w35_10 & heap_bh30_w34_6 & heap_bh30_w33_10 & heap_bh30_w32_6 & heap_bh30_w31_10 & heap_bh30_w30_6 & heap_bh30_w29_10 & heap_bh30_w28_5 & heap_bh30_w27_9 & heap_bh30_w26_7 & heap_bh30_w25_8 & heap_bh30_w24_6 & heap_bh30_w23_8 & heap_bh30_w22_6 & heap_bh30_w21_8 & heap_bh30_w20_7 & heap_bh30_w19_4 & heap_bh30_w18_8 & heap_bh30_w17_7 & heap_bh30_w16_11 & heap_bh30_w15_14 & heap_bh30_w14_13 & heap_bh30_w13_14 & heap_bh30_w12_16 & heap_bh30_w11_15 & heap_bh30_w10_14 & heap_bh30_w9_15 & heap_bh30_w8_15 & heap_bh30_w7_14 & heap_bh30_w6_11 & heap_bh30_w5_12 & heap_bh30_w4_8 & heap_bh30_w3_7 & heap_bh30_w2_6 & heap_bh30_w1_0 & heap_bh30_w0_0;
   finalAdderIn1_bh30 <= "0" & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & heap_bh30_w101_1 & '0' & '0' & '0' & '0' & '0' & heap_bh30_w95_4 & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & heap_bh30_w84_4 & heap_bh30_w83_7 & '0' & heap_bh30_w81_7 & '0' & heap_bh30_w79_7 & '0' & heap_bh30_w77_7 & '0' & heap_bh30_w75_7 & '0' & heap_bh30_w73_7 & heap_bh30_w72_7 & '0' & '0' & '0' & '0' & heap_bh30_w67_8 & heap_bh30_w66_9 & heap_bh30_w65_9 & heap_bh30_w64_9 & heap_bh30_w63_9 & heap_bh30_w62_9 & heap_bh30_w61_9 & heap_bh30_w60_9 & heap_bh30_w59_9 & heap_bh30_w58_9 & heap_bh30_w57_9 & heap_bh30_w56_9 & heap_bh30_w55_9 & heap_bh30_w54_9 & heap_bh30_w53_9 & heap_bh30_w52_9 & heap_bh30_w51_9 & heap_bh30_w50_9 & heap_bh30_w49_9 & heap_bh30_w48_9 & heap_bh30_w47_9 & heap_bh30_w46_9 & heap_bh30_w45_9 & heap_bh30_w44_9 & heap_bh30_w43_9 & heap_bh30_w42_9 & heap_bh30_w41_9 & heap_bh30_w40_9 & heap_bh30_w39_9 & heap_bh30_w38_9 & heap_bh30_w37_9 & heap_bh30_w36_9 & heap_bh30_w35_9 & heap_bh30_w34_9 & heap_bh30_w33_9 & heap_bh30_w32_9 & heap_bh30_w31_9 & heap_bh30_w30_9 & heap_bh30_w29_9 & heap_bh30_w28_8 & heap_bh30_w27_8 & '0' & heap_bh30_w25_7 & '0' & heap_bh30_w23_7 & heap_bh30_w22_7 & '0' & '0' & heap_bh30_w19_7 & heap_bh30_w18_7 & heap_bh30_w17_8 & '0' & heap_bh30_w15_13 & '0' & '0' & '0' & heap_bh30_w11_14 & '0' & heap_bh30_w9_16 & '0' & '0' & heap_bh30_w6_12 & '0' & heap_bh30_w4_7 & heap_bh30_w3_6 & '0' & heap_bh30_w1_1 & heap_bh30_w0_1;
   finalAdderCin_bh30 <= '0';
      Adder_final30_0: IntAdder_119_f400_uid376
      port map ( Cin => finalAdderCin_bh30,
                 R => finalAdderOut_bh30,
                 X => finalAdderIn0_bh30,
                 Y => finalAdderIn1_bh30);
   -- concatenate all the compressed chunks
   CompressionResult30 <= finalAdderOut_bh30;
   -- End of code generated by BitHeap::generateCompressorVHDL
   R <= CompressionResult30(117 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                   RightShifter_126_by_max_68_comb_uid386
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

entity RightShifter_126_by_max_68_comb_uid386 is
   port ( X : in  std_logic_vector(125 downto 0);
          S : in  std_logic_vector(6 downto 0);
          R : out  std_logic_vector(193 downto 0)   );
end entity;

architecture arch of RightShifter_126_by_max_68_comb_uid386 is
signal level0 :  std_logic_vector(125 downto 0);
signal ps :  std_logic_vector(6 downto 0);
signal level1 :  std_logic_vector(126 downto 0);
signal level2 :  std_logic_vector(128 downto 0);
signal level3 :  std_logic_vector(132 downto 0);
signal level4 :  std_logic_vector(140 downto 0);
signal level5 :  std_logic_vector(156 downto 0);
signal level6 :  std_logic_vector(188 downto 0);
signal level7 :  std_logic_vector(252 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<=  (0 downto 0 => '0') & level0 when ps(0) = '1' else    level0 & (0 downto 0 => '0');
   level2<=  (1 downto 0 => '0') & level1 when ps(1) = '1' else    level1 & (1 downto 0 => '0');
   level3<=  (3 downto 0 => '0') & level2 when ps(2) = '1' else    level2 & (3 downto 0 => '0');
   level4<=  (7 downto 0 => '0') & level3 when ps(3) = '1' else    level3 & (7 downto 0 => '0');
   level5<=  (15 downto 0 => '0') & level4 when ps(4) = '1' else    level4 & (15 downto 0 => '0');
   level6<=  (31 downto 0 => '0') & level5 when ps(5) = '1' else    level5 & (31 downto 0 => '0');
   level7<=  (63 downto 0 => '0') & level6 when ps(6) = '1' else    level6 & (63 downto 0 => '0');
   R <= level7(252 downto 59);
end architecture;

--------------------------------------------------------------------------------
--                          PositMult_68_7_comb_uid2
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

entity PositMult_68_7_comb_uid2 is
   port ( InputA : in  std_logic_vector(67 downto 0);
          InputB : in  std_logic_vector(67 downto 0);
          Output : out  std_logic_vector(67 downto 0)   );
end entity;

architecture arch of PositMult_68_7_comb_uid2 is
   component PositDecoder_68_7_comb_uid4 is
      port ( Input : in  std_logic_vector(67 downto 0);
             Sign : out  std_logic;
             Reg : out  std_logic_vector(7 downto 0);
             Exp : out  std_logic_vector(6 downto 0);
             Frac : out  std_logic_vector(58 downto 0);
             z : out  std_logic;
             inf : out  std_logic   );
   end component;

   component PositDecoder_68_7_comb_uid16 is
      port ( Input : in  std_logic_vector(67 downto 0);
             Sign : out  std_logic;
             Reg : out  std_logic_vector(7 downto 0);
             Exp : out  std_logic_vector(6 downto 0);
             Frac : out  std_logic_vector(58 downto 0);
             z : out  std_logic;
             inf : out  std_logic   );
   end component;

   component IntMultiplier_UsingDSP_59_59_118_unsigned_comb_uid28 is
      port ( X : in  std_logic_vector(58 downto 0);
             Y : in  std_logic_vector(58 downto 0);
             R : out  std_logic_vector(117 downto 0)   );
   end component;

   component RightShifter_126_by_max_68_comb_uid386 is
      port ( X : in  std_logic_vector(125 downto 0);
             S : in  std_logic_vector(6 downto 0);
             R : out  std_logic_vector(193 downto 0)   );
   end component;

signal sign_A :  std_logic;
signal reg_A :  std_logic_vector(7 downto 0);
signal exp_A :  std_logic_vector(6 downto 0);
signal frac_A :  std_logic_vector(58 downto 0);
signal z_A :  std_logic;
signal inf_A :  std_logic;
signal sign_B :  std_logic;
signal reg_B :  std_logic_vector(7 downto 0);
signal exp_B :  std_logic_vector(6 downto 0);
signal frac_B :  std_logic_vector(58 downto 0);
signal z_B :  std_logic;
signal inf_B :  std_logic;
signal sf_A :  std_logic_vector(14 downto 0);
signal sf_B :  std_logic_vector(14 downto 0);
signal sign :  std_logic;
signal z :  std_logic;
signal inf :  std_logic;
signal frac_mult :  std_logic_vector(117 downto 0);
signal ovf_m :  std_logic;
signal normFrac :  std_logic_vector(118 downto 0);
signal sf_mult :  std_logic_vector(15 downto 0);
signal sf_sign :  std_logic;
signal nzero :  std_logic;
signal ExpBits :  std_logic_vector(6 downto 0);
signal RegimeAns_tmp :  std_logic_vector(6 downto 0);
signal RegimeAns :  std_logic_vector(6 downto 0);
signal ovf_reg :  std_logic;
signal FinalRegime :  std_logic_vector(6 downto 0);
signal ovf_regF :  std_logic;
signal FinalExp :  std_logic_vector(6 downto 0);
signal tmp1 :  std_logic_vector(125 downto 0);
signal tmp2 :  std_logic_vector(125 downto 0);
signal shift_neg :  std_logic_vector(6 downto 0);
signal shift_pos :  std_logic_vector(6 downto 0);
signal shifter_in :  std_logic_vector(125 downto 0);
signal shifter_S :  std_logic_vector(6 downto 0);
signal shifter_out :  std_logic_vector(193 downto 0);
signal tmp_ans :  std_logic_vector(66 downto 0);
signal LSB :  std_logic;
signal G :  std_logic;
signal R :  std_logic;
signal S :  std_logic;
signal round :  std_logic;
begin
------------------------------- Data Extraction -------------------------------
   decoderA: PositDecoder_68_7_comb_uid4
      port map ( Exp => exp_A,
                 Frac => frac_A,
                 Input => InputA,
                 Reg => reg_A,
                 Sign => sign_A,
                 inf => inf_A,
                 z => z_A);
   decoderB: PositDecoder_68_7_comb_uid16
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
   mult: IntMultiplier_UsingDSP_59_59_118_unsigned_comb_uid28
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
   RegimeAns_tmp <= sf_mult(13 downto 7);
   -- Get Regime's absolute value
   RegimeAns <= (NOT RegimeAns_tmp)+1 when sf_sign = '1' else RegimeAns_tmp;
   -- Check for Regime overflow
   ovf_reg <= RegimeAns(RegimeAns'high);
   FinalRegime <= '0' & "111111" when ovf_reg = '1' else RegimeAns;
   ovf_regF <= '1' when FinalRegime = ('0' & "111111") else '0';
   FinalExp <= "0000000" when ((ovf_reg = '1') OR (ovf_regF = '1') OR (nzero='0')) else ExpBits;
------------------------------- Packing Stage 1 -------------------------------
   tmp1 <= nzero & '0' & FinalExp & normFrac(116 downto 0);
   tmp2 <= '0' & nzero & FinalExp & normFrac(116 downto 0);
   shift_neg <= FinalRegime - 2 when (ovf_regF = '1') else FinalRegime - 1;
   shift_pos <= FinalRegime - 1 when (ovf_regF = '1') else FinalRegime;
   shifter_in <= tmp2 when sf_sign = '1' else tmp1;
   shifter_S <= shift_neg when sf_sign = '1' else shift_pos;
   RightShifterComponent: RightShifter_126_by_max_68_comb_uid386
      port map ( R => shifter_out,
                 S => shifter_S,
                 X => shifter_in);
   tmp_ans <= shifter_out(193 downto 127);
--------------------- Packing Stage 2 - Unbiased Rounding ---------------------
   LSB <= shifter_out(127);
   G <= shifter_out(126);
   R <= shifter_out(125);
   S <= '0' when shifter_out(124 downto 0) = 0 else '1';
   round <= G AND (LSB OR R OR S) when NOT((ovf_reg OR ovf_regF) = '1') else '0';
   Output <= '1' & "0000000000000000000000000000000000000000000000000000000000000000000" when inf = '1' else "00000000000000000000000000000000000000000000000000000000000000000000" when z = '1' else '0' & (tmp_ans + round) when sign = '0' else NOT('0' & (tmp_ans + round))+1;
end architecture;

