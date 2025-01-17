--------------------------------------------------------------------------------
--                           InputIEEE_6_24_to_6_24
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin (2008)
--------------------------------------------------------------------------------
-- Pipeline depth: 0 cycles

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity InputIEEE_6_24_to_6_24 is
   port ( clk, rst : in std_logic;
          X : in  std_logic_vector(30 downto 0);
          R : out  std_logic_vector(6+24+2 downto 0)   );
end entity;

architecture arch of InputIEEE_6_24_to_6_24 is
signal expX :  std_logic_vector(5 downto 0);
signal fracX :  std_logic_vector(23 downto 0);
signal sX :  std_logic;
signal expZero :  std_logic;
signal expInfty :  std_logic;
signal fracZero :  std_logic;
signal reprSubNormal :  std_logic;
signal sfracX :  std_logic_vector(23 downto 0);
signal fracR :  std_logic_vector(23 downto 0);
signal expR :  std_logic_vector(5 downto 0);
signal infinity :  std_logic;
signal zero :  std_logic;
signal NaN :  std_logic;
signal exnR :  std_logic_vector(1 downto 0);
begin
   process(clk)
      begin
         if clk'event and clk = '1' then
         end if;
      end process;
   expX  <= X(29 downto 24);
   fracX  <= X(23 downto 0);
   sX  <= X(30);
   expZero  <= '1' when expX = (5 downto 0 => '0') else '0';
   expInfty  <= '1' when expX = (5 downto 0 => '1') else '0';
   fracZero <= '1' when fracX = (23 downto 0 => '0') else '0';
   reprSubNormal <= fracX(23);
   -- since we have one more exponent value than IEEE (field 0...0, value emin-1),
   -- we can represent subnormal numbers whose mantissa field begins with a 1
   sfracX <= fracX(22 downto 0) & '0' when (expZero='1' and reprSubNormal='1')    else fracX;
   fracR <= sfracX;
   -- copy exponent. This will be OK even for subnormals, zero and infty since in such cases the exn bits will prevail
   expR <= expX;
   infinity <= expInfty and fracZero;
   zero <= expZero and not reprSubNormal;
   NaN <= expInfty and not fracZero;
   exnR <= 
           "00" when zero='1' 
      else "10" when infinity='1' 
      else "11" when NaN='1' 
      else "01" ;  -- normal number
   R <= exnR & sX & expR & fracR; 
end architecture;

