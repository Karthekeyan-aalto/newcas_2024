-- This is a SumNode_Fixed  VHDL model
-- Initially written by Marko Kosunen
-- Last modification by Marko Kosunen, marko.kosunen@aalto.fi, 16.01.2020 15:51
library ieee;
library ieee_proposed;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use ieee.numeric_std_unsigned.all;
use std.textio.all;
use ieee_proposed.fixed_pkg.all;
use ieee_proposed.fixed_float_types.all;

entity SumNode_Fixed is
  generic(numberOfBits: integer := 8);
    port( vinf1  : in  sfixed (0 downto (1-numberOfBits));
          vinf2  : in  sfixed (0 downto (1-numberOfBits));
          voutf0 : out  sfixed (0 downto (1-numberOfBits))
        );
end SumNode_Fixed;

architecture rtl of SumNode_Fixed is

   signal tempOutput: sfixed (1 downto (1-numberOfBits)):=to_sfixed(1,1,(1-numberOfBits));

begin
   tempOutput <= vinf2 + vinf1;
   voutf0(0 downto (1-numberOfBits)) <= tempOutput(0 downto (1-numberOfBits));
end rtl;
