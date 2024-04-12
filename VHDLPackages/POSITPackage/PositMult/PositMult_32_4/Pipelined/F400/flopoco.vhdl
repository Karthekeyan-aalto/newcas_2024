

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;
entity reg is
 port (
clk: in std_logic;
ram_read_en: in std_logic;
ram_data_in: in std_logic_vector(31 downto 0);
ram_data_out: out std_logic_vector(31 downto 0));
end reg ;

architecture reg  of reg  is 
type ram_array is array (0 to 9000) of std_logic_vector(31 downto 0);
signal ram_address_in: integer range 0 to 9000:=9000;
signal ram_address_out: integer range 0 to 9000:=9000;
signal ram:ram_array:=(others=>(others=>'0'));
signal ram_data_in_sub: std_logic_vector(31 downto 0);
signal ram_write_en: std_logic;
signal count_reg: integer:=0;
begin


--wait for each input event, strat to write from bottom
process(clk)  
begin
if rising_edge(clk) then
ram_data_in_sub<=ram_data_in;
end if;
end process;

process(clk)
begin
if ( clk ='1' and ram_address_in >0  and ram_data_in>=0) then
ram_address_in <= ram_address_in -1;
end if;
end process;


process(ram_data_in,clk)
begin
if (ram_data_in /= ram_data_in_sub and ram_address_in >0) then
ram_write_en <= '1';
end if;
end process;



process(ram_data_in,clk)
begin
if (ram_write_en = '1') then
ram(ram_address_in) <= ram_data_in ;
end if;
end process;



process(clk)
begin
if ( clk = '1' and ram_read_en ='1' and ram_address_out>0) then
ram_address_out <= ram_address_out -1;
end if;
end process;

--wait for two input event, this controlled by top level through read_en, strat to read from bottom
process(clk)
begin
if ( clk ='1'  and ram_read_en ='1' ) then
ram_data_out<=ram(ram_address_out);
end if;
end process;

end reg ;










--------------------------------------------------------------------------------
--                    SmallMultTableP3x3r6XuYu_F400_uid33
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin (2007-2012)
--------------------------------------------------------------------------------
library ieee; 
use ieee.std_logic_1164.all;
library work;
entity SmallMultTableP3x3r6XuYu_F400_uid33 is
   port ( clk, rst : in std_logic;
          X : in  std_logic_vector(5 downto 0);
          Y : out  std_logic_vector(5 downto 0)   );
end entity;

architecture arch of SmallMultTableP3x3r6XuYu_F400_uid33 is
signal TableOut :  std_logic_vector(5 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
         end if;
      end process;
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
--                    SmallMultTableP3x3r6XuYu_F400_uid48
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin (2007-2012)
--------------------------------------------------------------------------------
library ieee; 
use ieee.std_logic_1164.all;
library work;
entity SmallMultTableP3x3r6XuYu_F400_uid48 is
   port ( clk, rst : in std_logic;
          X : in  std_logic_vector(5 downto 0);
          Y : out  std_logic_vector(5 downto 0)   );
end entity;

architecture arch of SmallMultTableP3x3r6XuYu_F400_uid48 is
signal TableOut :  std_logic_vector(5 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
         end if;
      end process;
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
--                             LZOC_31_F400_uid6
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, Bogdan Pasca (2007)
--------------------------------------------------------------------------------
-- Pipeline depth: 2 cycles

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity LZOC_31_F400_uid6 is
   port ( clk, rst : in std_logic;
          I : in  std_logic_vector(30 downto 0);
          OZB : in  std_logic;
          O : out  std_logic_vector(4 downto 0)   );
end entity;

architecture arch of LZOC_31_F400_uid6 is
signal sozb, sozb_d1, sozb_d2 :  std_logic;
signal level5 :  std_logic_vector(31 downto 0);
signal digit5, digit5_d1, digit5_d2 :  std_logic;
signal level4, level4_d1 :  std_logic_vector(15 downto 0);
signal digit4, digit4_d1 :  std_logic;
signal level3 :  std_logic_vector(7 downto 0);
signal digit3, digit3_d1 :  std_logic;
signal level2, level2_d1 :  std_logic_vector(3 downto 0);
signal digit2 :  std_logic;
signal level1 :  std_logic_vector(1 downto 0);
signal digit1 :  std_logic;
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            sozb_d1 <=  sozb;
            sozb_d2 <=  sozb_d1;
            digit5_d1 <=  digit5;
            digit5_d2 <=  digit5_d1;
            level4_d1 <=  level4;
            digit4_d1 <=  digit4;
            digit3_d1 <=  digit3;
            level2_d1 <=  level2;
         end if;
      end process;
   sozb <= OZB;
   level5<= I& (0 downto 0 => not(sozb));
   digit5<= '1' when level5(31 downto 16) = (31 downto 16 => sozb) else '0';
   level4<= level5(15 downto 0) when digit5='1' else level5(31 downto 16);
   ----------------Synchro barrier, entering cycle 1----------------
   digit4<= '1' when level4_d1(15 downto 8) = (15 downto 8 => sozb_d1) else '0';
   level3<= level4_d1(7 downto 0) when digit4='1' else level4_d1(15 downto 8);
   digit3<= '1' when level3(7 downto 4) = (7 downto 4 => sozb_d1) else '0';
   level2<= level3(3 downto 0) when digit3='1' else level3(7 downto 4);
   ----------------Synchro barrier, entering cycle 2----------------
   digit2<= '1' when level2_d1(3 downto 2) = (3 downto 2 => sozb_d2) else '0';
   level1<= level2_d1(1 downto 0) when digit2='1' else level2_d1(3 downto 2);
   digit1<= '1' when level1(1 downto 1) = (1 downto 1 => sozb_d2) else '0';
   O <= digit5_d2 & digit4_d1 & digit3_d1 & digit2 & digit1;
end architecture;

--------------------------------------------------------------------------------
--                    LeftShifter_31_by_max_31_F400_uid10
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca, Florent de Dinechin (2008-2011)
--------------------------------------------------------------------------------
-- Pipeline depth: 1 cycles

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity LeftShifter_31_by_max_31_F400_uid10 is
   port ( clk, rst : in std_logic;
          X : in  std_logic_vector(30 downto 0);
          S : in  std_logic_vector(4 downto 0);
          R : out  std_logic_vector(61 downto 0)   );
end entity;

architecture arch of LeftShifter_31_by_max_31_F400_uid10 is
signal level0 :  std_logic_vector(30 downto 0);
signal ps, ps_d1 :  std_logic_vector(4 downto 0);
signal level1 :  std_logic_vector(31 downto 0);
signal level2, level2_d1 :  std_logic_vector(33 downto 0);
signal level3 :  std_logic_vector(37 downto 0);
signal level4 :  std_logic_vector(45 downto 0);
signal level5 :  std_logic_vector(61 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            ps_d1 <=  ps;
            level2_d1 <=  level2;
         end if;
      end process;
   level0<= X;
   ps<= S;
   level1<= level0 & (0 downto 0 => '0') when ps(0)= '1' else     (0 downto 0 => '0') & level0;
   level2<= level1 & (1 downto 0 => '0') when ps(1)= '1' else     (1 downto 0 => '0') & level1;
   ----------------Synchro barrier, entering cycle 1----------------
   level3<= level2_d1 & (3 downto 0 => '0') when ps_d1(2)= '1' else     (3 downto 0 => '0') & level2_d1;
   level4<= level3 & (7 downto 0 => '0') when ps_d1(3)= '1' else     (7 downto 0 => '0') & level3;
   level5<= level4 & (15 downto 0 => '0') when ps_d1(4)= '1' else     (15 downto 0 => '0') & level4;
   R <= level5(61 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                        PositDecoder_32_4_F400_uid4
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Raul Murillo, 2019
--------------------------------------------------------------------------------
-- Pipeline depth: 5 cycles

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PositDecoder_32_4_F400_uid4 is
   port ( clk, rst : in std_logic;
          Input : in  std_logic_vector(31 downto 0);
          Sign : out  std_logic;
          Reg : out  std_logic_vector(5 downto 0);
          Exp : out  std_logic_vector(3 downto 0);
          Frac : out  std_logic_vector(25 downto 0);
          z : out  std_logic;
          inf : out  std_logic   );
end entity;

architecture arch of PositDecoder_32_4_F400_uid4 is
   component LZOC_31_F400_uid6 is
      port ( clk, rst : in std_logic;
             I : in  std_logic_vector(30 downto 0);
             OZB : in  std_logic;
             O : out  std_logic_vector(4 downto 0)   );
   end component;

   component LeftShifter_31_by_max_31_F400_uid10 is
      port ( clk, rst : in std_logic;
             X : in  std_logic_vector(30 downto 0);
             S : in  std_logic_vector(4 downto 0);
             R : out  std_logic_vector(61 downto 0)   );
   end component;

signal nzero, nzero_d1, nzero_d2, nzero_d3, nzero_d4, nzero_d5 :  std_logic;
signal my_sign :  std_logic;
signal rep_sign :  std_logic_vector(30 downto 0);
signal twos, twos_d1, twos_d2, twos_d3 :  std_logic_vector(30 downto 0);
signal rc, rc_d1, rc_d2, rc_d3, rc_d4 :  std_logic;
signal rep_rc :  std_logic_vector(30 downto 0);
signal inv :  std_logic_vector(30 downto 0);
signal zero_var :  std_logic;
signal zc, zc_d1, zc_d2 :  std_logic_vector(4 downto 0);
signal zc_sub, zc_sub_d1, zc_sub_d2 :  std_logic_vector(4 downto 0);
signal shifted_twos, shifted_twos_d1 :  std_logic_vector(61 downto 0);
signal tmp :  std_logic_vector(28 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            nzero_d1 <=  nzero;
            nzero_d2 <=  nzero_d1;
            nzero_d3 <=  nzero_d2;
            nzero_d4 <=  nzero_d3;
            nzero_d5 <=  nzero_d4;
            twos_d1 <=  twos;
            twos_d2 <=  twos_d1;
            twos_d3 <=  twos_d2;
            rc_d1 <=  rc;
            rc_d2 <=  rc_d1;
            rc_d3 <=  rc_d2;
            rc_d4 <=  rc_d3;
            zc_d1 <=  zc;
            zc_d2 <=  zc_d1;
            zc_sub_d1 <=  zc_sub;
            zc_sub_d2 <=  zc_sub_d1;
            shifted_twos_d1 <=  shifted_twos;
         end if;
      end process;
-------------------------------- Special Cases --------------------------------
   nzero <= '0' when Input(30 downto 0) = 0 else '1';
   -- 1 if Input is zero
   z <= Input(31) NOR nzero;
   -- 1 if Input is infinity
   inf <= Input(31) AND (NOT nzero);
------------------------------- Extract Sign bit -------------------------------
   my_sign <= Input(31);
   Sign <= my_sign;
--------------------------- 2's Complement of Input ---------------------------
   rep_sign <= (others => my_sign);
   twos <= (rep_sign XOR Input(30 downto 0)) + my_sign;
   ----------------Synchro barrier, entering cycle 1----------------
   rc <= twos_d1(30);
------------------------ Count leading zeros of regime ------------------------
   rep_rc <= (others => rc);
   -- Invert 2's
   inv <= rep_rc XOR twos_d1;
   zero_var <= '0';
   LZOC_Component: LZOC_31_F400_uid6  -- pipelineDepth=2 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 I => inv,
                 O => zc,
                 OZB => zero_var);
   ----------------Synchro barrier, entering cycle 3----------------
----------------------------- Shift out the regime -----------------------------
   zc_sub <= zc - 1;
   LeftShifterComponent: LeftShifter_31_by_max_31_F400_uid10  -- pipelineDepth=1 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 R => shifted_twos,
                 S => zc_sub,
                 X => twos_d3);
   ----------------Synchro barrier, entering cycle 4----------------
   ----------------Synchro barrier, entering cycle 5----------------
   tmp <= shifted_twos_d1(28 downto 0);
------------------------ Extract fraction and exponent ------------------------
   Frac <= nzero_d5 & tmp(24 downto 0);
   Exp <= tmp(28 downto 25);
-------------------------------- Select regime --------------------------------
   Reg <= '0' & zc_sub_d2 when rc_d4 = '1' else NOT('0' & zc_d2) + 1;
end architecture;

--------------------------------------------------------------------------------
--                             LZOC_31_F400_uid18
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, Bogdan Pasca (2007)
--------------------------------------------------------------------------------
-- Pipeline depth: 2 cycles

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity LZOC_31_F400_uid18 is
   port ( clk, rst : in std_logic;
          I : in  std_logic_vector(30 downto 0);
          OZB : in  std_logic;
          O : out  std_logic_vector(4 downto 0)   );
end entity;

architecture arch of LZOC_31_F400_uid18 is
signal sozb, sozb_d1, sozb_d2 :  std_logic;
signal level5 :  std_logic_vector(31 downto 0);
signal digit5, digit5_d1, digit5_d2 :  std_logic;
signal level4, level4_d1 :  std_logic_vector(15 downto 0);
signal digit4, digit4_d1 :  std_logic;
signal level3 :  std_logic_vector(7 downto 0);
signal digit3, digit3_d1 :  std_logic;
signal level2, level2_d1 :  std_logic_vector(3 downto 0);
signal digit2 :  std_logic;
signal level1 :  std_logic_vector(1 downto 0);
signal digit1 :  std_logic;
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            sozb_d1 <=  sozb;
            sozb_d2 <=  sozb_d1;
            digit5_d1 <=  digit5;
            digit5_d2 <=  digit5_d1;
            level4_d1 <=  level4;
            digit4_d1 <=  digit4;
            digit3_d1 <=  digit3;
            level2_d1 <=  level2;
         end if;
      end process;
   sozb <= OZB;
   level5<= I& (0 downto 0 => not(sozb));
   digit5<= '1' when level5(31 downto 16) = (31 downto 16 => sozb) else '0';
   level4<= level5(15 downto 0) when digit5='1' else level5(31 downto 16);
   ----------------Synchro barrier, entering cycle 1----------------
   digit4<= '1' when level4_d1(15 downto 8) = (15 downto 8 => sozb_d1) else '0';
   level3<= level4_d1(7 downto 0) when digit4='1' else level4_d1(15 downto 8);
   digit3<= '1' when level3(7 downto 4) = (7 downto 4 => sozb_d1) else '0';
   level2<= level3(3 downto 0) when digit3='1' else level3(7 downto 4);
   ----------------Synchro barrier, entering cycle 2----------------
   digit2<= '1' when level2_d1(3 downto 2) = (3 downto 2 => sozb_d2) else '0';
   level1<= level2_d1(1 downto 0) when digit2='1' else level2_d1(3 downto 2);
   digit1<= '1' when level1(1 downto 1) = (1 downto 1 => sozb_d2) else '0';
   O <= digit5_d2 & digit4_d1 & digit3_d1 & digit2 & digit1;
end architecture;

--------------------------------------------------------------------------------
--                    LeftShifter_31_by_max_31_F400_uid22
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca, Florent de Dinechin (2008-2011)
--------------------------------------------------------------------------------
-- Pipeline depth: 1 cycles

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity LeftShifter_31_by_max_31_F400_uid22 is
   port ( clk, rst : in std_logic;
          X : in  std_logic_vector(30 downto 0);
          S : in  std_logic_vector(4 downto 0);
          R : out  std_logic_vector(61 downto 0)   );
end entity;

architecture arch of LeftShifter_31_by_max_31_F400_uid22 is
signal level0 :  std_logic_vector(30 downto 0);
signal ps, ps_d1 :  std_logic_vector(4 downto 0);
signal level1 :  std_logic_vector(31 downto 0);
signal level2, level2_d1 :  std_logic_vector(33 downto 0);
signal level3 :  std_logic_vector(37 downto 0);
signal level4 :  std_logic_vector(45 downto 0);
signal level5 :  std_logic_vector(61 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            ps_d1 <=  ps;
            level2_d1 <=  level2;
         end if;
      end process;
   level0<= X;
   ps<= S;
   level1<= level0 & (0 downto 0 => '0') when ps(0)= '1' else     (0 downto 0 => '0') & level0;
   level2<= level1 & (1 downto 0 => '0') when ps(1)= '1' else     (1 downto 0 => '0') & level1;
   ----------------Synchro barrier, entering cycle 1----------------
   level3<= level2_d1 & (3 downto 0 => '0') when ps_d1(2)= '1' else     (3 downto 0 => '0') & level2_d1;
   level4<= level3 & (7 downto 0 => '0') when ps_d1(3)= '1' else     (7 downto 0 => '0') & level3;
   level5<= level4 & (15 downto 0 => '0') when ps_d1(4)= '1' else     (15 downto 0 => '0') & level4;
   R <= level5(61 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                        PositDecoder_32_4_F400_uid16
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Raul Murillo, 2019
--------------------------------------------------------------------------------
-- Pipeline depth: 5 cycles

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PositDecoder_32_4_F400_uid16 is
   port ( clk, rst : in std_logic;
          Input : in  std_logic_vector(31 downto 0);
          Sign : out  std_logic;
          Reg : out  std_logic_vector(5 downto 0);
          Exp : out  std_logic_vector(3 downto 0);
          Frac : out  std_logic_vector(25 downto 0);
          z : out  std_logic;
          inf : out  std_logic   );
end entity;

architecture arch of PositDecoder_32_4_F400_uid16 is
   component LZOC_31_F400_uid18 is
      port ( clk, rst : in std_logic;
             I : in  std_logic_vector(30 downto 0);
             OZB : in  std_logic;
             O : out  std_logic_vector(4 downto 0)   );
   end component;

   component LeftShifter_31_by_max_31_F400_uid22 is
      port ( clk, rst : in std_logic;
             X : in  std_logic_vector(30 downto 0);
             S : in  std_logic_vector(4 downto 0);
             R : out  std_logic_vector(61 downto 0)   );
   end component;

signal nzero, nzero_d1, nzero_d2, nzero_d3, nzero_d4, nzero_d5 :  std_logic;
signal my_sign :  std_logic;
signal rep_sign :  std_logic_vector(30 downto 0);
signal twos, twos_d1, twos_d2, twos_d3 :  std_logic_vector(30 downto 0);
signal rc, rc_d1, rc_d2, rc_d3, rc_d4 :  std_logic;
signal rep_rc :  std_logic_vector(30 downto 0);
signal inv :  std_logic_vector(30 downto 0);
signal zero_var :  std_logic;
signal zc, zc_d1, zc_d2 :  std_logic_vector(4 downto 0);
signal zc_sub, zc_sub_d1, zc_sub_d2 :  std_logic_vector(4 downto 0);
signal shifted_twos, shifted_twos_d1 :  std_logic_vector(61 downto 0);
signal tmp :  std_logic_vector(28 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            nzero_d1 <=  nzero;
            nzero_d2 <=  nzero_d1;
            nzero_d3 <=  nzero_d2;
            nzero_d4 <=  nzero_d3;
            nzero_d5 <=  nzero_d4;
            twos_d1 <=  twos;
            twos_d2 <=  twos_d1;
            twos_d3 <=  twos_d2;
            rc_d1 <=  rc;
            rc_d2 <=  rc_d1;
            rc_d3 <=  rc_d2;
            rc_d4 <=  rc_d3;
            zc_d1 <=  zc;
            zc_d2 <=  zc_d1;
            zc_sub_d1 <=  zc_sub;
            zc_sub_d2 <=  zc_sub_d1;
            shifted_twos_d1 <=  shifted_twos;
         end if;
      end process;
-------------------------------- Special Cases --------------------------------
   nzero <= '0' when Input(30 downto 0) = 0 else '1';
   -- 1 if Input is zero
   z <= Input(31) NOR nzero;
   -- 1 if Input is infinity
   inf <= Input(31) AND (NOT nzero);
------------------------------- Extract Sign bit -------------------------------
   my_sign <= Input(31);
   Sign <= my_sign;
--------------------------- 2's Complement of Input ---------------------------
   rep_sign <= (others => my_sign);
   twos <= (rep_sign XOR Input(30 downto 0)) + my_sign;
   ----------------Synchro barrier, entering cycle 1----------------
   rc <= twos_d1(30);
------------------------ Count leading zeros of regime ------------------------
   rep_rc <= (others => rc);
   -- Invert 2's
   inv <= rep_rc XOR twos_d1;
   zero_var <= '0';
   LZOC_Component: LZOC_31_F400_uid18  -- pipelineDepth=2 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 I => inv,
                 O => zc,
                 OZB => zero_var);
   ----------------Synchro barrier, entering cycle 3----------------
----------------------------- Shift out the regime -----------------------------
   zc_sub <= zc - 1;
   LeftShifterComponent: LeftShifter_31_by_max_31_F400_uid22  -- pipelineDepth=1 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 R => shifted_twos,
                 S => zc_sub,
                 X => twos_d3);
   ----------------Synchro barrier, entering cycle 4----------------
   ----------------Synchro barrier, entering cycle 5----------------
   tmp <= shifted_twos_d1(28 downto 0);
------------------------ Extract fraction and exponent ------------------------
   Frac <= nzero_d5 & tmp(24 downto 0);
   Exp <= tmp(28 downto 25);
-------------------------------- Select regime --------------------------------
   Reg <= '0' & zc_sub_d2 when rc_d4 = '1' else NOT('0' & zc_d2) + 1;
end architecture;

--------------------------------------------------------------------------------
--                          IntAdder_53_f400_uid129
--                    (IntAdderAlternative_53_F400_uid133)
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca, Florent de Dinechin (2008-2010)
--------------------------------------------------------------------------------
-- Pipeline depth: 1 cycles

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity IntAdder_53_f400_uid129 is
   port ( clk, rst : in std_logic;
          X : in  std_logic_vector(52 downto 0);
          Y : in  std_logic_vector(52 downto 0);
          Cin : in  std_logic;
          R : out  std_logic_vector(52 downto 0)   );
end entity;

architecture arch of IntAdder_53_f400_uid129 is
signal s_sum_l0_idx0 :  std_logic_vector(42 downto 0);
signal s_sum_l0_idx1, s_sum_l0_idx1_d1 :  std_logic_vector(11 downto 0);
signal sum_l0_idx0, sum_l0_idx0_d1 :  std_logic_vector(41 downto 0);
signal c_l0_idx0, c_l0_idx0_d1 :  std_logic_vector(0 downto 0);
signal sum_l0_idx1 :  std_logic_vector(10 downto 0);
signal c_l0_idx1 :  std_logic_vector(0 downto 0);
signal s_sum_l1_idx1 :  std_logic_vector(11 downto 0);
signal sum_l1_idx1 :  std_logic_vector(10 downto 0);
signal c_l1_idx1 :  std_logic_vector(0 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            s_sum_l0_idx1_d1 <=  s_sum_l0_idx1;
            sum_l0_idx0_d1 <=  sum_l0_idx0;
            c_l0_idx0_d1 <=  c_l0_idx0;
         end if;
      end process;
   --Alternative
   s_sum_l0_idx0 <= ( "0" & X(41 downto 0)) + ( "0" & Y(41 downto 0)) + Cin;
   s_sum_l0_idx1 <= ( "0" & X(52 downto 42)) + ( "0" & Y(52 downto 42));
   sum_l0_idx0 <= s_sum_l0_idx0(41 downto 0);
   c_l0_idx0 <= s_sum_l0_idx0(42 downto 42);
   sum_l0_idx1 <= s_sum_l0_idx1(10 downto 0);
   c_l0_idx1 <= s_sum_l0_idx1(11 downto 11);
   ----------------Synchro barrier, entering cycle 1----------------
   s_sum_l1_idx1 <=  s_sum_l0_idx1_d1 + c_l0_idx0_d1(0 downto 0);
   sum_l1_idx1 <= s_sum_l1_idx1(10 downto 0);
   c_l1_idx1 <= s_sum_l1_idx1(11 downto 11);
   R <= sum_l1_idx1(10 downto 0) & sum_l0_idx0_d1(41 downto 0);
end architecture;

--------------------------------------------------------------------------------
--            IntMultiplier_UsingDSP_26_26_52_unsigned_F400_uid28
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, Kinga Illyes, Bogdan Popa, Bogdan Pasca, 2012
--------------------------------------------------------------------------------
-- Pipeline depth: 4 cycles

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
library std;
use std.textio.all;
library work;

entity IntMultiplier_UsingDSP_26_26_52_unsigned_F400_uid28 is
   port ( clk, rst : in std_logic;
          X : in  std_logic_vector(25 downto 0);
          Y : in  std_logic_vector(25 downto 0);
          R : out  std_logic_vector(51 downto 0)   );
end entity;

architecture arch of IntMultiplier_UsingDSP_26_26_52_unsigned_F400_uid28 is
   component IntAdder_53_f400_uid129 is
      port ( clk, rst : in std_logic;
             X : in  std_logic_vector(52 downto 0);
             Y : in  std_logic_vector(52 downto 0);
             Cin : in  std_logic;
             R : out  std_logic_vector(52 downto 0)   );
   end component;

   component SmallMultTableP3x3r6XuYu_F400_uid33 is
      port ( clk, rst : in std_logic;
             X : in  std_logic_vector(5 downto 0);
             Y : out  std_logic_vector(5 downto 0)   );
   end component;

   component SmallMultTableP3x3r6XuYu_F400_uid48 is
      port ( clk, rst : in std_logic;
             X : in  std_logic_vector(5 downto 0);
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

signal XX_m29 :  std_logic_vector(25 downto 0);
signal YY_m29 :  std_logic_vector(25 downto 0);
signal Xp_m29b31 :  std_logic_vector(2 downto 0);
signal Yp_m29b31 :  std_logic_vector(17 downto 0);
signal x_m29b31_0 :  std_logic_vector(2 downto 0);
signal y_m29b31_0 :  std_logic_vector(2 downto 0);
signal y_m29b31_1 :  std_logic_vector(2 downto 0);
signal y_m29b31_2 :  std_logic_vector(2 downto 0);
signal y_m29b31_3 :  std_logic_vector(2 downto 0);
signal y_m29b31_4 :  std_logic_vector(2 downto 0);
signal y_m29b31_5 :  std_logic_vector(2 downto 0);
signal Y0X0_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X0Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w9_0, heap_bh30_w9_0_d1 :  std_logic;
signal heap_bh30_w10_0, heap_bh30_w10_0_d1 :  std_logic;
signal heap_bh30_w11_0, heap_bh30_w11_0_d1 :  std_logic;
signal heap_bh30_w12_0, heap_bh30_w12_0_d1 :  std_logic;
signal Y1X0_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X0Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w11_1, heap_bh30_w11_1_d1 :  std_logic;
signal heap_bh30_w12_1, heap_bh30_w12_1_d1 :  std_logic;
signal heap_bh30_w13_0, heap_bh30_w13_0_d1 :  std_logic;
signal heap_bh30_w14_0, heap_bh30_w14_0_d1 :  std_logic;
signal heap_bh30_w15_0, heap_bh30_w15_0_d1 :  std_logic;
signal Y2X0_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X0Y2_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w14_1, heap_bh30_w14_1_d1 :  std_logic;
signal heap_bh30_w15_1, heap_bh30_w15_1_d1 :  std_logic;
signal heap_bh30_w16_0, heap_bh30_w16_0_d1 :  std_logic;
signal heap_bh30_w17_0, heap_bh30_w17_0_d1 :  std_logic;
signal heap_bh30_w18_0, heap_bh30_w18_0_d1 :  std_logic;
signal Y3X0_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X0Y3_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w17_1, heap_bh30_w17_1_d1 :  std_logic;
signal heap_bh30_w18_1, heap_bh30_w18_1_d1 :  std_logic;
signal heap_bh30_w19_0, heap_bh30_w19_0_d1 :  std_logic;
signal heap_bh30_w20_0, heap_bh30_w20_0_d1 :  std_logic;
signal heap_bh30_w21_0, heap_bh30_w21_0_d1 :  std_logic;
signal Y4X0_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X0Y4_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w20_1, heap_bh30_w20_1_d1 :  std_logic;
signal heap_bh30_w21_1, heap_bh30_w21_1_d1 :  std_logic;
signal heap_bh30_w22_0, heap_bh30_w22_0_d1 :  std_logic;
signal heap_bh30_w23_0, heap_bh30_w23_0_d1 :  std_logic;
signal heap_bh30_w24_0, heap_bh30_w24_0_d1 :  std_logic;
signal Y5X0_31_m29 :  std_logic_vector(5 downto 0);
signal PP31X0Y5_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w23_1, heap_bh30_w23_1_d1 :  std_logic;
signal heap_bh30_w24_1, heap_bh30_w24_1_d1 :  std_logic;
signal heap_bh30_w25_0, heap_bh30_w25_0_d1 :  std_logic;
signal heap_bh30_w26_0, heap_bh30_w26_0_d1 :  std_logic;
signal heap_bh30_w27_0, heap_bh30_w27_0_d1 :  std_logic;
signal Xp_m29b46 :  std_logic_vector(2 downto 0);
signal Yp_m29b46 :  std_logic_vector(8 downto 0);
signal x_m29b46_0 :  std_logic_vector(2 downto 0);
signal y_m29b46_0 :  std_logic_vector(2 downto 0);
signal y_m29b46_1 :  std_logic_vector(2 downto 0);
signal y_m29b46_2 :  std_logic_vector(2 downto 0);
signal Y0X0_46_m29 :  std_logic_vector(5 downto 0);
signal PP46X0Y0_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w0_0, heap_bh30_w0_0_d1, heap_bh30_w0_0_d2, heap_bh30_w0_0_d3 :  std_logic;
signal heap_bh30_w1_0, heap_bh30_w1_0_d1, heap_bh30_w1_0_d2, heap_bh30_w1_0_d3 :  std_logic;
signal heap_bh30_w2_0, heap_bh30_w2_0_d1, heap_bh30_w2_0_d2, heap_bh30_w2_0_d3 :  std_logic;
signal heap_bh30_w3_0, heap_bh30_w3_0_d1 :  std_logic;
signal heap_bh30_w4_0, heap_bh30_w4_0_d1 :  std_logic;
signal Y1X0_46_m29 :  std_logic_vector(5 downto 0);
signal PP46X0Y1_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w3_1, heap_bh30_w3_1_d1 :  std_logic;
signal heap_bh30_w4_1, heap_bh30_w4_1_d1 :  std_logic;
signal heap_bh30_w5_0, heap_bh30_w5_0_d1 :  std_logic;
signal heap_bh30_w6_0, heap_bh30_w6_0_d1 :  std_logic;
signal heap_bh30_w7_0, heap_bh30_w7_0_d1 :  std_logic;
signal Y2X0_46_m29 :  std_logic_vector(5 downto 0);
signal PP46X0Y2_m29 :  std_logic_vector(5 downto 0);
signal heap_bh30_w6_1, heap_bh30_w6_1_d1 :  std_logic;
signal heap_bh30_w7_1, heap_bh30_w7_1_d1 :  std_logic;
signal heap_bh30_w8_0, heap_bh30_w8_0_d1 :  std_logic;
signal heap_bh30_w9_1, heap_bh30_w9_1_d1 :  std_logic;
signal heap_bh30_w10_1, heap_bh30_w10_1_d1 :  std_logic;
signal DSP_bh30_ch0_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w51_0, heap_bh30_w51_0_d1, heap_bh30_w51_0_d2, heap_bh30_w51_0_d3 :  std_logic;
signal heap_bh30_w50_0, heap_bh30_w50_0_d1, heap_bh30_w50_0_d2, heap_bh30_w50_0_d3 :  std_logic;
signal heap_bh30_w49_0, heap_bh30_w49_0_d1, heap_bh30_w49_0_d2, heap_bh30_w49_0_d3 :  std_logic;
signal heap_bh30_w48_0, heap_bh30_w48_0_d1, heap_bh30_w48_0_d2, heap_bh30_w48_0_d3 :  std_logic;
signal heap_bh30_w47_0, heap_bh30_w47_0_d1, heap_bh30_w47_0_d2, heap_bh30_w47_0_d3 :  std_logic;
signal heap_bh30_w46_0, heap_bh30_w46_0_d1, heap_bh30_w46_0_d2, heap_bh30_w46_0_d3 :  std_logic;
signal heap_bh30_w45_0, heap_bh30_w45_0_d1, heap_bh30_w45_0_d2, heap_bh30_w45_0_d3 :  std_logic;
signal heap_bh30_w44_0, heap_bh30_w44_0_d1, heap_bh30_w44_0_d2, heap_bh30_w44_0_d3 :  std_logic;
signal heap_bh30_w43_0, heap_bh30_w43_0_d1, heap_bh30_w43_0_d2, heap_bh30_w43_0_d3 :  std_logic;
signal heap_bh30_w42_0, heap_bh30_w42_0_d1, heap_bh30_w42_0_d2, heap_bh30_w42_0_d3 :  std_logic;
signal heap_bh30_w41_0, heap_bh30_w41_0_d1, heap_bh30_w41_0_d2, heap_bh30_w41_0_d3 :  std_logic;
signal heap_bh30_w40_0, heap_bh30_w40_0_d1, heap_bh30_w40_0_d2, heap_bh30_w40_0_d3 :  std_logic;
signal heap_bh30_w39_0, heap_bh30_w39_0_d1, heap_bh30_w39_0_d2, heap_bh30_w39_0_d3 :  std_logic;
signal heap_bh30_w38_0, heap_bh30_w38_0_d1, heap_bh30_w38_0_d2, heap_bh30_w38_0_d3 :  std_logic;
signal heap_bh30_w37_0, heap_bh30_w37_0_d1, heap_bh30_w37_0_d2, heap_bh30_w37_0_d3 :  std_logic;
signal heap_bh30_w36_0, heap_bh30_w36_0_d1, heap_bh30_w36_0_d2, heap_bh30_w36_0_d3 :  std_logic;
signal heap_bh30_w35_0, heap_bh30_w35_0_d1, heap_bh30_w35_0_d2 :  std_logic;
signal heap_bh30_w34_0, heap_bh30_w34_0_d1, heap_bh30_w34_0_d2 :  std_logic;
signal heap_bh30_w33_0, heap_bh30_w33_0_d1 :  std_logic;
signal heap_bh30_w32_0, heap_bh30_w32_0_d1 :  std_logic;
signal heap_bh30_w31_0, heap_bh30_w31_0_d1 :  std_logic;
signal heap_bh30_w30_0, heap_bh30_w30_0_d1 :  std_logic;
signal heap_bh30_w29_0, heap_bh30_w29_0_d1 :  std_logic;
signal heap_bh30_w28_0, heap_bh30_w28_0_d1 :  std_logic;
signal heap_bh30_w27_1, heap_bh30_w27_1_d1 :  std_logic;
signal heap_bh30_w26_1, heap_bh30_w26_1_d1 :  std_logic;
signal heap_bh30_w25_1, heap_bh30_w25_1_d1 :  std_logic;
signal heap_bh30_w24_2, heap_bh30_w24_2_d1 :  std_logic;
signal heap_bh30_w23_2, heap_bh30_w23_2_d1 :  std_logic;
signal heap_bh30_w22_1, heap_bh30_w22_1_d1 :  std_logic;
signal heap_bh30_w21_2, heap_bh30_w21_2_d1 :  std_logic;
signal heap_bh30_w20_2, heap_bh30_w20_2_d1 :  std_logic;
signal heap_bh30_w19_1, heap_bh30_w19_1_d1 :  std_logic;
signal heap_bh30_w18_2, heap_bh30_w18_2_d1 :  std_logic;
signal heap_bh30_w17_2, heap_bh30_w17_2_d1 :  std_logic;
signal heap_bh30_w16_1, heap_bh30_w16_1_d1 :  std_logic;
signal heap_bh30_w15_2, heap_bh30_w15_2_d1 :  std_logic;
signal heap_bh30_w14_2, heap_bh30_w14_2_d1 :  std_logic;
signal heap_bh30_w13_1, heap_bh30_w13_1_d1 :  std_logic;
signal heap_bh30_w12_2, heap_bh30_w12_2_d1 :  std_logic;
signal heap_bh30_w11_2, heap_bh30_w11_2_d1 :  std_logic;
signal DSP_bh30_ch1_0 :  std_logic_vector(40 downto 0);
signal heap_bh30_w34_1, heap_bh30_w34_1_d1, heap_bh30_w34_1_d2 :  std_logic;
signal heap_bh30_w33_1, heap_bh30_w33_1_d1 :  std_logic;
signal heap_bh30_w32_1, heap_bh30_w32_1_d1 :  std_logic;
signal heap_bh30_w31_1, heap_bh30_w31_1_d1 :  std_logic;
signal heap_bh30_w30_1, heap_bh30_w30_1_d1 :  std_logic;
signal heap_bh30_w29_1, heap_bh30_w29_1_d1 :  std_logic;
signal heap_bh30_w28_1, heap_bh30_w28_1_d1 :  std_logic;
signal heap_bh30_w27_2, heap_bh30_w27_2_d1 :  std_logic;
signal heap_bh30_w26_2, heap_bh30_w26_2_d1 :  std_logic;
signal heap_bh30_w25_2, heap_bh30_w25_2_d1 :  std_logic;
signal heap_bh30_w24_3, heap_bh30_w24_3_d1 :  std_logic;
signal heap_bh30_w23_3, heap_bh30_w23_3_d1 :  std_logic;
signal heap_bh30_w22_2, heap_bh30_w22_2_d1 :  std_logic;
signal heap_bh30_w21_3, heap_bh30_w21_3_d1 :  std_logic;
signal heap_bh30_w20_3, heap_bh30_w20_3_d1 :  std_logic;
signal heap_bh30_w19_2, heap_bh30_w19_2_d1 :  std_logic;
signal heap_bh30_w18_3, heap_bh30_w18_3_d1 :  std_logic;
signal heap_bh30_w17_3, heap_bh30_w17_3_d1 :  std_logic;
signal heap_bh30_w16_2, heap_bh30_w16_2_d1 :  std_logic;
signal heap_bh30_w15_3, heap_bh30_w15_3_d1 :  std_logic;
signal heap_bh30_w14_3, heap_bh30_w14_3_d1 :  std_logic;
signal heap_bh30_w13_2, heap_bh30_w13_2_d1 :  std_logic;
signal heap_bh30_w12_3, heap_bh30_w12_3_d1 :  std_logic;
signal heap_bh30_w11_3, heap_bh30_w11_3_d1 :  std_logic;
signal heap_bh30_w10_2, heap_bh30_w10_2_d1 :  std_logic;
signal heap_bh30_w9_2, heap_bh30_w9_2_d1 :  std_logic;
signal heap_bh30_w8_1, heap_bh30_w8_1_d1 :  std_logic;
signal heap_bh30_w7_2, heap_bh30_w7_2_d1 :  std_logic;
signal heap_bh30_w6_2, heap_bh30_w6_2_d1 :  std_logic;
signal heap_bh30_w5_1, heap_bh30_w5_1_d1 :  std_logic;
signal heap_bh30_w4_2, heap_bh30_w4_2_d1, heap_bh30_w4_2_d2, heap_bh30_w4_2_d3 :  std_logic;
signal heap_bh30_w3_2, heap_bh30_w3_2_d1 :  std_logic;
signal heap_bh30_w2_1, heap_bh30_w2_1_d1, heap_bh30_w2_1_d2, heap_bh30_w2_1_d3 :  std_logic;
signal heap_bh30_w1_1, heap_bh30_w1_1_d1, heap_bh30_w1_1_d2, heap_bh30_w1_1_d3 :  std_logic;
signal heap_bh30_w0_1, heap_bh30_w0_1_d1, heap_bh30_w0_1_d2, heap_bh30_w0_1_d3 :  std_logic;
signal CompressorIn_bh30_0_0 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_0_1 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_0_0 :  std_logic_vector(2 downto 0);
signal heap_bh30_w11_4 :  std_logic;
signal heap_bh30_w12_4 :  std_logic;
signal heap_bh30_w13_3 :  std_logic;
signal CompressorIn_bh30_1_2 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_1_3 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_1_1 :  std_logic_vector(2 downto 0);
signal heap_bh30_w14_4 :  std_logic;
signal heap_bh30_w15_4 :  std_logic;
signal heap_bh30_w16_3 :  std_logic;
signal CompressorIn_bh30_2_4 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_2_5 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_2_2 :  std_logic_vector(2 downto 0);
signal heap_bh30_w17_4 :  std_logic;
signal heap_bh30_w18_4 :  std_logic;
signal heap_bh30_w19_3 :  std_logic;
signal CompressorIn_bh30_3_6 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_3_7 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_3_3 :  std_logic_vector(2 downto 0);
signal heap_bh30_w20_4 :  std_logic;
signal heap_bh30_w21_4 :  std_logic;
signal heap_bh30_w22_3 :  std_logic;
signal CompressorIn_bh30_4_8 :  std_logic_vector(3 downto 0);
signal CompressorIn_bh30_4_9 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_4_4 :  std_logic_vector(2 downto 0);
signal heap_bh30_w23_4 :  std_logic;
signal heap_bh30_w24_4 :  std_logic;
signal heap_bh30_w25_3 :  std_logic;
signal CompressorIn_bh30_5_10 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_5_11 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_5_5 :  std_logic_vector(2 downto 0);
signal heap_bh30_w3_3, heap_bh30_w3_3_d1, heap_bh30_w3_3_d2 :  std_logic;
signal heap_bh30_w4_3, heap_bh30_w4_3_d1, heap_bh30_w4_3_d2 :  std_logic;
signal heap_bh30_w5_2 :  std_logic;
signal CompressorIn_bh30_6_12 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_6_13 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_6_6 :  std_logic_vector(2 downto 0);
signal heap_bh30_w6_3 :  std_logic;
signal heap_bh30_w7_3 :  std_logic;
signal heap_bh30_w8_2 :  std_logic;
signal CompressorIn_bh30_7_14 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_7_15 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_7_7 :  std_logic_vector(2 downto 0);
signal heap_bh30_w9_3 :  std_logic;
signal heap_bh30_w10_3 :  std_logic;
signal heap_bh30_w11_5 :  std_logic;
signal CompressorIn_bh30_8_16 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_8_17 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_8_8 :  std_logic_vector(2 downto 0);
signal heap_bh30_w12_5 :  std_logic;
signal heap_bh30_w13_4 :  std_logic;
signal heap_bh30_w14_5 :  std_logic;
signal CompressorIn_bh30_9_18 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_9_19 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_9_9 :  std_logic_vector(2 downto 0);
signal heap_bh30_w15_5 :  std_logic;
signal heap_bh30_w16_4 :  std_logic;
signal heap_bh30_w17_5 :  std_logic;
signal CompressorIn_bh30_10_20 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_10_21 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_10_10 :  std_logic_vector(2 downto 0);
signal heap_bh30_w18_5 :  std_logic;
signal heap_bh30_w19_4 :  std_logic;
signal heap_bh30_w20_5 :  std_logic;
signal CompressorIn_bh30_11_22 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_11_23 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_11_11 :  std_logic_vector(2 downto 0);
signal heap_bh30_w21_5 :  std_logic;
signal heap_bh30_w22_4 :  std_logic;
signal heap_bh30_w23_5 :  std_logic;
signal CompressorIn_bh30_12_24 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_12_25 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_12_12 :  std_logic_vector(2 downto 0);
signal heap_bh30_w24_5 :  std_logic;
signal heap_bh30_w25_4 :  std_logic;
signal heap_bh30_w26_3 :  std_logic;
signal CompressorIn_bh30_13_26 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_13_27 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_13_13 :  std_logic_vector(2 downto 0);
signal heap_bh30_w26_4 :  std_logic;
signal heap_bh30_w27_3 :  std_logic;
signal heap_bh30_w28_2 :  std_logic;
signal CompressorIn_bh30_14_28 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_14_29 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_14_14 :  std_logic_vector(2 downto 0);
signal heap_bh30_w13_5 :  std_logic;
signal heap_bh30_w14_6, heap_bh30_w14_6_d1, heap_bh30_w14_6_d2 :  std_logic;
signal heap_bh30_w15_6 :  std_logic;
signal CompressorIn_bh30_15_30 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_15_31 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_15_15 :  std_logic_vector(2 downto 0);
signal heap_bh30_w16_5 :  std_logic;
signal heap_bh30_w17_6, heap_bh30_w17_6_d1, heap_bh30_w17_6_d2 :  std_logic;
signal heap_bh30_w18_6 :  std_logic;
signal CompressorIn_bh30_16_32 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_16_33 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_16_16 :  std_logic_vector(2 downto 0);
signal heap_bh30_w19_5 :  std_logic;
signal heap_bh30_w20_6, heap_bh30_w20_6_d1, heap_bh30_w20_6_d2 :  std_logic;
signal heap_bh30_w21_6 :  std_logic;
signal CompressorIn_bh30_17_34 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_17_35 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_17_17 :  std_logic_vector(2 downto 0);
signal heap_bh30_w22_5 :  std_logic;
signal heap_bh30_w23_6, heap_bh30_w23_6_d1, heap_bh30_w23_6_d2 :  std_logic;
signal heap_bh30_w24_6 :  std_logic;
signal CompressorIn_bh30_18_36 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_18_37 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_18_18 :  std_logic_vector(2 downto 0);
signal heap_bh30_w25_5 :  std_logic;
signal heap_bh30_w26_5, heap_bh30_w26_5_d1, heap_bh30_w26_5_d2 :  std_logic;
signal heap_bh30_w27_4 :  std_logic;
signal CompressorIn_bh30_19_38 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_19_39 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_19_19 :  std_logic_vector(2 downto 0);
signal heap_bh30_w28_3 :  std_logic;
signal heap_bh30_w29_2, heap_bh30_w29_2_d1, heap_bh30_w29_2_d2 :  std_logic;
signal heap_bh30_w30_2 :  std_logic;
signal CompressorIn_bh30_20_40 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_20_41 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_20_20 :  std_logic_vector(2 downto 0);
signal heap_bh30_w5_3, heap_bh30_w5_3_d1, heap_bh30_w5_3_d2 :  std_logic;
signal heap_bh30_w6_4, heap_bh30_w6_4_d1, heap_bh30_w6_4_d2 :  std_logic;
signal heap_bh30_w7_4 :  std_logic;
signal CompressorIn_bh30_21_42 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_21_43 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_21_21 :  std_logic_vector(2 downto 0);
signal heap_bh30_w8_3 :  std_logic;
signal heap_bh30_w9_4, heap_bh30_w9_4_d1, heap_bh30_w9_4_d2 :  std_logic;
signal heap_bh30_w10_4 :  std_logic;
signal CompressorIn_bh30_22_44 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_22_45 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_22_22 :  std_logic_vector(2 downto 0);
signal heap_bh30_w10_5, heap_bh30_w10_5_d1, heap_bh30_w10_5_d2 :  std_logic;
signal heap_bh30_w11_6, heap_bh30_w11_6_d1, heap_bh30_w11_6_d2 :  std_logic;
signal heap_bh30_w12_6 :  std_logic;
signal CompressorIn_bh30_23_46 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_23_47 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_23_23 :  std_logic_vector(2 downto 0);
signal heap_bh30_w30_3, heap_bh30_w30_3_d1, heap_bh30_w30_3_d2 :  std_logic;
signal heap_bh30_w31_2, heap_bh30_w31_2_d1, heap_bh30_w31_2_d2 :  std_logic;
signal heap_bh30_w32_2 :  std_logic;
signal CompressorIn_bh30_24_48 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_24_49 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_24_24 :  std_logic_vector(2 downto 0);
signal heap_bh30_w7_5, heap_bh30_w7_5_d1, heap_bh30_w7_5_d2 :  std_logic;
signal heap_bh30_w8_4, heap_bh30_w8_4_d1, heap_bh30_w8_4_d2 :  std_logic;
signal heap_bh30_w9_5, heap_bh30_w9_5_d1, heap_bh30_w9_5_d2 :  std_logic;
signal CompressorIn_bh30_25_50 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_25_51 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_25_25 :  std_logic_vector(2 downto 0);
signal heap_bh30_w15_7, heap_bh30_w15_7_d1, heap_bh30_w15_7_d2 :  std_logic;
signal heap_bh30_w16_6, heap_bh30_w16_6_d1, heap_bh30_w16_6_d2 :  std_logic;
signal heap_bh30_w17_7, heap_bh30_w17_7_d1, heap_bh30_w17_7_d2 :  std_logic;
signal CompressorIn_bh30_26_52 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_26_53 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_26_26 :  std_logic_vector(2 downto 0);
signal heap_bh30_w18_7, heap_bh30_w18_7_d1, heap_bh30_w18_7_d2 :  std_logic;
signal heap_bh30_w19_6, heap_bh30_w19_6_d1, heap_bh30_w19_6_d2 :  std_logic;
signal heap_bh30_w20_7, heap_bh30_w20_7_d1, heap_bh30_w20_7_d2 :  std_logic;
signal CompressorIn_bh30_27_54 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_27_55 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_27_27 :  std_logic_vector(2 downto 0);
signal heap_bh30_w21_7, heap_bh30_w21_7_d1, heap_bh30_w21_7_d2 :  std_logic;
signal heap_bh30_w22_6, heap_bh30_w22_6_d1, heap_bh30_w22_6_d2 :  std_logic;
signal heap_bh30_w23_7, heap_bh30_w23_7_d1, heap_bh30_w23_7_d2 :  std_logic;
signal CompressorIn_bh30_28_56 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_28_57 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_28_28 :  std_logic_vector(2 downto 0);
signal heap_bh30_w24_7, heap_bh30_w24_7_d1, heap_bh30_w24_7_d2 :  std_logic;
signal heap_bh30_w25_6, heap_bh30_w25_6_d1, heap_bh30_w25_6_d2 :  std_logic;
signal heap_bh30_w26_6, heap_bh30_w26_6_d1, heap_bh30_w26_6_d2 :  std_logic;
signal CompressorIn_bh30_29_58 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_29_59 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_29_29 :  std_logic_vector(2 downto 0);
signal heap_bh30_w27_5, heap_bh30_w27_5_d1, heap_bh30_w27_5_d2 :  std_logic;
signal heap_bh30_w28_4, heap_bh30_w28_4_d1, heap_bh30_w28_4_d2 :  std_logic;
signal heap_bh30_w29_3, heap_bh30_w29_3_d1, heap_bh30_w29_3_d2 :  std_logic;
signal CompressorIn_bh30_30_60 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_30_61 :  std_logic_vector(1 downto 0);
signal CompressorOut_bh30_30_30 :  std_logic_vector(2 downto 0);
signal heap_bh30_w32_3, heap_bh30_w32_3_d1, heap_bh30_w32_3_d2 :  std_logic;
signal heap_bh30_w33_2, heap_bh30_w33_2_d1, heap_bh30_w33_2_d2 :  std_logic;
signal heap_bh30_w34_2, heap_bh30_w34_2_d1 :  std_logic;
signal CompressorIn_bh30_31_62 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_31_63 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_31_31 :  std_logic_vector(2 downto 0);
signal heap_bh30_w12_7, heap_bh30_w12_7_d1, heap_bh30_w12_7_d2 :  std_logic;
signal heap_bh30_w13_6, heap_bh30_w13_6_d1, heap_bh30_w13_6_d2 :  std_logic;
signal heap_bh30_w14_7, heap_bh30_w14_7_d1, heap_bh30_w14_7_d2 :  std_logic;
signal CompressorIn_bh30_32_64 :  std_logic_vector(2 downto 0);
signal CompressorIn_bh30_32_65 :  std_logic_vector(0 downto 0);
signal CompressorOut_bh30_32_32 :  std_logic_vector(2 downto 0);
signal heap_bh30_w34_3, heap_bh30_w34_3_d1 :  std_logic;
signal heap_bh30_w35_1, heap_bh30_w35_1_d1 :  std_logic;
signal heap_bh30_w36_1, heap_bh30_w36_1_d1 :  std_logic;
signal finalAdderIn0_bh30 :  std_logic_vector(52 downto 0);
signal finalAdderIn1_bh30 :  std_logic_vector(52 downto 0);
signal finalAdderCin_bh30 :  std_logic;
signal finalAdderOut_bh30 :  std_logic_vector(52 downto 0);
signal CompressionResult30 :  std_logic_vector(52 downto 0);
attribute rom_extract: string;
attribute rom_style: string;
attribute rom_extract of SmallMultTableP3x3r6XuYu_F400_uid33: component is "yes";
attribute rom_extract of SmallMultTableP3x3r6XuYu_F400_uid48: component is "yes";
attribute rom_style of SmallMultTableP3x3r6XuYu_F400_uid33: component is "distributed";
attribute rom_style of SmallMultTableP3x3r6XuYu_F400_uid48: component is "distributed";
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            heap_bh30_w9_0_d1 <=  heap_bh30_w9_0;
            heap_bh30_w10_0_d1 <=  heap_bh30_w10_0;
            heap_bh30_w11_0_d1 <=  heap_bh30_w11_0;
            heap_bh30_w12_0_d1 <=  heap_bh30_w12_0;
            heap_bh30_w11_1_d1 <=  heap_bh30_w11_1;
            heap_bh30_w12_1_d1 <=  heap_bh30_w12_1;
            heap_bh30_w13_0_d1 <=  heap_bh30_w13_0;
            heap_bh30_w14_0_d1 <=  heap_bh30_w14_0;
            heap_bh30_w15_0_d1 <=  heap_bh30_w15_0;
            heap_bh30_w14_1_d1 <=  heap_bh30_w14_1;
            heap_bh30_w15_1_d1 <=  heap_bh30_w15_1;
            heap_bh30_w16_0_d1 <=  heap_bh30_w16_0;
            heap_bh30_w17_0_d1 <=  heap_bh30_w17_0;
            heap_bh30_w18_0_d1 <=  heap_bh30_w18_0;
            heap_bh30_w17_1_d1 <=  heap_bh30_w17_1;
            heap_bh30_w18_1_d1 <=  heap_bh30_w18_1;
            heap_bh30_w19_0_d1 <=  heap_bh30_w19_0;
            heap_bh30_w20_0_d1 <=  heap_bh30_w20_0;
            heap_bh30_w21_0_d1 <=  heap_bh30_w21_0;
            heap_bh30_w20_1_d1 <=  heap_bh30_w20_1;
            heap_bh30_w21_1_d1 <=  heap_bh30_w21_1;
            heap_bh30_w22_0_d1 <=  heap_bh30_w22_0;
            heap_bh30_w23_0_d1 <=  heap_bh30_w23_0;
            heap_bh30_w24_0_d1 <=  heap_bh30_w24_0;
            heap_bh30_w23_1_d1 <=  heap_bh30_w23_1;
            heap_bh30_w24_1_d1 <=  heap_bh30_w24_1;
            heap_bh30_w25_0_d1 <=  heap_bh30_w25_0;
            heap_bh30_w26_0_d1 <=  heap_bh30_w26_0;
            heap_bh30_w27_0_d1 <=  heap_bh30_w27_0;
            heap_bh30_w0_0_d1 <=  heap_bh30_w0_0;
            heap_bh30_w0_0_d2 <=  heap_bh30_w0_0_d1;
            heap_bh30_w0_0_d3 <=  heap_bh30_w0_0_d2;
            heap_bh30_w1_0_d1 <=  heap_bh30_w1_0;
            heap_bh30_w1_0_d2 <=  heap_bh30_w1_0_d1;
            heap_bh30_w1_0_d3 <=  heap_bh30_w1_0_d2;
            heap_bh30_w2_0_d1 <=  heap_bh30_w2_0;
            heap_bh30_w2_0_d2 <=  heap_bh30_w2_0_d1;
            heap_bh30_w2_0_d3 <=  heap_bh30_w2_0_d2;
            heap_bh30_w3_0_d1 <=  heap_bh30_w3_0;
            heap_bh30_w4_0_d1 <=  heap_bh30_w4_0;
            heap_bh30_w3_1_d1 <=  heap_bh30_w3_1;
            heap_bh30_w4_1_d1 <=  heap_bh30_w4_1;
            heap_bh30_w5_0_d1 <=  heap_bh30_w5_0;
            heap_bh30_w6_0_d1 <=  heap_bh30_w6_0;
            heap_bh30_w7_0_d1 <=  heap_bh30_w7_0;
            heap_bh30_w6_1_d1 <=  heap_bh30_w6_1;
            heap_bh30_w7_1_d1 <=  heap_bh30_w7_1;
            heap_bh30_w8_0_d1 <=  heap_bh30_w8_0;
            heap_bh30_w9_1_d1 <=  heap_bh30_w9_1;
            heap_bh30_w10_1_d1 <=  heap_bh30_w10_1;
            heap_bh30_w51_0_d1 <=  heap_bh30_w51_0;
            heap_bh30_w51_0_d2 <=  heap_bh30_w51_0_d1;
            heap_bh30_w51_0_d3 <=  heap_bh30_w51_0_d2;
            heap_bh30_w50_0_d1 <=  heap_bh30_w50_0;
            heap_bh30_w50_0_d2 <=  heap_bh30_w50_0_d1;
            heap_bh30_w50_0_d3 <=  heap_bh30_w50_0_d2;
            heap_bh30_w49_0_d1 <=  heap_bh30_w49_0;
            heap_bh30_w49_0_d2 <=  heap_bh30_w49_0_d1;
            heap_bh30_w49_0_d3 <=  heap_bh30_w49_0_d2;
            heap_bh30_w48_0_d1 <=  heap_bh30_w48_0;
            heap_bh30_w48_0_d2 <=  heap_bh30_w48_0_d1;
            heap_bh30_w48_0_d3 <=  heap_bh30_w48_0_d2;
            heap_bh30_w47_0_d1 <=  heap_bh30_w47_0;
            heap_bh30_w47_0_d2 <=  heap_bh30_w47_0_d1;
            heap_bh30_w47_0_d3 <=  heap_bh30_w47_0_d2;
            heap_bh30_w46_0_d1 <=  heap_bh30_w46_0;
            heap_bh30_w46_0_d2 <=  heap_bh30_w46_0_d1;
            heap_bh30_w46_0_d3 <=  heap_bh30_w46_0_d2;
            heap_bh30_w45_0_d1 <=  heap_bh30_w45_0;
            heap_bh30_w45_0_d2 <=  heap_bh30_w45_0_d1;
            heap_bh30_w45_0_d3 <=  heap_bh30_w45_0_d2;
            heap_bh30_w44_0_d1 <=  heap_bh30_w44_0;
            heap_bh30_w44_0_d2 <=  heap_bh30_w44_0_d1;
            heap_bh30_w44_0_d3 <=  heap_bh30_w44_0_d2;
            heap_bh30_w43_0_d1 <=  heap_bh30_w43_0;
            heap_bh30_w43_0_d2 <=  heap_bh30_w43_0_d1;
            heap_bh30_w43_0_d3 <=  heap_bh30_w43_0_d2;
            heap_bh30_w42_0_d1 <=  heap_bh30_w42_0;
            heap_bh30_w42_0_d2 <=  heap_bh30_w42_0_d1;
            heap_bh30_w42_0_d3 <=  heap_bh30_w42_0_d2;
            heap_bh30_w41_0_d1 <=  heap_bh30_w41_0;
            heap_bh30_w41_0_d2 <=  heap_bh30_w41_0_d1;
            heap_bh30_w41_0_d3 <=  heap_bh30_w41_0_d2;
            heap_bh30_w40_0_d1 <=  heap_bh30_w40_0;
            heap_bh30_w40_0_d2 <=  heap_bh30_w40_0_d1;
            heap_bh30_w40_0_d3 <=  heap_bh30_w40_0_d2;
            heap_bh30_w39_0_d1 <=  heap_bh30_w39_0;
            heap_bh30_w39_0_d2 <=  heap_bh30_w39_0_d1;
            heap_bh30_w39_0_d3 <=  heap_bh30_w39_0_d2;
            heap_bh30_w38_0_d1 <=  heap_bh30_w38_0;
            heap_bh30_w38_0_d2 <=  heap_bh30_w38_0_d1;
            heap_bh30_w38_0_d3 <=  heap_bh30_w38_0_d2;
            heap_bh30_w37_0_d1 <=  heap_bh30_w37_0;
            heap_bh30_w37_0_d2 <=  heap_bh30_w37_0_d1;
            heap_bh30_w37_0_d3 <=  heap_bh30_w37_0_d2;
            heap_bh30_w36_0_d1 <=  heap_bh30_w36_0;
            heap_bh30_w36_0_d2 <=  heap_bh30_w36_0_d1;
            heap_bh30_w36_0_d3 <=  heap_bh30_w36_0_d2;
            heap_bh30_w35_0_d1 <=  heap_bh30_w35_0;
            heap_bh30_w35_0_d2 <=  heap_bh30_w35_0_d1;
            heap_bh30_w34_0_d1 <=  heap_bh30_w34_0;
            heap_bh30_w34_0_d2 <=  heap_bh30_w34_0_d1;
            heap_bh30_w33_0_d1 <=  heap_bh30_w33_0;
            heap_bh30_w32_0_d1 <=  heap_bh30_w32_0;
            heap_bh30_w31_0_d1 <=  heap_bh30_w31_0;
            heap_bh30_w30_0_d1 <=  heap_bh30_w30_0;
            heap_bh30_w29_0_d1 <=  heap_bh30_w29_0;
            heap_bh30_w28_0_d1 <=  heap_bh30_w28_0;
            heap_bh30_w27_1_d1 <=  heap_bh30_w27_1;
            heap_bh30_w26_1_d1 <=  heap_bh30_w26_1;
            heap_bh30_w25_1_d1 <=  heap_bh30_w25_1;
            heap_bh30_w24_2_d1 <=  heap_bh30_w24_2;
            heap_bh30_w23_2_d1 <=  heap_bh30_w23_2;
            heap_bh30_w22_1_d1 <=  heap_bh30_w22_1;
            heap_bh30_w21_2_d1 <=  heap_bh30_w21_2;
            heap_bh30_w20_2_d1 <=  heap_bh30_w20_2;
            heap_bh30_w19_1_d1 <=  heap_bh30_w19_1;
            heap_bh30_w18_2_d1 <=  heap_bh30_w18_2;
            heap_bh30_w17_2_d1 <=  heap_bh30_w17_2;
            heap_bh30_w16_1_d1 <=  heap_bh30_w16_1;
            heap_bh30_w15_2_d1 <=  heap_bh30_w15_2;
            heap_bh30_w14_2_d1 <=  heap_bh30_w14_2;
            heap_bh30_w13_1_d1 <=  heap_bh30_w13_1;
            heap_bh30_w12_2_d1 <=  heap_bh30_w12_2;
            heap_bh30_w11_2_d1 <=  heap_bh30_w11_2;
            heap_bh30_w34_1_d1 <=  heap_bh30_w34_1;
            heap_bh30_w34_1_d2 <=  heap_bh30_w34_1_d1;
            heap_bh30_w33_1_d1 <=  heap_bh30_w33_1;
            heap_bh30_w32_1_d1 <=  heap_bh30_w32_1;
            heap_bh30_w31_1_d1 <=  heap_bh30_w31_1;
            heap_bh30_w30_1_d1 <=  heap_bh30_w30_1;
            heap_bh30_w29_1_d1 <=  heap_bh30_w29_1;
            heap_bh30_w28_1_d1 <=  heap_bh30_w28_1;
            heap_bh30_w27_2_d1 <=  heap_bh30_w27_2;
            heap_bh30_w26_2_d1 <=  heap_bh30_w26_2;
            heap_bh30_w25_2_d1 <=  heap_bh30_w25_2;
            heap_bh30_w24_3_d1 <=  heap_bh30_w24_3;
            heap_bh30_w23_3_d1 <=  heap_bh30_w23_3;
            heap_bh30_w22_2_d1 <=  heap_bh30_w22_2;
            heap_bh30_w21_3_d1 <=  heap_bh30_w21_3;
            heap_bh30_w20_3_d1 <=  heap_bh30_w20_3;
            heap_bh30_w19_2_d1 <=  heap_bh30_w19_2;
            heap_bh30_w18_3_d1 <=  heap_bh30_w18_3;
            heap_bh30_w17_3_d1 <=  heap_bh30_w17_3;
            heap_bh30_w16_2_d1 <=  heap_bh30_w16_2;
            heap_bh30_w15_3_d1 <=  heap_bh30_w15_3;
            heap_bh30_w14_3_d1 <=  heap_bh30_w14_3;
            heap_bh30_w13_2_d1 <=  heap_bh30_w13_2;
            heap_bh30_w12_3_d1 <=  heap_bh30_w12_3;
            heap_bh30_w11_3_d1 <=  heap_bh30_w11_3;
            heap_bh30_w10_2_d1 <=  heap_bh30_w10_2;
            heap_bh30_w9_2_d1 <=  heap_bh30_w9_2;
            heap_bh30_w8_1_d1 <=  heap_bh30_w8_1;
            heap_bh30_w7_2_d1 <=  heap_bh30_w7_2;
            heap_bh30_w6_2_d1 <=  heap_bh30_w6_2;
            heap_bh30_w5_1_d1 <=  heap_bh30_w5_1;
            heap_bh30_w4_2_d1 <=  heap_bh30_w4_2;
            heap_bh30_w4_2_d2 <=  heap_bh30_w4_2_d1;
            heap_bh30_w4_2_d3 <=  heap_bh30_w4_2_d2;
            heap_bh30_w3_2_d1 <=  heap_bh30_w3_2;
            heap_bh30_w2_1_d1 <=  heap_bh30_w2_1;
            heap_bh30_w2_1_d2 <=  heap_bh30_w2_1_d1;
            heap_bh30_w2_1_d3 <=  heap_bh30_w2_1_d2;
            heap_bh30_w1_1_d1 <=  heap_bh30_w1_1;
            heap_bh30_w1_1_d2 <=  heap_bh30_w1_1_d1;
            heap_bh30_w1_1_d3 <=  heap_bh30_w1_1_d2;
            heap_bh30_w0_1_d1 <=  heap_bh30_w0_1;
            heap_bh30_w0_1_d2 <=  heap_bh30_w0_1_d1;
            heap_bh30_w0_1_d3 <=  heap_bh30_w0_1_d2;
            heap_bh30_w3_3_d1 <=  heap_bh30_w3_3;
            heap_bh30_w3_3_d2 <=  heap_bh30_w3_3_d1;
            heap_bh30_w4_3_d1 <=  heap_bh30_w4_3;
            heap_bh30_w4_3_d2 <=  heap_bh30_w4_3_d1;
            heap_bh30_w14_6_d1 <=  heap_bh30_w14_6;
            heap_bh30_w14_6_d2 <=  heap_bh30_w14_6_d1;
            heap_bh30_w17_6_d1 <=  heap_bh30_w17_6;
            heap_bh30_w17_6_d2 <=  heap_bh30_w17_6_d1;
            heap_bh30_w20_6_d1 <=  heap_bh30_w20_6;
            heap_bh30_w20_6_d2 <=  heap_bh30_w20_6_d1;
            heap_bh30_w23_6_d1 <=  heap_bh30_w23_6;
            heap_bh30_w23_6_d2 <=  heap_bh30_w23_6_d1;
            heap_bh30_w26_5_d1 <=  heap_bh30_w26_5;
            heap_bh30_w26_5_d2 <=  heap_bh30_w26_5_d1;
            heap_bh30_w29_2_d1 <=  heap_bh30_w29_2;
            heap_bh30_w29_2_d2 <=  heap_bh30_w29_2_d1;
            heap_bh30_w5_3_d1 <=  heap_bh30_w5_3;
            heap_bh30_w5_3_d2 <=  heap_bh30_w5_3_d1;
            heap_bh30_w6_4_d1 <=  heap_bh30_w6_4;
            heap_bh30_w6_4_d2 <=  heap_bh30_w6_4_d1;
            heap_bh30_w9_4_d1 <=  heap_bh30_w9_4;
            heap_bh30_w9_4_d2 <=  heap_bh30_w9_4_d1;
            heap_bh30_w10_5_d1 <=  heap_bh30_w10_5;
            heap_bh30_w10_5_d2 <=  heap_bh30_w10_5_d1;
            heap_bh30_w11_6_d1 <=  heap_bh30_w11_6;
            heap_bh30_w11_6_d2 <=  heap_bh30_w11_6_d1;
            heap_bh30_w30_3_d1 <=  heap_bh30_w30_3;
            heap_bh30_w30_3_d2 <=  heap_bh30_w30_3_d1;
            heap_bh30_w31_2_d1 <=  heap_bh30_w31_2;
            heap_bh30_w31_2_d2 <=  heap_bh30_w31_2_d1;
            heap_bh30_w7_5_d1 <=  heap_bh30_w7_5;
            heap_bh30_w7_5_d2 <=  heap_bh30_w7_5_d1;
            heap_bh30_w8_4_d1 <=  heap_bh30_w8_4;
            heap_bh30_w8_4_d2 <=  heap_bh30_w8_4_d1;
            heap_bh30_w9_5_d1 <=  heap_bh30_w9_5;
            heap_bh30_w9_5_d2 <=  heap_bh30_w9_5_d1;
            heap_bh30_w15_7_d1 <=  heap_bh30_w15_7;
            heap_bh30_w15_7_d2 <=  heap_bh30_w15_7_d1;
            heap_bh30_w16_6_d1 <=  heap_bh30_w16_6;
            heap_bh30_w16_6_d2 <=  heap_bh30_w16_6_d1;
            heap_bh30_w17_7_d1 <=  heap_bh30_w17_7;
            heap_bh30_w17_7_d2 <=  heap_bh30_w17_7_d1;
            heap_bh30_w18_7_d1 <=  heap_bh30_w18_7;
            heap_bh30_w18_7_d2 <=  heap_bh30_w18_7_d1;
            heap_bh30_w19_6_d1 <=  heap_bh30_w19_6;
            heap_bh30_w19_6_d2 <=  heap_bh30_w19_6_d1;
            heap_bh30_w20_7_d1 <=  heap_bh30_w20_7;
            heap_bh30_w20_7_d2 <=  heap_bh30_w20_7_d1;
            heap_bh30_w21_7_d1 <=  heap_bh30_w21_7;
            heap_bh30_w21_7_d2 <=  heap_bh30_w21_7_d1;
            heap_bh30_w22_6_d1 <=  heap_bh30_w22_6;
            heap_bh30_w22_6_d2 <=  heap_bh30_w22_6_d1;
            heap_bh30_w23_7_d1 <=  heap_bh30_w23_7;
            heap_bh30_w23_7_d2 <=  heap_bh30_w23_7_d1;
            heap_bh30_w24_7_d1 <=  heap_bh30_w24_7;
            heap_bh30_w24_7_d2 <=  heap_bh30_w24_7_d1;
            heap_bh30_w25_6_d1 <=  heap_bh30_w25_6;
            heap_bh30_w25_6_d2 <=  heap_bh30_w25_6_d1;
            heap_bh30_w26_6_d1 <=  heap_bh30_w26_6;
            heap_bh30_w26_6_d2 <=  heap_bh30_w26_6_d1;
            heap_bh30_w27_5_d1 <=  heap_bh30_w27_5;
            heap_bh30_w27_5_d2 <=  heap_bh30_w27_5_d1;
            heap_bh30_w28_4_d1 <=  heap_bh30_w28_4;
            heap_bh30_w28_4_d2 <=  heap_bh30_w28_4_d1;
            heap_bh30_w29_3_d1 <=  heap_bh30_w29_3;
            heap_bh30_w29_3_d2 <=  heap_bh30_w29_3_d1;
            heap_bh30_w32_3_d1 <=  heap_bh30_w32_3;
            heap_bh30_w32_3_d2 <=  heap_bh30_w32_3_d1;
            heap_bh30_w33_2_d1 <=  heap_bh30_w33_2;
            heap_bh30_w33_2_d2 <=  heap_bh30_w33_2_d1;
            heap_bh30_w34_2_d1 <=  heap_bh30_w34_2;
            heap_bh30_w12_7_d1 <=  heap_bh30_w12_7;
            heap_bh30_w12_7_d2 <=  heap_bh30_w12_7_d1;
            heap_bh30_w13_6_d1 <=  heap_bh30_w13_6;
            heap_bh30_w13_6_d2 <=  heap_bh30_w13_6_d1;
            heap_bh30_w14_7_d1 <=  heap_bh30_w14_7;
            heap_bh30_w14_7_d2 <=  heap_bh30_w14_7_d1;
            heap_bh30_w34_3_d1 <=  heap_bh30_w34_3;
            heap_bh30_w35_1_d1 <=  heap_bh30_w35_1;
            heap_bh30_w36_1_d1 <=  heap_bh30_w36_1;
         end if;
      end process;
   XX_m29 <= X ;
   YY_m29 <= Y ;
   -- code generated by IntMultiplier::buildHeapLogicOnly()
   -- buildheaplogiconly called for lsbX=0 lsbY=9 msbX=2 msbY=26
   Xp_m29b31 <= XX_m29(1 downto 0) & "0";
   Yp_m29b31 <= YY_m29(25 downto 9) & "0";
   x_m29b31_0 <= Xp_m29b31(2 downto 0);
   y_m29b31_0 <= Yp_m29b31(2 downto 0);
   y_m29b31_1 <= Yp_m29b31(5 downto 3);
   y_m29b31_2 <= Yp_m29b31(8 downto 6);
   y_m29b31_3 <= Yp_m29b31(11 downto 9);
   y_m29b31_4 <= Yp_m29b31(14 downto 12);
   y_m29b31_5 <= Yp_m29b31(17 downto 15);
   ----------------Synchro barrier, entering cycle 0----------------
   -- Partial product row number 0
   Y0X0_31_m29 <= y_m29b31_0 & x_m29b31_0;
   PP_m29_31X0Y0_Tbl: SmallMultTableP3x3r6XuYu_F400_uid33  -- pipelineDepth=0 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 X => Y0X0_31_m29,
                 Y => PP31X0Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w9_0 <= PP31X0Y0_m29(2); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w10_0 <= PP31X0Y0_m29(3); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w11_0 <= PP31X0Y0_m29(4); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w12_0 <= PP31X0Y0_m29(5); -- cycle= 0 cp= 5.3072e-10

   -- Partial product row number 1
   Y1X0_31_m29 <= y_m29b31_1 & x_m29b31_0;
   PP_m29_31X0Y1_Tbl: SmallMultTableP3x3r6XuYu_F400_uid33  -- pipelineDepth=0 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 X => Y1X0_31_m29,
                 Y => PP31X0Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w11_1 <= PP31X0Y1_m29(1); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w12_1 <= PP31X0Y1_m29(2); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w13_0 <= PP31X0Y1_m29(3); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w14_0 <= PP31X0Y1_m29(4); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w15_0 <= PP31X0Y1_m29(5); -- cycle= 0 cp= 5.3072e-10

   -- Partial product row number 2
   Y2X0_31_m29 <= y_m29b31_2 & x_m29b31_0;
   PP_m29_31X0Y2_Tbl: SmallMultTableP3x3r6XuYu_F400_uid33  -- pipelineDepth=0 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 X => Y2X0_31_m29,
                 Y => PP31X0Y2_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w14_1 <= PP31X0Y2_m29(1); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w15_1 <= PP31X0Y2_m29(2); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w16_0 <= PP31X0Y2_m29(3); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w17_0 <= PP31X0Y2_m29(4); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w18_0 <= PP31X0Y2_m29(5); -- cycle= 0 cp= 5.3072e-10

   -- Partial product row number 3
   Y3X0_31_m29 <= y_m29b31_3 & x_m29b31_0;
   PP_m29_31X0Y3_Tbl: SmallMultTableP3x3r6XuYu_F400_uid33  -- pipelineDepth=0 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 X => Y3X0_31_m29,
                 Y => PP31X0Y3_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w17_1 <= PP31X0Y3_m29(1); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w18_1 <= PP31X0Y3_m29(2); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w19_0 <= PP31X0Y3_m29(3); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w20_0 <= PP31X0Y3_m29(4); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w21_0 <= PP31X0Y3_m29(5); -- cycle= 0 cp= 5.3072e-10

   -- Partial product row number 4
   Y4X0_31_m29 <= y_m29b31_4 & x_m29b31_0;
   PP_m29_31X0Y4_Tbl: SmallMultTableP3x3r6XuYu_F400_uid33  -- pipelineDepth=0 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 X => Y4X0_31_m29,
                 Y => PP31X0Y4_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w20_1 <= PP31X0Y4_m29(1); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w21_1 <= PP31X0Y4_m29(2); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w22_0 <= PP31X0Y4_m29(3); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w23_0 <= PP31X0Y4_m29(4); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w24_0 <= PP31X0Y4_m29(5); -- cycle= 0 cp= 5.3072e-10

   -- Partial product row number 5
   Y5X0_31_m29 <= y_m29b31_5 & x_m29b31_0;
   PP_m29_31X0Y5_Tbl: SmallMultTableP3x3r6XuYu_F400_uid33  -- pipelineDepth=0 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 X => Y5X0_31_m29,
                 Y => PP31X0Y5_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w23_1 <= PP31X0Y5_m29(1); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w24_1 <= PP31X0Y5_m29(2); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w25_0 <= PP31X0Y5_m29(3); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w26_0 <= PP31X0Y5_m29(4); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w27_0 <= PP31X0Y5_m29(5); -- cycle= 0 cp= 5.3072e-10

   -- code generated by IntMultiplier::buildHeapLogicOnly()
   -- buildheaplogiconly called for lsbX=0 lsbY=0 msbX=2 msbY=9
   Xp_m29b46 <= XX_m29(1 downto 0) & "0";
   Yp_m29b46 <= YY_m29(8 downto 0) & "";
   x_m29b46_0 <= Xp_m29b46(2 downto 0);
   y_m29b46_0 <= Yp_m29b46(2 downto 0);
   y_m29b46_1 <= Yp_m29b46(5 downto 3);
   y_m29b46_2 <= Yp_m29b46(8 downto 6);
   ----------------Synchro barrier, entering cycle 0----------------
   -- Partial product row number 0
   Y0X0_46_m29 <= y_m29b46_0 & x_m29b46_0;
   PP_m29_46X0Y0_Tbl: SmallMultTableP3x3r6XuYu_F400_uid48  -- pipelineDepth=0 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 X => Y0X0_46_m29,
                 Y => PP46X0Y0_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w0_0 <= PP46X0Y0_m29(1); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w1_0 <= PP46X0Y0_m29(2); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w2_0 <= PP46X0Y0_m29(3); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w3_0 <= PP46X0Y0_m29(4); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w4_0 <= PP46X0Y0_m29(5); -- cycle= 0 cp= 5.3072e-10

   -- Partial product row number 1
   Y1X0_46_m29 <= y_m29b46_1 & x_m29b46_0;
   PP_m29_46X0Y1_Tbl: SmallMultTableP3x3r6XuYu_F400_uid48  -- pipelineDepth=0 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 X => Y1X0_46_m29,
                 Y => PP46X0Y1_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w3_1 <= PP46X0Y1_m29(1); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w4_1 <= PP46X0Y1_m29(2); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w5_0 <= PP46X0Y1_m29(3); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w6_0 <= PP46X0Y1_m29(4); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w7_0 <= PP46X0Y1_m29(5); -- cycle= 0 cp= 5.3072e-10

   -- Partial product row number 2
   Y2X0_46_m29 <= y_m29b46_2 & x_m29b46_0;
   PP_m29_46X0Y2_Tbl: SmallMultTableP3x3r6XuYu_F400_uid48  -- pipelineDepth=0 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 X => Y2X0_46_m29,
                 Y => PP46X0Y2_m29);
   -- Adding the relevant bits to the heap of bits
   heap_bh30_w6_1 <= PP46X0Y2_m29(1); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w7_1 <= PP46X0Y2_m29(2); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w8_0 <= PP46X0Y2_m29(3); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w9_1 <= PP46X0Y2_m29(4); -- cycle= 0 cp= 5.3072e-10
   heap_bh30_w10_1 <= PP46X0Y2_m29(5); -- cycle= 0 cp= 5.3072e-10

   
   -- Beginning of code generated by BitHeap::generateCompressorVHDL
   -- code generated by BitHeap::generateSupertileVHDL()
   ----------------Synchro barrier, entering cycle 0----------------
   DSP_bh30_ch0_0 <= std_logic_vector(unsigned("" & XX_m29(25 downto 2) & "") * unsigned("" & YY_m29(25 downto 9) & ""));
   heap_bh30_w51_0 <= DSP_bh30_ch0_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w50_0 <= DSP_bh30_ch0_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w49_0 <= DSP_bh30_ch0_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w48_0 <= DSP_bh30_ch0_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w47_0 <= DSP_bh30_ch0_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w46_0 <= DSP_bh30_ch0_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w45_0 <= DSP_bh30_ch0_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w44_0 <= DSP_bh30_ch0_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w43_0 <= DSP_bh30_ch0_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w42_0 <= DSP_bh30_ch0_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w41_0 <= DSP_bh30_ch0_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w40_0 <= DSP_bh30_ch0_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w39_0 <= DSP_bh30_ch0_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w38_0 <= DSP_bh30_ch0_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w37_0 <= DSP_bh30_ch0_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w36_0 <= DSP_bh30_ch0_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w35_0 <= DSP_bh30_ch0_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w34_0 <= DSP_bh30_ch0_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w33_0 <= DSP_bh30_ch0_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w32_0 <= DSP_bh30_ch0_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w31_0 <= DSP_bh30_ch0_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w30_0 <= DSP_bh30_ch0_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w29_0 <= DSP_bh30_ch0_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w28_0 <= DSP_bh30_ch0_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w27_1 <= DSP_bh30_ch0_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w26_1 <= DSP_bh30_ch0_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w25_1 <= DSP_bh30_ch0_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w24_2 <= DSP_bh30_ch0_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w23_2 <= DSP_bh30_ch0_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w22_1 <= DSP_bh30_ch0_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w21_2 <= DSP_bh30_ch0_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w20_2 <= DSP_bh30_ch0_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w19_1 <= DSP_bh30_ch0_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w18_2 <= DSP_bh30_ch0_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w17_2 <= DSP_bh30_ch0_0(6); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w16_1 <= DSP_bh30_ch0_0(5); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w15_2 <= DSP_bh30_ch0_0(4); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w14_2 <= DSP_bh30_ch0_0(3); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w13_1 <= DSP_bh30_ch0_0(2); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w12_2 <= DSP_bh30_ch0_0(1); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w11_2 <= DSP_bh30_ch0_0(0); -- cycle= 0 cp= 2.387e-09
   ----------------Synchro barrier, entering cycle 0----------------
   DSP_bh30_ch1_0 <= std_logic_vector(unsigned("" & XX_m29(25 downto 2) & "") * unsigned("" & YY_m29(8 downto 0) & "00000000"));
   heap_bh30_w34_1 <= DSP_bh30_ch1_0(40); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w33_1 <= DSP_bh30_ch1_0(39); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w32_1 <= DSP_bh30_ch1_0(38); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w31_1 <= DSP_bh30_ch1_0(37); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w30_1 <= DSP_bh30_ch1_0(36); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w29_1 <= DSP_bh30_ch1_0(35); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w28_1 <= DSP_bh30_ch1_0(34); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w27_2 <= DSP_bh30_ch1_0(33); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w26_2 <= DSP_bh30_ch1_0(32); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w25_2 <= DSP_bh30_ch1_0(31); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w24_3 <= DSP_bh30_ch1_0(30); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w23_3 <= DSP_bh30_ch1_0(29); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w22_2 <= DSP_bh30_ch1_0(28); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w21_3 <= DSP_bh30_ch1_0(27); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w20_3 <= DSP_bh30_ch1_0(26); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w19_2 <= DSP_bh30_ch1_0(25); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w18_3 <= DSP_bh30_ch1_0(24); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w17_3 <= DSP_bh30_ch1_0(23); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w16_2 <= DSP_bh30_ch1_0(22); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w15_3 <= DSP_bh30_ch1_0(21); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w14_3 <= DSP_bh30_ch1_0(20); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w13_2 <= DSP_bh30_ch1_0(19); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w12_3 <= DSP_bh30_ch1_0(18); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w11_3 <= DSP_bh30_ch1_0(17); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w10_2 <= DSP_bh30_ch1_0(16); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w9_2 <= DSP_bh30_ch1_0(15); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w8_1 <= DSP_bh30_ch1_0(14); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w7_2 <= DSP_bh30_ch1_0(13); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w6_2 <= DSP_bh30_ch1_0(12); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w5_1 <= DSP_bh30_ch1_0(11); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w4_2 <= DSP_bh30_ch1_0(10); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w3_2 <= DSP_bh30_ch1_0(9); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w2_1 <= DSP_bh30_ch1_0(8); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w1_1 <= DSP_bh30_ch1_0(7); -- cycle= 0 cp= 2.387e-09
   heap_bh30_w0_1 <= DSP_bh30_ch1_0(6); -- cycle= 0 cp= 2.387e-09
   ----------------Synchro barrier, entering cycle 0----------------

   -- Adding the constant bits
      -- All the constant bits are zero, nothing to add

   ----------------Synchro barrier, entering cycle 0----------------

   ----------------Synchro barrier, entering cycle 0----------------
   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_0_0 <= heap_bh30_w11_1_d1 & heap_bh30_w11_0_d1 & heap_bh30_w11_3_d1 & heap_bh30_w11_2_d1;
   CompressorIn_bh30_0_1(0) <= heap_bh30_w12_1_d1;
      Compressor_bh30_0: Compressor_14_3
      port map ( R => CompressorOut_bh30_0_0,
                 X0 => CompressorIn_bh30_0_0,
                 X1 => CompressorIn_bh30_0_1);
   heap_bh30_w11_4 <= CompressorOut_bh30_0_0(0); -- cycle= 1 cp= 0
   heap_bh30_w12_4 <= CompressorOut_bh30_0_0(1); -- cycle= 1 cp= 0
   heap_bh30_w13_3 <= CompressorOut_bh30_0_0(2); -- cycle= 1 cp= 0

   ----------------Synchro barrier, entering cycle 0----------------
   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_1_2 <= heap_bh30_w14_1_d1 & heap_bh30_w14_0_d1 & heap_bh30_w14_3_d1 & heap_bh30_w14_2_d1;
   CompressorIn_bh30_1_3(0) <= heap_bh30_w15_1_d1;
      Compressor_bh30_1: Compressor_14_3
      port map ( R => CompressorOut_bh30_1_1,
                 X0 => CompressorIn_bh30_1_2,
                 X1 => CompressorIn_bh30_1_3);
   heap_bh30_w14_4 <= CompressorOut_bh30_1_1(0); -- cycle= 1 cp= 0
   heap_bh30_w15_4 <= CompressorOut_bh30_1_1(1); -- cycle= 1 cp= 0
   heap_bh30_w16_3 <= CompressorOut_bh30_1_1(2); -- cycle= 1 cp= 0

   ----------------Synchro barrier, entering cycle 0----------------
   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_2_4 <= heap_bh30_w17_1_d1 & heap_bh30_w17_0_d1 & heap_bh30_w17_3_d1 & heap_bh30_w17_2_d1;
   CompressorIn_bh30_2_5(0) <= heap_bh30_w18_1_d1;
      Compressor_bh30_2: Compressor_14_3
      port map ( R => CompressorOut_bh30_2_2,
                 X0 => CompressorIn_bh30_2_4,
                 X1 => CompressorIn_bh30_2_5);
   heap_bh30_w17_4 <= CompressorOut_bh30_2_2(0); -- cycle= 1 cp= 0
   heap_bh30_w18_4 <= CompressorOut_bh30_2_2(1); -- cycle= 1 cp= 0
   heap_bh30_w19_3 <= CompressorOut_bh30_2_2(2); -- cycle= 1 cp= 0

   ----------------Synchro barrier, entering cycle 0----------------
   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_3_6 <= heap_bh30_w20_1_d1 & heap_bh30_w20_0_d1 & heap_bh30_w20_3_d1 & heap_bh30_w20_2_d1;
   CompressorIn_bh30_3_7(0) <= heap_bh30_w21_1_d1;
      Compressor_bh30_3: Compressor_14_3
      port map ( R => CompressorOut_bh30_3_3,
                 X0 => CompressorIn_bh30_3_6,
                 X1 => CompressorIn_bh30_3_7);
   heap_bh30_w20_4 <= CompressorOut_bh30_3_3(0); -- cycle= 1 cp= 0
   heap_bh30_w21_4 <= CompressorOut_bh30_3_3(1); -- cycle= 1 cp= 0
   heap_bh30_w22_3 <= CompressorOut_bh30_3_3(2); -- cycle= 1 cp= 0

   ----------------Synchro barrier, entering cycle 0----------------
   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_4_8 <= heap_bh30_w23_1_d1 & heap_bh30_w23_0_d1 & heap_bh30_w23_3_d1 & heap_bh30_w23_2_d1;
   CompressorIn_bh30_4_9(0) <= heap_bh30_w24_1_d1;
      Compressor_bh30_4: Compressor_14_3
      port map ( R => CompressorOut_bh30_4_4,
                 X0 => CompressorIn_bh30_4_8,
                 X1 => CompressorIn_bh30_4_9);
   heap_bh30_w23_4 <= CompressorOut_bh30_4_4(0); -- cycle= 1 cp= 0
   heap_bh30_w24_4 <= CompressorOut_bh30_4_4(1); -- cycle= 1 cp= 0
   heap_bh30_w25_3 <= CompressorOut_bh30_4_4(2); -- cycle= 1 cp= 0

   ----------------Synchro barrier, entering cycle 0----------------
   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_5_10 <= heap_bh30_w3_1_d1 & heap_bh30_w3_0_d1 & heap_bh30_w3_2_d1;
   CompressorIn_bh30_5_11 <= heap_bh30_w4_1_d1 & heap_bh30_w4_0_d1;
      Compressor_bh30_5: Compressor_23_3
      port map ( R => CompressorOut_bh30_5_5,
                 X0 => CompressorIn_bh30_5_10,
                 X1 => CompressorIn_bh30_5_11);
   heap_bh30_w3_3 <= CompressorOut_bh30_5_5(0); -- cycle= 1 cp= 0
   heap_bh30_w4_3 <= CompressorOut_bh30_5_5(1); -- cycle= 1 cp= 0
   heap_bh30_w5_2 <= CompressorOut_bh30_5_5(2); -- cycle= 1 cp= 0

   ----------------Synchro barrier, entering cycle 0----------------
   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_6_12 <= heap_bh30_w6_1_d1 & heap_bh30_w6_0_d1 & heap_bh30_w6_2_d1;
   CompressorIn_bh30_6_13 <= heap_bh30_w7_1_d1 & heap_bh30_w7_0_d1;
      Compressor_bh30_6: Compressor_23_3
      port map ( R => CompressorOut_bh30_6_6,
                 X0 => CompressorIn_bh30_6_12,
                 X1 => CompressorIn_bh30_6_13);
   heap_bh30_w6_3 <= CompressorOut_bh30_6_6(0); -- cycle= 1 cp= 0
   heap_bh30_w7_3 <= CompressorOut_bh30_6_6(1); -- cycle= 1 cp= 0
   heap_bh30_w8_2 <= CompressorOut_bh30_6_6(2); -- cycle= 1 cp= 0

   ----------------Synchro barrier, entering cycle 0----------------
   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_7_14 <= heap_bh30_w9_1_d1 & heap_bh30_w9_0_d1 & heap_bh30_w9_2_d1;
   CompressorIn_bh30_7_15 <= heap_bh30_w10_1_d1 & heap_bh30_w10_0_d1;
      Compressor_bh30_7: Compressor_23_3
      port map ( R => CompressorOut_bh30_7_7,
                 X0 => CompressorIn_bh30_7_14,
                 X1 => CompressorIn_bh30_7_15);
   heap_bh30_w9_3 <= CompressorOut_bh30_7_7(0); -- cycle= 1 cp= 0
   heap_bh30_w10_3 <= CompressorOut_bh30_7_7(1); -- cycle= 1 cp= 0
   heap_bh30_w11_5 <= CompressorOut_bh30_7_7(2); -- cycle= 1 cp= 0

   ----------------Synchro barrier, entering cycle 0----------------
   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_8_16 <= heap_bh30_w12_0_d1 & heap_bh30_w12_3_d1 & heap_bh30_w12_2_d1;
   CompressorIn_bh30_8_17 <= heap_bh30_w13_0_d1 & heap_bh30_w13_2_d1;
      Compressor_bh30_8: Compressor_23_3
      port map ( R => CompressorOut_bh30_8_8,
                 X0 => CompressorIn_bh30_8_16,
                 X1 => CompressorIn_bh30_8_17);
   heap_bh30_w12_5 <= CompressorOut_bh30_8_8(0); -- cycle= 1 cp= 0
   heap_bh30_w13_4 <= CompressorOut_bh30_8_8(1); -- cycle= 1 cp= 0
   heap_bh30_w14_5 <= CompressorOut_bh30_8_8(2); -- cycle= 1 cp= 0

   ----------------Synchro barrier, entering cycle 0----------------
   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_9_18 <= heap_bh30_w15_0_d1 & heap_bh30_w15_3_d1 & heap_bh30_w15_2_d1;
   CompressorIn_bh30_9_19 <= heap_bh30_w16_0_d1 & heap_bh30_w16_2_d1;
      Compressor_bh30_9: Compressor_23_3
      port map ( R => CompressorOut_bh30_9_9,
                 X0 => CompressorIn_bh30_9_18,
                 X1 => CompressorIn_bh30_9_19);
   heap_bh30_w15_5 <= CompressorOut_bh30_9_9(0); -- cycle= 1 cp= 0
   heap_bh30_w16_4 <= CompressorOut_bh30_9_9(1); -- cycle= 1 cp= 0
   heap_bh30_w17_5 <= CompressorOut_bh30_9_9(2); -- cycle= 1 cp= 0

   ----------------Synchro barrier, entering cycle 0----------------
   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_10_20 <= heap_bh30_w18_0_d1 & heap_bh30_w18_3_d1 & heap_bh30_w18_2_d1;
   CompressorIn_bh30_10_21 <= heap_bh30_w19_0_d1 & heap_bh30_w19_2_d1;
      Compressor_bh30_10: Compressor_23_3
      port map ( R => CompressorOut_bh30_10_10,
                 X0 => CompressorIn_bh30_10_20,
                 X1 => CompressorIn_bh30_10_21);
   heap_bh30_w18_5 <= CompressorOut_bh30_10_10(0); -- cycle= 1 cp= 0
   heap_bh30_w19_4 <= CompressorOut_bh30_10_10(1); -- cycle= 1 cp= 0
   heap_bh30_w20_5 <= CompressorOut_bh30_10_10(2); -- cycle= 1 cp= 0

   ----------------Synchro barrier, entering cycle 0----------------
   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_11_22 <= heap_bh30_w21_0_d1 & heap_bh30_w21_3_d1 & heap_bh30_w21_2_d1;
   CompressorIn_bh30_11_23 <= heap_bh30_w22_0_d1 & heap_bh30_w22_2_d1;
      Compressor_bh30_11: Compressor_23_3
      port map ( R => CompressorOut_bh30_11_11,
                 X0 => CompressorIn_bh30_11_22,
                 X1 => CompressorIn_bh30_11_23);
   heap_bh30_w21_5 <= CompressorOut_bh30_11_11(0); -- cycle= 1 cp= 0
   heap_bh30_w22_4 <= CompressorOut_bh30_11_11(1); -- cycle= 1 cp= 0
   heap_bh30_w23_5 <= CompressorOut_bh30_11_11(2); -- cycle= 1 cp= 0

   ----------------Synchro barrier, entering cycle 0----------------
   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_12_24 <= heap_bh30_w24_0_d1 & heap_bh30_w24_3_d1 & heap_bh30_w24_2_d1;
   CompressorIn_bh30_12_25 <= heap_bh30_w25_0_d1 & heap_bh30_w25_2_d1;
      Compressor_bh30_12: Compressor_23_3
      port map ( R => CompressorOut_bh30_12_12,
                 X0 => CompressorIn_bh30_12_24,
                 X1 => CompressorIn_bh30_12_25);
   heap_bh30_w24_5 <= CompressorOut_bh30_12_12(0); -- cycle= 1 cp= 0
   heap_bh30_w25_4 <= CompressorOut_bh30_12_12(1); -- cycle= 1 cp= 0
   heap_bh30_w26_3 <= CompressorOut_bh30_12_12(2); -- cycle= 1 cp= 0

   ----------------Synchro barrier, entering cycle 0----------------
   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_13_26 <= heap_bh30_w26_0_d1 & heap_bh30_w26_2_d1 & heap_bh30_w26_1_d1;
   CompressorIn_bh30_13_27 <= heap_bh30_w27_0_d1 & heap_bh30_w27_2_d1;
      Compressor_bh30_13: Compressor_23_3
      port map ( R => CompressorOut_bh30_13_13,
                 X0 => CompressorIn_bh30_13_26,
                 X1 => CompressorIn_bh30_13_27);
   heap_bh30_w26_4 <= CompressorOut_bh30_13_13(0); -- cycle= 1 cp= 0
   heap_bh30_w27_3 <= CompressorOut_bh30_13_13(1); -- cycle= 1 cp= 0
   heap_bh30_w28_2 <= CompressorOut_bh30_13_13(2); -- cycle= 1 cp= 0

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_14_28 <= heap_bh30_w13_1_d1 & heap_bh30_w13_4 & heap_bh30_w13_3;
   CompressorIn_bh30_14_29 <= heap_bh30_w14_5 & heap_bh30_w14_4;
      Compressor_bh30_14: Compressor_23_3
      port map ( R => CompressorOut_bh30_14_14,
                 X0 => CompressorIn_bh30_14_28,
                 X1 => CompressorIn_bh30_14_29);
   heap_bh30_w13_5 <= CompressorOut_bh30_14_14(0); -- cycle= 1 cp= 5.3072e-10
   heap_bh30_w14_6 <= CompressorOut_bh30_14_14(1); -- cycle= 1 cp= 5.3072e-10
   heap_bh30_w15_6 <= CompressorOut_bh30_14_14(2); -- cycle= 1 cp= 5.3072e-10

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_15_30 <= heap_bh30_w16_1_d1 & heap_bh30_w16_4 & heap_bh30_w16_3;
   CompressorIn_bh30_15_31 <= heap_bh30_w17_5 & heap_bh30_w17_4;
      Compressor_bh30_15: Compressor_23_3
      port map ( R => CompressorOut_bh30_15_15,
                 X0 => CompressorIn_bh30_15_30,
                 X1 => CompressorIn_bh30_15_31);
   heap_bh30_w16_5 <= CompressorOut_bh30_15_15(0); -- cycle= 1 cp= 5.3072e-10
   heap_bh30_w17_6 <= CompressorOut_bh30_15_15(1); -- cycle= 1 cp= 5.3072e-10
   heap_bh30_w18_6 <= CompressorOut_bh30_15_15(2); -- cycle= 1 cp= 5.3072e-10

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_16_32 <= heap_bh30_w19_1_d1 & heap_bh30_w19_4 & heap_bh30_w19_3;
   CompressorIn_bh30_16_33 <= heap_bh30_w20_5 & heap_bh30_w20_4;
      Compressor_bh30_16: Compressor_23_3
      port map ( R => CompressorOut_bh30_16_16,
                 X0 => CompressorIn_bh30_16_32,
                 X1 => CompressorIn_bh30_16_33);
   heap_bh30_w19_5 <= CompressorOut_bh30_16_16(0); -- cycle= 1 cp= 5.3072e-10
   heap_bh30_w20_6 <= CompressorOut_bh30_16_16(1); -- cycle= 1 cp= 5.3072e-10
   heap_bh30_w21_6 <= CompressorOut_bh30_16_16(2); -- cycle= 1 cp= 5.3072e-10

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_17_34 <= heap_bh30_w22_1_d1 & heap_bh30_w22_4 & heap_bh30_w22_3;
   CompressorIn_bh30_17_35 <= heap_bh30_w23_5 & heap_bh30_w23_4;
      Compressor_bh30_17: Compressor_23_3
      port map ( R => CompressorOut_bh30_17_17,
                 X0 => CompressorIn_bh30_17_34,
                 X1 => CompressorIn_bh30_17_35);
   heap_bh30_w22_5 <= CompressorOut_bh30_17_17(0); -- cycle= 1 cp= 5.3072e-10
   heap_bh30_w23_6 <= CompressorOut_bh30_17_17(1); -- cycle= 1 cp= 5.3072e-10
   heap_bh30_w24_6 <= CompressorOut_bh30_17_17(2); -- cycle= 1 cp= 5.3072e-10

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_18_36 <= heap_bh30_w25_1_d1 & heap_bh30_w25_4 & heap_bh30_w25_3;
   CompressorIn_bh30_18_37 <= heap_bh30_w26_4 & heap_bh30_w26_3;
      Compressor_bh30_18: Compressor_23_3
      port map ( R => CompressorOut_bh30_18_18,
                 X0 => CompressorIn_bh30_18_36,
                 X1 => CompressorIn_bh30_18_37);
   heap_bh30_w25_5 <= CompressorOut_bh30_18_18(0); -- cycle= 1 cp= 5.3072e-10
   heap_bh30_w26_5 <= CompressorOut_bh30_18_18(1); -- cycle= 1 cp= 5.3072e-10
   heap_bh30_w27_4 <= CompressorOut_bh30_18_18(2); -- cycle= 1 cp= 5.3072e-10

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_19_38 <= heap_bh30_w28_1_d1 & heap_bh30_w28_0_d1 & heap_bh30_w28_2;
   CompressorIn_bh30_19_39 <= heap_bh30_w29_1_d1 & heap_bh30_w29_0_d1;
      Compressor_bh30_19: Compressor_23_3
      port map ( R => CompressorOut_bh30_19_19,
                 X0 => CompressorIn_bh30_19_38,
                 X1 => CompressorIn_bh30_19_39);
   heap_bh30_w28_3 <= CompressorOut_bh30_19_19(0); -- cycle= 1 cp= 5.3072e-10
   heap_bh30_w29_2 <= CompressorOut_bh30_19_19(1); -- cycle= 1 cp= 5.3072e-10
   heap_bh30_w30_2 <= CompressorOut_bh30_19_19(2); -- cycle= 1 cp= 5.3072e-10

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_20_40 <= heap_bh30_w5_0_d1 & heap_bh30_w5_1_d1 & heap_bh30_w5_2;
   CompressorIn_bh30_20_41(0) <= heap_bh30_w6_3;
      Compressor_bh30_20: Compressor_13_3
      port map ( R => CompressorOut_bh30_20_20,
                 X0 => CompressorIn_bh30_20_40,
                 X1 => CompressorIn_bh30_20_41);
   heap_bh30_w5_3 <= CompressorOut_bh30_20_20(0); -- cycle= 1 cp= 5.3072e-10
   heap_bh30_w6_4 <= CompressorOut_bh30_20_20(1); -- cycle= 1 cp= 5.3072e-10
   heap_bh30_w7_4 <= CompressorOut_bh30_20_20(2); -- cycle= 1 cp= 5.3072e-10

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_21_42 <= heap_bh30_w8_0_d1 & heap_bh30_w8_1_d1 & heap_bh30_w8_2;
   CompressorIn_bh30_21_43(0) <= heap_bh30_w9_3;
      Compressor_bh30_21: Compressor_13_3
      port map ( R => CompressorOut_bh30_21_21,
                 X0 => CompressorIn_bh30_21_42,
                 X1 => CompressorIn_bh30_21_43);
   heap_bh30_w8_3 <= CompressorOut_bh30_21_21(0); -- cycle= 1 cp= 5.3072e-10
   heap_bh30_w9_4 <= CompressorOut_bh30_21_21(1); -- cycle= 1 cp= 5.3072e-10
   heap_bh30_w10_4 <= CompressorOut_bh30_21_21(2); -- cycle= 1 cp= 5.3072e-10

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_22_44 <= heap_bh30_w10_2_d1 & heap_bh30_w10_3 & heap_bh30_w10_4;
   CompressorIn_bh30_22_45 <= heap_bh30_w11_5 & heap_bh30_w11_4;
      Compressor_bh30_22: Compressor_23_3
      port map ( R => CompressorOut_bh30_22_22,
                 X0 => CompressorIn_bh30_22_44,
                 X1 => CompressorIn_bh30_22_45);
   heap_bh30_w10_5 <= CompressorOut_bh30_22_22(0); -- cycle= 1 cp= 1.06144e-09
   heap_bh30_w11_6 <= CompressorOut_bh30_22_22(1); -- cycle= 1 cp= 1.06144e-09
   heap_bh30_w12_6 <= CompressorOut_bh30_22_22(2); -- cycle= 1 cp= 1.06144e-09

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_23_46 <= heap_bh30_w30_1_d1 & heap_bh30_w30_0_d1 & heap_bh30_w30_2;
   CompressorIn_bh30_23_47 <= heap_bh30_w31_1_d1 & heap_bh30_w31_0_d1;
      Compressor_bh30_23: Compressor_23_3
      port map ( R => CompressorOut_bh30_23_23,
                 X0 => CompressorIn_bh30_23_46,
                 X1 => CompressorIn_bh30_23_47);
   heap_bh30_w30_3 <= CompressorOut_bh30_23_23(0); -- cycle= 1 cp= 1.06144e-09
   heap_bh30_w31_2 <= CompressorOut_bh30_23_23(1); -- cycle= 1 cp= 1.06144e-09
   heap_bh30_w32_2 <= CompressorOut_bh30_23_23(2); -- cycle= 1 cp= 1.06144e-09

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_24_48 <= heap_bh30_w7_2_d1 & heap_bh30_w7_3 & heap_bh30_w7_4;
   CompressorIn_bh30_24_49(0) <= heap_bh30_w8_3;
      Compressor_bh30_24: Compressor_13_3
      port map ( R => CompressorOut_bh30_24_24,
                 X0 => CompressorIn_bh30_24_48,
                 X1 => CompressorIn_bh30_24_49);
   heap_bh30_w7_5 <= CompressorOut_bh30_24_24(0); -- cycle= 1 cp= 1.06144e-09
   heap_bh30_w8_4 <= CompressorOut_bh30_24_24(1); -- cycle= 1 cp= 1.06144e-09
   heap_bh30_w9_5 <= CompressorOut_bh30_24_24(2); -- cycle= 1 cp= 1.06144e-09

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_25_50 <= heap_bh30_w15_5 & heap_bh30_w15_4 & heap_bh30_w15_6;
   CompressorIn_bh30_25_51(0) <= heap_bh30_w16_5;
      Compressor_bh30_25: Compressor_13_3
      port map ( R => CompressorOut_bh30_25_25,
                 X0 => CompressorIn_bh30_25_50,
                 X1 => CompressorIn_bh30_25_51);
   heap_bh30_w15_7 <= CompressorOut_bh30_25_25(0); -- cycle= 1 cp= 1.06144e-09
   heap_bh30_w16_6 <= CompressorOut_bh30_25_25(1); -- cycle= 1 cp= 1.06144e-09
   heap_bh30_w17_7 <= CompressorOut_bh30_25_25(2); -- cycle= 1 cp= 1.06144e-09

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_26_52 <= heap_bh30_w18_5 & heap_bh30_w18_4 & heap_bh30_w18_6;
   CompressorIn_bh30_26_53(0) <= heap_bh30_w19_5;
      Compressor_bh30_26: Compressor_13_3
      port map ( R => CompressorOut_bh30_26_26,
                 X0 => CompressorIn_bh30_26_52,
                 X1 => CompressorIn_bh30_26_53);
   heap_bh30_w18_7 <= CompressorOut_bh30_26_26(0); -- cycle= 1 cp= 1.06144e-09
   heap_bh30_w19_6 <= CompressorOut_bh30_26_26(1); -- cycle= 1 cp= 1.06144e-09
   heap_bh30_w20_7 <= CompressorOut_bh30_26_26(2); -- cycle= 1 cp= 1.06144e-09

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_27_54 <= heap_bh30_w21_5 & heap_bh30_w21_4 & heap_bh30_w21_6;
   CompressorIn_bh30_27_55(0) <= heap_bh30_w22_5;
      Compressor_bh30_27: Compressor_13_3
      port map ( R => CompressorOut_bh30_27_27,
                 X0 => CompressorIn_bh30_27_54,
                 X1 => CompressorIn_bh30_27_55);
   heap_bh30_w21_7 <= CompressorOut_bh30_27_27(0); -- cycle= 1 cp= 1.06144e-09
   heap_bh30_w22_6 <= CompressorOut_bh30_27_27(1); -- cycle= 1 cp= 1.06144e-09
   heap_bh30_w23_7 <= CompressorOut_bh30_27_27(2); -- cycle= 1 cp= 1.06144e-09

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_28_56 <= heap_bh30_w24_5 & heap_bh30_w24_4 & heap_bh30_w24_6;
   CompressorIn_bh30_28_57(0) <= heap_bh30_w25_5;
      Compressor_bh30_28: Compressor_13_3
      port map ( R => CompressorOut_bh30_28_28,
                 X0 => CompressorIn_bh30_28_56,
                 X1 => CompressorIn_bh30_28_57);
   heap_bh30_w24_7 <= CompressorOut_bh30_28_28(0); -- cycle= 1 cp= 1.06144e-09
   heap_bh30_w25_6 <= CompressorOut_bh30_28_28(1); -- cycle= 1 cp= 1.06144e-09
   heap_bh30_w26_6 <= CompressorOut_bh30_28_28(2); -- cycle= 1 cp= 1.06144e-09

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_29_58 <= heap_bh30_w27_1_d1 & heap_bh30_w27_3 & heap_bh30_w27_4;
   CompressorIn_bh30_29_59(0) <= heap_bh30_w28_3;
      Compressor_bh30_29: Compressor_13_3
      port map ( R => CompressorOut_bh30_29_29,
                 X0 => CompressorIn_bh30_29_58,
                 X1 => CompressorIn_bh30_29_59);
   heap_bh30_w27_5 <= CompressorOut_bh30_29_29(0); -- cycle= 1 cp= 1.06144e-09
   heap_bh30_w28_4 <= CompressorOut_bh30_29_29(1); -- cycle= 1 cp= 1.06144e-09
   heap_bh30_w29_3 <= CompressorOut_bh30_29_29(2); -- cycle= 1 cp= 1.06144e-09

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_30_60 <= heap_bh30_w32_1_d1 & heap_bh30_w32_0_d1 & heap_bh30_w32_2;
   CompressorIn_bh30_30_61 <= heap_bh30_w33_1_d1 & heap_bh30_w33_0_d1;
      Compressor_bh30_30: Compressor_23_3
      port map ( R => CompressorOut_bh30_30_30,
                 X0 => CompressorIn_bh30_30_60,
                 X1 => CompressorIn_bh30_30_61);
   heap_bh30_w32_3 <= CompressorOut_bh30_30_30(0); -- cycle= 1 cp= 1.59216e-09
   heap_bh30_w33_2 <= CompressorOut_bh30_30_30(1); -- cycle= 1 cp= 1.59216e-09
   heap_bh30_w34_2 <= CompressorOut_bh30_30_30(2); -- cycle= 1 cp= 1.59216e-09

   ----------------Synchro barrier, entering cycle 1----------------
   CompressorIn_bh30_31_62 <= heap_bh30_w12_5 & heap_bh30_w12_4 & heap_bh30_w12_6;
   CompressorIn_bh30_31_63(0) <= heap_bh30_w13_5;
      Compressor_bh30_31: Compressor_13_3
      port map ( R => CompressorOut_bh30_31_31,
                 X0 => CompressorIn_bh30_31_62,
                 X1 => CompressorIn_bh30_31_63);
   heap_bh30_w12_7 <= CompressorOut_bh30_31_31(0); -- cycle= 1 cp= 1.59216e-09
   heap_bh30_w13_6 <= CompressorOut_bh30_31_31(1); -- cycle= 1 cp= 1.59216e-09
   heap_bh30_w14_7 <= CompressorOut_bh30_31_31(2); -- cycle= 1 cp= 1.59216e-09

   ----------------Synchro barrier, entering cycle 1----------------
   ----------------Synchro barrier, entering cycle 2----------------
   CompressorIn_bh30_32_64 <= heap_bh30_w34_1_d2 & heap_bh30_w34_0_d2 & heap_bh30_w34_2_d1;
   CompressorIn_bh30_32_65(0) <= heap_bh30_w35_0_d2;
      Compressor_bh30_32: Compressor_13_3
      port map ( R => CompressorOut_bh30_32_32,
                 X0 => CompressorIn_bh30_32_64,
                 X1 => CompressorIn_bh30_32_65);
   heap_bh30_w34_3 <= CompressorOut_bh30_32_32(0); -- cycle= 2 cp= 0
   heap_bh30_w35_1 <= CompressorOut_bh30_32_32(1); -- cycle= 2 cp= 0
   heap_bh30_w36_1 <= CompressorOut_bh30_32_32(2); -- cycle= 2 cp= 0
   ----------------Synchro barrier, entering cycle 2----------------
   ----------------Synchro barrier, entering cycle 3----------------
   finalAdderIn0_bh30 <= "0" & heap_bh30_w51_0_d3 & heap_bh30_w50_0_d3 & heap_bh30_w49_0_d3 & heap_bh30_w48_0_d3 & heap_bh30_w47_0_d3 & heap_bh30_w46_0_d3 & heap_bh30_w45_0_d3 & heap_bh30_w44_0_d3 & heap_bh30_w43_0_d3 & heap_bh30_w42_0_d3 & heap_bh30_w41_0_d3 & heap_bh30_w40_0_d3 & heap_bh30_w39_0_d3 & heap_bh30_w38_0_d3 & heap_bh30_w37_0_d3 & heap_bh30_w36_0_d3 & heap_bh30_w35_1_d1 & heap_bh30_w34_3_d1 & heap_bh30_w33_2_d2 & heap_bh30_w32_3_d2 & heap_bh30_w31_2_d2 & heap_bh30_w30_3_d2 & heap_bh30_w29_2_d2 & heap_bh30_w28_4_d2 & heap_bh30_w27_5_d2 & heap_bh30_w26_5_d2 & heap_bh30_w25_6_d2 & heap_bh30_w24_7_d2 & heap_bh30_w23_6_d2 & heap_bh30_w22_6_d2 & heap_bh30_w21_7_d2 & heap_bh30_w20_6_d2 & heap_bh30_w19_6_d2 & heap_bh30_w18_7_d2 & heap_bh30_w17_6_d2 & heap_bh30_w16_6_d2 & heap_bh30_w15_7_d2 & heap_bh30_w14_6_d2 & heap_bh30_w13_6_d2 & heap_bh30_w12_7_d2 & heap_bh30_w11_6_d2 & heap_bh30_w10_5_d2 & heap_bh30_w9_4_d2 & heap_bh30_w8_4_d2 & heap_bh30_w7_5_d2 & heap_bh30_w6_4_d2 & heap_bh30_w5_3_d2 & heap_bh30_w4_2_d3 & heap_bh30_w3_3_d2 & heap_bh30_w2_0_d3 & heap_bh30_w1_0_d3 & heap_bh30_w0_0_d3;
   finalAdderIn1_bh30 <= "0" & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & '0' & heap_bh30_w36_1_d1 & '0' & '0' & '0' & '0' & '0' & '0' & heap_bh30_w29_3_d2 & '0' & '0' & heap_bh30_w26_6_d2 & '0' & '0' & heap_bh30_w23_7_d2 & '0' & '0' & heap_bh30_w20_7_d2 & '0' & '0' & heap_bh30_w17_7_d2 & '0' & '0' & heap_bh30_w14_7_d2 & '0' & '0' & '0' & '0' & heap_bh30_w9_5_d2 & '0' & '0' & '0' & '0' & heap_bh30_w4_3_d2 & '0' & heap_bh30_w2_1_d3 & heap_bh30_w1_1_d3 & heap_bh30_w0_1_d3;
   finalAdderCin_bh30 <= '0';
      Adder_final30_0: IntAdder_53_f400_uid129  -- pipelineDepth=1 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 Cin => finalAdderCin_bh30,
                 R => finalAdderOut_bh30,
                 X => finalAdderIn0_bh30,
                 Y => finalAdderIn1_bh30);
   ----------------Synchro barrier, entering cycle 4----------------
   -- concatenate all the compressed chunks
   CompressionResult30 <= finalAdderOut_bh30;
   -- End of code generated by BitHeap::generateCompressorVHDL
   R <= CompressionResult30(51 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                   RightShifter_57_by_max_32_F400_uid139
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca, Florent de Dinechin (2008-2011)
--------------------------------------------------------------------------------
-- Pipeline depth: 2 cycles

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity RightShifter_57_by_max_32_F400_uid139 is
   port ( clk, rst : in std_logic;
          X : in  std_logic_vector(56 downto 0);
          S : in  std_logic_vector(5 downto 0);
          R : out  std_logic_vector(88 downto 0)   );
end entity;

architecture arch of RightShifter_57_by_max_32_F400_uid139 is
signal level0 :  std_logic_vector(56 downto 0);
signal ps, ps_d1, ps_d2 :  std_logic_vector(5 downto 0);
signal level1 :  std_logic_vector(57 downto 0);
signal level2, level2_d1 :  std_logic_vector(59 downto 0);
signal level3 :  std_logic_vector(63 downto 0);
signal level4, level4_d1 :  std_logic_vector(71 downto 0);
signal level5 :  std_logic_vector(87 downto 0);
signal level6 :  std_logic_vector(119 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
            ps_d1 <=  ps;
            ps_d2 <=  ps_d1;
            level2_d1 <=  level2;
            level4_d1 <=  level4;
         end if;
      end process;
   level0<= X;
   ps<= S;
   level1<=  (0 downto 0 => '0') & level0 when ps(0) = '1' else    level0 & (0 downto 0 => '0');
   level2<=  (1 downto 0 => '0') & level1 when ps(1) = '1' else    level1 & (1 downto 0 => '0');
   ----------------Synchro barrier, entering cycle 1----------------
   level3<=  (3 downto 0 => '0') & level2_d1 when ps_d1(2) = '1' else    level2_d1 & (3 downto 0 => '0');
   level4<=  (7 downto 0 => '0') & level3 when ps_d1(3) = '1' else    level3 & (7 downto 0 => '0');
   ----------------Synchro barrier, entering cycle 2----------------
   level5<=  (15 downto 0 => '0') & level4_d1 when ps_d2(4) = '1' else    level4_d1 & (15 downto 0 => '0');
   level6<=  (31 downto 0 => '0') & level5 when ps_d2(5) = '1' else    level5 & (31 downto 0 => '0');
   R <= level6(119 downto 31);
end architecture;

--------------------------------------------------------------------------------
--                          PositMult_32_4_F400_uid2
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Raul Murillo, 2019
--------------------------------------------------------------------------------
-- Pipeline depth: 15 cycles

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PositMult_32_4_F400_uid2 is
   port ( clk, rst : in std_logic;
          InputA : in  std_logic_vector(31 downto 0);
          InputB : in  std_logic_vector(31 downto 0);
          Output : out  std_logic_vector(31 downto 0)   );
end entity;

architecture arch of PositMult_32_4_F400_uid2 is




----------------
----------------
----------------
component reg is
 port (
clk: in std_logic;
ram_read_en: in std_logic;
ram_data_in: in std_logic_vector(31 downto 0);
ram_data_out: out std_logic_vector(31 downto 0));
end component;

----------------
----------------
----------------
   component PositDecoder_32_4_F400_uid4 is
      port ( clk, rst : in std_logic;
             Input : in  std_logic_vector(31 downto 0);
             Sign : out  std_logic;
             Reg : out  std_logic_vector(5 downto 0);
             Exp : out  std_logic_vector(3 downto 0);
             Frac : out  std_logic_vector(25 downto 0);
             z : out  std_logic;
             inf : out  std_logic   );
   end component;

   component PositDecoder_32_4_F400_uid16 is
      port ( clk, rst : in std_logic;
             Input : in  std_logic_vector(31 downto 0);
             Sign : out  std_logic;
             Reg : out  std_logic_vector(5 downto 0);
             Exp : out  std_logic_vector(3 downto 0);
             Frac : out  std_logic_vector(25 downto 0);
             z : out  std_logic;
             inf : out  std_logic   );
   end component;

   component IntMultiplier_UsingDSP_26_26_52_unsigned_F400_uid28 is
      port ( clk, rst : in std_logic;
             X : in  std_logic_vector(25 downto 0);
             Y : in  std_logic_vector(25 downto 0);
             R : out  std_logic_vector(51 downto 0)   );
   end component;

   component RightShifter_57_by_max_32_F400_uid139 is
      port ( clk, rst : in std_logic;
             X : in  std_logic_vector(56 downto 0);
             S : in  std_logic_vector(5 downto 0);
             R : out  std_logic_vector(88 downto 0)   );
   end component;

signal sign_A :  std_logic;
signal reg_A :  std_logic_vector(5 downto 0);
signal exp_A :  std_logic_vector(3 downto 0);
signal frac_A :  std_logic_vector(25 downto 0);
signal z_A :  std_logic;
signal inf_A :  std_logic;
signal sign_B :  std_logic;
signal reg_B :  std_logic_vector(5 downto 0);
signal exp_B :  std_logic_vector(3 downto 0);
signal frac_B :  std_logic_vector(25 downto 0);
signal z_B :  std_logic;
signal inf_B :  std_logic;
signal sf_A, sf_A_d1, sf_A_d2, sf_A_d3, sf_A_d4 :  std_logic_vector(9 downto 0);
signal sf_B, sf_B_d1, sf_B_d2, sf_B_d3, sf_B_d4 :  std_logic_vector(9 downto 0);
signal sign, sign_d1, sign_d2, sign_d3, sign_d4, sign_d5, sign_d6, sign_d7, sign_d8, sign_d9, sign_d10 :  std_logic;
signal z, z_d1, z_d2, z_d3, z_d4, z_d5, z_d6, z_d7, z_d8, z_d9, z_d10 :  std_logic;
signal inf, inf_d1, inf_d2, inf_d3, inf_d4, inf_d5, inf_d6, inf_d7, inf_d8, inf_d9, inf_d10 :  std_logic;
signal frac_mult :  std_logic_vector(51 downto 0);
signal ovf_m :  std_logic;
signal normFrac, normFrac_d1, normFrac_d2, normFrac_d3 :  std_logic_vector(52 downto 0);
signal sf_mult :  std_logic_vector(10 downto 0);
signal sf_sign, sf_sign_d1, sf_sign_d2, sf_sign_d3 :  std_logic;
signal nzero, nzero_d1, nzero_d2, nzero_d3 :  std_logic;
signal ExpBits, ExpBits_d1, ExpBits_d2, ExpBits_d3 :  std_logic_vector(3 downto 0);
signal RegimeAns_tmp, RegimeAns_tmp_d1 :  std_logic_vector(5 downto 0);
signal RegimeAns :  std_logic_vector(5 downto 0);
signal ovf_reg, ovf_reg_d1, ovf_reg_d2, ovf_reg_d3, ovf_reg_d4, ovf_reg_d5 :  std_logic;
signal FinalRegime, FinalRegime_d1, FinalRegime_d2 :  std_logic_vector(5 downto 0);
signal ovf_regF, ovf_regF_d1, ovf_regF_d2, ovf_regF_d3, ovf_regF_d4 :  std_logic;
signal FinalExp :  std_logic_vector(3 downto 0);
signal tmp1 :  std_logic_vector(56 downto 0);
signal tmp2 :  std_logic_vector(56 downto 0);
signal shift_neg :  std_logic_vector(5 downto 0);
signal shift_pos :  std_logic_vector(5 downto 0);
signal shifter_in :  std_logic_vector(56 downto 0);
signal shifter_S :  std_logic_vector(5 downto 0);
signal shifter_out, shifter_out_d1 :  std_logic_vector(88 downto 0);
signal tmp_ans :  std_logic_vector(30 downto 0);
signal LSB :  std_logic;
signal G :  std_logic;
signal R :  std_logic;
signal S :  std_logic;
signal round :  std_logic;

signal InputA_buff : std_logic_vector(31 downto 0);
signal InputB_buff : std_logic_vector(31 downto 0);
signal Output_buff : std_logic_vector(31 downto 0);
signal Output_buff_sub : std_logic_vector(31 downto 0);
signal ram_read_en : std_logic;
signal out_en_1 : std_logic;
signal out_en_2 : std_logic;
signal out_en_3 : std_logic;
signal out_en_4 : std_logic;
signal out_en_5 : std_logic;
signal out_en_6 : std_logic;
signal out_en_7 : std_logic;
signal out_en_8 : std_logic;
signal out_en_9 : std_logic;
signal out_en_10 : std_logic;
signal out_en_11 : std_logic;
signal out_en_12 : std_logic;
signal out_en_13 : std_logic;
signal out_en_14 : std_logic;
signal out_en_15 : std_logic;
begin


process(InputA,InputB)   
begin
if ( InputA>=0 and InputB>=0  )then
ram_read_en<=  '1';
end if;
end process;



process(clk)  
begin
if (InputA_buff>=0 and InputB_buff>=0 and clk'event and clk = '1' )then
out_en_1 <= '1' ;
end if;
end process;

process(clk)  
begin
if (out_en_1 = '1' and clk'event and clk = '1' )then
out_en_2 <= '1' ;
end if;
end process;

process(clk)  
begin
if (out_en_2 = '1' and clk'event and clk = '1' )then
out_en_3 <= '1' ;
end if;
end process;

process(clk)  
begin
if (out_en_3 = '1' and clk'event and clk = '1' )then
out_en_4 <= '1' ;
end if;
end process;

process(clk)  
begin
if (out_en_4 = '1' and clk'event and clk = '1' )then
out_en_5 <= '1' ;
end if;
end process;

process(clk)  
begin
if (out_en_5 = '1' and clk'event and clk = '1' )then
out_en_6 <= '1' ;
end if;
end process;

process(clk)  
begin
if (out_en_6 = '1' and clk'event and clk = '1' )then
out_en_7 <= '1' ;
end if;
end process;

process(clk)  
begin
if (out_en_7 = '1' and clk'event and clk = '1' )then
out_en_8 <= '1' ;
end if;
end process;
process(clk)  
begin
if (out_en_8 = '1' and clk'event and clk = '1' )then
out_en_9 <= '1' ;
end if;
end process;

process(clk)  
begin
if (out_en_9 = '1' and clk'event and clk = '1' )then
out_en_10 <= '1' ;
end if;
end process;

process(clk)  
begin
if (out_en_10 = '1' and clk'event and clk = '1' )then
out_en_11 <= '1' ;
end if;
end process;

process(clk)  
begin
if (out_en_11 = '1' and clk'event and clk = '1' )then
out_en_12 <= '1' ;
end if;
end process;

process(clk)  
begin
if (out_en_12 = '1' and clk'event and clk = '1' )then
out_en_13 <= '1' ;
end if;
end process;

process(clk)  
begin
if (out_en_13 = '1' and clk'event and clk = '1' )then
out_en_14 <= '1' ;
end if;
end process;

process(clk)  
begin
if (out_en_14 = '1' and clk'event and clk = '1' )then
out_en_15 <= '1' ;
end if;
end process;

process(clk )   
begin
if (out_en_15 = '1' and clk'event and clk = '1'  )then
Output <= Output_buff ;
end if;
end process;
----------------
----------------
----------------
------------------------------- Data Extraction -------------------------------










   process(clk)
      begin
         if clk'event and clk = '1' then
            sf_A_d1 <=  sf_A;
            sf_A_d2 <=  sf_A_d1;
            sf_A_d3 <=  sf_A_d2;
            sf_A_d4 <=  sf_A_d3;
            sf_B_d1 <=  sf_B;
            sf_B_d2 <=  sf_B_d1;
            sf_B_d3 <=  sf_B_d2;
            sf_B_d4 <=  sf_B_d3;
            sign_d1 <=  sign;
            sign_d2 <=  sign_d1;
            sign_d3 <=  sign_d2;
            sign_d4 <=  sign_d3;
            sign_d5 <=  sign_d4;
            sign_d6 <=  sign_d5;
            sign_d7 <=  sign_d6;
            sign_d8 <=  sign_d7;
            sign_d9 <=  sign_d8;
            sign_d10 <=  sign_d9;
            z_d1 <=  z;
            z_d2 <=  z_d1;
            z_d3 <=  z_d2;
            z_d4 <=  z_d3;
            z_d5 <=  z_d4;
            z_d6 <=  z_d5;
            z_d7 <=  z_d6;
            z_d8 <=  z_d7;
            z_d9 <=  z_d8;
            z_d10 <=  z_d9;
            inf_d1 <=  inf;
            inf_d2 <=  inf_d1;
            inf_d3 <=  inf_d2;
            inf_d4 <=  inf_d3;
            inf_d5 <=  inf_d4;
            inf_d6 <=  inf_d5;
            inf_d7 <=  inf_d6;
            inf_d8 <=  inf_d7;
            inf_d9 <=  inf_d8;
            inf_d10 <=  inf_d9;
            normFrac_d1 <=  normFrac;
            normFrac_d2 <=  normFrac_d1;
            normFrac_d3 <=  normFrac_d2;
            sf_sign_d1 <=  sf_sign;
            sf_sign_d2 <=  sf_sign_d1;
            sf_sign_d3 <=  sf_sign_d2;
            nzero_d1 <=  nzero;
            nzero_d2 <=  nzero_d1;
            nzero_d3 <=  nzero_d2;
            ExpBits_d1 <=  ExpBits;
            ExpBits_d2 <=  ExpBits_d1;
            ExpBits_d3 <=  ExpBits_d2;
            RegimeAns_tmp_d1 <=  RegimeAns_tmp;
            ovf_reg_d1 <=  ovf_reg;
            ovf_reg_d2 <=  ovf_reg_d1;
            ovf_reg_d3 <=  ovf_reg_d2;
            ovf_reg_d4 <=  ovf_reg_d3;
            ovf_reg_d5 <=  ovf_reg_d4;
            FinalRegime_d1 <=  FinalRegime;
            FinalRegime_d2 <=  FinalRegime_d1;
            ovf_regF_d1 <=  ovf_regF;
            ovf_regF_d2 <=  ovf_regF_d1;
            ovf_regF_d3 <=  ovf_regF_d2;
            ovf_regF_d4 <=  ovf_regF_d3;
            shifter_out_d1 <=  shifter_out;
         end if;
      end process;
------------------------------- Data Extraction -------------------------------

----------------
regA: reg  
      port map ( clk  => clk,
ram_read_en=> ram_read_en,
ram_data_in=> InputA,
ram_data_out=> InputA_buff);


regB: reg 
      port map ( clk  => clk,
ram_read_en=> ram_read_en,
ram_data_in=> InputB,
ram_data_out=> InputB_buff);
----------------
----------------
----------------


   decoderA: PositDecoder_32_4_F400_uid4  -- pipelineDepth=5 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 Exp => exp_A,
                 Frac => frac_A,
                 Input => InputA_buff,
                 Reg => reg_A,
                 Sign => sign_A,
                 inf => inf_A,
                 z => z_A);
   decoderB: PositDecoder_32_4_F400_uid16  -- pipelineDepth=5 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 Exp => exp_B,
                 Frac => frac_B,
                 Input => InputB_buff,
                 Reg => reg_B,
                 Sign => sign_B,
                 inf => inf_B,
                 z => z_B);
   ----------------Synchro barrier, entering cycle 5----------------
   -- Gather scale factors
   sf_A <= reg_A & exp_A;
   sf_B <= reg_B & exp_B;
---------------------- Sign and Special Cases Computation ----------------------
   sign <= sign_A XOR sign_B;
   z <= z_A OR z_B;
   inf <= inf_A OR inf_B;
--------------- Multiply the fractions, add the exponent values ---------------
   mult: IntMultiplier_UsingDSP_26_26_52_unsigned_F400_uid28  -- pipelineDepth=4 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 R => frac_mult,
                 X => frac_A,
                 Y => frac_B);
   ----------------Synchro barrier, entering cycle 9----------------
   -- Adjust for overflow
   ovf_m <= frac_mult(frac_mult'high);
   normFrac <= frac_mult & '0' when ovf_m = '0' else '0' & frac_mult;
   sf_mult <= (sf_A_d4(sf_A_d4'high) & sf_A_d4) + (sf_B_d4(sf_B_d4'high) & sf_B_d4) + ovf_m;
   sf_sign <= sf_mult(sf_mult'high);
---------------------- Compute Regime and Exponent value ----------------------
   nzero <= '0' when frac_mult = 0 else '1';
   -- Unpack scaling factors
   ExpBits <= sf_mult(3 downto 0);
   RegimeAns_tmp <= sf_mult(9 downto 4);
   ----------------Synchro barrier, entering cycle 10----------------
   -- Get Regime's absolute value
   RegimeAns <= (NOT RegimeAns_tmp_d1)+1 when sf_sign_d1 = '1' else RegimeAns_tmp_d1;
   -- Check for Regime overflow
   ovf_reg <= RegimeAns(RegimeAns'high);
   FinalRegime <= '0' & "11111" when ovf_reg = '1' else RegimeAns;
   ----------------Synchro barrier, entering cycle 11----------------
   ovf_regF <= '1' when FinalRegime_d1 = ('0' & "11111") else '0';
   ----------------Synchro barrier, entering cycle 12----------------
   FinalExp <= "0000" when ((ovf_reg_d2 = '1') OR (ovf_regF_d1 = '1') OR (nzero_d3='0')) else ExpBits_d3;
------------------------------- Packing Stage 1 -------------------------------
   tmp1 <= nzero_d3 & '0' & FinalExp & normFrac_d3(50 downto 0);
   tmp2 <= '0' & nzero_d3 & FinalExp & normFrac_d3(50 downto 0);
   shift_neg <= FinalRegime_d2 - 2 when (ovf_regF_d1 = '1') else FinalRegime_d2 - 1;
   shift_pos <= FinalRegime_d2 - 1 when (ovf_regF_d1 = '1') else FinalRegime_d2;
   shifter_in <= tmp2 when sf_sign_d3 = '1' else tmp1;
   shifter_S <= shift_neg when sf_sign_d3 = '1' else shift_pos;
   RightShifterComponent: RightShifter_57_by_max_32_F400_uid139  -- pipelineDepth=2 maxInDelay=0
      port map ( clk  => clk,
                 rst  => rst,
                 R => shifter_out,
                 S => shifter_S,
                 X => shifter_in);
   ----------------Synchro barrier, entering cycle 14----------------
   ----------------Synchro barrier, entering cycle 15----------------
   tmp_ans <= shifter_out_d1(88 downto 58);
--------------------- Packing Stage 2 - Unbiased Rounding ---------------------
   LSB <= shifter_out_d1(58);
   G <= shifter_out_d1(57);
   R <= shifter_out_d1(56);
   S <= '0' when shifter_out_d1(55 downto 0) = 0 else '1';
   round <= G AND (LSB OR R OR S) when NOT((ovf_reg_d5 OR ovf_regF_d4) = '1') else '0';
   Output_buff <= '1' & "0000000000000000000000000000000" when inf_d10 = '1' else "00000000000000000000000000000000" when z_d10 = '1' else '0' & (tmp_ans + round) when sign_d10 = '0' else NOT('0' & (tmp_ans + round))+1;
end architecture;










