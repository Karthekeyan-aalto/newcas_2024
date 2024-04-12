-- This is a SumNode_Float  VHDL model
-- Initially written by Marko Kosunen
-- Last modification by Marko Kosunen, marko.kosunen@aalto.fi, 16.01.2020 15:51
library ieee;
library ieee_proposed;
--use ieee.std_logic_1164.all;
--use ieee.numeric_std.all;
--use ieee.numeric_std_unsigned.all;
--use std.textio.all;
use ieee_proposed.fixed_pkg.all;
use ieee_proposed.fixed_float_types.all;
use ieee_proposed.float_pkg.all;

entity SumNode_Float is
  generic(mantissaBits: integer := 24; exponentBits: integer := 8);
    port( vinf1  : in  float (exponentBits downto (1-mantissaBits));
          vinf2  : in  float (exponentBits downto (1-mantissaBits));
          voutf0 : out float (exponentBits downto (1-mantissaBits))
        );
end SumNode_Float;

architecture rtl of SumNode_Float is

   --signal tempOutput: float(exponentBits downto (1-mantissaBits)) := to_float(1,1,(1-mantissaBits));

begin
   --tempOutput <= vinf2 + vinf1;
   voutf0 <=  vinf2 + vinf1;
end rtl;
