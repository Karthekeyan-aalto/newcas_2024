--------------------------------------------------------------------------------
--                          OutputIEEE_7_21_to_7_21
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: F. Ferrandi  (2009-2012)
--------------------------------------------------------------------------------
-- Pipeline depth: 0 cycles

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity OutputIEEE_7_21_to_7_21 is
   port ( clk, rst : in std_logic;
          X : in  std_logic_vector(7+21+2 downto 0);
          R : out  std_logic_vector(28 downto 0)   );
end entity;

architecture arch of OutputIEEE_7_21_to_7_21 is
signal expX :  std_logic_vector(6 downto 0);
signal fracX :  std_logic_vector(20 downto 0);
signal exnX :  std_logic_vector(1 downto 0);
signal sX :  std_logic;
signal expZero :  std_logic;
signal sfracX :  std_logic_vector(20 downto 0);
signal fracR :  std_logic_vector(20 downto 0);
signal expR :  std_logic_vector(6 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
         end if;
      end process;
   expX  <= X(27 downto 21);
   fracX  <= X(20 downto 0);
   exnX  <= X(30 downto 29);
   sX  <= X(28) when (exnX = "01" or exnX = "10" or exnX = "00") else '0';
   expZero  <= '1' when expX = (6 downto 0 => '0') else '0';
   -- since we have one more exponent value than IEEE (field 0...0, value emin-1),
   -- we can represent subnormal numbers whose mantissa field begins with a 1
   sfracX <= 
      (20 downto 0 => '0') when (exnX = "00") else
      '1' & fracX(20 downto 1) when (expZero = '1' and exnX = "01") else
      fracX when (exnX = "01") else 
      (20 downto 1 => '0') & exnX(0);
   fracR <= sfracX;
   expR <=  
      (6 downto 0 => '0') when (exnX = "00") else
      expX when (exnX = "01") else 
      (6 downto 0 => '1');
   R <= sX & expR & fracR; 
end architecture;

