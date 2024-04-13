--------------------------------------------------------------------------------
--                          OutputIEEE_7_14_to_7_14
-- VHDL generated for Virtex6 @ 800MHz
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: F. Ferrandi  (2009-2012)
--------------------------------------------------------------------------------
-- Pipeline depth: 0 cycles
-- Clock period (ns): 1.25
-- Target frequency (MHz): 800
-- Input signals: X
-- Output signals: R

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity OutputIEEE_7_14_to_7_14 is
    port (clk : in std_logic;
          X : in  std_logic_vector(7+14+2 downto 0);
          R : out  std_logic_vector(21 downto 0)   );
end entity;

architecture arch of OutputIEEE_7_14_to_7_14 is
signal fracX :  std_logic_vector(13 downto 0);
signal exnX :  std_logic_vector(1 downto 0);
signal expX :  std_logic_vector(6 downto 0);
signal sX :  std_logic;
signal expZero :  std_logic;
signal fracR :  std_logic_vector(13 downto 0);
signal expR :  std_logic_vector(6 downto 0);
begin
   fracX  <= X(13 downto 0);
   exnX  <= X(23 downto 22);
   expX  <= X(20 downto 14);
   sX  <= X(21) when (exnX = "01" or exnX = "10" or exnX = "00") else '0';
   expZero  <= '1' when expX = (6 downto 0 => '0') else '0';
   -- since we have one more exponent value than IEEE (field 0...0, value emin-1),
   -- we can represent subnormal numbers whose mantissa field begins with a 1
   fracR <= 
      "00000000000000" when (exnX = "00") else
      '1' & fracX(13 downto 1) & "" when (expZero = '1' and exnX = "01") else
      fracX  & "" when (exnX = "01") else 
      "0000000000000" & exnX(0);
   expR <=  
      (6 downto 0 => '0') when (exnX = "00") else
      expX when (exnX = "01") else 
      (6 downto 0 => '1');
   R <= sX & expR & fracR; 
end architecture;

