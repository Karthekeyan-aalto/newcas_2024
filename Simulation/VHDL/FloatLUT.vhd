LIBRARY ieee; 
LIBRARY std; 
USE ieee.std_logic_1164.all; 
USE ieee.std_logic_arith.all; 
USE ieee.std_logic_unsigned.all; 
USE std.textio.all; 
 
LIBRARY ieee_proposed; 
USE ieee_proposed.fixed_pkg.all; 
USE ieee_proposed.fixed_float_types.all; 
USE ieee_proposed.float_pkg.all; 
 
ENTITY FloatLUT IS
    GENERIC (mantissaBits :INTEGER := 15 ; exponentBits :INTEGER := 7; numberOfBits :INTEGER := 22);
    PORT (
    v5a:IN std_logic;
    --clk:IN std_logic;
    --rst:IN std_logic;
    vout:OUT std_logic_vector(numberOfBits-1 DOWNTO 0)
);
END FloatLUT;
ARCHITECTURE rtl of FloatLUT IS
    SIGNAL voutsignal :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL floatOneSignal :std_logic_vector(numberOfBits-1 DOWNTO 0):= to_slv(to_float(1.0,exponentBits,mantissaBits-1));
BEGIN
    WITH v5a SELECT  voutsignal <=
    "00000000000000000000000000000000" WHEN '0',
    floatOneSignal WHEN '1',
    "--------------------------------" WHEN OTHERS;
    vout <= voutsignal;

END ARCHITECTURE;
